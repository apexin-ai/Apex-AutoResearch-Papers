# analysis paper f1 audit table

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_analysis_paper_f1_audit_table_20260518T215058.jsonl`
- **Structured JSON:** [`85c5f5493b740870b880.json`](../../sessions/85/85c5f5493b740870b880.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-18T21:53:23.961695+00:00_

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
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
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

_source line 2 · 2026-05-18T21:53:23.961991+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T21:53:23.962206+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/unified_oracle_audit/oracle_f1_recalc_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/unified_oracle_audit/oracle_f1_recalc_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T21:53:23.962350+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/unified_degeneracy_audit/degeneracy_recalc_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/unified_degeneracy_audit/degeneracy_recalc_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-18T21:53:23.962714+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"exp_dir\\\": \\\"exp_001_seed123_v2\\\",\\n    \\\"n_instances\\\": 529,\\n    \\\"greedy_f1_unified\\\": 0.6442,\\n    \\\"oracle_f1_unified\\\": 0.8172,\\n    \\\"oracle_f1_old\\\": 0.8128,\\n    \\\"delta\\\": \\\"+0.44pp\\\"\\n  },\\n  {\\n    \\\"exp_dir\\\": \\\"exp_001_seed42_v2\\\",\\n    \\\"n_instances\\\": 529,\\n    \\\"greedy_f1_unified\\\": 0.6442,\\n    \\\"oracle_f1_unified\\\": 0.8194,\\n    \\\"oracle_f1_old\\\": 0.815,\\n    \\\"delta\\\": \\\"+0.44pp\\\"\\n  },\\n  {\\n    \\\"exp_dir\\\": \\\"exp_001_seed42_v2_r1024\\\",\\n    \\\"n_instances\\\": 529,\\n    \\\"greedy_f1_unified\\\": 0.6417,\\n    \\\"oracle_f1_unified\\\": 0.8134,\\n    \\\"oracle_f1_old\\\": 0.8167,\\n    \\\"delta\\\": \\\"-0.33pp\\\"\\n  },\\n  {\\n    \\\"exp_dir\\\": \\\"exp_001_seed456_v2\\\",\\n    \\\"n_instances\\\": 529,\\n    \\\"greedy_f1_unified\\\": 0.6439,\\n    \\\"oracle_f1_unified\\\": 0.8229,\\n    \\\"oracle_f1_old\\\": 0.8172,\\n    \\\"delta\\\": \\\"+0.58pp\\\"\\n  },\\n  {\\n    \\\"exp_dir\\\": \\\"exp_001_seed456_v2_ner\\\",\\n    \\\"n_instances\\\": 529,\\n    \\\"greedy_f1_unified\\\": 0.6486,\\n    \\\"oracle_f1_unified\\\": 0.8148,\\n    \\\"oracle_f1_old\\\": 0.8112,\\n    \\\"delta\\\": \\\"+0.37pp\\\"\\n  },\\n  {\\n    \\\"exp_dir\\\": \\\"exp_002_conll_n16\\\",\\n    \\\"n_instances\\\": 2756,\\n    \\\"greedy_f1_unified\\\": 0.907,\\n    \\\"oracle_f1_unified\\\": 0.9581,\\n    \\\"oracle_f1_old\\\": 0.9566,\\n    \\\"delta\\\": \\\"+0.14pp\\\"\\n  },\\n  {\\n    \\\"exp_dir\\\": \\\"exp_002_conll_n16_r1024\\\",\\n    \\\"n_instances\\\": 2756,\\n    \\\"greedy_f1_unified\\\": 0.907,\\n    \\\"oracle_f1_unified\\\": 0.9571,\\n    \\\"oracle_f1_old\\\": 0.9544,\\n    \\\"delta\\\": \\\"+0.27pp\\\"\\n  },\\n  {\\n    \\\"exp_dir\\\": \\\"exp_002_conll_n16_seed123\\\",\\n    \\\"n_instances\\\": 2756,\\n    \\\"greedy_f1_unified\\\": 0.9065,\\n    \\\"oracle_f1_unified\\
…[truncated 8864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T21:53:23.963096+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"label\\\": \\\"Qwen3-8B / SciERC / T=1.0 / seed=42\\\",\\n    \\\"dir\\\": \\\"exp_012_rerun_1024\\\",\\n    \\\"dataset\\\": \\\"scierc\\\",\\n    \\\"model\\\": \\\"Qwen3-8B\\\",\\n    \\\"T\\\": 1.0,\\n    \\\"seed\\\": 42,\\n    \\\"status\\\": \\\"OK\\\",\\n    \\\"n_instances\\\": 529,\\n    \\\"n_degenerate\\\": 94,\\n    \\\"degen_pct_unified\\\": 17.77,\\n    \\\"greedy_f1\\\": 64.39,\\n    \\\"old_sample_f1_pct_zero\\\": 12.59,\\n    \\\"delta\\\": 5.17\\n  },\\n  {\\n    \\\"label\\\": \\\"Qwen3-8B / SciERC / T=1.0 / seed=123\\\",\\n    \\\"dir\\\": \\\"exp_018_qwen_scierc_seed123\\\",\\n    \\\"dataset\\\": \\\"scierc\\\",\\n    \\\"model\\\": \\\"Qwen3-8B\\\",\\n    \\\"T\\\": 1.0,\\n    \\\"seed\\\": 123,\\n    \\\"status\\\": \\\"OK\\\",\\n    \\\"n_instances\\\": 529,\\n    \\\"n_degenerate\\\": 91,\\n    \\\"degen_pct_unified\\\": 17.2,\\n    \\\"greedy_f1\\\": 64.57,\\n    \\\"old_sample_f1_pct_zero\\\": 11.67,\\n    \\\"delta\\\": 5.53\\n  },\\n  {\\n    \\\"label\\\": \\\"Qwen3-8B / SciERC / T=1.0 / seed=456\\\",\\n    \\\"dir\\\": \\\"exp_018_qwen_scierc_seed456\\\",\\n    \\\"dataset\\\": \\\"scierc\\\",\\n    \\\"model\\\": \\\"Qwen3-8B\\\",\\n    \\\"T\\\": 1.0,\\n    \\\"seed\\\": 456,\\n    \\\"status\\\": \\\"OK\\\",\\n    \\\"n_instances\\\": 529,\\n    \\\"n_degenerate\\\": 108,\\n    \\\"degen_pct_unified\\\": 20.42,\\n    \\\"greedy_f1\\\": 64.78,\\n    \\\"old_sample_f1_pct_zero\\\": 13.26,\\n    \\\"delta\\\": 7.16\\n  },\\n  {\\n    \\\"label\\\": \\\"Qwen3-8B / CoNLL / T=1.0 N=16 / seed=42\\\",\\n    \\\"dir\\\": \\\"exp_002_conll_n16\\\",\\n    \\\"dataset\\\": \\\"conll2003\\\",\\n    \\\"model\\\": \\\"Qwen3-8B\\\",\\n    \\\"T\\\": 1.0,\\n    \\\"seed\\\": 42,\\n    \\\"N\\\": 16,\\n    \\\"status\\\": \\\"OK\\\",\\n    \\\"n_instances\\\": 2756,\\n    \\\"n_degenerate\\\": 1335,\\n    \\\"degen_pct_unified\\\": 48.44,\\n    \\\"greedy_f1\\\": 90.7,\\n   
…[truncated 8424 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T21:53:23.963332+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/struct_self_consist_ie/output/unified_oracle_audit/oracle_f1_recalc_results.json')); print(len(d)); [print(r['exp_dir']) for r in d]\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/struct_self_consist_ie/output/unified_oracle_audit/oracle_f1_recalc_results.json')); print(len(d)); [print(r['exp_dir']) for r in d]\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T21:53:23.963470+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T21:53:23.963595+00:00_

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
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
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

_source line 10 · 2026-05-18T21:53:23.963796+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"adalp_analysis_results.json\\nadaptive_temperature_results.json\\nanalysis_epsilon_sweep\\nanalysis_fk_bootstrap_ci.json\\nanalysis_fk_bootstrap_per_instance.json\\nanalysis_lp_range_cdf.json\\nanalysis_lp_range_cdf_n16_3seed.json\\nanalysis_mbr_selection.json\\nanalysis_multiseed_selection_f1.json\\nanalysis_round8\\nanalysis_scierc_n16_3seed_selection_f1.json\\nanalysis_scierc_n16_3seed_selection_f1_merged.json\\nanalysis_scierc_re_n16_3seed_selection_f1.json\\nanalysis_unified_rho_full.json\\nbootstrap_ci_nscaling\\nbootstrap_ci_summary.json\\nbootstrap_ci_tables.tex\\ncalibration_baseline_results.json\\nccs_selection_report.md\\nccs_selection_results.json\\nconditional_filter_diagnosis.json\\nd108_greedy_f1\\nd108_lp_vc_combination\\nd108_mbr_within_rho\\nd108_q4q5\\nd110_4b_degeneracy\\nd112_disk_cleanup\\nd112_hybrid_strategy\\nd112_mf3_random_single\\nd112_table2_fix\\nd114_auroc_investigation\\nd140_oracle_gated\\nd141_conditional_decomp\\nd141_degeneracy_scatter\\nd141_entity_merge\\ndals_analysis.json\\ndals_cross_model.json\\ndals_hardening_results.json\\ndeberta_verifier\\ndeberta_verifier_5fold\\ndgs_epoch_rank_analysis.json\\ndgs_selection_results.json\\ndiagnostic_calibration\\ndiagnostic_calibration_results.json\\nentity_consensus_report.md\\nentity_consensus_results.json\\nentity_token_lp_full\\nepoch_scierc_textbased_rho.json\\nexp001_n16_seed123\\nexp001_n16_seed123_200only\\nexp001_n16_seed123_200only_backup\\nexp001_n16_seed123_full\\nexp001_n16_seed123_run.log\\nexp001_n16_seed42\\nexp001_n16_seed42_200only_backup\\nexp001_n16_seed42_run.log\\nexp001_n16_seed456\\nexp001_n16_seed456_200only\\nexp001_n16_seed456_run.log\\nexp001_seed123_t10_full\\nexp001_seed123_t10_full.log\\nexp001_seed456_t10_full\\nexp001_seed456_t10_full.log\\nexp002_conll2003\\nexp003_wnut17_dryrun\\nexp003_wnut17_eval\\nexp003_wnut17_eval.log\\nexp003_wnut17_pilot\\nexp003_wnut17_pilot.log\\nexp004_re_diagnostic\\nex
…[truncated 5444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T21:53:23.964001+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "account": "root",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && python3 << 'PYEOF'\nimport json, os, glob\n\n# Load oracle audit data\nwith open('output/unified_oracle_audit/oracle_f1_recalc_results.json') as f:\n    oracle_audit = json.load(f)\n\n# Load degeneracy audit data\nwith open('output/unified_degeneracy_audit/degeneracy_recalc_results.json') as f:\n    degen_audit = json.load(f)\n\n# Build maps\noracle_map = {r['exp_dir']: r for r in oracle_audit}\ndegen_map = {r['dir']: r for r in degen_audit}\n\nprint(f\"Oracle audit: {len(oracle_audit)} experiments\")\nprint(f\"Degeneracy audit: {len(degen_audit)} experiments\")\nprint(f\"Oracle exp_dirs: {sorted(oracle_map.keys())}\")\n\n# Paper locations to verify\npaper_locations = [\n    {\"paper_location\": \"4B SciERC greedy/oracle/headroom\", \"exp_dirs\": [\"exp_qwen3_4b_scierc_scs_inference\"], \"model\": \"Qwen3-4B\"},\n    {\"paper_location\": \"4B CoNLL greedy/oracle/headroom\", \"exp_dirs\": [\"exp_qwen3_4b_conll_scs_inference\", \"exp_qwen3_4b_conll_scs_inference_v2\"], \"model\": \"Qwen3-4B\"},\n    {\"paper_location\": \"rank=8 SciERC greedy/oracle/headroom\", \"exp_dirs\": [\"exp_023_rank8_inference\", \"exp_023_lora_rank8\"], \"model\": \"Qwen3-8B rank=8\"},\n    {\"paper_location\": \"N=32 SciERC greedy/oracle\", \"exp_dirs\": [\"exp_025_n32\"], \"model\": \"Qwen3-8B N=32\"},\n    {\"paper_location\": \"N=16 SciERC greedy/oracle (seed42)\", \"exp_dirs\": [\"exp_001_seed42_v2\", \"exp_012_rerun_1024\"], \"model\": \"Qwen3-8B N=16\"},\n    {\"paper_location\": \"FewNERD N=8 seed42 greedy/oracle/headroom\", \"exp_dirs\": [\"exp_021_inference\", \"exp_021_fewnerd_full\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"FewNERD N=16 greedy/oracle\", \"exp_dirs\": [\"exp_027_fewnerd_n16\"], \"model\": \"Qwen3-8B N=16\"},\n    {\"paper_location\": \"LLaMA SciERC greedy/oracle seed42\", \"exp_dirs\": [\"exp_018_llama_scierc_seed42_r1024\", \"exp_007_llama_n16\", \"exp_007_llama_n16_r1024\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA SciERC greedy/oracle seed123\", \"exp_dirs\": [\"exp_018_llama_scierc_seed123\", \"exp_007_llama_scierc_seed123\", \"exp_007_llama_seed123\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA SciERC greedy/oracle seed456\", \"exp_dirs\": [\"exp_018_llama_scierc_seed456_r1024\", \"exp_007_llama_seed456\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA CoNLL greedy/oracle seed42\", \"exp_dirs\": [\"exp_017_llama_conll_n16_r1024\", \"exp_017_llama_conll_n16\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA CoNLL greedy/oracle seed123\", \"exp_dirs\": [\"exp_017_llama_conll_n16_s123_r1024\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA CoNLL greedy/oracle seed456\", \"exp_dirs\": [\"exp_017_llama_conll_n16_s456_r1024\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"CoNLL Qwen greedy/oracle/headroom seed42\", \"exp_dirs\": [\"exp_002_conll_n16\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"CoNLL Qwen greedy/oracle seed123\", \"exp_dirs\": [\"exp_002_conll_n16_seed123\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"CoNLL Qwen greedy/oracle seed456\", \"exp_dirs\": [\"exp_002_conll_n16_seed456\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"3-epoch SciERC greedy/oracle/headroom\", \"exp_dirs\": [\"exp_029a_scierc_3epoch\", \"exp_029a_inference\"], \"model\": \"Qwen3-8B 3ep\"},\n    {\"paper_location\": \"10-epoch SciERC greedy/oracle/headroom\", \"exp_dirs\": [\"exp_029b_scierc_10epoch\", \"exp_029b_inference\"], \"model\": \"Qwen3-8B 10ep\"},\n    {\"paper_location\": \"T=0.5 SciERC greedy/oracle\", \"exp_dirs\": [\"exp_026_t05\"], \"model\": \"Qwen3-8B T=0.5\"},\n    {\"paper_location\": \"T=0.8 SciERC greedy/oracle\", \"exp_dirs\": [\"exp_026_t08\"], \"model\": \"Qwen3-8B T=0.8\"},\n    {\"paper_location\": \"T=1.2 SciERC greedy/oracle\", \"exp_dirs\": [\"exp_026_t12\"], \"model\": \"Qwen3-8B T=1.2\"},\n    {\"paper_location\": \"SciERC canonical greedy/oracle seed42\", \"exp_dirs\": [\"exp_012_rerun_1024\"], \"model\": \"Qwen3-8B canonical\"},\n    {\"paper_location\": \"SciERC seed123\", \"exp_dirs\": [\"exp_001_seed123_v2\", \"exp_018_qwen_scierc_seed123\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"SciERC seed456\", \"exp_dirs\": [\"exp_001_seed456_v2\", \"exp_018_qwen_scierc_seed456\"], \"model\": \"Qwen3-8B\"},\n]\n\nresults = []\nfor loc in paper_locations:\n    found = False\n    for exp_dir in loc['exp_dirs']:\n        if exp_dir in oracle_map:\n            r = oracle_map[exp_dir]\n            greedy = r.get('greedy_f1_unified', r.get('greedy_f1'))\n            oracle = r.get('oracle_f1_unified', r.get('oracle_f1'))\n            headroom = round((oracle - greedy) * 100, 2) if greedy is not None and oracle is not None else None\n            \n            # Get degeneracy info if available\n            degen_info = degen_map.get(exp_dir, {})\n            degen_pct = degen_info.get('degen_pct_unified')\n            \n            results.append({\n                'paper_location': loc['paper_location'],\n                'model': loc['model'],\n                'experiment_id': exp_dir,\n                'n_instances': r.get('n_instances'),\n                'greedy_f1': round(greedy, 4) if greedy is not None else None,\n                'oracle_f1': round(oracle, 4) if oracle is not None else None,\n                'headroom_pp': headroom,\n                'old_oracle': r.get('oracle_f1_old'),\n                'delta_pp': r.get('delta'),\n                'degen_pct': degen_pct,\n                'status': 'verified'\n            })\n            found = True\n            break\n    if not found:\n        results.append({\n            'paper_location': loc['paper_location'],\n            'model': loc['model'],\n            'experiment_id': None,\n            'status': 'missing',\n            'tried_dirs': loc['exp_dirs']\n        })\n\n# Save\nos.makedirs('output/paper_f1_audit', exist_ok=True)\nwith open('output/paper_f1_audit/paper_f1_audit_table.json', 'w') as f:\n    json.dump(results, f, indent=2)\n\n# Print table\nprint(f\"\\n{'Paper Location':<50} {'Model':<22} {'Greedy':>8} {'Oracle':>8} {'Head':>7} {'Degen%':>7} {'OldOrc':>8} {'Delta':>8} {'Status':<8}\")\nprint('=' * 130)\nfor r in results:\n    if r['status'] == 'verified':\n        degen_str = f\"{r['degen_pct']:.1f}\" if r.get('degen_pct') is not None else \"N/A\"\n        old_orc = f\"{r['old_oracle']:.4f}\" if r.get('old_oracle') is not None else \"N/A\"\n        print(f\"{r['paper_location']:<50} {r['model']:<22} {r['greedy_f1']:>8.4f} {r['oracle_f1']:>8.4f} {r['headroom_pp']:>6.2f}pp {degen_str:>7} {old_orc:>8} {r['delta_pp']:>8} OK\")\n    else:\n        print(f\"{r['paper_location']:<50} {r['model']:<22} {'---':>8} {'---':>8} {'---':>7} {'---':>7} {'---':>8} {'---':>8} MISSING\")\n\nverified = sum(1 for r in results if r['status']=='verified')\nmissing = sum(1 for r in results if r['status']=='missing')\nprint(f\"\\nTotal: {len(results)} locations, {verified} verified, {missing} missing\")\n\n# List missing details\nif missing > 0:\n    print(\"\\n--- Missing experiments ---\")\n    for r in results:\n        if r['status'] == 'missing':\n            print(f\"  {r['paper_location']}: tried {r['tried_dirs']}\")\n            # Try fuzzy match\n            for tried in r['tried_dirs']:\n                matches = glob.glob(f'output/*{tried}*')\n                if matches:\n                    print(f\"    -> Potential matches: {matches}\")\nPYEOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "account": "root",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && python3 << 'PYEOF'\nimport json, os, glob\n\n# Load oracle audit data\nwith open('output/unified_oracle_audit/oracle_f1_recalc_results.json') as f:\n    oracle_audit = json.load(f)\n\n# Load degeneracy audit data\nwith open('output/unified_degeneracy_audit/degeneracy_recalc_results.json') as f:\n    degen_audit = json.load(f)\n\n# Build maps\noracle_map = {r['exp_dir']: r for r in oracle_audit}\ndegen_map = {r['dir']: r for r in degen_audit}\n\nprint(f\"Oracle audit: {len(oracle_audit)} experiments\")\nprint(f\"Degeneracy audit: {len(degen_audit)} experiments\")\nprint(f\"Oracle exp_dirs: {sorted(oracle_map.keys())}\")\n\n# Paper locations to verify\npaper_locations = [\n    {\"paper_location\": \"4B SciERC greedy/oracle/headroom\", \"exp_dirs\": [\"exp_qwen3_4b_scierc_scs_inference\"], \"model\": \"Qwen3-4B\"},\n    {\"paper_location\": \"4B CoNLL greedy/oracle/headroom\", \"exp_dirs\": [\"exp_qwen3_4b_conll_scs_inference\", \"exp_qwen3_4b_conll_scs_inference_v2\"], \"model\": \"Qwen3-4B\"},\n    {\"paper_location\": \"rank=8 SciERC greedy/oracle/headroom\", \"exp_dirs\": [\"exp_023_rank8_inference\", \"exp_023_lora_rank8\"], \"model\": \"Qwen3-8B rank=8\"},\n    {\"paper_location\": \"N=32 SciERC greedy/oracle\", \"exp_dirs\": [\"exp_025_n32\"], \"model\": \"Qwen3-8B N=32\"},\n    {\"paper_location\": \"N=16 SciERC greedy/oracle (seed42)\", \"exp_dirs\": [\"exp_001_seed42_v2\", \"exp_012_rerun_1024\"], \"model\": \"Qwen3-8B N=16\"},\n    {\"paper_location\": \"FewNERD N=8 seed42 greedy/oracle/headroom\", \"exp_dirs\": [\"exp_021_inference\", \"exp_021_fewnerd_full\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"FewNERD N=16 greedy/oracle\", \"exp_dirs\": [\"exp_027_fewnerd_n16\"], \"model\": \"Qwen3-8B N=16\"},\n    {\"paper_location\": \"LLaMA SciERC greedy/oracle seed42\", \"exp_dirs\": [\"exp_018_llama_scierc_seed42_r1024\", \"exp_007_llama_n16\", \"exp_007_llama_n16_r1024\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA SciERC greedy/oracle seed123\", \"exp_dirs\": [\"exp_018_llama_scierc_seed123\", \"exp_007_llama_scierc_seed123\", \"exp_007_llama_seed123\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA SciERC greedy/oracle seed456\", \"exp_dirs\": [\"exp_018_llama_scierc_seed456_r1024\", \"exp_007_llama_seed456\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA CoNLL greedy/oracle seed42\", \"exp_dirs\": [\"exp_017_llama_conll_n16_r1024\", \"exp_017_llama_conll_n16\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA CoNLL greedy/oracle seed123\", \"exp_dirs\": [\"exp_017_llama_conll_n16_s123_r1024\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA CoNLL greedy/oracle seed456\", \"exp_dirs\": [\"exp_017_llama_conll_n16_s456_r1024\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"CoNLL Qwen greedy/oracle/headroom seed42\", \"exp_dirs\": [\"exp_002_conll_n16\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"CoNLL Qwen greedy/oracle seed123\", \"exp_dirs\": [\"exp_002_conll_n16_seed123\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"CoNLL Qwen greedy/oracle seed456\", \"exp_dirs\": [\"exp_002_conll_n16_seed456\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"3-epoch SciERC greedy/oracle/headroom\", \"exp_dirs\": [\"exp_029a_scierc_3epoch\", \"exp_029a_inference\"], \"model\": \"Qwen3-8B 3ep\"},\n    {\"paper_location\": \"10-epoch SciERC greedy/oracle/headroom\", \"exp_dirs\": [\"exp_029b_scierc_10epoch\", \"exp_029b_inference\"], \"model\": \"Qwen3-8B 10ep\"},\n    {\"paper_location\": \"T=0.5 SciERC greedy/oracle\", \"exp_dirs\": [\"exp_026_t05\"], \"model\": \"Qwen3-8B T=0.5\"},\n    {\"paper_location\": \"T=0.8 SciERC greedy/oracle\", \"exp_dirs\": [\"exp_026_t08\"], \"model\": \"Qwen3-8B T=0.8\"},\n    {\"paper_location\": \"T=1.2 SciERC greedy/oracle\", \"exp_dirs\": [\"exp_026_t12\"], \"model\": \"Qwen3-8B T=1.2\"},\n    {\"paper_location\": \"SciERC canonical greedy/oracle seed42\", \"exp_dirs\": [\"exp_012_rerun_1024\"], \"model\": \"Qwen3-8B canonical\"},\n    {\"paper_location\": \"SciERC seed123\", \"exp_dirs\": [\"exp_001_seed123_v2\", \"exp_018_qwen_scierc_seed123\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"SciERC seed456\", \"exp_dirs\": [\"exp_001_seed456_v2\", \"exp_018_qwen_scierc_seed456\"], \"model\": \"Qwen3-8B\"},\n]\n\nresults = []\nfor loc in paper_locations:\n    found = False\n    for exp_dir in loc['exp_dirs']:\n        if exp_dir in oracle_map:\n            r = oracle_map[exp_dir]\n            greedy = r.get('greedy_f1_unified', r.get('greedy_f1'))\n            oracle = r.get('oracle_f1_unified', r.get('oracle_f1'))\n            headroom = round((oracle - greedy) * 100, 2) if greedy is not None and oracle is not None else None\n            \n            # Get degeneracy info if available\n            degen_info = degen_map.get(exp_dir, {})\n            degen_pct = degen_info.get('degen_pct_unified')\n            \n            results.append({\n                'paper_location': loc['paper_location'],\n                'model': loc['model'],\n                'experiment_id': exp_dir,\n                'n_instances': r.get('n_instances'),\n                'greedy_f1': round(greedy, 4) if greedy is not None else None,\n                'oracle_f1': round(oracle, 4) if oracle is not None else None,\n                'headroom_pp': headroom,\n                'old_oracle': r.get('oracle_f1_old'),\n                'delta_pp': r.get('delta'),\n                'degen_pct': degen_pct,\n                'status': 'verified'\n            })\n            found = True\n            break\n    if not found:\n        results.append({\n            'paper_location': loc['paper_location'],\n            'model': loc['model'],\n            'experiment_id': None,\n            'status': 'missing',\n            'tried_dirs': loc['exp_dirs']\n        })\n\n# Save\nos.makedirs('output/paper_f1_audit', exist_ok=True)\nwith open('output/paper_f1_audit/paper_f1_audit_table.json', 'w') as f:\n    json.dump(results, f, indent=2)\n\n# Print table\nprint(f\"\\n{'Paper Location':<50} {'Model':<22} {'Greedy':>8} {'Oracle':>8} {'Head':>7} {'Degen%':>7} {'OldOrc':>8} {'Delta':>8} {'Status':<8}\")\nprint('=' * 130)\nfor r in results:\n    if r['status'] == 'verified':\n        degen_str = f\"{r['degen_pct']:.1f}\" if r.get('degen_pct') is not None else \"N/A\"\n        old_orc = f\"{r['old_oracle']:.4f}\" if r.get('old_oracle') is not None else \"N/A\"\n        print(f\"{r['paper_location']:<50} {r['model']:<22} {r['greedy_f1']:>8.4f} {r['oracle_f1']:>8.4f} {r['headroom_pp']:>6.2f}pp {degen_str:>7} {old_orc:>8} {r['delta_pp']:>8} OK\")\n    else:\n        print(f\"{r['paper_location']:<50} {r['model']:<22} {'---':>8} {'---':>8} {'---':>7} {'---':>7} {'---':>8} {'---':>8} MISSING\")\n\nverified = sum(1 for r in results if r['status']=='verified')\nmissing = sum(1 for r in results if r['status']=='missing')\nprint(f\"\\nTotal: {len(results)} locations, {verified} verified, {missing} missing\")\n\n# List missing details\nif missing > 0:\n    print(\"\\n--- Missing experiments ---\")\n    for r in results:\n        if r['status'] == 'missing':\n            print(f\"  {r['paper_location']}: tried {r['tried_dirs']}\")\n            # Try fuzzy match\n            for tried in r['tried_dirs']:\n                matches = glob.glob(f'output/*{tried}*')\n                if matches:\n                    print(f\"    -> Potential matches: {matches}\")\nPYEOF"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T21:53:23.964352+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/autodl-tmp/struct_self_consist_ie && python3 << \\\\'PYEOF\\\\'\\\\nimport json, os, glob\\\\n\\\\n# Load oracle audit data\\\\nwith open(\\\\'output/unified_oracle_audit/oracle_f1_recalc_results.json\\\\') as f:\\\\n    oracle_audit = json.load(f)\\\\n\\\\n# Load degeneracy audit data\\\\nwith open(\\\\'output/unified_degeneracy_audit/degeneracy_recalc_results.json\\\\') as f:\\\\n    degen_audit = json.load(f)\\\\n\\\\n# Build maps\\\\noracle_map = {r[\\\\'exp_dir\\\\']: r for r in oracle_audit}\\\\ndegen_map = {r[\\\\'dir\\\\']: r for r in degen_audit}\\\\n\\\\nprint(f\\\"Oracle audit: {len(oracle_audit)} experiments\\\")\\\\nprint(f\\\"Degeneracy audit: {len(degen_audit)} experiments\\\")\\\\nprint(f\\\"Oracle exp_dirs: {sorted(oracle_map.keys())}\\\")\\\\n\\\\n# Paper locations to verify\\\\npaper_locations = [\\\\n    {\\\"paper_location\\\": \\\"4B SciERC greedy/oracle/headroom\\\", \\\"exp_dirs\\\": [\\\"exp_qwen3_4b_scierc_scs_inference\\\"], \\\"model\\\": \\\"Qwen3-4B\\\"},\\\\n    {\\\"paper_location\\\": \\\"4B CoNLL greedy/oracle/headroom\\\", \\\"exp_dirs\\\": [\\\"exp_qwen3_4b_conll_scs_inference\\\", \\\"exp_qwen3_4b_conll_scs_inference_v2\\\"], \\\"model\\\": \\\"Qwen3-4B\\\"},\\\\n    {\\\"paper_location\\\": \\\"rank=8 SciERC greedy/oracle/headroom\\\", \\\"exp_dirs\\\": [\\\"exp_023_rank8_inference\\\", \\\"exp_023_lora_rank8\\\"], \\\"model\\\": \\\"Qwen3-8B rank=8\\\"},\\\\n    {\\\"paper_location\\\": \\\"N=32 SciERC greedy/oracle\\\", \\\"exp_dirs\\\": [\\\"exp_025_n32\\\"], \\\"model\\\": \\\"Qwen3-8B N=32\\\"},\\\\n    {\\\"paper_location\\\": \\\"N=16 SciERC greedy/oracle (seed42)\\\", \\\"exp_dirs\\\": [\\\"exp_001_seed42_v2\\\", \\\"exp_012_rerun_1024\\\"], \\\"model\\\": \\\"Qwen3-8B N=16\\\"},\\\\n    {\\\"paper_location\\\": \\\"FewNERD N=8 seed42 greedy/oracle/headroom\\\", \\\"exp_dirs\\\": [\\\"exp_021_inference\
…[truncated 7519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T21:53:23.964546+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /usr/bin/python*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /usr/bin/python*",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T21:53:23.964678+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/miniconda3/bin/python*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/miniconda3/bin/python*",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T21:53:23.964804+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/usr/bin/python*': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.92}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T21:53:23.964932+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n/root/miniconda3/bin/python3\\n/root/miniconda3/bin/python3-config\\n/root/miniconda3/bin/python3.1\\n/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T21:53:23.965119+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "account": "root",
  "command": "cat > /root/autodl-tmp/struct_self_consist_ie/output/paper_f1_audit_script.py << 'PYEOF'\nimport json, os, glob\n\nos.chdir('/root/autodl-tmp/struct_self_consist_ie')\n\nwith open('output/unified_oracle_audit/oracle_f1_recalc_results.json') as f:\n    oracle_audit = json.load(f)\n\nwith open('output/unified_degeneracy_audit/degeneracy_recalc_results.json') as f:\n    degen_audit = json.load(f)\n\noracle_map = {r['exp_dir']: r for r in oracle_audit}\ndegen_map = {r['dir']: r for r in degen_audit}\n\nprint(f\"Oracle audit: {len(oracle_audit)} experiments\")\nprint(f\"Degeneracy audit: {len(degen_audit)} experiments\")\n\npaper_locations = [\n    {\"paper_location\": \"4B SciERC greedy/oracle/headroom\", \"exp_dirs\": [\"exp_qwen3_4b_scierc_scs_inference\"], \"model\": \"Qwen3-4B\"},\n    {\"paper_location\": \"4B CoNLL greedy/oracle/headroom\", \"exp_dirs\": [\"exp_qwen3_4b_conll_scs_inference\", \"exp_qwen3_4b_conll_scs_inference_v2\"], \"model\": \"Qwen3-4B\"},\n    {\"paper_location\": \"rank=8 SciERC greedy/oracle/headroom\", \"exp_dirs\": [\"exp_023_rank8_inference\", \"exp_023_lora_rank8\"], \"model\": \"Qwen3-8B rank=8\"},\n    {\"paper_location\": \"N=32 SciERC greedy/oracle\", \"exp_dirs\": [\"exp_025_n32\"], \"model\": \"Qwen3-8B N=32\"},\n    {\"paper_location\": \"N=16 SciERC greedy/oracle (seed42)\", \"exp_dirs\": [\"exp_001_seed42_v2\", \"exp_012_rerun_1024\"], \"model\": \"Qwen3-8B N=16\"},\n    {\"paper_location\": \"FewNERD N=8 seed42 greedy/oracle\", \"exp_dirs\": [\"exp_021_inference\", \"exp_021_fewnerd_full\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"FewNERD N=16 greedy/oracle\", \"exp_dirs\": [\"exp_027_fewnerd_n16\"], \"model\": \"Qwen3-8B N=16\"},\n    {\"paper_location\": \"LLaMA SciERC seed42\", \"exp_dirs\": [\"exp_018_llama_scierc_seed42_r1024\", \"exp_007_llama_n16\", \"exp_007_llama_n16_r1024\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA SciERC seed123\", \"exp_dirs\": [\"exp_018_llama_scierc_seed123\", \"exp_007_llama_scierc_seed123\", \"exp_007_llama_seed123\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA SciERC seed456\", \"exp_dirs\": [\"exp_018_llama_scierc_seed456_r1024\", \"exp_007_llama_seed456\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA CoNLL seed42\", \"exp_dirs\": [\"exp_017_llama_conll_n16_r1024\", \"exp_017_llama_conll_n16\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA CoNLL seed123\", \"exp_dirs\": [\"exp_017_llama_conll_n16_s123_r1024\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA CoNLL seed456\", \"exp_dirs\": [\"exp_017_llama_conll_n16_s456_r1024\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"CoNLL Qwen seed42\", \"exp_dirs\": [\"exp_002_conll_n16\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"CoNLL Qwen seed123\", \"exp_dirs\": [\"exp_002_conll_n16_seed123\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"CoNLL Qwen seed456\", \"exp_dirs\": [\"exp_002_conll_n16_seed456\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"3-epoch SciERC\", \"exp_dirs\": [\"exp_029a_scierc_3epoch\", \"exp_029a_inference\"], \"model\": \"Qwen3-8B 3ep\"},\n    {\"paper_location\": \"10-epoch SciERC\", \"exp_dirs\": [\"exp_029b_scierc_10epoch\", \"exp_029b_inference\"], \"model\": \"Qwen3-8B 10ep\"},\n    {\"paper_location\": \"T=0.5 SciERC\", \"exp_dirs\": [\"exp_026_t05\"], \"model\": \"Qwen3-8B T=0.5\"},\n    {\"paper_location\": \"T=0.8 SciERC\", \"exp_dirs\": [\"exp_026_t08\"], \"model\": \"Qwen3-8B T=0.8\"},\n    {\"paper_location\": \"T=1.2 SciERC\", \"exp_dirs\": [\"exp_026_t12\"], \"model\": \"Qwen3-8B T=1.2\"},\n    {\"paper_location\": \"SciERC canonical seed42\", \"exp_dirs\": [\"exp_012_rerun_1024\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"SciERC seed123\", \"exp_dirs\": [\"exp_001_seed123_v2\", \"exp_018_qwen_scierc_seed123\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"SciERC seed456\", \"exp_dirs\": [\"exp_001_seed456_v2\", \"exp_018_qwen_scierc_seed456\"], \"model\": \"Qwen3-8B\"},\n]\n\nresults = []\nfor loc in paper_locations:\n    found = False\n    for exp_dir in loc['exp_dirs']:\n        if exp_dir in oracle_map:\n            r = oracle_map[exp_dir]\n            greedy = r.get('greedy_f1_unified', r.get('greedy_f1'))\n            oracle_val = r.get('oracle_f1_unified', r.get('oracle_f1'))\n            headroom = round((oracle_val - greedy) * 100, 2) if greedy is not None and oracle_val is not None else None\n            degen_info = degen_map.get(exp_dir, {})\n            degen_pct = degen_info.get('degen_pct_unified')\n            results.append({\n                'paper_location': loc['paper_location'],\n                'model': loc['model'],\n                'experiment_id': exp_dir,\n                'n_instances': r.get('n_instances'),\n                'greedy_f1': round(greedy, 4) if greedy is not None else None,\n                'oracle_f1': round(oracle_val, 4) if oracle_val is not None else None,\n                'headroom_pp': headroom,\n                'old_oracle': r.get('oracle_f1_old'),\n                'delta_pp': r.get('delta'),\n                'degen_pct': degen_pct,\n                'status': 'verified'\n            })\n            found = True\n            break\n    if not found:\n        results.append({\n            'paper_location': loc['paper_location'],\n            'model': loc['model'],\n            'experiment_id': None,\n            'status': 'missing',\n            'tried_dirs': loc['exp_dirs']\n        })\n\nos.makedirs('output/paper_f1_audit', exist_ok=True)\nwith open('output/paper_f1_audit/paper_f1_audit_table.json', 'w') as f:\n    json.dump(results, f, indent=2)\n\nhdr = f\"{'Paper Location':<45} {'Model':<20} {'Greedy':>8} {'Oracle':>8} {'Head':>8} {'Degen%':>7} {'OldOrc':>8} {'Delta':>8} {'St':<7}\"\nprint()\nprint(hdr)\nprint('=' * len(hdr))\nfor r in results:\n    if r['status'] == 'verified':\n        ds = f\"{r['degen_pct']:.1f}\" if r.get('degen_pct') is not None else \"N/A\"\n        oo = f\"{r['old_oracle']:.4f}\" if r.get('old_oracle') is not None else \"N/A\"\n        print(f\"{r['paper_location']:<45} {r['model']:<20} {r['greedy_f1']:>8.4f} {r['oracle_f1']:>8.4f} {r['headroom_pp']:>7.2f}pp {ds:>7} {oo:>8} {str(r['delta_pp']):>8} OK\")\n    else:\n        print(f\"{r['paper_location']:<45} {r['model']:<20} {'---':>8} {'---':>8} {'---':>8} {'---':>7} {'---':>8} {'---':>8} MISS\")\n\nv = sum(1 for r in results if r['status']=='verified')\nm = sum(1 for r in results if r['status']=='missing')\nprint(f\"\\nTotal: {len(results)}, verified={v}, missing={m}\")\n\nif m > 0:\n    print(\"\\n--- Missing ---\")\n    for r in results:\n        if r['status'] == 'missing':\n            print(f\"  {r['paper_location']}: tried {r['tried_dirs']}\")\n            for tried in r['tried_dirs']:\n                matches = glob.glob(f'output/*{tried}*')\n                if matches:\n                    print(f\"    -> Potential: {matches}\")\nPYEOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "account": "root",
    "command": "cat > /root/autodl-tmp/struct_self_consist_ie/output/paper_f1_audit_script.py << 'PYEOF'\nimport json, os, glob\n\nos.chdir('/root/autodl-tmp/struct_self_consist_ie')\n\nwith open('output/unified_oracle_audit/oracle_f1_recalc_results.json') as f:\n    oracle_audit = json.load(f)\n\nwith open('output/unified_degeneracy_audit/degeneracy_recalc_results.json') as f:\n    degen_audit = json.load(f)\n\noracle_map = {r['exp_dir']: r for r in oracle_audit}\ndegen_map = {r['dir']: r for r in degen_audit}\n\nprint(f\"Oracle audit: {len(oracle_audit)} experiments\")\nprint(f\"Degeneracy audit: {len(degen_audit)} experiments\")\n\npaper_locations = [\n    {\"paper_location\": \"4B SciERC greedy/oracle/headroom\", \"exp_dirs\": [\"exp_qwen3_4b_scierc_scs_inference\"], \"model\": \"Qwen3-4B\"},\n    {\"paper_location\": \"4B CoNLL greedy/oracle/headroom\", \"exp_dirs\": [\"exp_qwen3_4b_conll_scs_inference\", \"exp_qwen3_4b_conll_scs_inference_v2\"], \"model\": \"Qwen3-4B\"},\n    {\"paper_location\": \"rank=8 SciERC greedy/oracle/headroom\", \"exp_dirs\": [\"exp_023_rank8_inference\", \"exp_023_lora_rank8\"], \"model\": \"Qwen3-8B rank=8\"},\n    {\"paper_location\": \"N=32 SciERC greedy/oracle\", \"exp_dirs\": [\"exp_025_n32\"], \"model\": \"Qwen3-8B N=32\"},\n    {\"paper_location\": \"N=16 SciERC greedy/oracle (seed42)\", \"exp_dirs\": [\"exp_001_seed42_v2\", \"exp_012_rerun_1024\"], \"model\": \"Qwen3-8B N=16\"},\n    {\"paper_location\": \"FewNERD N=8 seed42 greedy/oracle\", \"exp_dirs\": [\"exp_021_inference\", \"exp_021_fewnerd_full\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"FewNERD N=16 greedy/oracle\", \"exp_dirs\": [\"exp_027_fewnerd_n16\"], \"model\": \"Qwen3-8B N=16\"},\n    {\"paper_location\": \"LLaMA SciERC seed42\", \"exp_dirs\": [\"exp_018_llama_scierc_seed42_r1024\", \"exp_007_llama_n16\", \"exp_007_llama_n16_r1024\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA SciERC seed123\", \"exp_dirs\": [\"exp_018_llama_scierc_seed123\", \"exp_007_llama_scierc_seed123\", \"exp_007_llama_seed123\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA SciERC seed456\", \"exp_dirs\": [\"exp_018_llama_scierc_seed456_r1024\", \"exp_007_llama_seed456\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA CoNLL seed42\", \"exp_dirs\": [\"exp_017_llama_conll_n16_r1024\", \"exp_017_llama_conll_n16\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA CoNLL seed123\", \"exp_dirs\": [\"exp_017_llama_conll_n16_s123_r1024\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"LLaMA CoNLL seed456\", \"exp_dirs\": [\"exp_017_llama_conll_n16_s456_r1024\"], \"model\": \"LLaMA3.1-8B\"},\n    {\"paper_location\": \"CoNLL Qwen seed42\", \"exp_dirs\": [\"exp_002_conll_n16\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"CoNLL Qwen seed123\", \"exp_dirs\": [\"exp_002_conll_n16_seed123\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"CoNLL Qwen seed456\", \"exp_dirs\": [\"exp_002_conll_n16_seed456\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"3-epoch SciERC\", \"exp_dirs\": [\"exp_029a_scierc_3epoch\", \"exp_029a_inference\"], \"model\": \"Qwen3-8B 3ep\"},\n    {\"paper_location\": \"10-epoch SciERC\", \"exp_dirs\": [\"exp_029b_scierc_10epoch\", \"exp_029b_inference\"], \"model\": \"Qwen3-8B 10ep\"},\n    {\"paper_location\": \"T=0.5 SciERC\", \"exp_dirs\": [\"exp_026_t05\"], \"model\": \"Qwen3-8B T=0.5\"},\n    {\"paper_location\": \"T=0.8 SciERC\", \"exp_dirs\": [\"exp_026_t08\"], \"model\": \"Qwen3-8B T=0.8\"},\n    {\"paper_location\": \"T=1.2 SciERC\", \"exp_dirs\": [\"exp_026_t12\"], \"model\": \"Qwen3-8B T=1.2\"},\n    {\"paper_location\": \"SciERC canonical seed42\", \"exp_dirs\": [\"exp_012_rerun_1024\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"SciERC seed123\", \"exp_dirs\": [\"exp_001_seed123_v2\", \"exp_018_qwen_scierc_seed123\"], \"model\": \"Qwen3-8B\"},\n    {\"paper_location\": \"SciERC seed456\", \"exp_dirs\": [\"exp_001_seed456_v2\", \"exp_018_qwen_scierc_seed456\"], \"model\": \"Qwen3-8B\"},\n]\n\nresults = []\nfor loc in paper_locations:\n    found = False\n    for exp_dir in loc['exp_dirs']:\n        if exp_dir in oracle_map:\n            r = oracle_map[exp_dir]\n            greedy = r.get('greedy_f1_unified', r.get('greedy_f1'))\n            oracle_val = r.get('oracle_f1_unified', r.get('oracle_f1'))\n            headroom = round((oracle_val - greedy) * 100, 2) if greedy is not None and oracle_val is not None else None\n            degen_info = degen_map.get(exp_dir, {})\n            degen_pct = degen_info.get('degen_pct_unified')\n            results.append({\n                'paper_location': loc['paper_location'],\n                'model': loc['model'],\n                'experiment_id': exp_dir,\n                'n_instances': r.get('n_instances'),\n                'greedy_f1': round(greedy, 4) if greedy is not None else None,\n                'oracle_f1': round(oracle_val, 4) if oracle_val is not None else None,\n                'headroom_pp': headroom,\n                'old_oracle': r.get('oracle_f1_old'),\n                'delta_pp': r.get('delta'),\n                'degen_pct': degen_pct,\n                'status': 'verified'\n            })\n            found = True\n            break\n    if not found:\n        results.append({\n            'paper_location': loc['paper_location'],\n            'model': loc['model'],\n            'experiment_id': None,\n            'status': 'missing',\n            'tried_dirs': loc['exp_dirs']\n        })\n\nos.makedirs('output/paper_f1_audit', exist_ok=True)\nwith open('output/paper_f1_audit/paper_f1_audit_table.json', 'w') as f:\n    json.dump(results, f, indent=2)\n\nhdr = f\"{'Paper Location':<45} {'Model':<20} {'Greedy':>8} {'Oracle':>8} {'Head':>8} {'Degen%':>7} {'OldOrc':>8} {'Delta':>8} {'St':<7}\"\nprint()\nprint(hdr)\nprint('=' * len(hdr))\nfor r in results:\n    if r['status'] == 'verified':\n        ds = f\"{r['degen_pct']:.1f}\" if r.get('degen_pct') is not None else \"N/A\"\n        oo = f\"{r['old_oracle']:.4f}\" if r.get('old_oracle') is not None else \"N/A\"\n        print(f\"{r['paper_location']:<45} {r['model']:<20} {r['greedy_f1']:>8.4f} {r['oracle_f1']:>8.4f} {r['headroom_pp']:>7.2f}pp {ds:>7} {oo:>8} {str(r['delta_pp']):>8} OK\")\n    else:\n        print(f\"{r['paper_location']:<45} {r['model']:<20} {'---':>8} {'---':>8} {'---':>8} {'---':>7} {'---':>8} {'---':>8} MISS\")\n\nv = sum(1 for r in results if r['status']=='verified')\nm = sum(1 for r in results if r['status']=='missing')\nprint(f\"\\nTotal: {len(results)}, verified={v}, missing={m}\")\n\nif m > 0:\n    print(\"\\n--- Missing ---\")\n    for r in results:\n        if r['status'] == 'missing':\n            print(f\"  {r['paper_location']}: tried {r['tried_dirs']}\")\n            for tried in r['tried_dirs']:\n                matches = glob.glob(f'output/*{tried}*')\n                if matches:\n                    print(f\"    -> Potential: {matches}\")\nPYEOF"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T21:53:23.965335+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T21:53:23.965461+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "account": "root",
  "command": "/root/miniconda3/bin/python3 /root/autodl-tmp/struct_self_consist_ie/output/paper_f1_audit_script.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "account": "root",
    "command": "/root/miniconda3/bin/python3 /root/autodl-tmp/struct_self_consist_ie/output/paper_f1_audit_script.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T21:53:23.965608+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Oracle audit: 74 experiments\\nDegeneracy audit: 20 experiments\\n\\nPaper Location                                Model                  Greedy   Oracle     Head  Degen%   OldOrc    Delta St     \\n===============================================================================================================================\\n4B SciERC greedy/oracle/headroom              Qwen3-4B               0.6622   0.7925   13.03pp    10.4   0.7839  +0.85pp OK\\n4B CoNLL greedy/oracle/headroom               Qwen3-4B               0.9236   0.9394    1.58pp     N/A   0.9408  -0.13pp OK\\nrank=8 SciERC greedy/oracle/headroom          Qwen3-8B rank=8        0.6397   0.7998   16.01pp     N/A   0.7937  +0.61pp OK\\nN=32 SciERC greedy/oracle                     Qwen3-8B N=32          0.6397   0.8396   19.99pp     N/A   0.8379  +0.16pp OK\\nN=16 SciERC greedy/oracle (seed42)            Qwen3-8B N=16          0.6442   0.8194   17.52pp     N/A   0.8150  +0.44pp OK\\nFewNERD N=8 seed42 greedy/oracle              Qwen3-8B               0.7478   0.8719   12.41pp     N/A      N/A      N/A OK\\nFewNERD N=16 greedy/oracle                    Qwen3-8B N=16          0.7478   0.9020   15.42pp     7.1      N/A      N/A OK\\nLLaMA SciERC seed42                           LLaMA3.1-8B            0.6460   0.7748   12.88pp    24.9   0.7781  -0.33pp OK\\nLLaMA SciERC seed123                          LLaMA3.1-8B            0.6454   0.7657   12.03pp    26.6   0.7689  -0.32pp OK\\nLLaMA SciERC seed456                          LLaMA3.1-8B            0.6459   0.7631   11.72pp    27.4   0.7683  -0.52pp OK\\nLLaMA CoNLL seed42                            LLaMA3.1-8B            0.9239   0.9482    2.43pp    86.5   0.9494  -0.11pp OK\\nLLaMA CoNLL seed123                           LLaMA3.1-8B            0.9238   0.9494    2.56pp    86.4   0.9498  -0.04pp OK\\nLLaMA CoNLL seed456                           LLaMA3.1-8B            0.9242   0.9488    2.46pp    86.7 
…[truncated 1551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T21:53:23.965797+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/paper_f1_audit/paper_f1_audit_table.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/paper_f1_audit/paper_f1_audit_table.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T21:53:23.965927+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"313 /root/autodl-tmp/struct_self_consist_ie/output/paper_f1_audit/paper_f1_audit_table.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-18T21:53:23.966093+00:00_

JSON 已保存（313 行）。结果汇总：

**24/24 论文位置全部 verified，0 missing。**

| Paper Location | Model | Greedy | Oracle | Headroom | Degen% | Old→New Delta |
|---|---|---|---|---|---|---|
| 4B SciERC | Qwen3-4B | 0.6622 | 0.7925 | 13.03pp | 10.4% | +0.85pp |
| 4B CoNLL | Qwen3-4B | 0.9236 | 0.9394 | 1.58pp | — | -0.13pp |
| rank=8 SciERC | Qwen3-8B r8 | 0.6397 | 0.7998 | 16.01pp | — | +0.61pp |
| N=32 SciERC | Qwen3-8B | 0.6397 | 0.8396 | 19.99pp | — | +0.16pp |
| N=16 SciERC seed42 | Qwen3-8B | 0.6442 | 0.8194 | 17.52pp | — | +0.44pp |
| FewNERD N=8 seed42 | Qwen3-8B | 0.7478 | 0.8719 | 12.41pp | — | N/A |
| FewNERD N=16 | Qwen3-8B | 0.7478 | 0.9020 | 15.42pp | 7.1% | N/A |
| LLaMA SciERC s42/123/456 | LLaMA3.1-8B | 0.645-0.646 | 0.763-0.775 | 11.7-12.9pp | 25-27% | -0.3~-0.5pp |
| LLaMA CoNLL s42/123/456 | LLaMA3.1-8B | 0.924 | 0.948-0.949 | 2.4-2.6pp | 86-87% | -0.04~-0.11pp |
| CoNLL Qwen s42/123/456 | Qwen3-8B | 0.907 | 0.957-0.959 | 5.0-5.2pp | 47-55% | -0.48~+0.18pp |
| 3-epoch SciERC | Qwen3-8B | 0.6501 | 0.7998 | 14.97pp | — | +0.52pp |
| 10-epoch SciERC | Qwen3-8B | 0.6467 | 0.7331 | 8.64pp | — | -0.68pp |
| T=0.5/0.8/1.2 SciERC | Qwen3-8B | 0.643-0.649 | 0.740-0.789 | 9.1-14.6pp | 15-41% | -0.28~+0.06pp |
| SciERC canonical seed42 | Qwen3-8B | 0.6439 | 0.7758 | 13.19pp | 17.8% | -0.17pp |
| SciERC seed123/456 | Qwen3-8B | 0.644 | 0.817-0.823 | 17.3-17.9pp | — | +0.44~+0.58pp |

关键发现：
- unified 与 old oracle 的 delta 绝大多数在 ±0.6pp 以内，数值一致性良好
- 退化率最高的是 LLaMA CoNLL（86-87%）和 4B CoNLL（90.6%）
- 产出文件：`output/paper_f1_audit/paper_f1_audit_table.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_paper_f1_audit_table_20260518T215058"
}
```

</details>

---
