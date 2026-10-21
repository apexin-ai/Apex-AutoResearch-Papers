# analysis provenance audit c032 c023 c021

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 137
- **Recorded user turns:** 0
- **Tool calls:** 68
- **Original source:** `logs/chats/worker_analysis_provenance_audit_c032_c023_c021_20260516T045025.jsonl`
- **Structured JSON:** [`60b836567dedbf4f7a4f.json`](../../sessions/60/60b836567dedbf4f7a4f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

137 recorded events

### Tool call

_source line 1 · 2026-05-16T04:57:39.007993+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__detect_image",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__detect_image",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T04:57:39.008413+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T04:57:39.008636+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T04:57:39.008883+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 6560\\ndrwxr-xr-x 92 root root    8192 May 16 10:51 .\\ndrwxr-xr-x 15 root root    4096 May 16 11:09 ..\\ndrwxr-xr-x  2 root root      85 May 16 00:37 analysis_epsilon_sweep\\n-rw-r--r--  1 root root    7926 May 15 20:56 analysis_fk_bootstrap_ci.json\\n-rw-r--r--  1 root root    5824 May 15 21:16 analysis_fk_bootstrap_per_instance.json\\n-rw-r--r--  1 root root  150381 May 15 21:15 analysis_lp_range_cdf.json\\n-rw-r--r--  1 root root    3197 May 15 21:15 analysis_lp_range_cdf_n16_3seed.json\\n-rw-r--r--  1 root root   10542 May 15 20:46 analysis_multiseed_selection_f1.json\\ndrwxr-xr-x  2 root root    4096 May 16 00:50 analysis_round8\\n-rw-r--r--  1 root root   20864 May 15 21:14 analysis_scierc_n16_3seed_selection_f1.json\\n-rw-r--r--  1 root root   30781 May 15 21:26 analysis_scierc_n16_3seed_selection_f1_merged.json\\n-rw-r--r--  1 root root    9919 May 15 21:26 analysis_scierc_re_n16_3seed_selection_f1.json\\n-rw-r--r--  1 root root    7621 May 15 22:57 analysis_unified_rho_full.json\\ndrwxr-xr-x  2 root root      69 May 15 05:17 bootstrap_ci_nscaling\\n-rw-r--r--  1 root root   18675 May 15 06:05 bootstrap_ci_summary.json\\n-rw-r--r--  1 root root    1977 May 15 06:06 bootstrap_ci_tables.tex\\n-rw-r--r--  1 root root    2098 May 14 20:48 conditional_filter_diagnosis.json\\ndrwxr-xr-x  2 root root      58 May 14 20:54 exp001_n16_seed123\\ndrwxr-xr-x  2 root root      77 May 14 20:13 exp001_n16_seed123_200only\\ndrwxr-xr-x  2 root root      10 May 14 20:43 exp001_n16_seed123_200only_backup\\ndrwxr-xr-x  2 root root      10 May 14 20:44 exp001_n16_seed123_full\\n-rw-r--r--  1 root root  108646 May 14 20:54 exp001_n16_seed123_run.log\\ndrwxr-xr-x  2 root root     146 May 14 20:49 exp001_n16_seed42\\ndrwxr-xr-x  2 root root     119 May 14 19:55 exp001_n16_seed42_200only_backup\\n-rw-r--r--  1 root root  107674 May 14 20:24 exp001_n16_seed42_run.log\\ndrwxr-xr-x  2 root root      58 May 15 18:41 exp001_n1
…[truncated 6429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T04:57:39.009058+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/analysis_round8/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/analysis_round8/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T04:57:39.009226+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 88\\ndrwxr-xr-x  2 root root  4096 May 16 06:06 .\\ndrwxr-xr-x 15 root root  4096 May 16 11:09 ..\\n-rw-r--r--  1 root root  4487 May 16 06:06 analysis_fk_tost_round8.md\\n-rw-r--r--  1 root root   452 May 15 23:36 epsilon_sweep.csv\\n-rw-r--r--  1 root root  3403 May 15 23:35 epsilon_sweep.py\\n-rw-r--r--  1 root root  3273 May 16 06:11 fk_independence_instance_test.json\\n-rw-r--r--  1 root root 10993 May 16 06:02 fk_independence_instance_test.py\\n-rw-r--r--  1 root root 33666 May 16 05:58 tost_external_delta.json\\n-rw-r--r--  1 root root 11380 May 16 05:58 tost_external_delta.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T04:57:39.009372+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -r \"0\\.002\" /root/autodl-tmp/struct_self_consist_ie/output/ --include=\"*.json\" --include=\"*.txt\" --include=\"*.csv\" --include=\"*.md\" --include=\"*.log\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -r \"0\\.002\" /root/autodl-tmp/struct_self_consist_ie/output/ --include=\"*.json\" --include=\"*.txt\" --include=\"*.csv\" --include=\"*.md\" --include=\"*.log\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T04:57:39.009538+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/gate0_ft002v2/report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/exp013_exact_match_report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42_200only_backup/exp001_all_signals_report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42/exp001_all_signals_report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/logprob_diagnosis/diagnosis.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed456_200only/report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_pilot/report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2/re_all_signals_report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp009_stratification_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp010_selection_curves/exp010_metrics.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123/report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_006_v2_run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_006_v2/exp_006_v2_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2_run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2/results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2/summary.txt\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_016_v2/linear_combo_grid.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2_re_rerun/results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/bootstrap_ci_nscaling/results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/llama_conll_n16_3seed_5signal_summary.json\\n/root/autodl-tm
…[truncated 3184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T04:57:39.009682+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -r \"0\\.002\" /root/autodl-tmp/struct_self_consist_ie/analysis_round8/ --include=\"*.json\" --include=\"*.txt\" --include=\"*.csv\" --include=\"*.md\" --include=\"*.log\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -r \"0\\.002\" /root/autodl-tmp/struct_self_consist_ie/analysis_round8/ --include=\"*.json\" --include=\"*.txt\" --include=\"*.csv\" --include=\"*.md\" --include=\"*.log\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T04:57:39.009811+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/analysis_round8/tost_external_delta.json\\n/root/autodl-tmp/struct_self_consist_ie/analysis_round8/analysis_fk_tost_round8.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T04:57:39.009938+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_provenance.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_provenance.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T04:57:39.010429+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml\", \"content\": \"paper:\\n  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence\\n    Signals for Test-Time Scaling in Information Extraction'\\n  version: 5\\n  generated_at: '2026-05-15T09:49:17.274112+00:00'\\n  source: manual provenance build by Paper Agent\\nclaims:\\n- id: c001_voting_rho_scierc_ner\\n  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation\\n    artifact)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_rho_full\\n    value: 0.379\\n  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected\\n    via exp_012_rerun_1024 (max_tokens=1024).\\n- id: c002_auroc_dissociation_scierc\\n  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while\\n    Voting leads ρ (NER 0.379, RE 0.422)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.em_auroc\\n    value: 0.749\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.em_auroc\\n    value: 0.706\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_auroc\\n    value: 0.684\\n  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected\\n    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline\\n    claim changed from \\\"entity voting achieves ρ=0.38 and AUROC=0.74\\\" to split ρ (Voting\\n    0.38) / AUROC (EM 0.75) claim.\\n- id: c003_sj_rho_scierc_ner\\n  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\
…[truncated 21948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T04:57:39.010663+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp009_stratification_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp009_stratification_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T04:57:39.010982+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc_ner\\\": {\\n    \\\"n_total\\\": 551,\\n    \\\"by_greedy_f1\\\": {\\n      \\\"[0, 0.25)\\\": {\\n        \\\"n\\\": 63,\\n        \\\"mean_f1\\\": 0.012964108202203438,\\n        \\\"std_f1\\\": 0.050002566931507855,\\n        \\\"signals\\\": {\\n          \\\"sj\\\": {\\n            \\\"rho\\\": 0.1591899032754564,\\n            \\\"rho_ci_lo\\\": 0.03484575311256299,\\n            \\\"rho_ci_hi\\\": 0.29441645758229157,\\n            \\\"p\\\": 0.21269348192185367,\\n            \\\"auroc\\\": 0.6864406779661016,\\n            \\\"auroc_ci_lo\\\": 0.5161290322580645,\\n            \\\"auroc_ci_hi\\\": 0.8158114035087718\\n          },\\n          \\\"fk\\\": {\\n            \\\"rho\\\": 0.25112822147572084,\\n            \\\"rho_ci_lo\\\": 0.11183009657879464,\\n            \\\"rho_ci_hi\\\": 0.3935594404481513,\\n            \\\"p\\\": 0.04711186360938125,\\n            \\\"auroc\\\": 0.7966101694915254,\\n            \\\"auroc_ci_lo\\\": 0.6694783752191701,\\n            \\\"auroc_ci_hi\\\": 0.8965794515023189\\n          },\\n          \\\"logprob\\\": {\\n            \\\"rho\\\": 0.07734328551539553,\\n            \\\"rho_ci_lo\\\": -0.11072736503133365,\\n            \\\"rho_ci_hi\\\": 0.285400972688807,\\n            \\\"p\\\": 0.5468388938510856,\\n            \\\"auroc\\\": 0.597457627118644,\\n            \\\"auroc_ci_lo\\\": 0.3225806451612903,\\n            \\\"auroc_ci_hi\\\": 0.967741935483871\\n          },\\n          \\\"voting_conf\\\": {\\n            \\\"rho\\\": 0.12773976400064793,\\n            \\\"rho_ci_lo\\\": -0.013989156754501072,\\n            \\\"rho_ci_hi\\\": 0.26940805593564277,\\n            \\\"p\\\": 0.3184276301710296,\\n            \\\"auroc\\\": 0.6504237288135594,\\n            \\\"auroc_ci_lo\\\": 0.4872404351273664,\\n            \\\"auroc_ci_hi\\\": 0.8277800546448086\\n          },\\n          \\\"em\\\": {\\n            \\\"rho\\\": -0.273904817
…[truncated 7982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T04:57:39.011186+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_eval/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_eval/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T04:57:39.011429+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"wnut17\\\",\\n  \\\"subtask\\\": \\\"ner\\\",\\n  \\\"n_samples\\\": 16,\\n  \\\"temperature\\\": 1.0,\\n  \\\"num_instances\\\": 1287,\\n  \\\"use_train_format\\\": true,\\n  \\\"greedy_f1\\\": 0.52316715542522,\\n  \\\"oracle_f1\\\": 0.6637217007178353,\\n  \\\"oracle_headroom\\\": 0.14055454529261535,\\n  \\\"fleiss_kappa_mean\\\": 0.7002625416298626,\\n  \\\"soft_jaccard_mean\\\": 0.8844110439882366,\\n  \\\"correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.12498639982700602,\\n    \\\"p_value\\\": 0.0010101389238927497,\\n    \\\"n\\\": 689\\n  },\\n  \\\"correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.08883161050304318,\\n    \\\"p_value\\\": 0.019695320766242228,\\n    \\\"n\\\": 689\\n  },\\n  \\\"correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.16863345538503793,\\n    \\\"p_value\\\": 0.0019847067973992236,\\n    \\\"n\\\": 334\\n  },\\n  \\\"correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.2884389703925184,\\n    \\\"p_value\\\": 8.044470580733825e-08,\\n    \\\"n\\\": 334\\n  },\\n  \\\"n_gold_empty_filtered\\\": 598,\\n  \\\"n_greedy_f1_zero_filtered\\\": 355,\\n  \\\"structural_beats_surface\\\": false,\\n  \\\"rho_advantage\\\": -0.036154789323962835,\\n  \\\"sample_f1_mean\\\": 0.4007648977651592,\\n  \\\"sample_f1_std\\\": 0.45324774277971985,\\n  \\\"sample_f1_pct_zero\\\": 53.68287373004354,\\n  \\\"logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": -0.4094891030514717,\\n      \\\"p_rho\\\": 3.0724001673695786e-29,\\n      \\\"tau\\\": -0.2984555640667542,\\n      \\\"p_tau\\\": 3.0647533023775854e-24,\\n      \\\"auroc\\\": 0.21888336004048242,\\n      \\\"n\\\": 689\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.35011390590805674,\\n      \\\"p_rho\\\": 4.575598794556641e-11,\\n      \\\"tau\\\": 0.2722466231418909,\\n      \\\"p_tau\\\": 1.373591283647736e-10,\\n      \\\"a
…[truncated 407 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T04:57:39.011594+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_pilot/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_pilot/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T04:57:39.011786+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"wnut17\\\",\\n  \\\"subtask\\\": \\\"ner\\\",\\n  \\\"n_samples\\\": 16,\\n  \\\"temperature\\\": 1.0,\\n  \\\"num_instances\\\": 1287,\\n  \\\"use_train_format\\\": true,\\n  \\\"greedy_f1\\\": 0.5246478873239436,\\n  \\\"oracle_f1\\\": 0.6640883977900552,\\n  \\\"oracle_headroom\\\": 0.1394405104661116,\\n  \\\"fleiss_kappa_mean\\\": 0.683003441168254,\\n  \\\"soft_jaccard_mean\\\": 0.8822903299654273,\\n  \\\"correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.12413887343520687,\\n    \\\"p_value\\\": 0.0010937938190619452,\\n    \\\"n\\\": 689\\n  },\\n  \\\"correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.0824641320128276,\\n    \\\"p_value\\\": 0.030438088421768046,\\n    \\\"n\\\": 689\\n  },\\n  \\\"correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.1638999025238164,\\n    \\\"p_value\\\": 0.0027407033200631823,\\n    \\\"n\\\": 332\\n  },\\n  \\\"correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.27455806190068305,\\n    \\\"p_value\\\": 3.7386117553263027e-07,\\n    \\\"n\\\": 332\\n  },\\n  \\\"n_gold_empty_filtered\\\": 598,\\n  \\\"n_greedy_f1_zero_filtered\\\": 357,\\n  \\\"structural_beats_surface\\\": false,\\n  \\\"rho_advantage\\\": -0.04167474142237927,\\n  \\\"sample_f1_mean\\\": 0.400518788270245,\\n  \\\"sample_f1_std\\\": 0.453005368675313,\\n  \\\"sample_f1_pct_zero\\\": 53.71915820029027,\\n  \\\"logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": -0.4138939788856724,\\n      \\\"p_rho\\\": 6.783004097628618e-30,\\n      \\\"tau\\\": -0.3019132806111708,\\n      \\\"p_tau\\\": 9.950349470683396e-25,\\n      \\\"auroc\\\": 0.21703621207519153,\\n      \\\"n\\\": 689\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.3519627321461846,\\n      \\\"p_rho\\\": 4.075928220112554e-11,\\n      \\\"tau\\\": 0.2740539886891814,\\n      \\\"p_tau\\\": 1.2208223275022382e-10,\\n      \\\"auroc\\
…[truncated 401 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T04:57:39.011941+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -r \"0\\.062\" /root/autodl-tmp/struct_self_consist_ie/output/ --include=\"*.json\" --include=\"*.txt\" --include=\"*.csv\" --include=\"*.md\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -r \"0\\.062\" /root/autodl-tmp/struct_self_consist_ie/output/ --include=\"*.json\" --include=\"*.txt\" --include=\"*.csv\" --include=\"*.md\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T04:57:39.012096+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp016_signal_ensemble/correlation_matrix.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp016_signal_ensemble/selection_f1_full.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp009_stratification_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_005_v2_temperature/temperature_sensitivity_report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2/results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2/summary.txt\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_016_v2/correlation_matrix.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_016_v2/linear_combo_grid.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_016_v2/logistic_ensemble.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_016_v2/summary.csv\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2_re_rerun/results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2_re_rerun/summary.txt\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/reliability_data_1024.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_016_rerun_1024/correlation_matrix.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_016_rerun_1024/selection_f1_full.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round4/logprob_tie_results_n529.json\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_lp_range_cdf.json\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_lp_range_cdf_n16_3seed.json\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_round8/seed456_lp_range.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round8/r8w4_lp_range_analysis.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round8/task2_lp_range_final.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"err
…[truncated 56 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T04:57:39.012311+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -r \"0\\.110\" /root/autodl-tmp/struct_self_consist_ie/output/ --include=\"*.json\" --include=\"*.txt\" --include=\"*.csv\" --include=\"*.md\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -r \"0\\.110\" /root/autodl-tmp/struct_self_consist_ie/output/ --include=\"*.json\" --include=\"*.txt\" --include=\"*.csv\" --include=\"*.md\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T04:57:39.012467+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/gate0_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/gate0_realigned_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_015_unified/exp015_unified_report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_015_unified/exp015_summary.md\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42/report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_011_ood_analysis/ood_cross_dataset_results.md\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_011_ood_analysis/ood_cross_dataset_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp009_stratification_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123/report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp004v2_re_diagnostic/cross_type_comparison.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp004v2_re_diagnostic/full_report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2/results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2/summary.txt\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2_re_rerun/results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2_re_rerun/summary.txt\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/reliability_data_1024.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_016_rerun_1024/correlation_matrix.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/diversity_analysis.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_018_llama_scierc_seed123/report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_011_ood_conll_to_scierc/report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_lp_range_cdf.json\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_multiseed_sel
…[truncated 204 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T04:57:39.012615+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -r \"0\\.473\" /root/autodl-tmp/struct_self_consist_ie/output/ --include=\"*.json\" --include=\"*.txt\" --include=\"*.csv\" --include=\"*.md\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -r \"0\\.473\" /root/autodl-tmp/struct_self_consist_ie/output/ --include=\"*.json\" --include=\"*.txt\" --include=\"*.csv\" --include=\"*.md\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T04:57:39.012755+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/analysis_report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp016_signal_ensemble/correlation_matrix.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp009_stratification_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_005_v2_temperature/temperature_sensitivity_report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_016_v2/linear_combo_grid.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2_re_rerun/summary.txt\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123/all_signals_report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/llama_conll_n16_3seed_5signal_summary.json\\n/root/autodl-tmp/struct_self_consist_ie/output/bootstrap_ci_summary.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/reliability_data_1024.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s456_r1024/report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_016_rerun_1024/correlation_matrix.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_016_rerun_1024/logistic_ensemble.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round4/logprob_tie_results_n529.json\\n/root/autodl-tmp/struct_self_consist_ie/output/rho_audit_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_unified_rho_full.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T04:57:39.012938+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T04:57:39.013286+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"ner_seed42\\\": {\\n    \\\"n_total\\\": 551,\\n    \\\"subtask\\\": \\\"ner\\\",\\n    \\\"by_greedy_f1\\\": {\\n      \\\"[0, 0.25)\\\": {\\n        \\\"n\\\": 78,\\n        \\\"mean_f1\\\": 0.00931105931105931,\\n        \\\"std_f1\\\": 0.04161191412076067,\\n        \\\"too_small\\\": false,\\n        \\\"signals\\\": {\\n          \\\"sj\\\": {\\n            \\\"rho\\\": 0.03970568636536484,\\n            \\\"ci_lo\\\": -0.17615526671331225,\\n            \\\"ci_hi\\\": 0.1916036640706902,\\n            \\\"p\\\": 0.7299848680515906\\n          },\\n          \\\"fk\\\": {\\n            \\\"rho\\\": 0.18066430068305409,\\n            \\\"ci_lo\\\": 0.03604247946642114,\\n            \\\"ci_hi\\\": 0.30723586761095606,\\n            \\\"p\\\": 0.11344921259234626\\n          },\\n          \\\"logprob\\\": {\\n            \\\"rho\\\": -0.014755600473946933,\\n            \\\"ci_lo\\\": -0.21678790177571897,\\n            \\\"ci_hi\\\": 0.1985560620256237,\\n            \\\"p\\\": 0.8979741674289845\\n          },\\n          \\\"voting_conf\\\": {\\n            \\\"rho\\\": 0.0848438115088091,\\n            \\\"ci_lo\\\": -0.04181147570504118,\\n            \\\"ci_hi\\\": 0.21378450887996164,\\n            \\\"p\\\": 0.46017689733899114\\n          },\\n          \\\"em\\\": {\\n            \\\"rho\\\": -0.3555172602890218,\\n            \\\"ci_lo\\\": -0.49989902115315443,\\n            \\\"ci_hi\\\": -0.17543243570602693,\\n            \\\"p\\\": 0.0014022340780114556\\n          }\\n        }\\n      },\\n      \\\"[0.25, 0.5)\\\": {\\n        \\\"n\\\": 73,\\n        \\\"mean_f1\\\": 0.3681780168081538,\\n        \\\"std_f1\\\": 0.0453827711238864,\\n        \\\"too_small\\\": false,\\n        \\\"signals\\\": {\\n          \\\"sj\\\": {\\n            \\\"rho\\\": 0.10200527558028614,\\n            \\\"ci_lo\\\": -0.1296629959207327,\\n            \\\"ci_hi\\\": 0.3356583335118884,\\n         
…[truncated 8113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T04:57:39.013457+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2_re_rerun/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2_re_rerun/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T04:57:39.013787+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"filter_stats\\\": {\\n    \\\"n_total_raw\\\": 551,\\n    \\\"n_empty_gold_filtered\\\": 154,\\n    \\\"n_after_filter\\\": 397\\n  },\\n  \\\"n_total\\\": 397,\\n  \\\"proxy_correlations\\\": {\\n    \\\"sent_len_vs_F1\\\": {\\n      \\\"rho\\\": -0.023099307562040112,\\n      \\\"p\\\": 0.6463344039583466\\n    },\\n    \\\"ent_count_vs_F1\\\": {\\n      \\\"rho\\\": -0.010902182599557667,\\n      \\\"p\\\": 0.8285622225106516\\n    },\\n    \\\"rel_count_vs_F1\\\": {\\n      \\\"rho\\\": 0.1306090722643033,\\n      \\\"p\\\": 0.009178563893527534\\n    },\\n    \\\"type_diversity_vs_F1\\\": {\\n      \\\"rho\\\": 0.07110951068229204,\\n      \\\"p\\\": 0.15731196139402373\\n    },\\n    \\\"sent_len_vs_ent_count\\\": {\\n      \\\"rho\\\": 0.6503553500932429,\\n      \\\"p\\\": 4.2324874173740275e-49\\n    },\\n    \\\"sent_len_vs_rel_count\\\": {\\n      \\\"rho\\\": 0.4312504917373513,\\n      \\\"p\\\": 2.0640413052928572e-19\\n    },\\n    \\\"ent_count_vs_rel_count\\\": {\\n      \\\"rho\\\": 0.7693628186640157,\\n      \\\"p\\\": 6.900215660957394e-79\\n    },\\n    \\\"ent_count_vs_type_diversity\\\": {\\n      \\\"rho\\\": 0.6435215826657187,\\n      \\\"p\\\": 8.619423661807758e-48\\n    }\\n  },\\n  \\\"proxy_ranking\\\": [\\n    {\\n      \\\"proxy\\\": \\\"ent_count\\\",\\n      \\\"abs_rho_with_f1\\\": 0.010902182599557667,\\n      \\\"independent\\\": true\\n    },\\n    {\\n      \\\"proxy\\\": \\\"sent_len\\\",\\n      \\\"abs_rho_with_f1\\\": 0.023099307562040112,\\n      \\\"independent\\\": true\\n    },\\n    {\\n      \\\"proxy\\\": \\\"type_diversity\\\",\\n      \\\"abs_rho_with_f1\\\": 0.07110951068229204,\\n      \\\"independent\\\": true\\n    },\\n    {\\n      \\\"proxy\\\": \\\"rel_count\\\",\\n      \\\"abs_rho_with_f1\\\": 0.1306090722643033,\\n      \\\"independent\\\": true\\n    }\\n  ],\\n  \\\"global_signals\\\": {\\n    \\\"sj\\\": {\\n      \\\"rho\\\": 0.28130
…[truncated 8305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T04:57:39.013951+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/rho_audit_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/rho_audit_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T04:57:39.014189+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_017_llama_conll_n16_r1024\\\": {\\n    \\\"exp_id\\\": \\\"exp_017_llama_conll_n16_r1024\\\",\\n    \\\"n_total\\\": 3453,\\n    \\\"n_gold_empty\\\": 697,\\n    \\\"n_valid\\\": 2756,\\n    \\\"n_conditional\\\": 2641,\\n    \\\"gold_empty_analysis\\\": {\\n      \\\"n\\\": 697,\\n      \\\"fk_mean\\\": 0.0372,\\n      \\\"fk_std\\\": 0.1982,\\n      \\\"sj_mean\\\": 0.9789,\\n      \\\"f1_mean\\\": 0.0\\n    },\\n    \\\"old_pipeline\\\": {\\n      \\\"n\\\": 3453,\\n      \\\"rho_fk\\\": 0.8095,\\n      \\\"rho_sj\\\": 0.1815,\\n      \\\"registry_rho_fk\\\": 0.8095,\\n      \\\"registry_rho_sj\\\": 0.1815\\n    },\\n    \\\"new_pipeline_full\\\": {\\n      \\\"n\\\": 2756,\\n      \\\"rho_fk\\\": 0.4752,\\n      \\\"rho_sj\\\": 0.4836,\\n      \\\"rho_vc\\\": 0.4746,\\n      \\\"rho_em\\\": 0.4818,\\n      \\\"rho_lp\\\": 0.3136,\\n      \\\"auroc_fk\\\": 0.7467,\\n      \\\"auroc_sj\\\": 0.7496,\\n      \\\"auroc_vc\\\": 0.7529,\\n      \\\"auroc_em\\\": 0.7508,\\n      \\\"auroc_lp\\\": 0.7661,\\n      \\\"median_f1\\\": 1.0\\n    },\\n    \\\"new_pipeline_conditional\\\": {\\n      \\\"n\\\": 2641,\\n      \\\"rho_fk\\\": 0.4767,\\n      \\\"rho_sj\\\": 0.4856\\n    }\\n  },\\n  \\\"exp_017_llama_conll_n16_s456_r1024\\\": {\\n    \\\"exp_id\\\": \\\"exp_017_llama_conll_n16_s456_r1024\\\",\\n    \\\"n_total\\\": 3453,\\n    \\\"n_gold_empty\\\": 697,\\n    \\\"n_valid\\\": 2756,\\n    \\\"n_conditional\\\": 2642,\\n    \\\"gold_empty_analysis\\\": {\\n      \\\"n\\\": 697,\\n      \\\"fk_mean\\\": 0.0372,\\n      \\\"fk_std\\\": 0.1991,\\n      \\\"sj_mean\\\": 0.9777,\\n      \\\"f1_mean\\\": 0.0\\n    },\\n    \\\"old_pipeline\\\": {\\n      \\\"n\\\": 3453,\\n      \\\"rho_fk\\\": 0.8085,\\n      \\\"rho_sj\\\": 0.1895,\\n      \\\"registry_rho_fk\\\": 0.8085,\\n      \\\"registry_rho_sj\\\": 0.1895\\n    },\\n    \\\"new_pipeline_full\\\": {\\n      \\\"n\\\": 2756,\\n      \\\"rho_fk\\\
…[truncated 3112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T04:57:39.014355+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/analysis_unified_rho_full.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/analysis_unified_rho_full.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T04:57:39.014640+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"metadata\\\": {\\n    \\\"pipeline\\\": \\\"unified_gold_filtered\\\",\\n    \\\"date\\\": \\\"2026-05-15\\\",\\n    \\\"fk_empty_fix\\\": true,\\n    \\\"gold_filter\\\": \\\"exclude instances where len(gold.entities)==0\\\",\\n    \\\"conll_n_valid\\\": 2756,\\n    \\\"scierc_n_valid\\\": 529,\\n    \\\"n8_seed123_added\\\": true\\n  },\\n  \\\"results\\\": {\\n    \\\"llama_conll_n16_seed42\\\": {\\n      \\\"n_instances\\\": 2756,\\n      \\\"n_total\\\": 3453,\\n      \\\"n_gold_empty\\\": 697,\\n      \\\"VC\\\": 0.4746,\\n      \\\"SJ\\\": 0.4836,\\n      \\\"FK\\\": 0.4752,\\n      \\\"EM\\\": 0.4818,\\n      \\\"LP\\\": 0.3136,\\n      \\\"auroc_VC\\\": 0.7529,\\n      \\\"auroc_SJ\\\": 0.7496,\\n      \\\"auroc_FK\\\": 0.7467,\\n      \\\"auroc_EM\\\": 0.7508,\\n      \\\"auroc_LP\\\": 0.7661\\n    },\\n    \\\"llama_conll_n16_seed123\\\": {\\n      \\\"n_instances\\\": 2756,\\n      \\\"n_total\\\": 3453,\\n      \\\"n_gold_empty\\\": 697,\\n      \\\"VC\\\": 0.4633,\\n      \\\"SJ\\\": 0.4662,\\n      \\\"FK\\\": 0.4573,\\n      \\\"EM\\\": 0.4632,\\n      \\\"LP\\\": 0.308,\\n      \\\"auroc_VC\\\": 0.7444,\\n      \\\"auroc_SJ\\\": 0.7391,\\n      \\\"auroc_FK\\\": 0.7358,\\n      \\\"auroc_EM\\\": 0.7395,\\n      \\\"auroc_LP\\\": 0.7611\\n    },\\n    \\\"llama_conll_n16_seed456\\\": {\\n      \\\"n_instances\\\": 2756,\\n      \\\"n_total\\\": 3453,\\n      \\\"n_gold_empty\\\": 697,\\n      \\\"VC\\\": 0.4722,\\n      \\\"SJ\\\": 0.4734,\\n      \\\"FK\\\": 0.469,\\n      \\\"EM\\\": 0.4752,\\n      \\\"LP\\\": 0.3099,\\n      \\\"auroc_VC\\\": 0.7495,\\n      \\\"auroc_SJ\\\": 0.7428,\\n      \\\"auroc_FK\\\": 0.7408,\\n      \\\"auroc_EM\\\": 0.7444,\\n      \\\"auroc_LP\\\": 0.7628\\n    },\\n    \\\"qwen_scierc_n16_seed42\\\": {\\n      \\\"n_instances\\\": 529,\\n      \\\"n_total\\\": 551,\\n      \\\"n_gold_empty\\\": 22,\\n      \\\"VC\\\": 0.3993,\\n      \\\"SJ\\\": 0.3984,
…[truncated 8259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T04:57:39.014798+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"0\\.002\" /root/autodl-tmp/struct_self_consist_ie/output/logprob_diagnosis/diagnosis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"0\\.002\" /root/autodl-tmp/struct_self_consist_ie/output/logprob_diagnosis/diagnosis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T04:57:39.014932+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"132:        \\\"max\\\": -0.002333983745691524\\n144:        \\\"max\\\": -0.002125299685368073\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T04:57:39.015056+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"logprob_rho_cond\\|logprob.*cond\\|cond.*logprob\" /root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"logprob_rho_cond\\|logprob.*cond\\|cond.*logprob\" /root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T04:57:39.015201+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T04:57:39.015365+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2_re_rerun/summary.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2_re_rerun/summary.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T04:57:39.015559+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"==========================================================================================\\nEXP-009 v2 RE RERUN — FILTERED + PROXY INDEPENDENCE CHECK\\n==========================================================================================\\n\\nFiltering: 551 raw → 154 empty-gold removed → 397 kept\\n\\n──────────────────────────────────────────────────────────────────────\\nProxy Independence Check (proxy vs F1 Spearman ρ)\\n──────────────────────────────────────────────────────────────────────\\n  ✓ ent_count            |ρ|=0.011\\n  ✓ sent_len             |ρ|=0.023\\n  ✓ type_diversity       |ρ|=0.071\\n  ✓ rel_count            |ρ|=0.131\\n\\nProxy cross-correlations:\\n  sent_len_vs_ent_count               ρ=0.650 (p=4.2e-49)\\n  sent_len_vs_rel_count               ρ=0.431 (p=2.1e-19)\\n  ent_count_vs_rel_count              ρ=0.769 (p=6.9e-79)\\n  ent_count_vs_type_diversity         ρ=0.644 (p=8.6e-48)\\n\\n──────────────────────────────────────────────────────────────────────\\nGlobal Signal ρ (n=397, after filtering)\\n──────────────────────────────────────────────────────────────────────\\n  sj             ρ=0.281 [0.182, 0.371]  p=1.2e-08\\n  fk             ρ=0.279 [0.173, 0.375]  p=1.6e-08\\n  logprob        ρ=0.287 [0.192, 0.379]  p=6.1e-09\\n  voting_conf    ρ=0.322 [0.228, 0.414]  p=4.9e-11\\n  em             ρ=0.165 [0.066, 0.263]  p=9.4e-04\\n\\n───────────────────────────��──────────────────────────────────────────\\n▸ Stratification by Sentence Length QUARTILES (primary, independent)\\n──────────────────────────────────────────────────────────────────────\\n  Stratum                       n  mean_F1              sj              fk         logprob     voting_conf              em\\n  ------------------------------------------------------------------------------------------------------------------------\\n  Q1 (low)                    117    0.454  0.110[-0.08,0.29]  0.188[-0.00,0.37]  0.152[-0
…[truncated 6490 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T04:57:39.015714+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"Q4\\|Q3\\|High\" /root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2_re_rerun/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"Q4\\|Q3\\|High\" /root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2_re_rerun/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T04:57:39.015841+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T04:57:39.015961+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"0\\.062\" /root/autodl-tmp/struct_self_consist_ie/output/exp009_stratification_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"0\\.062\" /root/autodl-tmp/struct_self_consist_ie/output/exp009_stratification_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T04:57:39.016083+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"794:            \\\"rho\\\": 0.06299743433466573,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T04:57:39.016225+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"0\\.062\" /root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"0\\.062\" /root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T04:57:39.016384+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"133:            \\\"rho\\\": 0.06299075221044065,\\n304:            \\\"ci_lo\\\": 0.062368124696574434,\\n1048:            \\\"ci_lo\\\": 0.06201718433847767,\\n1569:            \\\"rho\\\": 0.06219925338517256,\\n2315:        \\\"rho\\\": 0.06253885238151985,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T04:57:39.016551+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/logprob_diagnosis/diagnosis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/logprob_diagnosis/diagnosis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T04:57:39.016762+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"total_gap\\\": 0.174,\\n    \\\"subset_effect_a\\\": 0.03921671115753153,\\n    \\\"condition_effect_bc\\\": 0.13536498031029492,\\n    \\\"n_effect_c\\\": 0.006654974114404744,\\n    \\\"t_effect_b_inferred\\\": 0.12871000619589018,\\n    \\\"conclusions\\\": [\\n      \\\"(a) MINOR: Instance subset effect is only +0.0392\\\",\\n      \\\"(b+c) SIGNIFICANT: T/N differences contribute +0.1354 to rho gap\\\",\\n      \\\"(c) NEGLIGIBLE: N effect is only +0.0067\\\",\\n      \\\"(d) RULED OUT: Both use identical per-token mean logprob normalization\\\"\\n    ],\\n    \\\"normalization_difference\\\": false\\n  },\\n  \\\"tests\\\": {\\n    \\\"baseline_ner\\\": {\\n      \\\"exp001\\\": {\\n        \\\"rho\\\": 0.31418270668758275,\\n        \\\"p\\\": 8.602743251931677e-06,\\n        \\\"n\\\": 193\\n      },\\n      \\\"exp012\\\": {\\n        \\\"rho\\\": 0.1396010152197563,\\n        \\\"p\\\": 0.001286366893477423,\\n        \\\"n\\\": 529\\n      }\\n    },\\n    \\\"baseline_re\\\": {\\n      \\\"exp001\\\": {\\n        \\\"rho\\\": 0.30964447975786663,\\n        \\\"p\\\": 8.831418345497867e-05,\\n        \\\"n\\\": 155\\n      },\\n      \\\"exp012\\\": {\\n        \\\"rho\\\": 0.24668271217578314,\\n        \\\"p\\\": 6.466504185414077e-07,\\n        \\\"n\\\": 397\\n      }\\n    },\\n    \\\"subset_effect_ner\\\": {\\n      \\\"exp012_on_200_overlap\\\": {\\n        \\\"rho\\\": 0.17881772637728782,\\n        \\\"p\\\": 0.012840401686677279,\\n        \\\"n\\\": 193\\n      },\\n      \\\"exp012_full_529\\\": {\\n        \\\"rho\\\": 0.1396010152197563,\\n        \\\"p\\\": 0.001286366893477423,\\n        \\\"n\\\": 529\\n      },\\n      \\\"exp012_nonoverlap\\\": {\\n        \\\"rho\\\": 0.11488481105483911,\\n        \\\"p\\\": 0.035291311218680906,\\n        \\\"n\\\": 336\\n      }\\n    },\\n    \\\"subset_effect_re\\\": {\\n      \\\"exp012_on_200_overlap\\\":
…[truncated 3528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T04:57:39.016941+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"logprob.*rho.*cond\\|cond.*logprob.*rho\\|logprob_rho_cond\\|re.*logprob.*0\\.002\\|0\\.002.*logprob\" /root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"logprob.*rho.*cond\\|cond.*logprob.*rho\\|logprob_rho_cond\\|re.*logprob.*0\\.002\\|0\\.002.*logprob\" /root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T04:57:39.017091+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T04:57:39.017345+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T04:57:39.017560+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"scierc\\\",\\n  \\\"subtask\\\": \\\"re\\\",\\n  \\\"n_samples\\\": 16,\\n  \\\"temperature\\\": 1.0,\\n  \\\"num_instances\\\": 551,\\n  \\\"use_train_format\\\": true,\\n  \\\"greedy_f1\\\": 0.4228855721393035,\\n  \\\"oracle_f1\\\": 0.6266397578203834,\\n  \\\"oracle_headroom\\\": 0.2037541856810799,\\n  \\\"fleiss_kappa_mean\\\": 0.3510270407688936,\\n  \\\"soft_jaccard_mean\\\": 0.614509203908681,\\n  \\\"correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.27897818810694835,\\n    \\\"p_value\\\": 1.570213281520457e-08,\\n    \\\"n\\\": 397\\n  },\\n  \\\"correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.2813061996083854,\\n    \\\"p_value\\\": 1.1780042209260059e-08,\\n    \\\"n\\\": 397\\n  },\\n  \\\"correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.15246162499658367,\\n    \\\"p_value\\\": 0.018351602927135544,\\n    \\\"n\\\": 239\\n  },\\n  \\\"correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.3075703278261049,\\n    \\\"p_value\\\": 1.2469729314555676e-06,\\n    \\\"n\\\": 239\\n  },\\n  \\\"n_gold_empty_filtered\\\": 154,\\n  \\\"n_greedy_f1_zero_filtered\\\": 158,\\n  \\\"structural_beats_surface\\\": true,\\n  \\\"rho_advantage\\\": 0.0023280115014370217,\\n  \\\"sample_f1_mean\\\": 0.3625127524561398,\\n  \\\"sample_f1_std\\\": 0.3815864789403641,\\n  \\\"sample_f1_pct_zero\\\": 44.30100755667506,\\n  \\\"logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.2865841277011422,\\n      \\\"p_rho\\\": 6.079730418168513e-09,\\n      \\\"tau\\\": 0.20904431900055762,\\n      \\\"p_tau\\\": 9.7115757157968e-09,\\n      \\\"auroc\\\": 0.6445594792681052,\\n      \\\"n\\\": 397\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": -0.026348741145267595,\\n      \\\"p_rho\\\": 0.685274324226724,\\n      \\\"tau\\\": -0.019070287903681895,\\n      \\\"p_tau\\\": 0.6791346824108437,\\n      \\\"auroc\\\": 0
…[truncated 411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T04:57:39.017720+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"0\\.062\" /root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_eval/report.json /root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_pilot/report.json /root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_dryrun/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"0\\.062\" /root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_eval/report.json /root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_pilot/report.json /root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_dryrun/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T04:57:39.017853+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T04:57:39.017975+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"logprob_rho_cond\\|logprob.*conditional\\|conditional.*logprob\\|rho_logprob_cond\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_unified/exp015_unified_report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"logprob_rho_cond\\|logprob.*conditional\\|conditional.*logprob\\|rho_logprob_cond\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_unified/exp015_unified_report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T04:57:39.018098+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T04:57:39.018285+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/conditional_filter_diagnosis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/conditional_filter_diagnosis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T04:57:39.018514+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"diagnosis_date\\\": \\\"2026-05-14\\\",\\n  \\\"issue\\\": \\\"Conditional filtering definition inconsistency across analysis scripts\\\",\\n  \\\"standard_definition\\\": \\\"Exclude instances where greedy_F1 == 0 (knowledge-gap instances where the model has zero extraction capability at T=0)\\\",\\n  \\\"sources\\\": {\\n    \\\"exp001_postprocess.py\\\": {\\n      \\\"line\\\": 128,\\n      \\\"code\\\": \\\"cond = [i for i in valid if f1s[i] > 0]\\\",\\n      \\\"filter\\\": \\\"greedy_f1 > 0\\\",\\n      \\\"status\\\": \\\"CORRECT\\\",\\n      \\\"report_file\\\": \\\"exp001_all_signals_report.json\\\",\\n      \\\"re_n_cond\\\": 238,\\n      \\\"ner_n_cond\\\": 478\\n    },\\n    \\\"run_mvp_pilot.py\\\": {\\n      \\\"line\\\": 259,\\n      \\\"code\\\": \\\"cond_mask.append(any(f > 0 for f in sample_f1s_i))\\\",\\n      \\\"filter\\\": \\\"any sample F1 > 0\\\",\\n      \\\"status\\\": \\\"WRONG\\\",\\n      \\\"report_file\\\": \\\"report.json\\\",\\n      \\\"re_n_cond\\\": 331,\\n      \\\"ner_n_cond\\\": 510\\n    },\\n    \\\"analyze_exp015_unified.py\\\": {\\n      \\\"lines\\\": \\\"290-297\\\",\\n      \\\"code\\\": \\\"any(per_instance_f1(s, inst['gold'], subtask=subtask) > 0 for s in inst['samples'])\\\",\\n      \\\"filter\\\": \\\"any sample F1 > 0\\\",\\n      \\\"status\\\": \\\"WRONG\\\"\\n    },\\n    \\\"analyze_logprob_baseline.py\\\": {\\n      \\\"lines\\\": \\\"95-100\\\",\\n      \\\"code\\\": \\\"any(f > 0 for f in sample_f1s)\\\",\\n      \\\"filter\\\": \\\"any sample F1 > 0\\\",\\n      \\\"status\\\": \\\"WRONG\\\"\\n    },\\n    \\\"analyze_component_wise_re.py\\\": {\\n      \\\"lines\\\": \\\"107-110\\\",\\n      \\\"code\\\": \\\"any(per_instance_f1(s, inst['gold'], subtask='re') > 0 for s in inst['samples'])\\\",\\n      \\\"filter\\\": \\\"any sample F1 > 0\\\",\\n      \\\"status\\\": \\\"WRONG\\\"\\n    },\\n    \\\"analyze_exp004_re_diagnostic.py\\\": {\\n 
…[truncated 858 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T04:57:39.018731+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -name \"*.json\" -path \"*exp_015*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -name \"*.json\" -path \"*exp_015*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-16T04:57:39.018870+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_015_unified/exp015_unified_report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T04:57:39.019020+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_015_unified/exp015_unified_report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_015_unified/exp015_unified_report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-16T04:57:39.019180+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"0\\.002\" /root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"0\\.002\" /root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-16T04:57:39.019527+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"ner\\\": {\\n    \\\"n_total\\\": 551,\\n    \\\"n_valid\\\": 529,\\n    \\\"n_conditional\\\": 501,\\n    \\\"median_f1_full\\\": 0.6666666666666666,\\n    \\\"median_f1_cond\\\": 0.6666666666666666,\\n    \\\"signals\\\": {\\n      \\\"soft_jaccard\\\": {\\n        \\\"full\\\": {\\n          \\\"rho\\\": 0.3565325519208428,\\n          \\\"p_rho\\\": 2.6630584025369088e-17,\\n          \\\"tau\\\": 0.2657836835394407,\\n          \\\"p_tau\\\": 6.647794397251756e-18,\\n          \\\"auroc\\\": 0.6656378600823045,\\n          \\\"n\\\": 529\\n        },\\n        \\\"cond\\\": {\\n          \\\"rho\\\": 0.4120469334760367,\\n          \\\"p_rho\\\": 5.914759491394964e-22,\\n          \\\"tau\\\": 0.3017489674161096,\\n          \\\"p_tau\\\": 1.3124956005559717e-21,\\n          \\\"auroc\\\": 0.6871361196942593,\\n          \\\"n\\\": 501\\n        }\\n      },\\n      \\\"fleiss_kappa\\\": {\\n        \\\"full\\\": {\\n          \\\"rho\\\": 0.2651050577998432,\\n          \\\"p_rho\\\": 5.859602237137789e-10,\\n          \\\"tau\\\": 0.20273442316972345,\\n          \\\"p_tau\\\": 4.802036629715087e-11,\\n          \\\"auroc\\\": 0.6243489021266799,\\n          \\\"n\\\": 529\\n        },\\n        \\\"cond\\\": {\\n          \\\"rho\\\": 0.3060194865287414,\\n          \\\"p_rho\\\": 2.537977550420891e-12,\\n          \\\"tau\\\": 0.2307818354774394,\\n          \\\"p_tau\\\": 2.7798130476385713e-13,\\n          \\\"auroc\\\": 0.6416734428362335,\\n          \\\"n\\\": 501\\n        }\\n      },\\n      \\\"mean_logprob\\\": {\\n        \\\"full\\\": {\\n          \\\"rho\\\": 0.1396010152197563,\\n          \\\"p_rho\\\": 0.001286366893477423,\\n          \\\"tau\\\": 0.10064101054079479,\\n          \\\"p_tau\\\": 0.0009969869396821928,\\n          \\\"auroc\\\": 0.5584765029209474,\\n          \\\"n\\\": 529\\n        },\\n        \\\"cond\\\": {\\n          \\\"rho\\\": 0.16273823232575188,\\
…[truncated 8031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-16T04:57:39.019697+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"36:  \\\"rho_advantage\\\": 0.0023280115014370217,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-16T04:57:39.019825+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"0\\.002\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"0\\.002\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-16T04:57:39.019952+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"1647:          \\\"max\\\": -0.0027346352079722996\\n2387:          \\\"max\\\": -0.002734562366314261\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-16T04:57:39.020071+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"wnut\\|WNUT\" /root/autodl-tmp/struct_self_consist_ie/output/analysis_unified_rho_full.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"wnut\\|WNUT\" /root/autodl-tmp/struct_self_consist_ie/output/analysis_unified_rho_full.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-16T04:57:39.020216+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-16T04:57:39.020336+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"*.tex\" -path \"*/sections/*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"*.tex\" -path \"*/sections/*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-16T04:57:39.020464+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-16T04:57:39.020618+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-16T04:57:39.020947+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc_n8_logprob_ner\\\": {\\n    \\\"metrics\\\": {\\n      \\\"SJ\\\": {\\n        \\\"AUROC\\\": {\\n          \\\"value\\\": 0.7151643358013084,\\n          \\\"ci_95\\\": [\\n            0.6584056764120945,\\n            0.7682940600519558\\n          ]\\n        },\\n        \\\"Spearman_rho\\\": {\\n          \\\"value\\\": 0.3565325519208428,\\n          \\\"ci_95\\\": [\\n            0.27093589913089045,\\n            0.43847517254753815\\n          ]\\n        },\\n        \\\"Kendall_tau\\\": {\\n          \\\"value\\\": 0.2657836835394407,\\n          \\\"ci_95\\\": [\\n            0.20308584802623142,\\n            0.32764058791077727\\n          ]\\n        },\\n        \\\"ECE\\\": {\\n          \\\"value\\\": 0.45194957670806446\\n        }\\n      },\\n      \\\"FK\\\": {\\n        \\\"AUROC\\\": {\\n          \\\"value\\\": 0.628716652955694,\\n          \\\"ci_95\\\": [\\n            0.5673132538124828,\\n            0.6923820223647049\\n          ]\\n        },\\n        \\\"Spearman_rho\\\": {\\n          \\\"value\\\": 0.2651050577998432,\\n          \\\"ci_95\\\": [\\n            0.1682875300012899,\\n            0.35268256172379303\\n          ]\\n        },\\n        \\\"Kendall_tau\\\": {\\n          \\\"value\\\": 0.20273442316972345,\\n          \\\"ci_95\\\": [\\n            0.13006411469552326,\\n            0.27188613541902706\\n          ]\\n        },\\n        \\\"ECE\\\": {\\n          \\\"value\\\": 0.4511674846945833\\n        }\\n      },\\n      \\\"logprob\\\": {\\n        \\\"AUROC\\\": {\\n          \\\"value\\\": 0.5805813452422924,\\n          \\\"ci_95\\\": [\\n            0.5218723422636723,\\n            0.6426371957852407\\n          ]\\n        },\\n        \\\"Spearman_rho\\\": {\\n          \\\"value\\\": 0.1396010152197563,\\n          \\\"ci_95\\\": [\\n            0.05136070196928419,\\n            0.2238566300960571\\n          ]\\n        },\\n 
…[truncated 7966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-16T04:57:39.021147+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find paper tex files locally",
  "subagent_type": "Explore",
  "prompt": "Find all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ — I need to locate the paper sections that contain specific numerical values (0.002, 0.062, 0.110, 0.473). Search for these files using glob patterns, and grep for these values in any tex files found. Report file paths and matching lines with context."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Agent",
  "tool_args": {
    "description": "Find paper tex files locally",
    "subagent_type": "Explore",
    "prompt": "Find all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ — I need to locate the paper sections that contain specific numerical values (0.002, 0.062, 0.110, 0.473). Search for these files using glob patterns, and grep for these values in any tex files found. Report file paths and matching lines with context."
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-16T04:57:39.021313+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"logprob\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_unified/exp015_unified_report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"logprob\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_unified/exp015_unified_report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-16T04:57:39.021449+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-16T04:57:39.021570+00:00_

artifacts/dream_reports/dream_20260514T093336/best/paper.tex
artifacts/dream_reports/dream_20260514T093336/median/paper.tex
artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
artifacts/dream_reports/dream_20260514T105303/best/paper.tex
artifacts/dream_reports/dream_20260514T105303/median/paper.tex
artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/dream_reports/dream_20260514T203201/best/paper.tex
artifacts/dream_reports/dream_20260514T203201/median/paper.tex
artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
artifacts/bootstrap_ci_tables.tex
artifacts/dream_reports/dream_20260515T092545/best/paper.tex
artifacts/dream_reports/dream_20260515T092545/median/paper.tex
artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
artifacts/_project/paper/freeform_ablation_appendix_table.tex
artifacts/freeform_ablation_appendix_table.tex
artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
artifacts/n_scaling_appendix_tables.tex
docs/paper/main.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/n_scaling_appendix_tables.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/experiments.tex
docs/paper/sections/abstract.tex
docs/paper/sections/introduction.tex
docs/paper/sections/experiments.tex
docs/paper/sections/discussion.tex
docs/paper/sections/related_work.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/limitations.tex
docs/paper/sections/method.tex
docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-16T04:57:39.021706+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.002|0\\.062|0\\.110|0\\.473",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "type": "tex",
  "output_mode": "content",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.002|0\\.062|0\\.110|0\\.473",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "type": "tex",
    "output_mode": "content",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-16T04:57:39.021829+00:00_

&lt;persisted-output>
Output too large (20.4KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/ff14a560-c52e-4a4a-af53-469861f178d5/tool-results/toolu_01RfgyuTasSYsCUTs7uaW7EU.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-15-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-16-Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
artifacts/freeform_ablation_appendix_table.tex:17:Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-18-Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-19-\bottomrule
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-31-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-32-\multirow{3}{*}{NER}
artifacts/freeform_ablation_appendix_table.tex:33:  & Greedy        & 0.6182 & 0.6204 & \textbf{+0.0022} \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-34-  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-35-  & Selection gap & +0.0059 & +0.0018 & $-$0.0041 \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-57-FK & 0.2665 & 0.3197 & \textbf{+0.0532} &
…[truncated 272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-16T04:57:39.021976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/ff14a560-c52e-4a4a-af53-469861f178d5/tool-results/toolu_01RfgyuTasSYsCUTs7uaW7EU.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/ff14a560-c52e-4a4a-af53-469861f178d5/tool-results/toolu_01RfgyuTasSYsCUTs7uaW7EU.txt"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-16T04:57:39.022165+00:00_

1	/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-15-\midrule
2	/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-16-Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
3	artifacts/freeform_ablation_appendix_table.tex:17:Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
4	/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-18-Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
5	/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-19-\bottomrule
6	--
7	/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-31-\midrule
8	/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-32-\multirow{3}{*}{NER}
9	artifacts/freeform_ablation_appendix_table.tex:33:  & Greedy        & 0.6182 & 0.6204 & \textbf{+0.0022} \\
10	/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-34-  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
11	/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-35-  & Selection gap & +0.0059 & +0.0018 & $-$0.0041 \\
12	--
13	/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-57-FK & 0.2665 & 0.3197 & \textbf{+0.0532} & 0.2752 & 0.3145 & \textbf{+0.0393} \\
14	/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex-58-LP & 0.2052 & 0.2129 & \textbf{+0.0077} & 0.2662 & 0.3042 & \textbf{+0.0379} \\
15	artifacts/
…[truncated 19344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-16T04:57:39.022380+00:00_

Perfect! Now I have the complete search results. Let me compile the findings for you.

## Summary of Findings

I found **35 .tex files** in the project directory. The search for the four specific numerical values (0.002, 0.062, 0.110, 0.473) returned **multiple matches** across several files. Here are the key locations:

### Files Containing the Target Values:

1. **/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex**
   - Line 73: Contains `0.002` - Part of table with instance-level signals (consensus-proximity selection): `SJ & $0.646 \pm 0.002$ & .68 & 0.386 \\`

2. **/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex**
   - Line 60: Contains `0.473` - `\quad EM & $0.473{\pm}0.010$ & --- \\`
   - Line 87: Contains `0.002` - Comparing SJ and VC at N=16: `At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$)`
   - Line 150: Contains `0.110` and `0.473` - `For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$)`
   - Line 203: Contains `0.002` - `The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$)`
   - Line 306: Contains `0.002` - Statistical significance testing: `On SciERC NER ($n{=}529$), SJ--FK ($\Delta\rho{=}0.147$--$0.160$, all $p{\leq}0.002$)`
   - Line 686: Contains `0.062` - Table with LP range values: `Mean LP range & 0.0623 & 0.0599 & $-$0.0024 \\` (0.0623 rounds/matches the pattern)
   - Line 701: Contains `0.002` - Table row: `& Greedy & 0.6182 & 0.6204 & $+$0.0022 \\`
   - Line 726: Contains `0.002` - Table row: `EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\`

3. **/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex**
   - Line
…[truncated 2338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Agent",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-16T04:57:39.022544+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"45:      \\\"mean_logprob\\\": {\\n107:      \\\"sj_vs_mean_logprob\\\": {\\n238:      \\\"mean_logprob\\\": [\\n439:      \\\"mean_logprob\\\": {\\n501:      \\\"sj_vs_mean_logprob\\\": {\\n632:      \\\"mean_logprob\\\": [\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-16T04:57:39.022708+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.002|logprob.*cond|cond.*logprob",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.002|logprob.*cond|cond.*logprob",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-16T04:57:39.022863+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-71-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-72-\multicolumn{4}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
docs/paper/sections/experiments.tex:73:SJ           & $0.646 \pm 0.002$ & .68 & 0.386 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-74-FK           & $0.646 \pm 0.001$ & .79 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-75-EM           & $0.637 \pm 0.001$ & .45 & 0.372 \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-85-VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-86-SJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, suggesting that structural and binary-agreement signals are the most robust to $N$.
docs/paper/sections/appendix.tex:87:At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), making it a more stable alternative at higher sample sizes.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-88-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-89-\paragraph{Transfer across model families.}
--
docs/paper/sections/appendix.tex-201-On the full set, EM is dil
…[truncated 4136 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-16T04:57:39.023011+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.062|WNUT|wnut",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.062|WNUT|wnut",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-16T04:57:39.023222+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-9-\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-10-\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
docs/paper/sections/experiments.tex:11:\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-12-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-13-\paragraph{Models and sampling.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-48-On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$); the $\rho$--AUROC dissociation across datasets reflects use-case alignment.
docs/paper/sections/experiments.tex-49-On $^\dagger$RE, LP rises above SJ and FK at $N{=}16$ (Table~\ref{tab:multiseed}).
docs/paper/sections/experiments.tex:50:At the capability boundary---WNUT-17 (52\% zero F1)---all conditional signals collapse (Table~\ref{tab:wnut}); restricting to non-zero instances reshuffles rankings, with EM strongest on NER ($\rho{=}0.360$) and $^\dagger$RE ($\rho{=}0.417$) while LP $^\dagger$RE collapses to $\rho{=}0.011$ (Figure~\ref{fig:signal_heatmap}, Appendix~\ref{app:additional}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-51-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/expe
…[truncated 13818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-16T04:57:39.023381+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.110|0\\.473|sentence.length|sent.len",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.110|0\\.473|sentence.length|sent.len",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-16T04:57:39.023520+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-58-\quad SJ &  & $0.474{\pm}0.009$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-59-\quad FK &  & $0.467{\pm}0.009$ & --- \\
docs/paper/sections/appendix.tex:60:\quad EM &  & $0.473{\pm}0.010$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-61-\quad VC &  & $0.470{\pm}0.006$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-62-\quad LP &  & $0.311{\pm}0.003$ & --- \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-147-\paragraph{Capability stratification.}
docs/paper/sections/appendix.tex-148-For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
docs/paper/sections/appendix.tex:149:The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
docs/paper/sections/appendix.tex:150:For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
docs/paper/sections/appendix.tex:151:Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-152-For RE, entity count and relation count are st
…[truncated 361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-16T04:57:39.023687+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "logprob.*RE|LP.*RE|RE.*LP|RE.*logprob|conditional.*RE|cond.*rho|logprob.*coll|LP.*coll",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "context": "2",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Grep",
  "tool_args": {
    "pattern": "logprob.*RE|LP.*RE|RE.*LP|RE.*logprob|conditional.*RE|cond.*rho|logprob.*coll|LP.*coll",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "context": "2",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-16T04:57:39.023916+00:00_

&lt;persisted-output>
Output too large (44.4KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/ff14a560-c52e-4a4a-af53-469861f178d5/tool-results/toolu_012ixdEELW31QN1YydkGbYoQ.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex-4-
docs/paper/sections/limitations.tex-5-We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
docs/paper/sections/limitations.tex:6:The free-form ablation covers SciERC NER and CoNLL NER with one model; RE shows a directional LP reversal under free-form decoding.
docs/paper/sections/limitations.tex-7-Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
docs/paper/sections/limitations.tex:8:LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
docs/paper/sections/limitations.tex-9-We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
docs/paper/sections/limitations.tex:10:We evaluate signals individually; whether signal combinations (e.g., LP $\times$ consistency) or learned weightings could close the selection gap is unexplored.
docs/paper/sections/limitations.tex:11:The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compres
…[truncated 85 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-16T04:57:39.024070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "205",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "205",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-16T04:57:39.024241+00:00_

205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
207	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
208	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
209	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
210	
211	\begin{table}[t]
212	\centering
213	\small
214	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
215	\label{tab:wnut}
216	\begin{tabular}{lccccc}
217	\toprule
218	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
219	\midrule
220	VC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
221	FK      & .125 & .001 & .555 & .169 & .002 \\
222	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
223	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
224	LP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	\paragraph{Cross-configuration selection analysis.}
230	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
231	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
232	On Co
…[truncated 1122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-16T04:57:39.024435+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/figures/ -name \"*heatmap*\" -o -name \"*signal*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output/figures/ -name \"*heatmap*\" -o -name \"*signal*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-16T04:57:39.024567+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-16T04:57:39.024687+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"logprob\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_unified/exp015_summary.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"logprob\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_unified/exp015_summary.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-16T04:57:39.024809+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-16T04:57:39.024939+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/figures/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/figures/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-16T04:57:39.025062+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"fig_selection_gap.pdf\\nfig_selection_gap.png\\nlp_range_cdf.pdf\\nlp_range_cdf.png\\nlp_range_cdf_check.png\\nlp_range_cdf_n16_3seed.pdf\\nlp_range_cdf_n16_3seed.png\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-16T04:57:39.025201+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "heatmap|signal_heatmap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "context": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Grep",
  "tool_args": {
    "pattern": "heatmap|signal_heatmap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "context": "5"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-16T04:57:39.025342+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-45-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-46-\paragraph{Signal rankings are difficulty-dependent.}
docs/paper/sections/experiments.tex-47-On SciERC NER, structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over surface ($\rho{\leq}0.295$) and LP ($0.205$); bootstrap CIs confirm the SJ--LP gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-48-On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$); the $\rho$--AUROC dissociation across datasets reflects use-case alignment.
docs/paper/sections/experiments.tex-49-On $^\dagger$RE, LP rises above SJ and FK at $N{=}16$ (Table~\ref{tab:multiseed}).
docs/paper/sections/experiments.tex:50:At the capability boundary---WNUT-17 (52\% zero F1)---all conditional signals collapse (Table~\ref{tab:wnut}); restricting to non-zero instances reshuffles rankings, with EM strongest on NER ($\rho{=}0.360$) and $^\dagger$RE ($\rho{=}0.417$) while LP $^\dagger$RE collapses to $\rho{=}0.011$ (Figure~\ref{fig:signal_heatmap}, Appendix~\ref{app:additional}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-51-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-52-%% ============================================================
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-53-\subsection{The Correlation-Selection Gap}
docs/paper/sections/experiments.tex-54-\label{sec:selection_gap}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
…[truncated 2022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-16T04:57:39.025532+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"logprob.*rho\\|rho.*logprob\\|mean_logprob\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"logprob.*rho\\|rho.*logprob\\|mean_logprob\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-16T04:57:39.025661+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-16T04:57:39.025781+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"scierc_n8.*re\\|scierc_re\\|re_n8\\|_re_\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"scierc_n8.*re\\|scierc_re\\|re_n8\\|_re_\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-16T04:57:39.025900+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-16T04:57:39.026014+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"0\\.011\\|0\\.0114\\|0\\.0110\" /root/autodl-tmp/struct_self_consist_ie/output/ --include=\"*.json\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"0\\.011\\|0\\.0114\\|0\\.0110\" /root/autodl-tmp/struct_self_consist_ie/output/ --include=\"*.json\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-16T04:57:39.026147+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-16T04:57:39.026282+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"mean_logprob\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"mean_logprob\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-16T04:57:39.026408+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-16T04:57:39.026522+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"scierc_n8\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"scierc_n8\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-16T04:57:39.026643+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2:  \\\"scierc_n8_logprob_ner\\\": {\\n187:  \\\"scierc_n8_logprob_re\\\": {\\n1482:  \\\"llama_scierc_n8_ner\\\": {\\n1667:  \\\"llama_scierc_n8_re\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-16T04:57:39.026757+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"0\\.011\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"0\\.011\" /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-16T04:57:39.026871+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-16T04:57:39.026981+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"re.*logprob_rho\" /root/autodl-tmp/struct_self_consist_ie/output/review_round8/ --include=\"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"re.*logprob_rho\" /root/autodl-tmp/struct_self_consist_ie/output/review_round8/ --include=\"*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-16T04:57:39.027097+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-16T04:57:39.027242+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -400 /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -400 /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-16T04:57:39.027624+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc_n8_logprob_ner\\\": {\\n    \\\"metrics\\\": {\\n      \\\"SJ\\\": {\\n        \\\"AUROC\\\": {\\n          \\\"value\\\": 0.7151643358013084,\\n          \\\"ci_95\\\": [\\n            0.6584056764120945,\\n            0.7682940600519558\\n          ]\\n        },\\n        \\\"Spearman_rho\\\": {\\n          \\\"value\\\": 0.3565325519208428,\\n          \\\"ci_95\\\": [\\n            0.27093589913089045,\\n            0.43847517254753815\\n          ]\\n        },\\n        \\\"Kendall_tau\\\": {\\n          \\\"value\\\": 0.2657836835394407,\\n          \\\"ci_95\\\": [\\n            0.20308584802623142,\\n            0.32764058791077727\\n          ]\\n        },\\n        \\\"ECE\\\": {\\n          \\\"value\\\": 0.45194957670806446\\n        }\\n      },\\n      \\\"FK\\\": {\\n        \\\"AUROC\\\": {\\n          \\\"value\\\": 0.628716652955694,\\n          \\\"ci_95\\\": [\\n            0.5673132538124828,\\n            0.6923820223647049\\n          ]\\n        },\\n        \\\"Spearman_rho\\\": {\\n          \\\"value\\\": 0.2651050577998432,\\n          \\\"ci_95\\\": [\\n            0.1682875300012899,\\n            0.35268256172379303\\n          ]\\n        },\\n        \\\"Kendall_tau\\\": {\\n          \\\"value\\\": 0.20273442316972345,\\n          \\\"ci_95\\\": [\\n            0.13006411469552326,\\n            0.27188613541902706\\n          ]\\n        },\\n        \\\"ECE\\\": {\\n          \\\"value\\\": 0.4511674846945833\\n        }\\n      },\\n      \\\"logprob\\\": {\\n        \\\"AUROC\\\": {\\n          \\\"value\\\": 0.5805813452422924,\\n          \\\"ci_95\\\": [\\n            0.5218723422636723,\\n            0.6426371957852407\\n          ]\\n        },\\n        \\\"Spearman_rho\\\": {\\n          \\\"value\\\": 0.1396010152197563,\\n          \\\"ci_95\\\": [\\n            0.05136070196928419,\\n            0.2238566300960571\\n          ]\\n        },\\n 
…[truncated 7969 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-16T04:57:39.027864+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"0\\.011\" /root/autodl-tmp/struct_self_consist_ie/output/review_round8/ --include=\"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"0\\.011\" /root/autodl-tmp/struct_self_consist_ie/output/review_round8/ --include=\"*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-16T04:57:39.028006+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-16T04:57:39.028155+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"0\\.011\" /root/autodl-tmp/struct_self_consist_ie/output/review_round9_experiments/ --include=\"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"0\\.011\" /root/autodl-tmp/struct_self_consist_ie/output/review_round9_experiments/ --include=\"*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-16T04:57:39.028337+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/review_round9_experiments/freeform_conll/summary.json:316:        \\\"std\\\": 0.011952115390956714,\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round9_experiments/freeform_conll/summary.json:328:        \\\"std\\\": 0.011909327006374204,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-16T04:57:39.028473+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"re_LP\\|re_lp\\|re.*logprob\\|logprob.*re\" /root/autodl-tmp/struct_self_consist_ie/output/rho_audit_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"re_LP\\|re_lp\\|re.*logprob\\|logprob.*re\" /root/autodl-tmp/struct_self_consist_ie/output/rho_audit_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-16T04:57:39.028597+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-16T04:57:39.028744+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"*heatmap*\" -not -path \"*/.git/*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"*heatmap*\" -not -path \"*/.git/*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-16T04:57:39.028878+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -rn \"0\\.011\" /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/ --include=\"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -rn \"0\\.011\" /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/ --include=\"*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-16T04:57:39.029009+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/figures/paper/fig_signal_heatmap.pdf\\n/root/autodl-tmp/struct_self_consist_ie/figures/paper/fig_signal_heatmap.png\\n/root/autodl-tmp/struct_self_consist_ie/artifacts/figures/fig_signal_heatmap.pdf\\n/root/autodl-tmp/struct_self_consist_ie/artifacts/figures/fig_signal_heatmap.png\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-16T04:57:39.029151+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/report.json:100:      \\\"rho\\\": 0.011185364740047766,\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/all_signals_5signal.json:403:            \\\"value\\\": 0.011185364740047766,\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/reliability_data_1024.json:408:    \\\"mean_logprob\\\": -0.011439259208573777\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/reliability_data_1024.json:1032:    \\\"mean_logprob\\\": -0.011435031874042564\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/reliability_data_1024.json:2640:    \\\"mean_logprob\\\": -0.011447283837923752\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-16T04:57:39.029286+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"*.py\" -path \"*heatmap*\" -not -path \"*/.git/*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"*.py\" -path \"*heatmap*\" -not -path \"*/.git/*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-16T04:57:39.029408+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-16T04:57:39.029524+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"generate_heatmap*\" -o -name \"plot_heatmap*\" -o -name \"fig_signal*\" -not -path \"*/.git/*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"generate_heatmap*\" -o -name \"plot_heatmap*\" -o -name \"fig_signal*\" -not -path \"*/.git/*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-16T04:57:39.029644+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/figures/paper/fig_signal_heatmap.pdf\\n/root/autodl-tmp/struct_self_consist_ie/figures/paper/fig_signal_heatmap.png\\n/root/autodl-tmp/struct_self_consist_ie/artifacts/figures/fig_signal_heatmap.pdf\\n/root/autodl-tmp/struct_self_consist_ie/artifacts/figures/fig_signal_heatmap.png\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-16T04:57:39.029797+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -120 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -120 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-16T04:57:39.030023+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"scierc\\\",\\n  \\\"subtask\\\": \\\"joint\\\",\\n  \\\"n_samples\\\": 8,\\n  \\\"temperature\\\": 1.0,\\n  \\\"num_instances\\\": 551,\\n  \\\"use_train_format\\\": true,\\n  \\\"ner_greedy_f1\\\": 0.6632805497460412,\\n  \\\"ner_oracle_f1\\\": 0.7775133848899465,\\n  \\\"ner_oracle_headroom\\\": 0.11423283514390525,\\n  \\\"ner_fleiss_kappa_mean\\\": 0.3932668065534345,\\n  \\\"ner_soft_jaccard_mean\\\": 0.6963097751953397,\\n  \\\"ner_correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.2665109373463269,\\n    \\\"p_value\\\": 4.716829112137585e-10,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.3598905669976535,\\n    \\\"p_value\\\": 1.2752281196882738e-17,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.17607370722783125,\\n    \\\"p_value\\\": 0.00011078924939793821,\\n    \\\"n\\\": 477\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.3113352549686453,\\n    \\\"p_value\\\": 3.5148620246813462e-12,\\n    \\\"n\\\": 477\\n  },\\n  \\\"ner_n_gold_empty_filtered\\\": 22,\\n  \\\"ner_n_greedy_f1_zero_filtered\\\": 52,\\n  \\\"ner_structural_beats_surface\\\": true,\\n  \\\"ner_rho_advantage\\\": 0.09337962965132657,\\n  \\\"ner_sample_f1_mean\\\": 0.6077394535406134,\\n  \\\"ner_sample_f1_std\\\": 0.3177849195309394,\\n  \\\"ner_sample_f1_pct_zero\\\": 12.594517958412098,\\n  \\\"ner_logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.20517413101613924,\\n      \\\"p_rho\\\": 1.9498006196855416e-06,\\n      \\\"tau\\\": 0.14782758668777154,\\n      \\\"p_tau\\\": 1.2434769103035355e-06,\\n      \\\"auroc\\\": 0.6115722797477874,\\n      \\\"n\\\": 529\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.1537825418721844,\\n      \\\"p_rho\\\": 0.0007519115126420073,\\n      \\\"tau\\\": 0.111054535706
…[truncated 2345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-16T04:57:39.030205+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"0\\.011\" /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/all_signals_5signal.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"0\\.011\" /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/all_signals_5signal.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-16T04:57:39.030341+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"403:            \\\"value\\\": 0.011185364740047766,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-16T04:57:39.030513+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-16T04:57:39.030658+00:00_

3seed_ner_summary.md
3seed_summary
__pycache__
_project
analysis_fk_bootstrap_ci_full.json
analysis_lp_range_cdf.json
analysis_lp_range_cdf_n16_3seed.json
analysis_scierc_n16_3seed_selection_f1.json
analysis_scierc_re_n16_3seed_selection_f1.json
analysis_unified_rho.json
analysis_unified_rho_full.json
analyze_exp004_re_diagnostic.py
analyze_exp004_v2_re_diagnostic.py
analyze_exp005_v2_temperature.py
analyze_exp015_metrics_expansion.py
analyze_exp016_ensemble.py
analyze_ood_signals.py
audit_autodl5090_loop3.md
audit_gpu5090_4x2_loop3.md
auroc_bug_diagnosis.md
autodl_process_check.md
bjb1_status_report.md
bootstrap_ci_nscaling
bootstrap_ci_summary.json
bootstrap_ci_tables.tex
consistency.py
d072_paper_patch_inventory.md
data
data_utils.py
dream_reports
evaluate_verifier.py
evaluation.py
exp-001
exp-015
exp001_postprocess.py
exp005_temperature
exp009_stratification_analysis.py
exp010_selection_curves
exp_001
exp_001_n16
exp_001_ner_n16_scierc
exp_001_seed456_v2_ner
exp_002
exp_003
exp_004_re_diagnostic
exp_004_v2
exp_005
exp_005_v2
exp_009_capability_stratification
exp_009_v2
exp_009_v2_re_rerun
exp_009_v2_stratification.py
exp_010_selection_curves
exp_011_ood_scierc_to_conll
exp_012_logprob_baseline
exp_012_rerun_1024
exp_015_metrics_expansion
exp_016_rerun_1024
exp_016_rerun_1024_bootstrap
exp_016_signal_ensemble
exp_016_v2
exp_016_v2_ensemble.py
exp_017_llama_conll_n8_t07
exp_018
exp_018_provenance_report.md
exp_freeform_ablation
exp_freeform_conll_4seed
exp_llama3b_scierc_ablation
exp_verbalized_confidence
fig_selection_gap.png
figures
fk_excess_agreement_all_configs.md
freeform_3seed_summary.json
freeform_ablation_appendix_table.tex
freeform_ablation_deep_analysis.md
freeform_ablation_results.md
ft_001
ft_002
greedy_f1_discrepancy_audit.md
heatmap_data_audit.md
logprob_tie_analysis.md
loo_sj_cross_dataset
lp_range_cdf.pdf
lp_range_cdf.png
lp_range_cdf_n16_3seed.pdf
lp_range_cdf_n16_3seed.png
manifest.yaml
multi_seed_stability_table.md
multiseed_flip_overlap_analys
…[truncated 687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-16T04:57:39.030825+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/provenance_audit_c032_c023_c021.md",
  "content": "# Provenance Audit: c032 / c023 / c021\n\n**Date**: 2026-05-16\n**Auditor**: automated provenance trace\n**Scope**: Three claims in paper_provenance.yaml where registered values diverge from paper text\n\n---\n\n## c032: logprob conditional RE ρ\n\n- **Provenance yaml claim**: paper says ρ=0.002\n- **Registry value**: exp_015_metrics_expansion → re.logprob_rho_cond = 0.1457\n- **Current paper text**: ρ=0.011 (experiments.tex:50, appendix.tex:137)\n\n### Source trace\n\nThe **current paper** says ρ=0.011 in two places:\n1. `experiments.tex:50` — \"LP †RE collapses to ρ=0.011\"\n2. `appendix.tex:137` — heatmap caption: \"LP RE collapses to near-zero (ρ=0.011)\"\n\nThe value **0.01119** is in:\n- `output/exp_012_rerun_1024/report.json:100` — `re_logprob_baseline.conditional.rho = 0.011185364740047766`\n- `output/exp_012_rerun_1024/all_signals_5signal.json:403` — same value\n- Conditions: SciERC RE, N=8, T=1.0, max_tokens=1024, **correct conditional filter** (greedy_f1 > 0, n=238)\n\n### Why the discrepancy\n\n| Value | Source | Filter | n_cond | Status |\n|-------|--------|--------|--------|--------|\n| 0.002 | provenance yaml claim | unknown | — | **STALE** — paper was updated to 0.011; 0.002 untraceable in any output file |\n| 0.1457 | exp_015_metrics_expansion | WRONG: any sample F1 > 0 | 331 | Wrong filter inflates n, changes correlation |\n| **0.011** | exp_012_rerun_1024 | CORRECT: greedy_f1 > 0 | 238 | Current paper value |\n\nThe `conditional_filter_diagnosis.json` documents that exp_015 (and several other scripts) used the wrong conditional filter (\"any sample F1 > 0\" instead of \"greedy_f1 > 0\"), inflating the conditional set from n=238 to n=331 for RE. This is the root cause of the registry's 0.1457.\n\n### Conclusion\n\n**Provenance yaml is stale.** The paper was already corrected from 0.002 to 0.011. The current paper value (0.011 from exp_012_rerun_1024, correct conditional filter) is correct. The registry value (0.1457) uses a known-wrong conditional filter and should be annotated as deprecated.\n\n---\n\n## c023: RE SJ ρ by sentence length (Q1/Q4)\n\n- **Paper values**: Q1=0.110, Q4=0.473, Fisher z p=0.004\n- **Registry values**: exp_009_capability_stratification → Q1=0.447, Q4=0.540\n\n### Source trace\n\nPaper values match **exp_009_v2_re_rerun** exactly:\n\nFrom `output/exp_009_v2_re_rerun/summary.txt`:\n```\nStratification by Sentence Length QUARTILES (primary, independent)\n  Q1 (low)   n=117  SJ 0.110[-0.08,0.29]\n  Q2         n=93   SJ 0.308[0.09,0.50]\n  Q3         n=92   SJ 0.372[0.18,0.54]\n  Q4 (high)  n=95   SJ 0.473[0.28,0.62]\n\nFisher z-test low_vs_high:\n  sj   z=-2.878  p=0.004*\n```\n\nAll three paper values (Q1=0.110, Q4=0.473, p=0.004) match the v2 rerun output character-for-character.\n\nFrom `output/exp_009_v2_re_rerun/results.json`:\n- `by_sent_len_quartiles.\"Q1 (low)\".signals.sj.rho = 0.10961735` → rounds to 0.110\n- `by_sent_len_quartiles.\"Q4 (high)\".signals.sj.rho = 0.47332...` → rounds to 0.473\n- Fisher z low_vs_high sj p = 0.00435... → rounds to 0.004\n\n### Why the registry differs\n\nThe registry values (Q1=0.447, Q4=0.540) come from the **original exp_009_capability_stratification**, which:\n1. Did NOT apply gold-empty filtering (included 154 instances with empty gold RE annotations)\n2. Used all 551 raw instances instead of the filtered 397\n\nThe v2 rerun applied proper gold-filtering (551 → 397 after removing gold-empty), which is the mandated pipeline for all ρ values in the paper.\n\n| Value set | Source | Gold filter | n_RE | Status |\n|-----------|--------|-------------|------|--------|\n| Q1=0.447, Q4=0.540 | exp_009 original | No | 551 | **Outdated** — pre-gold-filter |\n| **Q1=0.110, Q4=0.473** | exp_009_v2_re_rerun | Yes | 397 | Current paper value |\n\n### Conclusion\n\n**Paper values are correct.** They come from exp_009_v2_re_rerun with proper gold-filtering. The registry entry for exp_009_capability_stratification is outdated and should be annotated as superseded by exp_009_v2_re_rerun.\n\n---\n\n## c021: WNUT SJ ρ\n\n- **Provenance yaml claim**: paper says ρ=0.062 (p=0.106)\n- **Registry values**: exp_003_ner_wnut17 → 0.082; exp_003_wnut17_eval → 0.089\n\n### Source trace — current paper\n\nThe **current paper** (appendix.tex:222, Table tab:wnut) shows:\n```\nSJ  .089  .020  .517  .288  <1e-7\n```\ni.e., SJ full-set ρ = **0.089**, p = 0.020\n\nThis matches `output/exp003_wnut17_eval/report.json`:\n- `correlation_softjaccard_vs_f1_full.rho = 0.08883161` → rounds to 0.089\n- `correlation_softjaccard_vs_f1_full.p_value = 0.01970` → rounds to 0.020\n- n = 689 (after gold-empty filtering)\n\n### Tracing the 0.062\n\nThe value ρ=0.062 appears ONLY in the **old deprecated paper** at:\n- `artifacts/_project/paper/experiments.tex:181` — \"SJ achieves ρ=0.062 (p=0.106, not statistically significant)\"\n\nThis file is in `artifacts/_project/paper/` which is excluded from compilation per constraint C001. The current compiled paper at `docs/paper/sections/` does NOT contain 0.062 for WNUT.\n\nSearching all output files for 0.062 in WNUT context yields **no matches**. The closest values found are:\n- exp003_wnut17_pilot: SJ full rho = 0.0825 (different seed)\n- exp003_wnut17_eval: SJ full rho = 0.0888\n- exp_009_v2 global SJ rho (SciERC RE, not WNUT): 0.0625\n\nThe value 0.062 for WNUT SJ is **untraceable** — it does not appear in any analysis output file. It may have originated from:\n1. An earlier experiment run that was overwritten\n2. A different seed/N configuration\n3. A manual transcription error in the old draft\n\n### Conclusion\n\n**Provenance yaml is stale.** The current paper correctly uses ρ=0.089 from exp003_wnut17_eval (N=16, T=1.0, gold-filtered n=689). The 0.062 value from the old paper draft is untraceable and no longer appears in the compiled paper.\n\n---\n\n## Summary\n\n| Claim | Provenance yaml | Current paper | Ground truth source | Status |\n|-------|----------------|---------------|-------------------|--------|\n| c032 LP cond RE ρ | 0.002 | **0.011** | exp_012_rerun_1024 (correct filter, n=238) | Provenance stale; paper correct |\n| c023 RE SJ Q1/Q4 | Q1=0.447/Q4=0.540 (registry) | **Q1=0.110/Q4=0.473** | exp_009_v2_re_rerun (gold-filtered) | Registry outdated; paper correct |\n| c021 WNUT SJ ρ | 0.062 | **0.089** | exp003_wnut17_eval (n=689) | Provenance stale; paper correct |\n\n**All three paper values are correct in the current compiled paper.** The discrepancies exist only between the provenance yaml / registry entries and the paper — not between the paper and the ground truth data. The provenance yaml and registry entries need updating.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/provenance_audit_c032_c023_c021.md",
    "content": "# Provenance Audit: c032 / c023 / c021\n\n**Date**: 2026-05-16\n**Auditor**: automated provenance trace\n**Scope**: Three claims in paper_provenance.yaml where registered values diverge from paper text\n\n---\n\n## c032: logprob conditional RE ρ\n\n- **Provenance yaml claim**: paper says ρ=0.002\n- **Registry value**: exp_015_metrics_expansion → re.logprob_rho_cond = 0.1457\n- **Current paper text**: ρ=0.011 (experiments.tex:50, appendix.tex:137)\n\n### Source trace\n\nThe **current paper** says ρ=0.011 in two places:\n1. `experiments.tex:50` — \"LP †RE collapses to ρ=0.011\"\n2. `appendix.tex:137` — heatmap caption: \"LP RE collapses to near-zero (ρ=0.011)\"\n\nThe value **0.01119** is in:\n- `output/exp_012_rerun_1024/report.json:100` — `re_logprob_baseline.conditional.rho = 0.011185364740047766`\n- `output/exp_012_rerun_1024/all_signals_5signal.json:403` — same value\n- Conditions: SciERC RE, N=8, T=1.0, max_tokens=1024, **correct conditional filter** (greedy_f1 > 0, n=238)\n\n### Why the discrepancy\n\n| Value | Source | Filter | n_cond | Status |\n|-------|--------|--------|--------|--------|\n| 0.002 | provenance yaml claim | unknown | — | **STALE** — paper was updated to 0.011; 0.002 untraceable in any output file |\n| 0.1457 | exp_015_metrics_expansion | WRONG: any sample F1 > 0 | 331 | Wrong filter inflates n, changes correlation |\n| **0.011** | exp_012_rerun_1024 | CORRECT: greedy_f1 > 0 | 238 | Current paper value |\n\nThe `conditional_filter_diagnosis.json` documents that exp_015 (and several other scripts) used the wrong conditional filter (\"any sample F1 > 0\" instead of \"greedy_f1 > 0\"), inflating the conditional set from n=238 to n=331 for RE. This is the root cause of the registry's 0.1457.\n\n### Conclusion\n\n**Provenance yaml is stale.** The paper was already corrected from 0.002 to 0.011. The current paper value (0.011 from exp_012_rerun_1024, correct conditional filter) is correct. The registry value (0.1457) uses a known-wrong conditional filter and should be annotated as deprecated.\n\n---\n\n## c023: RE SJ ρ by sentence length (Q1/Q4)\n\n- **Paper values**: Q1=0.110, Q4=0.473, Fisher z p=0.004\n- **Registry values**: exp_009_capability_stratification → Q1=0.447, Q4=0.540\n\n### Source trace\n\nPaper values match **exp_009_v2_re_rerun** exactly:\n\nFrom `output/exp_009_v2_re_rerun/summary.txt`:\n```\nStratification by Sentence Length QUARTILES (primary, independent)\n  Q1 (low)   n=117  SJ 0.110[-0.08,0.29]\n  Q2         n=93   SJ 0.308[0.09,0.50]\n  Q3         n=92   SJ 0.372[0.18,0.54]\n  Q4 (high)  n=95   SJ 0.473[0.28,0.62]\n\nFisher z-test low_vs_high:\n  sj   z=-2.878  p=0.004*\n```\n\nAll three paper values (Q1=0.110, Q4=0.473, p=0.004) match the v2 rerun output character-for-character.\n\nFrom `output/exp_009_v2_re_rerun/results.json`:\n- `by_sent_len_quartiles.\"Q1 (low)\".signals.sj.rho = 0.10961735` → rounds to 0.110\n- `by_sent_len_quartiles.\"Q4 (high)\".signals.sj.rho = 0.47332...` → rounds to 0.473\n- Fisher z low_vs_high sj p = 0.00435... → rounds to 0.004\n\n### Why the registry differs\n\nThe registry values (Q1=0.447, Q4=0.540) come from the **original exp_009_capability_stratification**, which:\n1. Did NOT apply gold-empty filtering (included 154 instances with empty gold RE annotations)\n2. Used all 551 raw instances instead of the filtered 397\n\nThe v2 rerun applied proper gold-filtering (551 → 397 after removing gold-empty), which is the mandated pipeline for all ρ values in the paper.\n\n| Value set | Source | Gold filter | n_RE | Status |\n|-----------|--------|-------------|------|--------|\n| Q1=0.447, Q4=0.540 | exp_009 original | No | 551 | **Outdated** — pre-gold-filter |\n| **Q1=0.110, Q4=0.473** | exp_009_v2_re_rerun | Yes | 397 | Current paper value |\n\n### Conclusion\n\n**Paper values are correct.** They come from exp_009_v2_re_rerun with proper gold-filtering. The registry entry for exp_009_capability_stratification is outdated and should be annotated as superseded by exp_009_v2_re_rerun.\n\n---\n\n## c021: WNUT SJ ρ\n\n- **Provenance yaml claim**: paper says ρ=0.062 (p=0.106)\n- **Registry values**: exp_003_ner_wnut17 → 0.082; exp_003_wnut17_eval → 0.089\n\n### Source trace — current paper\n\nThe **current paper** (appendix.tex:222, Table tab:wnut) shows:\n```\nSJ  .089  .020  .517  .288  <1e-7\n```\ni.e., SJ full-set ρ = **0.089**, p = 0.020\n\nThis matches `output/exp003_wnut17_eval/report.json`:\n- `correlation_softjaccard_vs_f1_full.rho = 0.08883161` → rounds to 0.089\n- `correlation_softjaccard_vs_f1_full.p_value = 0.01970` → rounds to 0.020\n- n = 689 (after gold-empty filtering)\n\n### Tracing the 0.062\n\nThe value ρ=0.062 appears ONLY in the **old deprecated paper** at:\n- `artifacts/_project/paper/experiments.tex:181` — \"SJ achieves ρ=0.062 (p=0.106, not statistically significant)\"\n\nThis file is in `artifacts/_project/paper/` which is excluded from compilation per constraint C001. The current compiled paper at `docs/paper/sections/` does NOT contain 0.062 for WNUT.\n\nSearching all output files for 0.062 in WNUT context yields **no matches**. The closest values found are:\n- exp003_wnut17_pilot: SJ full rho = 0.0825 (different seed)\n- exp003_wnut17_eval: SJ full rho = 0.0888\n- exp_009_v2 global SJ rho (SciERC RE, not WNUT): 0.0625\n\nThe value 0.062 for WNUT SJ is **untraceable** — it does not appear in any analysis output file. It may have originated from:\n1. An earlier experiment run that was overwritten\n2. A different seed/N configuration\n3. A manual transcription error in the old draft\n\n### Conclusion\n\n**Provenance yaml is stale.** The current paper correctly uses ρ=0.089 from exp003_wnut17_eval (N=16, T=1.0, gold-filtered n=689). The 0.062 value from the old paper draft is untraceable and no longer appears in the compiled paper.\n\n---\n\n## Summary\n\n| Claim | Provenance yaml | Current paper | Ground truth source | Status |\n|-------|----------------|---------------|-------------------|--------|\n| c032 LP cond RE ρ | 0.002 | **0.011** | exp_012_rerun_1024 (correct filter, n=238) | Provenance stale; paper correct |\n| c023 RE SJ Q1/Q4 | Q1=0.447/Q4=0.540 (registry) | **Q1=0.110/Q4=0.473** | exp_009_v2_re_rerun (gold-filtered) | Registry outdated; paper correct |\n| c021 WNUT SJ ρ | 0.062 | **0.089** | exp003_wnut17_eval (n=689) | Provenance stale; paper correct |\n\n**All three paper values are correct in the current compiled paper.** The discrepancies exist only between the provenance yaml / registry entries and the paper — not between the paper and the ground truth data. The provenance yaml and registry entries need updating.\n"
  }
}
````

</details>

---

### Tool result

_source line 136 · 2026-05-16T04:57:39.031038+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/provenance_audit_c032_c023_c021.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 137 · 2026-05-16T04:57:39.031233+00:00_

审计完成。报告已写入 `artifacts/provenance_audit_c032_c023_c021.md`。

**结论：三个不一致项全部是 provenance yaml / registry 过时，当前论文值均正确。**

| 项 | Provenance/Registry 值 | 当前论文值 | 真实来源 | 状态 |
|---|---|---|---|---|
| c032 LP cond RE ρ | 0.002 / 0.1457 | **0.011** | exp_012_rerun_1024 (正确 filter, n=238) | 论文已修正 |
| c023 RE SJ Q1/Q4 | Q1=0.447, Q4=0.540 | **Q1=0.110, Q4=0.473** | exp_009_v2_re_rerun (gold-filtered) | 论文正确，registry 未更新 |
| c021 WNUT SJ ρ | 0.062 | **0.089** | exp003_wnut17_eval (n=689) | 论文已修正，0.062 无法追溯 |

关键发现：
- **c032**：registry 的 0.1457 来自 exp_015_metrics_expansion 使用了错误的 conditional filter（any sample F1>0 而非 greedy_f1>0），当前论文的 0.011 使用正确 filter
- **c023**：registry 来自原始 exp_009（未做 gold-filtering），论文使用了 v2 rerun（gold-filtered 后 n=397）
- **c021**：0.062 仅存在于 artifacts/_project/paper/ 旧版本中，在所有实验输出中无法追溯

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_provenance_audit_c032_c023_c021_20260516T045025"
}
```

</details>

---
