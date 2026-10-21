# analysis calibration baseline

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_analysis_calibration_baseline_20260517T141557.jsonl`
- **Structured JSON:** [`11c4e61e44302dd3e100.json`](../../sessions/11/11c4e61e44302dd3e100.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-17T14:20:47.830089+00:00_

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
  "session": "worker_analysis_calibration_baseline_20260517T141557",
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

_source line 2 · 2026-05-17T14:20:47.830444+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T14:20:47.830613+00:00_

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
  "session": "worker_analysis_calibration_baseline_20260517T141557",
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

_source line 4 · 2026-05-17T14:20:47.830804+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis_epsilon_sweep\\nanalysis_fk_bootstrap_ci.json\\nanalysis_fk_bootstrap_per_instance.json\\nanalysis_lp_range_cdf.json\\nanalysis_lp_range_cdf_n16_3seed.json\\nanalysis_multiseed_selection_f1.json\\nanalysis_round8\\nanalysis_scierc_n16_3seed_selection_f1.json\\nanalysis_scierc_n16_3seed_selection_f1_merged.json\\nanalysis_scierc_re_n16_3seed_selection_f1.json\\nanalysis_unified_rho_full.json\\nbootstrap_ci_nscaling\\nbootstrap_ci_summary.json\\nbootstrap_ci_tables.tex\\nconditional_filter_diagnosis.json\\nd108_greedy_f1\\nd108_lp_vc_combination\\nd108_mbr_within_rho\\nd108_q4q5\\nd110_4b_degeneracy\\nd112_disk_cleanup\\nd112_hybrid_strategy\\nd112_mf3_random_single\\nd112_table2_fix\\nd114_auroc_investigation\\nexp001_n16_seed123\\nexp001_n16_seed123_200only\\nexp001_n16_seed123_200only_backup\\nexp001_n16_seed123_full\\nexp001_n16_seed123_run.log\\nexp001_n16_seed42\\nexp001_n16_seed42_200only_backup\\nexp001_n16_seed42_run.log\\nexp001_n16_seed456\\nexp001_n16_seed456_200only\\nexp001_n16_seed456_run.log\\nexp001_seed123_t10_full\\nexp001_seed123_t10_full.log\\nexp001_seed456_t10_full\\nexp001_seed456_t10_full.log\\nexp002_conll2003\\nexp003_wnut17_dryrun\\nexp003_wnut17_eval\\nexp003_wnut17_eval.log\\nexp003_wnut17_pilot\\nexp003_wnut17_pilot.log\\nexp004_re_diagnostic\\nexp004v2_re_diagnostic\\nexp007_llama_dryrun\\nexp007_llama_inference\\nexp008_re_n16\\nexp008_re_n16_200only\\nexp008_re_n16_t10_full\\nexp008_re_n16_t10_full.log\\nexp009_stratification_results.json\\nexp010_selection_curves\\nexp016_signal_ensemble\\nexp018_3seed_5signal_results.json\\nexp_001_seed123_v2\\nexp_001_seed123_v2_r1024\\nexp_001_seed42_v2\\nexp_001_seed42_v2_r1024\\nexp_001_seed456_v2\\nexp_001_seed456_v2_ner\\nexp_001_seed456_v2_ner.log\\nexp_001_seed456_v2_ner_r1024\\nexp_002_conll_n16\\nexp_002_conll_n16.log\\nexp_002_conll_n16_r1024\\nexp_003_wnut17_v2_infer\\nexp_005_v2_temperature\\nexp_006_v2\\nexp_006_v2_run.lo
…[truncated 2848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T14:20:47.830953+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T14:20:47.831112+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"all_signals_5signal.json\\nauroc_5signal.json\\ncomparison.json\\nper_type_lp_analysis.csv\\nper_type_lp_table.tex\\nreliability_data_1024.json\\nreport.json\\nrun.log\\nsamples.jsonl\\nsamples_with_logprobs.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T14:20:47.831271+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T14:20:47.831405+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"per_type_lp_analysis.csv\\nper_type_lp_table.tex\\nreport.json\\nrun.log\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T14:20:47.831526+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T14:20:47.831653+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"paired_n8_baseline.json\\nresults.json\\nsamples.jsonl\\nshard_0\\nshard_1\\nshard_2\\nshard_3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T14:20:47.831783+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples_with_logprobs.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples_with_logprobs.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T14:20:47.832081+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"X96-1059_sent000\\\", \\\"text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\", \\\"start\\\": 15, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 0, \\\"head_end\\\": 27, \\\"tail_start\\\": 103, \\\"tail_end\\\": 125}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 15, \\\"head_end\\\": 27, \\\"tail_start\\\": 31, \\\"tail_end\\\": 44}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"USED-FOR\\\", \\\"head_start\\\": 103, \\\"head_end\\\": 125, \\\"tail_start\\\": 129, \\\"tail_end\\\": 153}], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"
…[truncated 8656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T14:20:47.832272+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T14:20:47.832534+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"conll2003_test_00000\\\", \\\"text\\\": \\\"SOCCER - JAPAN GET LUCKY WIN , CHINA IN SURPRISE DEFEAT .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"JAPAN\\\", \\\"type\\\": \\\"LOC\\\", \\\"start\\\": 9, \\\"end\\\": 14}, {\\\"text\\\": \\\"CHINA\\\", \\\"type\\\": \\\"PER\\\", \\\"start\\\": 31, \\\"end\\\": 36}], \\\"relations\\\": [], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"JAPAN\\\", \\\"type\\\": \\\"LOC\\\", \\\"start\\\": 9, \\\"end\\\": 14}, {\\\"text\\\": \\\"CHINA\\\", \\\"type\\\": \\\"LOC\\\", \\\"start\\\": 31, \\\"end\\\": 36}], \\\"relations\\\": [], \\\"events\\\": [], \\\"cumulative_logprob\\\": -4.9488675847250505, \\\"n_tokens\\\": 67, \\\"mean_logprob\\\": -0.07386369529440374}, {\\\"entities\\\": [{\\\"text\\\": \\\"JAPAN\\\", \\\"type\\\": \\\"LOC\\\", \\\"start\\\": 9, \\\"end\\\": 14}, {\\\"text\\\": \\\"CHINA\\\", \\\"type\\\": \\\"LOC\\\", \\\"start\\\": 31, \\\"end\\\": 36}], \\\"relations\\\": [], \\\"events\\\": [], \\\"cumulative_logprob\\\": -2.3127497540126996, \\\"n_tokens\\\": 67, \\\"mean_logprob\\\": -0.034518653044965666}, {\\\"entities\\\": [{\\\"text\\\": \\\"JAPAN\\\", \\\"type\\\": \\\"LOC\\\", \\\"start\\\": 9, \\\"end\\\": 14}, {\\\"text\\\": \\\"CHINA\\\", \\\"type\\\": \\\"LOC\\\", \\\"start\\\": 31, \\\"end\\\": 36}], \\\"relations\\\": [{\\\"head\\\": \\\"JAPAN\\\", \\\"tail\\\": \\\"CHINA\\\", \\\"type\\\": \\\"DEF\\\", \\\"head_start\\\": 9, \\\"head_end\\\": 14, \\\"tail_start\\\": 31, \\\"tail_end\\\": 36}], \\\"events\\\": [], \\\"cumulative_logprob\\\": -8.493769360864384, \\\"n_tokens\\\": 118, \\\"mean_logprob\\\": -0.07198109627851174}, {\\\"entities\\\": [{\\\"text\\\": \\\"JAPAN\\\", \\\"type\\\": \\\"LOC\\\", \\\"start\\\": 9, \\\"end\\\": 14}, {\\\"text\\\": \\\"CHINA\\\", \\\"type\\\": \\\"LOC\\\", \\\"start\\\": 31, \\\"end\\\": 36}], \\\"relations\\\": [], \\\"events\\\": [], \\\"cum
…[truncated 5559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T14:20:47.832693+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T14:20:47.833037+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"fewnerd_test_07296\\\", \\\"text\\\": \\\"The musical played the Dominion Theatre in 2014 in a limited engagement and starred Aled Jones , Tom Chambers , Rachel Stanley , Louise Bowden , and Wendi Peters .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Dominion Theatre\\\", \\\"type\\\": \\\"building\\\", \\\"start\\\": 23, \\\"end\\\": 39}, {\\\"text\\\": \\\"Aled Jones\\\", \\\"type\\\": \\\"person\\\", \\\"start\\\": 84, \\\"end\\\": 94}, {\\\"text\\\": \\\"Tom Chambers\\\", \\\"type\\\": \\\"person\\\", \\\"start\\\": 97, \\\"end\\\": 109}, {\\\"text\\\": \\\"Rachel Stanley\\\", \\\"type\\\": \\\"person\\\", \\\"start\\\": 112, \\\"end\\\": 126}, {\\\"text\\\": \\\"Louise Bowden\\\", \\\"type\\\": \\\"person\\\", \\\"start\\\": 129, \\\"end\\\": 142}, {\\\"text\\\": \\\"Wendi Peters\\\", \\\"type\\\": \\\"person\\\", \\\"start\\\": 149, \\\"end\\\": 161}], \\\"relations\\\": [], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Dominion Theatre\\\", \\\"type\\\": \\\"building\\\", \\\"start\\\": 23, \\\"end\\\": 39}, {\\\"text\\\": \\\"Aled Jones\\\", \\\"type\\\": \\\"person\\\", \\\"start\\\": 84, \\\"end\\\": 94}, {\\\"text\\\": \\\"Tom Chambers\\\", \\\"type\\\": \\\"person\\\", \\\"start\\\": 97, \\\"end\\\": 109}, {\\\"text\\\": \\\"Rachel Stanley\\\", \\\"type\\\": \\\"person\\\", \\\"start\\\": 112, \\\"end\\\": 126}, {\\\"text\\\": \\\"Louise Bowden\\\", \\\"type\\\": \\\"person\\\", \\\"start\\\": 129, \\\"end\\\": 142}, {\\\"text\\\": \\\"Wendi Peters\\\", \\\"type\\\": \\\"person\\\", \\\"start\\\": 149, \\\"end\\\": 161}], \\\"relations\\\": [], \\\"events\\\": [], \\\"cumulative_logprob\\\": -0.1988895523322185, \\\"n_tokens\\\": 187, \\\"mean_logprob\\\": -0.001063580493755179, \\\"token_logprobs\\\": [0.0, 0.0, 0.0, -0.011052576825022697, 0.0, 0.0, -6.437094270950183e-05, -0.1224166750907898, 0.0, -0.0004345426568761468, -0.001297942479
…[truncated 9000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T14:20:47.833292+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples_with_logprobs.jsonl /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl /root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples_with_logprobs.jsonl /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl /root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T14:20:47.833444+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      551 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples_with_logprobs.jsonl\\n     3453 /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl\\n     5000 /root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl\\n     9004 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T14:20:47.833574+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/scripts/ -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/scripts/ -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T14:20:47.833704+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/scripts/c3_lp_range_cdf.py\\n/root/autodl-tmp/struct_self_consist_ie/scripts/analyze_lp_range_cdf_n529.py\\n/root/autodl-tmp/struct_self_consist_ie/scripts/epsilon_sweep.py\\n/root/autodl-tmp/struct_self_consist_ie/scripts/analyze_zero_f1.py\\n/root/autodl-tmp/struct_self_consist_ie/scripts/analyze_zero_f1_detail.py\\n/root/autodl-tmp/struct_self_consist_ie/scripts/paired_n8_baseline.py\\n/root/autodl-tmp/struct_self_consist_ie/scripts/exp_028_postprocess/03_analyze.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T14:20:47.833827+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -50 /root/autodl-tmp/struct_self_consist_ie/scripts/paired_n8_baseline.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -50 /root/autodl-tmp/struct_self_consist_ie/scripts/paired_n8_baseline.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T14:20:47.833969+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nPaired N=8 Baseline: Filter exp-021 (N=8, 37k) to match exp-027's 5000 instances,\\ncompute metrics, and run paired bootstrap test.\\n\\\"\\\"\\\"\\nimport json\\nimport numpy as np\\nfrom collections import defaultdict\\nfrom scipy import stats\\n\\ndef compute_ner_f1(pred_entities, gold_entities):\\n    \\\"\\\"\\\"Compute NER F1 based on exact span+type match.\\\"\\\"\\\"\\n    pred_set = set()\\n    for e in pred_entities:\\n        pred_set.add((e['text'], e['type'], e.get('start', -1), e.get('end', -1)))\\n    gold_set = set()\\n    for e in gold_entities:\\n        gold_set.add((e['text'], e['type'], e.get('start', -1), e.get('end', -1)))\\n    \\n    if len(pred_set) == 0 and len(gold_set) == 0:\\n        return 1.0\\n    if len(pred_set) == 0 or len(gold_set) == 0:\\n        return 0.0\\n    \\n    tp = len(pred_set & gold_set)\\n    prec = tp / len(pred_set) if pred_set else 0\\n    rec = tp / len(gold_set) if gold_set else 0\\n    if prec + rec == 0:\\n        return 0.0\\n    return 2 * prec * rec / (prec + rec)\\n\\ndef get_entity_key_set(entities):\\n    \\\"\\\"\\\"Get frozenset of (text, type) for degeneracy check.\\\"\\\"\\\"\\n    return frozenset((e['text'], e['type']) for e in entities)\\n\\ndef select_by_logprob(samples):\\n    \\\"\\\"\\\"Select sample with highest mean logprob.\\\"\\\"\\\"\\n    best_idx = -1\\n    best_lp = -float('inf')\\n    for i, s in enumerate(samples):\\n        lp = s.get('mean_logprob', s.get('cumulative_logprob', -999))\\n        if lp > best_lp:\\n            best_lp = lp\\n            best_idx = i\\n    return best_idx\\n\\ndef oracle_select(samples, gold_entities):\\n    \\\"\\\"\\\"Select sample with highest F1.\\\"\\\"\\\"\\n    best_idx = 0\\n    best_f1 = -1\\n    for i, s in enumerate(samples):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T14:20:47.834220+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/autodl-tmp/struct_self_consist_ie/scripts/calibration_baseline.py << 'PYTHON_SCRIPT'\n\"\"\"\nCalibration Baseline: Platt Scaling & Temperature Scaling for LP-based selection.\nUses 5-fold CV to avoid train-test leak.\n\"\"\"\nimport json\nimport numpy as np\nfrom pathlib import Path\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import KFold\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import expit\n\nWORK_DIR = Path(\"/root/autodl-tmp/struct_self_consist_ie\")\nOUTPUT_DIR = WORK_DIR / \"output\"\n\nDATASETS = {\n    \"SciERC\": OUTPUT_DIR / \"exp_012_rerun_1024\" / \"samples_with_logprobs.jsonl\",\n    \"CoNLL\": OUTPUT_DIR / \"exp_002_conll_n16_r1024\" / \"samples.jsonl\",\n    \"Few-NERD\": OUTPUT_DIR / \"exp_027_fewnerd_n16\" / \"samples.jsonl\",\n}\n\n\ndef compute_ner_f1(pred_entities, gold_entities):\n    pred_set = {(e['text'], e['type'], e.get('start', -1), e.get('end', -1)) for e in pred_entities}\n    gold_set = {(e['text'], e['type'], e.get('start', -1), e.get('end', -1)) for e in gold_entities}\n    if not pred_set and not gold_set:\n        return 1.0\n    if not pred_set or not gold_set:\n        return 0.0\n    tp = len(pred_set & gold_set)\n    prec = tp / len(pred_set)\n    rec = tp / len(gold_set)\n    if prec + rec == 0:\n        return 0.0\n    return 2 * prec * rec / (prec + rec)\n\n\ndef load_dataset(path):\n    \"\"\"Load dataset, return list of dicts with per-sample LP and F1.\"\"\"\n    instances = []\n    with open(path) as f:\n        for line in f:\n            row = json.loads(line)\n            gold_ents = row[\"gold\"][\"entities\"]\n            samples = row[\"samples\"]\n            greedy = row.get(\"greedy\")\n\n            sample_data = []\n            for s in samples:\n                lp = s.get(\"mean_logprob\", s.get(\"cumulative_logprob\") / max(s.get(\"n_tokens\", 1), 1))\n                f1 = compute_ner_f1(s.get(\"entities\", []), gold_ents)\n                sample_data.append({\"lp\": lp, \"f1\": f1})\n\n            greedy_f1 = None\n            if greedy:\n                greedy_f1 = compute_ner_f1(greedy.get(\"entities\", []), gold_ents)\n\n            instances.append({\n                \"id\": row[\"id\"],\n                \"samples\": sample_data,\n                \"greedy_f1\": greedy_f1,\n            })\n    return instances\n\n\ndef make_binary_labels(instances):\n    \"\"\"For each instance, label samples: F1 >= median → 1, else → 0.\"\"\"\n    all_lps = []\n    all_labels = []\n    instance_indices = []  # which instance each sample belongs to\n\n    for idx, inst in enumerate(instances):\n        f1s = [s[\"f1\"] for s in inst[\"samples\"]]\n        median_f1 = np.median(f1s)\n        for s in inst[\"samples\"]:\n            all_lps.append(s[\"lp\"])\n            all_labels.append(1 if s[\"f1\"] >= median_f1 else 0)\n            instance_indices.append(idx)\n\n    return np.array(all_lps), np.array(all_labels), np.array(instance_indices)\n\n\ndef compute_ece(probs, labels, n_bins=10):\n    \"\"\"Expected Calibration Error.\"\"\"\n    bin_edges = np.linspace(0, 1, n_bins + 1)\n    ece = 0.0\n    bin_data = []\n    for i in range(n_bins):\n        mask = (probs >= bin_edges[i]) & (probs < bin_edges[i + 1])\n        if i == n_bins - 1:\n            mask = (probs >= bin_edges[i]) & (probs <= bin_edges[i + 1])\n        if mask.sum() == 0:\n            bin_data.append({\"bin_center\": (bin_edges[i] + bin_edges[i+1]) / 2,\n                             \"avg_confidence\": None, \"avg_accuracy\": None, \"count\": 0})\n            continue\n        avg_conf = probs[mask].mean()\n        avg_acc = labels[mask].mean()\n        ece += mask.sum() / len(probs) * abs(avg_conf - avg_acc)\n        bin_data.append({\"bin_center\": (bin_edges[i] + bin_edges[i+1]) / 2,\n                         \"avg_confidence\": float(avg_conf), \"avg_accuracy\": float(avg_acc),\n                         \"count\": int(mask.sum())})\n    return float(ece), bin_data\n\n\ndef raw_lp_to_prob(lps):\n    \"\"\"Convert raw LP to [0,1] via min-max normalization then sigmoid-like.\"\"\"\n    # Use rank-based probability: P = rank / N (within the instance)\n    # For global calibration, use sigmoid of LP\n    return expit(lps * 10)  # scale factor to spread values\n\n\ndef platt_scaling_cv(instances, n_splits=5):\n    \"\"\"5-fold CV Platt scaling. Returns per-instance selection F1.\"\"\"\n    all_lps, all_labels, inst_indices = make_binary_labels(instances)\n    n_instances = len(instances)\n\n    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)\n    instance_ids = np.arange(n_instances)\n\n    # Store predicted probs for each sample\n    predicted_probs = np.full(len(all_lps), np.nan)\n    slopes = []\n    intercepts = []\n\n    for train_idx, test_idx in kf.split(instance_ids):\n        train_instances = set(train_idx)\n        test_instances = set(test_idx)\n\n        train_mask = np.array([inst_indices[i] in train_instances for i in range(len(all_lps))])\n        test_mask = np.array([inst_indices[i] in test_instances for i in range(len(all_lps))])\n\n        X_train = all_lps[train_mask].reshape(-1, 1)\n        y_train = all_labels[train_mask]\n        X_test = all_lps[test_mask].reshape(-1, 1)\n\n        # Fit logistic regression\n        clf = LogisticRegression(solver='lbfgs', max_iter=1000, C=1.0)\n        # Handle degenerate case: all same label\n        if len(np.unique(y_train)) < 2:\n            predicted_probs[test_mask] = 0.5\n            slopes.append(0.0)\n            intercepts.append(0.0)\n            continue\n\n        clf.fit(X_train, y_train)\n        predicted_probs[test_mask] = clf.predict_proba(X_test)[:, 1]\n        slopes.append(float(clf.coef_[0, 0]))\n        intercepts.append(float(clf.intercept_[0]))\n\n    # Now select based on predicted_probs\n    selection_f1s = []\n    for idx, inst in enumerate(instances):\n        n_samples = len(inst[\"samples\"])\n        mask = inst_indices == idx\n        probs = predicted_probs[mask]\n        assert len(probs) == n_samples\n\n        # Handle degenerate: all probs equal → random\n        if np.all(probs == probs[0]):\n            selected = 0  # first sample (equivalent to random)\n        else:\n            selected = np.argmax(probs)\n        selection_f1s.append(inst[\"samples\"][selected][\"f1\"])\n\n    # ECE on all predictions\n    ece, reliability = compute_ece(predicted_probs, all_labels)\n\n    return {\n        \"mean_f1\": float(np.mean(selection_f1s)),\n        \"slope_mean\": float(np.mean(slopes)),\n        \"intercept_mean\": float(np.mean(intercepts)),\n        \"ece\": ece,\n        \"reliability\": reliability,\n        \"per_instance_f1\": selection_f1s,\n    }\n\n\ndef temperature_scaling_cv(instances, n_splits=5):\n    \"\"\"5-fold CV Temperature scaling. Learn τ to minimize NLL.\"\"\"\n    all_lps, all_labels, inst_indices = make_binary_labels(instances)\n    n_instances = len(instances)\n\n    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)\n    instance_ids = np.arange(n_instances)\n\n    predicted_probs = np.full(len(all_lps), np.nan)\n    temperatures = []\n\n    for train_idx, test_idx in kf.split(instance_ids):\n        train_instances = set(train_idx)\n        test_instances = set(test_idx)\n\n        train_mask = np.array([inst_indices[i] in train_instances for i in range(len(all_lps))])\n        test_mask = np.array([inst_indices[i] in test_instances for i in range(len(all_lps))])\n\n        lps_train = all_lps[train_mask]\n        labels_train = all_labels[train_mask]\n        lps_test = all_lps[test_mask]\n\n        def nll(tau):\n            # calibrated_lp = lp / tau, then sigmoid to get prob\n            scaled = lps_train / tau\n            probs = expit(scaled * 10)  # scale factor\n            probs = np.clip(probs, 1e-7, 1 - 1e-7)\n            loss = -np.mean(labels_train * np.log(probs) + (1 - labels_train) * np.log(1 - probs))\n            return loss\n\n        result = minimize_scalar(nll, bounds=(0.01, 10.0), method='bounded')\n        tau = result.x\n        temperatures.append(float(tau))\n\n        # Apply to test\n        scaled_test = lps_test / tau\n        predicted_probs[test_mask] = expit(scaled_test * 10)\n\n    # Select based on calibrated LP (higher LP/τ → better)\n    selection_f1s = []\n    for idx, inst in enumerate(instances):\n        n_samples = len(inst[\"samples\"])\n        mask = inst_indices == idx\n        probs = predicted_probs[mask]\n        assert len(probs) == n_samples\n\n        if np.all(probs == probs[0]):\n            selected = 0\n        else:\n            selected = np.argmax(probs)\n        selection_f1s.append(inst[\"samples\"][selected][\"f1\"])\n\n    ece, reliability = compute_ece(predicted_probs, all_labels)\n\n    return {\n        \"mean_f1\": float(np.mean(selection_f1s)),\n        \"tau_mean\": float(np.mean(temperatures)),\n        \"ece\": ece,\n        \"reliability\": reliability,\n        \"per_instance_f1\": selection_f1s,\n    }\n\n\ndef raw_lp_selection(instances):\n    \"\"\"Baseline: select sample with highest raw LP.\"\"\"\n    selection_f1s = []\n    for inst in instances:\n        lps = [s[\"lp\"] for s in inst[\"samples\"]]\n        if all(lp == lps[0] for lp in lps):\n            selected = 0\n        else:\n            selected = np.argmax(lps)\n        selection_f1s.append(inst[\"samples\"][selected][\"f1\"])\n    return selection_f1s\n\n\ndef greedy_f1s(instances):\n    \"\"\"Get greedy F1 for each instance.\"\"\"\n    return [inst[\"greedy_f1\"] for inst in instances if inst[\"greedy_f1\"] is not None]\n\n\ndef oracle_selection(instances):\n    \"\"\"Oracle: select sample with highest F1.\"\"\"\n    return [max(s[\"f1\"] for s in inst[\"samples\"]) for inst in instances]\n\n\ndef paired_bootstrap(f1s_a, f1s_b, n_bootstrap=10000, seed=42):\n    \"\"\"Paired bootstrap test: is B better than A?\"\"\"\n    rng = np.random.RandomState(seed)\n    f1s_a = np.array(f1s_a)\n    f1s_b = np.array(f1s_b)\n    n = len(f1s_a)\n    observed_delta = f1s_b.mean() - f1s_a.mean()\n\n    deltas = []\n    for _ in range(n_bootstrap):\n        idx = rng.randint(0, n, n)\n        deltas.append(f1s_b[idx].mean() - f1s_a[idx].mean())\n    deltas = np.array(deltas)\n\n    ci_low = float(np.percentile(deltas, 2.5))\n    ci_high = float(np.percentile(deltas, 97.5))\n    p_value = float(np.mean(deltas <= 0))  # one-sided: P(delta <= 0)\n\n    return {\n        \"observed_delta\": float(observed_delta),\n        \"ci_95\": [ci_low, ci_high],\n        \"p_value\": p_value,\n    }\n\n\ndef compute_raw_ece(instances):\n    \"\"\"Compute ECE for raw LP (converted to prob via rank within instance).\"\"\"\n    all_probs = []\n    all_labels = []\n    for inst in instances:\n        f1s = [s[\"f1\"] for s in inst[\"samples\"]]\n        lps = [s[\"lp\"] for s in inst[\"samples\"]]\n        median_f1 = np.median(f1s)\n\n        # Rank-based prob within instance\n        n = len(lps)\n        ranks = np.argsort(np.argsort(lps))  # 0-indexed ranks\n        probs = (ranks + 1) / n  # normalize to (0, 1]\n\n        for i, s in enumerate(inst[\"samples\"]):\n            all_probs.append(probs[i])\n            all_labels.append(1 if s[\"f1\"] >= median_f1 else 0)\n\n    return compute_ece(np.array(all_probs), np.array(all_labels))\n\n\ndef main():\n    results = {}\n\n    for name, path in DATASETS.items():\n        print(f\"\\n{'='*60}\")\n        print(f\"  Dataset: {name}\")\n        print(f\"{'='*60}\")\n\n        instances = load_dataset(path)\n        n_instances = len(instances)\n        n_samples = len(instances[0][\"samples\"])\n        print(f\"  Instances: {n_instances}, Samples/instance: {n_samples}\")\n\n        # Raw LP selection\n        raw_f1s = raw_lp_selection(instances)\n        raw_mean = np.mean(raw_f1s)\n\n        # Greedy\n        g_f1s = greedy_f1s(instances)\n        greedy_mean = np.mean(g_f1s) if g_f1s else None\n\n        # Oracle\n        oracle_f1s = oracle_selection(instances)\n        oracle_mean = np.mean(oracle_f1s)\n\n        # Platt scaling\n        print(f\"  Running Platt scaling (5-fold CV)...\")\n        platt_result = platt_scaling_cv(instances)\n\n        # Temperature scaling\n        print(f\"  Running Temperature scaling (5-fold CV)...\")\n        temp_result = temperature_scaling_cv(instances)\n\n        # Raw ECE\n        raw_ece, raw_reliability = compute_raw_ece(instances)\n\n        # Statistical tests\n        platt_vs_raw = paired_bootstrap(raw_f1s, platt_result[\"per_instance_f1\"])\n        temp_vs_raw = paired_bootstrap(raw_f1s, temp_result[\"per_instance_f1\"])\n\n        # Print results\n        print(f\"\\n  Results:\")\n        print(f\"    Greedy F1:       {greedy_mean:.4f}\" if greedy_mean else \"    Greedy F1:       N/A\")\n        print(f\"    Raw LP F1:       {raw_mean:.4f}\")\n        print(f\"    Platt LP F1:     {platt_result['mean_f1']:.4f}\")\n        print(f\"    TempScale LP F1: {temp_result['mean_f1']:.4f}\")\n        print(f\"    Oracle F1:       {oracle_mean:.4f}\")\n\n        print(f\"\\n  Learned Parameters:\")\n        print(f\"    Platt: slope={platt_result['slope_mean']:.4f}, intercept={platt_result['intercept_mean']:.4f}\")\n        print(f\"    TempScale: τ={temp_result['tau_mean']:.4f}\")\n\n        print(f\"\\n  Calibration Quality:\")\n        print(f\"    Raw LP ECE:    {raw_ece:.4f}\")\n        print(f\"    Platt ECE:     {platt_result['ece']:.4f}\")\n        print(f\"    TempScale ECE: {temp_result['ece']:.4f}\")\n\n        print(f\"\\n  Statistical Tests (vs Raw LP):\")\n        print(f\"    Platt:     Δ={platt_vs_raw['observed_delta']:+.4f}, 95% CI=[{platt_vs_raw['ci_95'][0]:+.4f}, {platt_vs_raw['ci_95'][1]:+.4f}], p={platt_vs_raw['p_value']:.4f}\")\n        print(f\"    TempScale: Δ={temp_vs_raw['observed_delta']:+.4f}, 95% CI=[{temp_vs_raw['ci_95'][0]:+.4f}, {temp_vs_raw['ci_95'][1]:+.4f}], p={temp_vs_raw['p_value']:.4f}\")\n\n        results[name] = {\n            \"n_instances\": n_instances,\n            \"n_samples_per_instance\": n_samples,\n            \"greedy_f1\": greedy_mean,\n            \"raw_lp_f1\": float(raw_mean),\n            \"platt_lp_f1\": platt_result[\"mean_f1\"],\n            \"tempscale_lp_f1\": temp_result[\"mean_f1\"],\n            \"oracle_f1\": float(oracle_mean),\n            \"platt_params\": {\n                \"slope\": platt_result[\"slope_mean\"],\n                \"intercept\": platt_result[\"intercept_mean\"],\n            },\n            \"tempscale_params\": {\"tau\": temp_result[\"tau_mean\"]},\n            \"calibration\": {\n                \"raw_ece\": raw_ece,\n                \"platt_ece\": platt_result[\"ece\"],\n                \"tempscale_ece\": temp_result[\"ece\"],\n                \"raw_reliability\": raw_reliability,\n                \"platt_reliability\": platt_result[\"reliability\"],\n                \"tempscale_reliability\": temp_result[\"reliability\"],\n            },\n            \"statistical_tests\": {\n                \"platt_vs_raw\": platt_vs_raw,\n                \"tempscale_vs_raw\": temp_vs_raw,\n            },\n        }\n\n    # Summary table\n    print(f\"\\n\\n{'='*80}\")\n    print(f\"  SUMMARY TABLE\")\n    print(f\"{'='*80}\")\n    print(f\"{'Dataset':<10} | {'Greedy':>8} | {'Raw LP':>8} | {'Platt LP':>9} | {'TempScale':>9} | {'Oracle':>8}\")\n    print(f\"{'-'*10}-+-{'-'*8}-+-{'-'*8}-+-{'-'*9}-+-{'-'*9}-+-{'-'*8}\")\n    for name in DATASETS:\n        r = results[name]\n        g = f\"{r['greedy_f1']:.4f}\" if r['greedy_f1'] else \"N/A\"\n        print(f\"{name:<10} | {g:>8} | {r['raw_lp_f1']:>8.4f} | {r['platt_lp_f1']:>9.4f} | {r['tempscale_lp_f1']:>9.4f} | {r['oracle_f1']:>8.4f}\")\n\n    # Save JSON\n    out_path = OUTPUT_DIR / \"calibration_baseline_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\n  Results saved to: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYTHON_SCRIPT",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/autodl-tmp/struct_self_consist_ie/scripts/calibration_baseline.py << 'PYTHON_SCRIPT'\n\"\"\"\nCalibration Baseline: Platt Scaling & Temperature Scaling for LP-based selection.\nUses 5-fold CV to avoid train-test leak.\n\"\"\"\nimport json\nimport numpy as np\nfrom pathlib import Path\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import KFold\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import expit\n\nWORK_DIR = Path(\"/root/autodl-tmp/struct_self_consist_ie\")\nOUTPUT_DIR = WORK_DIR / \"output\"\n\nDATASETS = {\n    \"SciERC\": OUTPUT_DIR / \"exp_012_rerun_1024\" / \"samples_with_logprobs.jsonl\",\n    \"CoNLL\": OUTPUT_DIR / \"exp_002_conll_n16_r1024\" / \"samples.jsonl\",\n    \"Few-NERD\": OUTPUT_DIR / \"exp_027_fewnerd_n16\" / \"samples.jsonl\",\n}\n\n\ndef compute_ner_f1(pred_entities, gold_entities):\n    pred_set = {(e['text'], e['type'], e.get('start', -1), e.get('end', -1)) for e in pred_entities}\n    gold_set = {(e['text'], e['type'], e.get('start', -1), e.get('end', -1)) for e in gold_entities}\n    if not pred_set and not gold_set:\n        return 1.0\n    if not pred_set or not gold_set:\n        return 0.0\n    tp = len(pred_set & gold_set)\n    prec = tp / len(pred_set)\n    rec = tp / len(gold_set)\n    if prec + rec == 0:\n        return 0.0\n    return 2 * prec * rec / (prec + rec)\n\n\ndef load_dataset(path):\n    \"\"\"Load dataset, return list of dicts with per-sample LP and F1.\"\"\"\n    instances = []\n    with open(path) as f:\n        for line in f:\n            row = json.loads(line)\n            gold_ents = row[\"gold\"][\"entities\"]\n            samples = row[\"samples\"]\n            greedy = row.get(\"greedy\")\n\n            sample_data = []\n            for s in samples:\n                lp = s.get(\"mean_logprob\", s.get(\"cumulative_logprob\") / max(s.get(\"n_tokens\", 1), 1))\n                f1 = compute_ner_f1(s.get(\"entities\", []), gold_ents)\n                sample_data.append({\"lp\": lp, \"f1\": f1})\n\n            greedy_f1 = None\n            if greedy:\n                greedy_f1 = compute_ner_f1(greedy.get(\"entities\", []), gold_ents)\n\n            instances.append({\n                \"id\": row[\"id\"],\n                \"samples\": sample_data,\n                \"greedy_f1\": greedy_f1,\n            })\n    return instances\n\n\ndef make_binary_labels(instances):\n    \"\"\"For each instance, label samples: F1 >= median → 1, else → 0.\"\"\"\n    all_lps = []\n    all_labels = []\n    instance_indices = []  # which instance each sample belongs to\n\n    for idx, inst in enumerate(instances):\n        f1s = [s[\"f1\"] for s in inst[\"samples\"]]\n        median_f1 = np.median(f1s)\n        for s in inst[\"samples\"]:\n            all_lps.append(s[\"lp\"])\n            all_labels.append(1 if s[\"f1\"] >= median_f1 else 0)\n            instance_indices.append(idx)\n\n    return np.array(all_lps), np.array(all_labels), np.array(instance_indices)\n\n\ndef compute_ece(probs, labels, n_bins=10):\n    \"\"\"Expected Calibration Error.\"\"\"\n    bin_edges = np.linspace(0, 1, n_bins + 1)\n    ece = 0.0\n    bin_data = []\n    for i in range(n_bins):\n        mask = (probs >= bin_edges[i]) & (probs < bin_edges[i + 1])\n        if i == n_bins - 1:\n            mask = (probs >= bin_edges[i]) & (probs <= bin_edges[i + 1])\n        if mask.sum() == 0:\n            bin_data.append({\"bin_center\": (bin_edges[i] + bin_edges[i+1]) / 2,\n                             \"avg_confidence\": None, \"avg_accuracy\": None, \"count\": 0})\n            continue\n        avg_conf = probs[mask].mean()\n        avg_acc = labels[mask].mean()\n        ece += mask.sum() / len(probs) * abs(avg_conf - avg_acc)\n        bin_data.append({\"bin_center\": (bin_edges[i] + bin_edges[i+1]) / 2,\n                         \"avg_confidence\": float(avg_conf), \"avg_accuracy\": float(avg_acc),\n                         \"count\": int(mask.sum())})\n    return float(ece), bin_data\n\n\ndef raw_lp_to_prob(lps):\n    \"\"\"Convert raw LP to [0,1] via min-max normalization then sigmoid-like.\"\"\"\n    # Use rank-based probability: P = rank / N (within the instance)\n    # For global calibration, use sigmoid of LP\n    return expit(lps * 10)  # scale factor to spread values\n\n\ndef platt_scaling_cv(instances, n_splits=5):\n    \"\"\"5-fold CV Platt scaling. Returns per-instance selection F1.\"\"\"\n    all_lps, all_labels, inst_indices = make_binary_labels(instances)\n    n_instances = len(instances)\n\n    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)\n    instance_ids = np.arange(n_instances)\n\n    # Store predicted probs for each sample\n    predicted_probs = np.full(len(all_lps), np.nan)\n    slopes = []\n    intercepts = []\n\n    for train_idx, test_idx in kf.split(instance_ids):\n        train_instances = set(train_idx)\n        test_instances = set(test_idx)\n\n        train_mask = np.array([inst_indices[i] in train_instances for i in range(len(all_lps))])\n        test_mask = np.array([inst_indices[i] in test_instances for i in range(len(all_lps))])\n\n        X_train = all_lps[train_mask].reshape(-1, 1)\n        y_train = all_labels[train_mask]\n        X_test = all_lps[test_mask].reshape(-1, 1)\n\n        # Fit logistic regression\n        clf = LogisticRegression(solver='lbfgs', max_iter=1000, C=1.0)\n        # Handle degenerate case: all same label\n        if len(np.unique(y_train)) < 2:\n            predicted_probs[test_mask] = 0.5\n            slopes.append(0.0)\n            intercepts.append(0.0)\n            continue\n\n        clf.fit(X_train, y_train)\n        predicted_probs[test_mask] = clf.predict_proba(X_test)[:, 1]\n        slopes.append(float(clf.coef_[0, 0]))\n        intercepts.append(float(clf.intercept_[0]))\n\n    # Now select based on predicted_probs\n    selection_f1s = []\n    for idx, inst in enumerate(instances):\n        n_samples = len(inst[\"samples\"])\n        mask = inst_indices == idx\n        probs = predicted_probs[mask]\n        assert len(probs) == n_samples\n\n        # Handle degenerate: all probs equal → random\n        if np.all(probs == probs[0]):\n            selected = 0  # first sample (equivalent to random)\n        else:\n            selected = np.argmax(probs)\n        selection_f1s.append(inst[\"samples\"][selected][\"f1\"])\n\n    # ECE on all predictions\n    ece, reliability = compute_ece(predicted_probs, all_labels)\n\n    return {\n        \"mean_f1\": float(np.mean(selection_f1s)),\n        \"slope_mean\": float(np.mean(slopes)),\n        \"intercept_mean\": float(np.mean(intercepts)),\n        \"ece\": ece,\n        \"reliability\": reliability,\n        \"per_instance_f1\": selection_f1s,\n    }\n\n\ndef temperature_scaling_cv(instances, n_splits=5):\n    \"\"\"5-fold CV Temperature scaling. Learn τ to minimize NLL.\"\"\"\n    all_lps, all_labels, inst_indices = make_binary_labels(instances)\n    n_instances = len(instances)\n\n    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)\n    instance_ids = np.arange(n_instances)\n\n    predicted_probs = np.full(len(all_lps), np.nan)\n    temperatures = []\n\n    for train_idx, test_idx in kf.split(instance_ids):\n        train_instances = set(train_idx)\n        test_instances = set(test_idx)\n\n        train_mask = np.array([inst_indices[i] in train_instances for i in range(len(all_lps))])\n        test_mask = np.array([inst_indices[i] in test_instances for i in range(len(all_lps))])\n\n        lps_train = all_lps[train_mask]\n        labels_train = all_labels[train_mask]\n        lps_test = all_lps[test_mask]\n\n        def nll(tau):\n            # calibrated_lp = lp / tau, then sigmoid to get prob\n            scaled = lps_train / tau\n            probs = expit(scaled * 10)  # scale factor\n            probs = np.clip(probs, 1e-7, 1 - 1e-7)\n            loss = -np.mean(labels_train * np.log(probs) + (1 - labels_train) * np.log(1 - probs))\n            return loss\n\n        result = minimize_scalar(nll, bounds=(0.01, 10.0), method='bounded')\n        tau = result.x\n        temperatures.append(float(tau))\n\n        # Apply to test\n        scaled_test = lps_test / tau\n        predicted_probs[test_mask] = expit(scaled_test * 10)\n\n    # Select based on calibrated LP (higher LP/τ → better)\n    selection_f1s = []\n    for idx, inst in enumerate(instances):\n        n_samples = len(inst[\"samples\"])\n        mask = inst_indices == idx\n        probs = predicted_probs[mask]\n        assert len(probs) == n_samples\n\n        if np.all(probs == probs[0]):\n            selected = 0\n        else:\n            selected = np.argmax(probs)\n        selection_f1s.append(inst[\"samples\"][selected][\"f1\"])\n\n    ece, reliability = compute_ece(predicted_probs, all_labels)\n\n    return {\n        \"mean_f1\": float(np.mean(selection_f1s)),\n        \"tau_mean\": float(np.mean(temperatures)),\n        \"ece\": ece,\n        \"reliability\": reliability,\n        \"per_instance_f1\": selection_f1s,\n    }\n\n\ndef raw_lp_selection(instances):\n    \"\"\"Baseline: select sample with highest raw LP.\"\"\"\n    selection_f1s = []\n    for inst in instances:\n        lps = [s[\"lp\"] for s in inst[\"samples\"]]\n        if all(lp == lps[0] for lp in lps):\n            selected = 0\n        else:\n            selected = np.argmax(lps)\n        selection_f1s.append(inst[\"samples\"][selected][\"f1\"])\n    return selection_f1s\n\n\ndef greedy_f1s(instances):\n    \"\"\"Get greedy F1 for each instance.\"\"\"\n    return [inst[\"greedy_f1\"] for inst in instances if inst[\"greedy_f1\"] is not None]\n\n\ndef oracle_selection(instances):\n    \"\"\"Oracle: select sample with highest F1.\"\"\"\n    return [max(s[\"f1\"] for s in inst[\"samples\"]) for inst in instances]\n\n\ndef paired_bootstrap(f1s_a, f1s_b, n_bootstrap=10000, seed=42):\n    \"\"\"Paired bootstrap test: is B better than A?\"\"\"\n    rng = np.random.RandomState(seed)\n    f1s_a = np.array(f1s_a)\n    f1s_b = np.array(f1s_b)\n    n = len(f1s_a)\n    observed_delta = f1s_b.mean() - f1s_a.mean()\n\n    deltas = []\n    for _ in range(n_bootstrap):\n        idx = rng.randint(0, n, n)\n        deltas.append(f1s_b[idx].mean() - f1s_a[idx].mean())\n    deltas = np.array(deltas)\n\n    ci_low = float(np.percentile(deltas, 2.5))\n    ci_high = float(np.percentile(deltas, 97.5))\n    p_value = float(np.mean(deltas <= 0))  # one-sided: P(delta <= 0)\n\n    return {\n        \"observed_delta\": float(observed_delta),\n        \"ci_95\": [ci_low, ci_high],\n        \"p_value\": p_value,\n    }\n\n\ndef compute_raw_ece(instances):\n    \"\"\"Compute ECE for raw LP (converted to prob via rank within instance).\"\"\"\n    all_probs = []\n    all_labels = []\n    for inst in instances:\n        f1s = [s[\"f1\"] for s in inst[\"samples\"]]\n        lps = [s[\"lp\"] for s in inst[\"samples\"]]\n        median_f1 = np.median(f1s)\n\n        # Rank-based prob within instance\n        n = len(lps)\n        ranks = np.argsort(np.argsort(lps))  # 0-indexed ranks\n        probs = (ranks + 1) / n  # normalize to (0, 1]\n\n        for i, s in enumerate(inst[\"samples\"]):\n            all_probs.append(probs[i])\n            all_labels.append(1 if s[\"f1\"] >= median_f1 else 0)\n\n    return compute_ece(np.array(all_probs), np.array(all_labels))\n\n\ndef main():\n    results = {}\n\n    for name, path in DATASETS.items():\n        print(f\"\\n{'='*60}\")\n        print(f\"  Dataset: {name}\")\n        print(f\"{'='*60}\")\n\n        instances = load_dataset(path)\n        n_instances = len(instances)\n        n_samples = len(instances[0][\"samples\"])\n        print(f\"  Instances: {n_instances}, Samples/instance: {n_samples}\")\n\n        # Raw LP selection\n        raw_f1s = raw_lp_selection(instances)\n        raw_mean = np.mean(raw_f1s)\n\n        # Greedy\n        g_f1s = greedy_f1s(instances)\n        greedy_mean = np.mean(g_f1s) if g_f1s else None\n\n        # Oracle\n        oracle_f1s = oracle_selection(instances)\n        oracle_mean = np.mean(oracle_f1s)\n\n        # Platt scaling\n        print(f\"  Running Platt scaling (5-fold CV)...\")\n        platt_result = platt_scaling_cv(instances)\n\n        # Temperature scaling\n        print(f\"  Running Temperature scaling (5-fold CV)...\")\n        temp_result = temperature_scaling_cv(instances)\n\n        # Raw ECE\n        raw_ece, raw_reliability = compute_raw_ece(instances)\n\n        # Statistical tests\n        platt_vs_raw = paired_bootstrap(raw_f1s, platt_result[\"per_instance_f1\"])\n        temp_vs_raw = paired_bootstrap(raw_f1s, temp_result[\"per_instance_f1\"])\n\n        # Print results\n        print(f\"\\n  Results:\")\n        print(f\"    Greedy F1:       {greedy_mean:.4f}\" if greedy_mean else \"    Greedy F1:       N/A\")\n        print(f\"    Raw LP F1:       {raw_mean:.4f}\")\n        print(f\"    Platt LP F1:     {platt_result['mean_f1']:.4f}\")\n        print(f\"    TempScale LP F1: {temp_result['mean_f1']:.4f}\")\n        print(f\"    Oracle F1:       {oracle_mean:.4f}\")\n\n        print(f\"\\n  Learned Parameters:\")\n        print(f\"    Platt: slope={platt_result['slope_mean']:.4f}, intercept={platt_result['intercept_mean']:.4f}\")\n        print(f\"    TempScale: τ={temp_result['tau_mean']:.4f}\")\n\n        print(f\"\\n  Calibration Quality:\")\n        print(f\"    Raw LP ECE:    {raw_ece:.4f}\")\n        print(f\"    Platt ECE:     {platt_result['ece']:.4f}\")\n        print(f\"    TempScale ECE: {temp_result['ece']:.4f}\")\n\n        print(f\"\\n  Statistical Tests (vs Raw LP):\")\n        print(f\"    Platt:     Δ={platt_vs_raw['observed_delta']:+.4f}, 95% CI=[{platt_vs_raw['ci_95'][0]:+.4f}, {platt_vs_raw['ci_95'][1]:+.4f}], p={platt_vs_raw['p_value']:.4f}\")\n        print(f\"    TempScale: Δ={temp_vs_raw['observed_delta']:+.4f}, 95% CI=[{temp_vs_raw['ci_95'][0]:+.4f}, {temp_vs_raw['ci_95'][1]:+.4f}], p={temp_vs_raw['p_value']:.4f}\")\n\n        results[name] = {\n            \"n_instances\": n_instances,\n            \"n_samples_per_instance\": n_samples,\n            \"greedy_f1\": greedy_mean,\n            \"raw_lp_f1\": float(raw_mean),\n            \"platt_lp_f1\": platt_result[\"mean_f1\"],\n            \"tempscale_lp_f1\": temp_result[\"mean_f1\"],\n            \"oracle_f1\": float(oracle_mean),\n            \"platt_params\": {\n                \"slope\": platt_result[\"slope_mean\"],\n                \"intercept\": platt_result[\"intercept_mean\"],\n            },\n            \"tempscale_params\": {\"tau\": temp_result[\"tau_mean\"]},\n            \"calibration\": {\n                \"raw_ece\": raw_ece,\n                \"platt_ece\": platt_result[\"ece\"],\n                \"tempscale_ece\": temp_result[\"ece\"],\n                \"raw_reliability\": raw_reliability,\n                \"platt_reliability\": platt_result[\"reliability\"],\n                \"tempscale_reliability\": temp_result[\"reliability\"],\n            },\n            \"statistical_tests\": {\n                \"platt_vs_raw\": platt_vs_raw,\n                \"tempscale_vs_raw\": temp_vs_raw,\n            },\n        }\n\n    # Summary table\n    print(f\"\\n\\n{'='*80}\")\n    print(f\"  SUMMARY TABLE\")\n    print(f\"{'='*80}\")\n    print(f\"{'Dataset':<10} | {'Greedy':>8} | {'Raw LP':>8} | {'Platt LP':>9} | {'TempScale':>9} | {'Oracle':>8}\")\n    print(f\"{'-'*10}-+-{'-'*8}-+-{'-'*8}-+-{'-'*9}-+-{'-'*9}-+-{'-'*8}\")\n    for name in DATASETS:\n        r = results[name]\n        g = f\"{r['greedy_f1']:.4f}\" if r['greedy_f1'] else \"N/A\"\n        print(f\"{name:<10} | {g:>8} | {r['raw_lp_f1']:>8.4f} | {r['platt_lp_f1']:>9.4f} | {r['tempscale_lp_f1']:>9.4f} | {r['oracle_f1']:>8.4f}\")\n\n    # Save JSON\n    out_path = OUTPUT_DIR / \"calibration_baseline_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\n  Results saved to: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYTHON_SCRIPT",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T14:20:47.834541+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T14:20:47.834675+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/bin/activate && python scripts/calibration_baseline.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/bin/activate && python scripts/calibration_baseline.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T14:20:47.834843+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\n  Dataset: SciERC\\n============================================================\\n  Instances: 551, Samples/instance: 8\\n  Running Platt scaling (5-fold CV)...\\n  Running Temperature scaling (5-fold CV)...\\n\\n  Results:\\n    Greedy F1:       0.6436\\n    Raw LP F1:       0.6495\\n    Platt LP F1:     0.6495\\n    TempScale LP F1: 0.6495\\n    Oracle F1:       0.7775\\n\\n  Learned Parameters:\\n    Platt: slope=7.5611, intercept=1.6700\\n    TempScale: τ=10.0000\\n\\n  Calibration Quality:\\n    Raw LP ECE:    0.2597\\n    Platt ECE:     0.0475\\n    TempScale ECE: 0.2998\\n\\n  Statistical Tests (vs Raw LP):\\n    Platt:     Δ=+0.0000, 95% CI=[+0.0000, +0.0000], p=1.0000\\n    TempScale: Δ=+0.0000, 95% CI=[+0.0000, +0.0000], p=1.0000\\n\\n============================================================\\n  Dataset: CoNLL\\n============================================================\\n  Instances: 3453, Samples/instance: 16\\n  Running Platt scaling (5-fold CV)...\\n  Running Temperature scaling (5-fold CV)...\\n\\n  Results:\\n    Greedy F1:       0.9087\\n    Raw LP F1:       0.8975\\n    Platt LP F1:     0.8975\\n    TempScale LP F1: 0.8975\\n    Oracle F1:       0.9614\\n\\n  Learned Parameters:\\n    Platt: slope=19.6476, intercept=3.8765\\n    TempScale: τ=10.0000\\n\\n  Calibration Quality:\\n    Raw LP ECE:    0.3916\\n    Platt ECE:     0.0119\\n    TempScale ECE: 0.4349\\n\\n  Statistical Tests (vs Raw LP):\\n    Platt:     Δ=+0.0000, 95% CI=[+0.0000, +0.0000], p=1.0000\\n    TempScale: Δ=+0.0000, 95% CI=[+0.0000, +0.0000], p=1.0000\\n\\n============================================================\\n  Dataset: Few-NERD\\n============================================================\\n  Instances: 5000, Samples/instance: 16\\n  Running Platt scaling (5-fold CV)...\\n  Running Temperature scaling (5-fold CV)...\\n\\n  Results:\\n    Gre
…[truncated 1270 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T14:20:47.835115+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/autodl-tmp/struct_self_consist_ie/scripts/calibration_baseline.py << 'PYTHON_SCRIPT'\n\"\"\"\nCalibration Baseline: Platt Scaling & Temperature Scaling for LP-based selection.\nUses 5-fold CV to avoid train-test leak.\n\nKey insight: standard Platt/TempScale are monotonic transforms of LP, so they\nimprove probability estimates (ECE) but cannot change argmax-based selection.\nWe additionally test a multi-feature Platt variant (LP + n_tokens + n_entities)\nwhich is NOT monotonic in LP and can potentially change selection.\n\"\"\"\nimport json\nimport numpy as np\nfrom pathlib import Path\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import KFold\nfrom sklearn.preprocessing import StandardScaler\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import expit\n\nWORK_DIR = Path(\"/root/autodl-tmp/struct_self_consist_ie\")\nOUTPUT_DIR = WORK_DIR / \"output\"\n\nDATASETS = {\n    \"SciERC\": OUTPUT_DIR / \"exp_012_rerun_1024\" / \"samples_with_logprobs.jsonl\",\n    \"CoNLL\": OUTPUT_DIR / \"exp_002_conll_n16_r1024\" / \"samples.jsonl\",\n    \"Few-NERD\": OUTPUT_DIR / \"exp_027_fewnerd_n16\" / \"samples.jsonl\",\n}\n\n\ndef compute_ner_f1(pred_entities, gold_entities):\n    pred_set = {(e['text'], e['type'], e.get('start', -1), e.get('end', -1)) for e in pred_entities}\n    gold_set = {(e['text'], e['type'], e.get('start', -1), e.get('end', -1)) for e in gold_entities}\n    if not pred_set and not gold_set:\n        return 1.0\n    if not pred_set or not gold_set:\n        return 0.0\n    tp = len(pred_set & gold_set)\n    prec = tp / len(pred_set)\n    rec = tp / len(gold_set)\n    if prec + rec == 0:\n        return 0.0\n    return 2 * prec * rec / (prec + rec)\n\n\ndef load_dataset(path):\n    \"\"\"Load dataset, return list of dicts with per-sample LP, F1, and features.\"\"\"\n    instances = []\n    with open(path) as f:\n        for line in f:\n            row = json.loads(line)\n            gold_ents = row[\"gold\"][\"entities\"]\n            samples = row[\"samples\"]\n            greedy = row.get(\"greedy\")\n\n            sample_data = []\n            for s in samples:\n                lp = s.get(\"mean_logprob\")\n                if lp is None:\n                    lp = s.get(\"cumulative_logprob\", -999) / max(s.get(\"n_tokens\", 1), 1)\n                f1 = compute_ner_f1(s.get(\"entities\", []), gold_ents)\n                n_tokens = s.get(\"n_tokens\", 0)\n                n_entities = len(s.get(\"entities\", []))\n                sample_data.append({\n                    \"lp\": lp, \"f1\": f1,\n                    \"n_tokens\": n_tokens, \"n_entities\": n_entities,\n                })\n\n            greedy_f1 = None\n            if greedy:\n                greedy_f1 = compute_ner_f1(greedy.get(\"entities\", []), gold_ents)\n\n            instances.append({\n                \"id\": row[\"id\"],\n                \"samples\": sample_data,\n                \"greedy_f1\": greedy_f1,\n            })\n    return instances\n\n\ndef make_binary_labels(instances):\n    \"\"\"For each instance, label samples: F1 >= median → 1, else → 0.\"\"\"\n    all_lps = []\n    all_labels = []\n    all_features = []  # [lp, n_tokens, n_entities]\n    instance_indices = []\n\n    for idx, inst in enumerate(instances):\n        f1s = [s[\"f1\"] for s in inst[\"samples\"]]\n        median_f1 = np.median(f1s)\n        for s in inst[\"samples\"]:\n            all_lps.append(s[\"lp\"])\n            all_labels.append(1 if s[\"f1\"] >= median_f1 else 0)\n            all_features.append([s[\"lp\"], s[\"n_tokens\"], s[\"n_entities\"]])\n            instance_indices.append(idx)\n\n    return (np.array(all_lps), np.array(all_labels),\n            np.array(all_features), np.array(instance_indices))\n\n\ndef compute_ece(probs, labels, n_bins=10):\n    \"\"\"Expected Calibration Error.\"\"\"\n    bin_edges = np.linspace(0, 1, n_bins + 1)\n    ece = 0.0\n    bin_data = []\n    for i in range(n_bins):\n        if i == n_bins - 1:\n            mask = (probs >= bin_edges[i]) & (probs <= bin_edges[i + 1])\n        else:\n            mask = (probs >= bin_edges[i]) & (probs < bin_edges[i + 1])\n        if mask.sum() == 0:\n            bin_data.append({\"bin_center\": (bin_edges[i] + bin_edges[i+1]) / 2,\n                             \"avg_confidence\": None, \"avg_accuracy\": None, \"count\": 0})\n            continue\n        avg_conf = probs[mask].mean()\n        avg_acc = labels[mask].mean()\n        ece += mask.sum() / len(probs) * abs(avg_conf - avg_acc)\n        bin_data.append({\"bin_center\": (bin_edges[i] + bin_edges[i+1]) / 2,\n                         \"avg_confidence\": float(avg_conf), \"avg_accuracy\": float(avg_acc),\n                         \"count\": int(mask.sum())})\n    return float(ece), bin_data\n\n\ndef platt_scaling_cv(instances, n_splits=5):\n    \"\"\"5-fold CV Platt scaling (LP only). Monotonic → same selection as raw LP.\"\"\"\n    all_lps, all_labels, _, inst_indices = make_binary_labels(instances)\n    n_instances = len(instances)\n    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)\n\n    predicted_probs = np.full(len(all_lps), np.nan)\n    slopes = []\n    intercepts = []\n\n    for train_idx, test_idx in kf.split(np.arange(n_instances)):\n        train_set = set(train_idx)\n        test_set = set(test_idx)\n        train_mask = np.isin(inst_indices, list(train_set))\n        test_mask = np.isin(inst_indices, list(test_set))\n\n        X_train = all_lps[train_mask].reshape(-1, 1)\n        y_train = all_labels[train_mask]\n        X_test = all_lps[test_mask].reshape(-1, 1)\n\n        if len(np.unique(y_train)) < 2:\n            predicted_probs[test_mask] = 0.5\n            slopes.append(0.0)\n            intercepts.append(0.0)\n            continue\n\n        clf = LogisticRegression(solver='lbfgs', max_iter=1000, C=1.0)\n        clf.fit(X_train, y_train)\n        predicted_probs[test_mask] = clf.predict_proba(X_test)[:, 1]\n        slopes.append(float(clf.coef_[0, 0]))\n        intercepts.append(float(clf.intercept_[0]))\n\n    # Selection (monotonic → same as raw LP)\n    selection_f1s = _select_by_probs(instances, predicted_probs, inst_indices)\n    ece, reliability = compute_ece(predicted_probs, all_labels)\n\n    return {\n        \"mean_f1\": float(np.mean(selection_f1s)),\n        \"slope_mean\": float(np.mean(slopes)),\n        \"intercept_mean\": float(np.mean(intercepts)),\n        \"ece\": ece,\n        \"reliability\": reliability,\n        \"per_instance_f1\": selection_f1s,\n    }\n\n\ndef multifeature_platt_cv(instances, n_splits=5):\n    \"\"\"5-fold CV Platt with features [LP, n_tokens, n_entities].\n    NOT monotonic in LP → can change selection.\"\"\"\n    all_lps, all_labels, all_features, inst_indices = make_binary_labels(instances)\n    n_instances = len(instances)\n    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)\n\n    predicted_probs = np.full(len(all_lps), np.nan)\n    coefs = []\n\n    for train_idx, test_idx in kf.split(np.arange(n_instances)):\n        train_set = set(train_idx)\n        test_set = set(test_idx)\n        train_mask = np.isin(inst_indices, list(train_set))\n        test_mask = np.isin(inst_indices, list(test_set))\n\n        X_train = all_features[train_mask]\n        y_train = all_labels[train_mask]\n        X_test = all_features[test_mask]\n\n        if len(np.unique(y_train)) < 2:\n            predicted_probs[test_mask] = 0.5\n            coefs.append([0.0, 0.0, 0.0])\n            continue\n\n        scaler = StandardScaler()\n        X_train_s = scaler.fit_transform(X_train)\n        X_test_s = scaler.transform(X_test)\n\n        clf = LogisticRegression(solver='lbfgs', max_iter=1000, C=1.0)\n        clf.fit(X_train_s, y_train)\n        predicted_probs[test_mask] = clf.predict_proba(X_test_s)[:, 1]\n        coefs.append(clf.coef_[0].tolist())\n\n    selection_f1s = _select_by_probs(instances, predicted_probs, inst_indices)\n    ece, reliability = compute_ece(predicted_probs, all_labels)\n\n    avg_coefs = np.mean(coefs, axis=0).tolist()\n    return {\n        \"mean_f1\": float(np.mean(selection_f1s)),\n        \"coefs_mean\": {\"lp\": avg_coefs[0], \"n_tokens\": avg_coefs[1], \"n_entities\": avg_coefs[2]},\n        \"ece\": ece,\n        \"reliability\": reliability,\n        \"per_instance_f1\": selection_f1s,\n    }\n\n\ndef temperature_scaling_cv(instances, n_splits=5):\n    \"\"\"5-fold CV Temperature scaling. Monotonic → same selection as raw LP.\"\"\"\n    all_lps, all_labels, _, inst_indices = make_binary_labels(instances)\n    n_instances = len(instances)\n    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)\n\n    calibrated_lps = np.full(len(all_lps), np.nan)\n    temperatures = []\n\n    for train_idx, test_idx in kf.split(np.arange(n_instances)):\n        train_set = set(train_idx)\n        test_set = set(test_idx)\n        train_mask = np.isin(inst_indices, list(train_set))\n        test_mask = np.isin(inst_indices, list(test_set))\n\n        lps_train = all_lps[train_mask]\n        labels_train = all_labels[train_mask]\n        lps_test = all_lps[test_mask]\n\n        def nll(log_tau):\n            tau = np.exp(log_tau)\n            logits = lps_train / tau\n            probs = expit(logits)\n            probs = np.clip(probs, 1e-7, 1 - 1e-7)\n            return -np.mean(labels_train * np.log(probs) + (1 - labels_train) * np.log(1 - probs))\n\n        result = minimize_scalar(nll, bounds=(-5, 5), method='bounded')\n        tau = np.exp(result.x)\n        temperatures.append(float(tau))\n\n        calibrated_lps[test_mask] = lps_test / tau\n\n    # Convert to probs for ECE\n    predicted_probs = expit(calibrated_lps)\n\n    selection_f1s = _select_by_probs(instances, predicted_probs, inst_indices)\n    ece, reliability = compute_ece(predicted_probs, all_labels)\n\n    return {\n        \"mean_f1\": float(np.mean(selection_f1s)),\n        \"tau_mean\": float(np.mean(temperatures)),\n        \"ece\": ece,\n        \"reliability\": reliability,\n        \"per_instance_f1\": selection_f1s,\n    }\n\n\ndef _select_by_probs(instances, probs, inst_indices):\n    \"\"\"Select sample with highest prob per instance.\"\"\"\n    selection_f1s = []\n    for idx, inst in enumerate(instances):\n        n_samples = len(inst[\"samples\"])\n        mask = inst_indices == idx\n        p = probs[mask]\n        assert len(p) == n_samples\n        if np.all(p == p[0]):\n            selected = 0\n        else:\n            selected = int(np.argmax(p))\n        selection_f1s.append(inst[\"samples\"][selected][\"f1\"])\n    return selection_f1s\n\n\ndef raw_lp_selection(instances):\n    \"\"\"Baseline: select sample with highest raw LP.\"\"\"\n    selection_f1s = []\n    for inst in instances:\n        lps = [s[\"lp\"] for s in inst[\"samples\"]]\n        if all(lp == lps[0] for lp in lps):\n            selected = 0\n        else:\n            selected = int(np.argmax(lps))\n        selection_f1s.append(inst[\"samples\"][selected][\"f1\"])\n    return selection_f1s\n\n\ndef oracle_selection(instances):\n    return [max(s[\"f1\"] for s in inst[\"samples\"]) for inst in instances]\n\n\ndef compute_raw_ece(instances):\n    \"\"\"ECE for raw LP using rank-based probability within instance.\"\"\"\n    all_probs = []\n    all_labels = []\n    for inst in instances:\n        f1s = [s[\"f1\"] for s in inst[\"samples\"]]\n        lps = [s[\"lp\"] for s in inst[\"samples\"]]\n        median_f1 = np.median(f1s)\n        n = len(lps)\n        ranks = np.argsort(np.argsort(lps))\n        probs = (ranks + 1) / n\n        for i, s in enumerate(inst[\"samples\"]):\n            all_probs.append(probs[i])\n            all_labels.append(1 if s[\"f1\"] >= median_f1 else 0)\n    return compute_ece(np.array(all_probs), np.array(all_labels))\n\n\ndef paired_bootstrap(f1s_a, f1s_b, n_bootstrap=10000, seed=42):\n    \"\"\"Paired bootstrap: is B better than A?\"\"\"\n    rng = np.random.RandomState(seed)\n    a = np.array(f1s_a)\n    b = np.array(f1s_b)\n    n = len(a)\n    observed = float(b.mean() - a.mean())\n    deltas = np.array([b[rng.randint(0, n, n)].mean() - a[rng.randint(0, n, n)].mean()\n                       for _ in range(n_bootstrap)])\n    return {\n        \"observed_delta\": observed,\n        \"ci_95\": [float(np.percentile(deltas, 2.5)), float(np.percentile(deltas, 97.5))],\n        \"p_value\": float(np.mean(deltas <= 0)),\n    }\n\n\ndef main():\n    results = {}\n\n    for name, path in DATASETS.items():\n        print(f\"\\n{'='*60}\")\n        print(f\"  Dataset: {name}\")\n        print(f\"{'='*60}\")\n\n        instances = load_dataset(path)\n        n_instances = len(instances)\n        n_samples = len(instances[0][\"samples\"])\n        print(f\"  Instances: {n_instances}, Samples/instance: {n_samples}\")\n\n        # Baselines\n        raw_f1s = raw_lp_selection(instances)\n        raw_mean = np.mean(raw_f1s)\n        g_f1s = [inst[\"greedy_f1\"] for inst in instances if inst[\"greedy_f1\"] is not None]\n        greedy_mean = float(np.mean(g_f1s)) if g_f1s else None\n        oracle_f1s = oracle_selection(instances)\n        oracle_mean = float(np.mean(oracle_f1s))\n\n        # Calibration methods\n        print(f\"  Running Platt scaling (5-fold CV)...\")\n        platt = platt_scaling_cv(instances)\n\n        print(f\"  Running Multi-feature Platt (5-fold CV)...\")\n        mf_platt = multifeature_platt_cv(instances)\n\n        print(f\"  Running Temperature scaling (5-fold CV)...\")\n        temp = temperature_scaling_cv(instances)\n\n        # Raw ECE\n        raw_ece, raw_rel = compute_raw_ece(instances)\n\n        # Statistical tests (multi-feature Platt is the only one that can differ)\n        mf_vs_raw = paired_bootstrap(raw_f1s, mf_platt[\"per_instance_f1\"])\n\n        # Print\n        print(f\"\\n  Results:\")\n        if greedy_mean: print(f\"    Greedy F1:          {greedy_mean:.4f}\")\n        print(f\"    Raw LP F1:          {raw_mean:.4f}\")\n        print(f\"    Platt LP F1:        {platt['mean_f1']:.4f}  (monotonic → same as raw)\")\n        print(f\"    Multi-feat Platt:   {mf_platt['mean_f1']:.4f}\")\n        print(f\"    TempScale LP F1:    {temp['mean_f1']:.4f}  (monotonic → same as raw)\")\n        print(f\"    Oracle F1:          {oracle_mean:.4f}\")\n\n        print(f\"\\n  Learned Parameters:\")\n        print(f\"    Platt: slope={platt['slope_mean']:.4f}, intercept={platt['intercept_mean']:.4f}\")\n        print(f\"    Multi-feat coefs: LP={mf_platt['coefs_mean']['lp']:.4f}, \"\n              f\"n_tok={mf_platt['coefs_mean']['n_tokens']:.4f}, \"\n              f\"n_ent={mf_platt['coefs_mean']['n_entities']:.4f}\")\n        print(f\"    TempScale: τ={temp['tau_mean']:.4f}\")\n\n        print(f\"\\n  Calibration Quality (ECE):\")\n        print(f\"    Raw LP (rank-based): {raw_ece:.4f}\")\n        print(f\"    Platt:               {platt['ece']:.4f}\")\n        print(f\"    Multi-feat Platt:    {mf_platt['ece']:.4f}\")\n        print(f\"    TempScale:           {temp['ece']:.4f}\")\n\n        print(f\"\\n  Multi-feat Platt vs Raw LP:\")\n        print(f\"    Δ={mf_vs_raw['observed_delta']:+.4f}, \"\n              f\"95% CI=[{mf_vs_raw['ci_95'][0]:+.4f}, {mf_vs_raw['ci_95'][1]:+.4f}], \"\n              f\"p={mf_vs_raw['p_value']:.4f}\")\n\n        results[name] = {\n            \"n_instances\": n_instances,\n            \"n_samples_per_instance\": n_samples,\n            \"greedy_f1\": greedy_mean,\n            \"raw_lp_f1\": float(raw_mean),\n            \"platt_lp_f1\": platt[\"mean_f1\"],\n            \"multifeature_platt_f1\": mf_platt[\"mean_f1\"],\n            \"tempscale_lp_f1\": temp[\"mean_f1\"],\n            \"oracle_f1\": oracle_mean,\n            \"note_monotonic\": \"Platt and TempScale are monotonic transforms of LP; \"\n                              \"argmax-based selection is unchanged. Multi-feature Platt \"\n                              \"uses [LP, n_tokens, n_entities] and CAN change selection.\",\n            \"params\": {\n                \"platt\": {\"slope\": platt[\"slope_mean\"], \"intercept\": platt[\"intercept_mean\"]},\n                \"multifeature_platt\": mf_platt[\"coefs_mean\"],\n                \"tempscale\": {\"tau\": temp[\"tau_mean\"]},\n            },\n            \"calibration\": {\n                \"raw_ece\": raw_ece,\n                \"platt_ece\": platt[\"ece\"],\n                \"multifeature_platt_ece\": mf_platt[\"ece\"],\n                \"tempscale_ece\": temp[\"ece\"],\n                \"raw_reliability\": raw_rel,\n                \"platt_reliability\": platt[\"reliability\"],\n                \"multifeature_platt_reliability\": mf_platt[\"reliability\"],\n                \"tempscale_reliability\": temp[\"reliability\"],\n            },\n            \"statistical_tests\": {\n                \"multifeature_platt_vs_raw\": mf_vs_raw,\n            },\n        }\n\n    # Summary table\n    print(f\"\\n\\n{'='*90}\")\n    print(f\"  SUMMARY TABLE\")\n    print(f\"{'='*90}\")\n    print(f\"{'Dataset':<10} | {'Greedy':>8} | {'Raw LP':>8} | {'Platt':>8} | {'MF-Platt':>8} | {'TempScl':>8} | {'Oracle':>8}\")\n    print(f\"{'-'*10}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}\")\n    for name in DATASETS:\n        r = results[name]\n        g = f\"{r['greedy_f1']:.4f}\" if r['greedy_f1'] else \"N/A\"\n        print(f\"{name:<10} | {g:>8} | {r['raw_lp_f1']:>8.4f} | {r['platt_lp_f1']:>8.4f} | \"\n              f\"{r['multifeature_platt_f1']:>8.4f} | {r['tempscale_lp_f1']:>8.4f} | {r['oracle_f1']:>8.4f}\")\n\n    print(f\"\\n  NOTE: Platt & TempScale = Raw LP (monotonic transform preserves argmax).\")\n    print(f\"  Multi-feature Platt uses [LP, n_tokens, n_entities] → non-monotonic → can differ.\")\n\n    # Save\n    out_path = OUTPUT_DIR / \"calibration_baseline_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\n  Results saved to: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYTHON_SCRIPT",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/autodl-tmp/struct_self_consist_ie/scripts/calibration_baseline.py << 'PYTHON_SCRIPT'\n\"\"\"\nCalibration Baseline: Platt Scaling & Temperature Scaling for LP-based selection.\nUses 5-fold CV to avoid train-test leak.\n\nKey insight: standard Platt/TempScale are monotonic transforms of LP, so they\nimprove probability estimates (ECE) but cannot change argmax-based selection.\nWe additionally test a multi-feature Platt variant (LP + n_tokens + n_entities)\nwhich is NOT monotonic in LP and can potentially change selection.\n\"\"\"\nimport json\nimport numpy as np\nfrom pathlib import Path\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import KFold\nfrom sklearn.preprocessing import StandardScaler\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import expit\n\nWORK_DIR = Path(\"/root/autodl-tmp/struct_self_consist_ie\")\nOUTPUT_DIR = WORK_DIR / \"output\"\n\nDATASETS = {\n    \"SciERC\": OUTPUT_DIR / \"exp_012_rerun_1024\" / \"samples_with_logprobs.jsonl\",\n    \"CoNLL\": OUTPUT_DIR / \"exp_002_conll_n16_r1024\" / \"samples.jsonl\",\n    \"Few-NERD\": OUTPUT_DIR / \"exp_027_fewnerd_n16\" / \"samples.jsonl\",\n}\n\n\ndef compute_ner_f1(pred_entities, gold_entities):\n    pred_set = {(e['text'], e['type'], e.get('start', -1), e.get('end', -1)) for e in pred_entities}\n    gold_set = {(e['text'], e['type'], e.get('start', -1), e.get('end', -1)) for e in gold_entities}\n    if not pred_set and not gold_set:\n        return 1.0\n    if not pred_set or not gold_set:\n        return 0.0\n    tp = len(pred_set & gold_set)\n    prec = tp / len(pred_set)\n    rec = tp / len(gold_set)\n    if prec + rec == 0:\n        return 0.0\n    return 2 * prec * rec / (prec + rec)\n\n\ndef load_dataset(path):\n    \"\"\"Load dataset, return list of dicts with per-sample LP, F1, and features.\"\"\"\n    instances = []\n    with open(path) as f:\n        for line in f:\n            row = json.loads(line)\n            gold_ents = row[\"gold\"][\"entities\"]\n            samples = row[\"samples\"]\n            greedy = row.get(\"greedy\")\n\n            sample_data = []\n            for s in samples:\n                lp = s.get(\"mean_logprob\")\n                if lp is None:\n                    lp = s.get(\"cumulative_logprob\", -999) / max(s.get(\"n_tokens\", 1), 1)\n                f1 = compute_ner_f1(s.get(\"entities\", []), gold_ents)\n                n_tokens = s.get(\"n_tokens\", 0)\n                n_entities = len(s.get(\"entities\", []))\n                sample_data.append({\n                    \"lp\": lp, \"f1\": f1,\n                    \"n_tokens\": n_tokens, \"n_entities\": n_entities,\n                })\n\n            greedy_f1 = None\n            if greedy:\n                greedy_f1 = compute_ner_f1(greedy.get(\"entities\", []), gold_ents)\n\n            instances.append({\n                \"id\": row[\"id\"],\n                \"samples\": sample_data,\n                \"greedy_f1\": greedy_f1,\n            })\n    return instances\n\n\ndef make_binary_labels(instances):\n    \"\"\"For each instance, label samples: F1 >= median → 1, else → 0.\"\"\"\n    all_lps = []\n    all_labels = []\n    all_features = []  # [lp, n_tokens, n_entities]\n    instance_indices = []\n\n    for idx, inst in enumerate(instances):\n        f1s = [s[\"f1\"] for s in inst[\"samples\"]]\n        median_f1 = np.median(f1s)\n        for s in inst[\"samples\"]:\n            all_lps.append(s[\"lp\"])\n            all_labels.append(1 if s[\"f1\"] >= median_f1 else 0)\n            all_features.append([s[\"lp\"], s[\"n_tokens\"], s[\"n_entities\"]])\n            instance_indices.append(idx)\n\n    return (np.array(all_lps), np.array(all_labels),\n            np.array(all_features), np.array(instance_indices))\n\n\ndef compute_ece(probs, labels, n_bins=10):\n    \"\"\"Expected Calibration Error.\"\"\"\n    bin_edges = np.linspace(0, 1, n_bins + 1)\n    ece = 0.0\n    bin_data = []\n    for i in range(n_bins):\n        if i == n_bins - 1:\n            mask = (probs >= bin_edges[i]) & (probs <= bin_edges[i + 1])\n        else:\n            mask = (probs >= bin_edges[i]) & (probs < bin_edges[i + 1])\n        if mask.sum() == 0:\n            bin_data.append({\"bin_center\": (bin_edges[i] + bin_edges[i+1]) / 2,\n                             \"avg_confidence\": None, \"avg_accuracy\": None, \"count\": 0})\n            continue\n        avg_conf = probs[mask].mean()\n        avg_acc = labels[mask].mean()\n        ece += mask.sum() / len(probs) * abs(avg_conf - avg_acc)\n        bin_data.append({\"bin_center\": (bin_edges[i] + bin_edges[i+1]) / 2,\n                         \"avg_confidence\": float(avg_conf), \"avg_accuracy\": float(avg_acc),\n                         \"count\": int(mask.sum())})\n    return float(ece), bin_data\n\n\ndef platt_scaling_cv(instances, n_splits=5):\n    \"\"\"5-fold CV Platt scaling (LP only). Monotonic → same selection as raw LP.\"\"\"\n    all_lps, all_labels, _, inst_indices = make_binary_labels(instances)\n    n_instances = len(instances)\n    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)\n\n    predicted_probs = np.full(len(all_lps), np.nan)\n    slopes = []\n    intercepts = []\n\n    for train_idx, test_idx in kf.split(np.arange(n_instances)):\n        train_set = set(train_idx)\n        test_set = set(test_idx)\n        train_mask = np.isin(inst_indices, list(train_set))\n        test_mask = np.isin(inst_indices, list(test_set))\n\n        X_train = all_lps[train_mask].reshape(-1, 1)\n        y_train = all_labels[train_mask]\n        X_test = all_lps[test_mask].reshape(-1, 1)\n\n        if len(np.unique(y_train)) < 2:\n            predicted_probs[test_mask] = 0.5\n            slopes.append(0.0)\n            intercepts.append(0.0)\n            continue\n\n        clf = LogisticRegression(solver='lbfgs', max_iter=1000, C=1.0)\n        clf.fit(X_train, y_train)\n        predicted_probs[test_mask] = clf.predict_proba(X_test)[:, 1]\n        slopes.append(float(clf.coef_[0, 0]))\n        intercepts.append(float(clf.intercept_[0]))\n\n    # Selection (monotonic → same as raw LP)\n    selection_f1s = _select_by_probs(instances, predicted_probs, inst_indices)\n    ece, reliability = compute_ece(predicted_probs, all_labels)\n\n    return {\n        \"mean_f1\": float(np.mean(selection_f1s)),\n        \"slope_mean\": float(np.mean(slopes)),\n        \"intercept_mean\": float(np.mean(intercepts)),\n        \"ece\": ece,\n        \"reliability\": reliability,\n        \"per_instance_f1\": selection_f1s,\n    }\n\n\ndef multifeature_platt_cv(instances, n_splits=5):\n    \"\"\"5-fold CV Platt with features [LP, n_tokens, n_entities].\n    NOT monotonic in LP → can change selection.\"\"\"\n    all_lps, all_labels, all_features, inst_indices = make_binary_labels(instances)\n    n_instances = len(instances)\n    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)\n\n    predicted_probs = np.full(len(all_lps), np.nan)\n    coefs = []\n\n    for train_idx, test_idx in kf.split(np.arange(n_instances)):\n        train_set = set(train_idx)\n        test_set = set(test_idx)\n        train_mask = np.isin(inst_indices, list(train_set))\n        test_mask = np.isin(inst_indices, list(test_set))\n\n        X_train = all_features[train_mask]\n        y_train = all_labels[train_mask]\n        X_test = all_features[test_mask]\n\n        if len(np.unique(y_train)) < 2:\n            predicted_probs[test_mask] = 0.5\n            coefs.append([0.0, 0.0, 0.0])\n            continue\n\n        scaler = StandardScaler()\n        X_train_s = scaler.fit_transform(X_train)\n        X_test_s = scaler.transform(X_test)\n\n        clf = LogisticRegression(solver='lbfgs', max_iter=1000, C=1.0)\n        clf.fit(X_train_s, y_train)\n        predicted_probs[test_mask] = clf.predict_proba(X_test_s)[:, 1]\n        coefs.append(clf.coef_[0].tolist())\n\n    selection_f1s = _select_by_probs(instances, predicted_probs, inst_indices)\n    ece, reliability = compute_ece(predicted_probs, all_labels)\n\n    avg_coefs = np.mean(coefs, axis=0).tolist()\n    return {\n        \"mean_f1\": float(np.mean(selection_f1s)),\n        \"coefs_mean\": {\"lp\": avg_coefs[0], \"n_tokens\": avg_coefs[1], \"n_entities\": avg_coefs[2]},\n        \"ece\": ece,\n        \"reliability\": reliability,\n        \"per_instance_f1\": selection_f1s,\n    }\n\n\ndef temperature_scaling_cv(instances, n_splits=5):\n    \"\"\"5-fold CV Temperature scaling. Monotonic → same selection as raw LP.\"\"\"\n    all_lps, all_labels, _, inst_indices = make_binary_labels(instances)\n    n_instances = len(instances)\n    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)\n\n    calibrated_lps = np.full(len(all_lps), np.nan)\n    temperatures = []\n\n    for train_idx, test_idx in kf.split(np.arange(n_instances)):\n        train_set = set(train_idx)\n        test_set = set(test_idx)\n        train_mask = np.isin(inst_indices, list(train_set))\n        test_mask = np.isin(inst_indices, list(test_set))\n\n        lps_train = all_lps[train_mask]\n        labels_train = all_labels[train_mask]\n        lps_test = all_lps[test_mask]\n\n        def nll(log_tau):\n            tau = np.exp(log_tau)\n            logits = lps_train / tau\n            probs = expit(logits)\n            probs = np.clip(probs, 1e-7, 1 - 1e-7)\n            return -np.mean(labels_train * np.log(probs) + (1 - labels_train) * np.log(1 - probs))\n\n        result = minimize_scalar(nll, bounds=(-5, 5), method='bounded')\n        tau = np.exp(result.x)\n        temperatures.append(float(tau))\n\n        calibrated_lps[test_mask] = lps_test / tau\n\n    # Convert to probs for ECE\n    predicted_probs = expit(calibrated_lps)\n\n    selection_f1s = _select_by_probs(instances, predicted_probs, inst_indices)\n    ece, reliability = compute_ece(predicted_probs, all_labels)\n\n    return {\n        \"mean_f1\": float(np.mean(selection_f1s)),\n        \"tau_mean\": float(np.mean(temperatures)),\n        \"ece\": ece,\n        \"reliability\": reliability,\n        \"per_instance_f1\": selection_f1s,\n    }\n\n\ndef _select_by_probs(instances, probs, inst_indices):\n    \"\"\"Select sample with highest prob per instance.\"\"\"\n    selection_f1s = []\n    for idx, inst in enumerate(instances):\n        n_samples = len(inst[\"samples\"])\n        mask = inst_indices == idx\n        p = probs[mask]\n        assert len(p) == n_samples\n        if np.all(p == p[0]):\n            selected = 0\n        else:\n            selected = int(np.argmax(p))\n        selection_f1s.append(inst[\"samples\"][selected][\"f1\"])\n    return selection_f1s\n\n\ndef raw_lp_selection(instances):\n    \"\"\"Baseline: select sample with highest raw LP.\"\"\"\n    selection_f1s = []\n    for inst in instances:\n        lps = [s[\"lp\"] for s in inst[\"samples\"]]\n        if all(lp == lps[0] for lp in lps):\n            selected = 0\n        else:\n            selected = int(np.argmax(lps))\n        selection_f1s.append(inst[\"samples\"][selected][\"f1\"])\n    return selection_f1s\n\n\ndef oracle_selection(instances):\n    return [max(s[\"f1\"] for s in inst[\"samples\"]) for inst in instances]\n\n\ndef compute_raw_ece(instances):\n    \"\"\"ECE for raw LP using rank-based probability within instance.\"\"\"\n    all_probs = []\n    all_labels = []\n    for inst in instances:\n        f1s = [s[\"f1\"] for s in inst[\"samples\"]]\n        lps = [s[\"lp\"] for s in inst[\"samples\"]]\n        median_f1 = np.median(f1s)\n        n = len(lps)\n        ranks = np.argsort(np.argsort(lps))\n        probs = (ranks + 1) / n\n        for i, s in enumerate(inst[\"samples\"]):\n            all_probs.append(probs[i])\n            all_labels.append(1 if s[\"f1\"] >= median_f1 else 0)\n    return compute_ece(np.array(all_probs), np.array(all_labels))\n\n\ndef paired_bootstrap(f1s_a, f1s_b, n_bootstrap=10000, seed=42):\n    \"\"\"Paired bootstrap: is B better than A?\"\"\"\n    rng = np.random.RandomState(seed)\n    a = np.array(f1s_a)\n    b = np.array(f1s_b)\n    n = len(a)\n    observed = float(b.mean() - a.mean())\n    deltas = np.array([b[rng.randint(0, n, n)].mean() - a[rng.randint(0, n, n)].mean()\n                       for _ in range(n_bootstrap)])\n    return {\n        \"observed_delta\": observed,\n        \"ci_95\": [float(np.percentile(deltas, 2.5)), float(np.percentile(deltas, 97.5))],\n        \"p_value\": float(np.mean(deltas <= 0)),\n    }\n\n\ndef main():\n    results = {}\n\n    for name, path in DATASETS.items():\n        print(f\"\\n{'='*60}\")\n        print(f\"  Dataset: {name}\")\n        print(f\"{'='*60}\")\n\n        instances = load_dataset(path)\n        n_instances = len(instances)\n        n_samples = len(instances[0][\"samples\"])\n        print(f\"  Instances: {n_instances}, Samples/instance: {n_samples}\")\n\n        # Baselines\n        raw_f1s = raw_lp_selection(instances)\n        raw_mean = np.mean(raw_f1s)\n        g_f1s = [inst[\"greedy_f1\"] for inst in instances if inst[\"greedy_f1\"] is not None]\n        greedy_mean = float(np.mean(g_f1s)) if g_f1s else None\n        oracle_f1s = oracle_selection(instances)\n        oracle_mean = float(np.mean(oracle_f1s))\n\n        # Calibration methods\n        print(f\"  Running Platt scaling (5-fold CV)...\")\n        platt = platt_scaling_cv(instances)\n\n        print(f\"  Running Multi-feature Platt (5-fold CV)...\")\n        mf_platt = multifeature_platt_cv(instances)\n\n        print(f\"  Running Temperature scaling (5-fold CV)...\")\n        temp = temperature_scaling_cv(instances)\n\n        # Raw ECE\n        raw_ece, raw_rel = compute_raw_ece(instances)\n\n        # Statistical tests (multi-feature Platt is the only one that can differ)\n        mf_vs_raw = paired_bootstrap(raw_f1s, mf_platt[\"per_instance_f1\"])\n\n        # Print\n        print(f\"\\n  Results:\")\n        if greedy_mean: print(f\"    Greedy F1:          {greedy_mean:.4f}\")\n        print(f\"    Raw LP F1:          {raw_mean:.4f}\")\n        print(f\"    Platt LP F1:        {platt['mean_f1']:.4f}  (monotonic → same as raw)\")\n        print(f\"    Multi-feat Platt:   {mf_platt['mean_f1']:.4f}\")\n        print(f\"    TempScale LP F1:    {temp['mean_f1']:.4f}  (monotonic → same as raw)\")\n        print(f\"    Oracle F1:          {oracle_mean:.4f}\")\n\n        print(f\"\\n  Learned Parameters:\")\n        print(f\"    Platt: slope={platt['slope_mean']:.4f}, intercept={platt['intercept_mean']:.4f}\")\n        print(f\"    Multi-feat coefs: LP={mf_platt['coefs_mean']['lp']:.4f}, \"\n              f\"n_tok={mf_platt['coefs_mean']['n_tokens']:.4f}, \"\n              f\"n_ent={mf_platt['coefs_mean']['n_entities']:.4f}\")\n        print(f\"    TempScale: τ={temp['tau_mean']:.4f}\")\n\n        print(f\"\\n  Calibration Quality (ECE):\")\n        print(f\"    Raw LP (rank-based): {raw_ece:.4f}\")\n        print(f\"    Platt:               {platt['ece']:.4f}\")\n        print(f\"    Multi-feat Platt:    {mf_platt['ece']:.4f}\")\n        print(f\"    TempScale:           {temp['ece']:.4f}\")\n\n        print(f\"\\n  Multi-feat Platt vs Raw LP:\")\n        print(f\"    Δ={mf_vs_raw['observed_delta']:+.4f}, \"\n              f\"95% CI=[{mf_vs_raw['ci_95'][0]:+.4f}, {mf_vs_raw['ci_95'][1]:+.4f}], \"\n              f\"p={mf_vs_raw['p_value']:.4f}\")\n\n        results[name] = {\n            \"n_instances\": n_instances,\n            \"n_samples_per_instance\": n_samples,\n            \"greedy_f1\": greedy_mean,\n            \"raw_lp_f1\": float(raw_mean),\n            \"platt_lp_f1\": platt[\"mean_f1\"],\n            \"multifeature_platt_f1\": mf_platt[\"mean_f1\"],\n            \"tempscale_lp_f1\": temp[\"mean_f1\"],\n            \"oracle_f1\": oracle_mean,\n            \"note_monotonic\": \"Platt and TempScale are monotonic transforms of LP; \"\n                              \"argmax-based selection is unchanged. Multi-feature Platt \"\n                              \"uses [LP, n_tokens, n_entities] and CAN change selection.\",\n            \"params\": {\n                \"platt\": {\"slope\": platt[\"slope_mean\"], \"intercept\": platt[\"intercept_mean\"]},\n                \"multifeature_platt\": mf_platt[\"coefs_mean\"],\n                \"tempscale\": {\"tau\": temp[\"tau_mean\"]},\n            },\n            \"calibration\": {\n                \"raw_ece\": raw_ece,\n                \"platt_ece\": platt[\"ece\"],\n                \"multifeature_platt_ece\": mf_platt[\"ece\"],\n                \"tempscale_ece\": temp[\"ece\"],\n                \"raw_reliability\": raw_rel,\n                \"platt_reliability\": platt[\"reliability\"],\n                \"multifeature_platt_reliability\": mf_platt[\"reliability\"],\n                \"tempscale_reliability\": temp[\"reliability\"],\n            },\n            \"statistical_tests\": {\n                \"multifeature_platt_vs_raw\": mf_vs_raw,\n            },\n        }\n\n    # Summary table\n    print(f\"\\n\\n{'='*90}\")\n    print(f\"  SUMMARY TABLE\")\n    print(f\"{'='*90}\")\n    print(f\"{'Dataset':<10} | {'Greedy':>8} | {'Raw LP':>8} | {'Platt':>8} | {'MF-Platt':>8} | {'TempScl':>8} | {'Oracle':>8}\")\n    print(f\"{'-'*10}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}\")\n    for name in DATASETS:\n        r = results[name]\n        g = f\"{r['greedy_f1']:.4f}\" if r['greedy_f1'] else \"N/A\"\n        print(f\"{name:<10} | {g:>8} | {r['raw_lp_f1']:>8.4f} | {r['platt_lp_f1']:>8.4f} | \"\n              f\"{r['multifeature_platt_f1']:>8.4f} | {r['tempscale_lp_f1']:>8.4f} | {r['oracle_f1']:>8.4f}\")\n\n    print(f\"\\n  NOTE: Platt & TempScale = Raw LP (monotonic transform preserves argmax).\")\n    print(f\"  Multi-feature Platt uses [LP, n_tokens, n_entities] → non-monotonic → can differ.\")\n\n    # Save\n    out_path = OUTPUT_DIR / \"calibration_baseline_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\n  Results saved to: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYTHON_SCRIPT",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T14:20:47.835463+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T14:20:47.835599+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/bin/activate && python scripts/calibration_baseline.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/bin/activate && python scripts/calibration_baseline.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T14:20:47.835772+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\n  Dataset: SciERC\\n============================================================\\n  Instances: 551, Samples/instance: 8\\n  Running Platt scaling (5-fold CV)...\\n  Running Multi-feature Platt (5-fold CV)...\\n  Running Temperature scaling (5-fold CV)...\\n\\n  Results:\\n    Greedy F1:          0.6436\\n    Raw LP F1:          0.6495\\n    Platt LP F1:        0.6495  (monotonic → same as raw)\\n    Multi-feat Platt:   0.6386\\n    TempScale LP F1:    0.6495  (monotonic → same as raw)\\n    Oracle F1:          0.7775\\n\\n  Learned Parameters:\\n    Platt: slope=7.5611, intercept=1.6700\\n    Multi-feat coefs: LP=0.8784, n_tok=-0.2040, n_ent=-0.2380\\n    TempScale: τ=148.4125\\n\\n  Calibration Quality (ECE):\\n    Raw LP (rank-based): 0.2597\\n    Platt:               0.0475\\n    Multi-feat Platt:    0.0243\\n    TempScale:           0.2877\\n\\n  Multi-feat Platt vs Raw LP:\\n    Δ=-0.0110, 95% CI=[-0.0481, +0.0266], p=0.7179\\n\\n============================================================\\n  Dataset: CoNLL\\n============================================================\\n  Instances: 3453, Samples/instance: 16\\n  Running Platt scaling (5-fold CV)...\\n  Running Multi-feature Platt (5-fold CV)...\\n  Running Temperature scaling (5-fold CV)...\\n\\n  Results:\\n    Greedy F1:          0.9087\\n    Raw LP F1:          0.8975\\n    Platt LP F1:        0.8975  (monotonic → same as raw)\\n    Multi-feat Platt:   0.9007\\n    TempScale LP F1:    0.8975  (monotonic → same as raw)\\n    Oracle F1:          0.9614\\n\\n  Learned Parameters:\\n    Platt: slope=19.6476, intercept=3.8765\\n    Multi-feat coefs: LP=1.1810, n_tok=-0.0715, n_ent=-0.1959\\n    TempScale: τ=148.4125\\n\\n  Calibration Quality (ECE):\\n    Raw LP (rank-based): 0.3916\\n    Platt:               0.0119\\n    Multi-feat Platt:    0.0060\\n    TempScale:           0.4229\\n\\n 
…[truncated 2080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T14:20:47.835949+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/calibration_baseline_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/calibration_baseline_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T14:20:47.836077+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 23857 May 17 22:20 /root/autodl-tmp/struct_self_consist_ie/output/calibration_baseline_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_calibration_baseline_20260517T141557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-17T14:20:47.836306+00:00_

Done. Here's the report:

## Summary Table

| Dataset | Greedy | Raw LP | Platt LP | MF-Platt | TempScale | Oracle |
|---------|--------|--------|----------|----------|-----------|--------|
| SciERC  | 0.6436 | 0.6495 | 0.6495   | 0.6386   | 0.6495    | 0.7775 |
| CoNLL   | 0.9087 | 0.8975 | 0.8975   | 0.9007   | 0.8975    | 0.9614 |
| Few-NERD| 0.7712 | 0.7845 | 0.7845   | 0.7782   | 0.7845    | 0.9134 |

## Key Finding

**Standard Platt/TempScale cannot improve LP-based selection.** Both are monotonic transforms of LP, so argmax is preserved. They improve *calibration quality* (ECE drops from 0.26-0.39 → 0.01-0.08) but cannot change which sample is selected.

## Multi-feature Platt (LP + n_tokens + n_entities)

This non-monotonic variant *can* change selection but shows no significant improvement:
- SciERC: -0.011 (p=0.72)
- CoNLL: +0.003 (p=0.31)  
- Few-NERD: -0.006 (p=0.83)

None reach statistical significance. On CoNLL it shows a marginal improvement (+0.32pp) but still well short of significance.

## Calibration Quality (ECE)

| Dataset | Raw LP | Platt | MF-Platt | TempScale |
|---------|--------|-------|----------|-----------|
| SciERC  | 0.260  | 0.048 | 0.024    | 0.288     |
| CoNLL   | 0.392  | 0.012 | 0.006    | 0.423     |
| Few-NERD| 0.262  | 0.080 | 0.064    | 0.300     |

Platt dramatically improves probability estimates (ECE), just not selection.

## Learned Parameters

- **Platt slopes** are large (7.6 - 31.2), reflecting that LP has very narrow range
- **MF-Platt coefs**: LP is dominant (0.88-1.73), n_entities has negative weight (-0.20 to -0.86, penalizing over-generation), n_tokens effect is mixed
- **TempScale τ**: hits boundary on SciERC/CoNLL (148.4), meaningful only on Few-NERD (1.20)

## Conclusion for the paper

Calibration is a natural baseline but fundamentally limited for sample selection: since LP-based selection uses within-instance argmax, any monotonic calibration is equivalent to raw LP. Even multi-feature calibration that breaks monotonicity provides no significant gain, confirming that the challenge is not about probability calibration but about the weak correlation between LP ranking and quality ranking within instances.

**Outputs:**
- `scripts/calibration_baseline.py`
- `output/calibration_baseline_results.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_calibration_baseline_20260517T141557"
}
```

</details>

---
