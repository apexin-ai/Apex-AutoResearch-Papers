# code exp026 t ablation submit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 151
- **Recorded user turns:** 0
- **Tool calls:** 75
- **Original source:** `logs/chats/worker_code_exp026_t_ablation_submit_20260518T152445.jsonl`
- **Structured JSON:** [`f605583a627b2742a4c3.json`](../../sessions/f6/f605583a627b2742a4c3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

151 recorded events

### Tool call

_source line 1 · 2026-05-18T15:30:47.070382+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T15:30:47.070728+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T15:30:47.070927+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_012_rerun_1024'}",
  "project": "struct_self_consist_ie",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_012_rerun_1024'}",
    "project": "struct_self_consist_ie",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T15:30:47.071079+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4463}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T15:30:47.071234+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'ft_002_v2'}",
  "project": "struct_self_consist_ie",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'ft_002_v2'}",
    "project": "struct_self_consist_ie",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T15:30:47.071364+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T15:30:47.071484+00:00_

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
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
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

### Tool call

_source line 8 · 2026-05-18T15:30:47.071604+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -path \"*/ft_002*\" -name \"*.safetensors\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -path \"*/ft_002*\" -name \"*.safetensors\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T15:30:47.071764+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\n_backup_cond_fix\\nanalysis_d140_oracle_gated.py\\nanalysis_multiseed_selection_f1.py\\nanalysis_scierc_n16_selection.py\\nanalysis_scierc_re_n16_selection.py\\nanalyze_3seed_5signal.py\\nanalyze_component_wise_re.py\\nanalyze_entity_voting.py\\nanalyze_exact_match_voting.py\\nanalyze_exp002_conll2003.py\\nanalyze_exp004_re_diagnostic.py\\nanalyze_exp004_v2_re_diagnostic.py\\nanalyze_exp005_v2_temperature.py\\nanalyze_exp012_rerun_5signal.py\\nanalyze_exp015_unified.py\\nanalyze_exp015_v2_metrics.py\\nanalyze_exp016_ensemble.py\\nanalyze_exp017_5signal.py\\nanalyze_exp017_llama_conll_n16.py\\nanalyze_exp017_llama_conll_n16_s123.py\\nanalyze_exp017_t07.py\\nanalyze_exp023_rank8.py\\nanalyze_exp023_rank8_full.py\\nanalyze_fewnerd_results.py\\nanalyze_llama3b_vs_8b.py\\nanalyze_llama_fewnerd.py\\nanalyze_logprob_baseline.py\\nanalyze_lp_range_cdf.py\\nanalyze_ood_signals.py\\nanalyze_per_type_lp.py\\nanalyze_per_type_lp_scierc.py\\nanalyze_scale_ablation_4b.py\\nanalyze_thinking_token_lp_dilution.py\\ncascade_selection_analysis.py\\ncompute_em_selection_f1.py\\ncompute_epoch_scierc_rho_textbased.py\\ncompute_metrics.py\\ncompute_re_conditional.py\\ncompute_selection_f1.py\\ncompute_within_lp_f1_llama.py\\nconll_seed123_analysis.py\\nconll_seed42_analysis.py\\nconll_seed456_analysis.py\\nconsistency.py\\nconvert_conll2003.py\\nconvert_fewnerd.py\\nconvert_to_llamafactory.py\\nconvert_wnut17.py\\nd140_oracle_gated_analysis.py\\ndals_analysis.py\\ndals_fixed_tau_evaluation.py\\ndata_utils.py\\ndeberta_verifier.py\\ndiagnose_logprob_rho.py\\ndiversity_analysis.py\\ndiversity_stratified_selection.py\\nem_exact_match_freq.py\\nentity_token_analysis.py\\neval_exp012_rerun_auroc.py\\neval_n16_5signal.py\\neval_n8_5signal.py\\neval_s456_5signal.py\\neval_seed42_r1024_5signal.py\\nevaluation.py\\nevaluation.py.bak_d141v2\\nexp001_3seed_all_signals.py\\nexp001_postprocess.py\\nexp009_stratification_analysis.py\
…[truncated 1457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T15:30:47.071918+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T15:30:47.072071+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "which python",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "which python",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T15:30:47.072216+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'which' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T15:30:47.072371+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -path \"*ft_002*\" -name \"*.safetensors\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -path \"*ft_002*\" -name \"*.safetensors\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T15:30:47.072498+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T15:30:47.072613+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/checkpoints/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/checkpoints/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T15:30:47.072740+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"exp017_train.log\\nfewnerd_train.log\\nft_001_train.log\\nft_fewnerd_smoke\\nllama3.1-8b-conll2003-lora\\nllama3.1-8b-fewnerd-lora\\nllama3.1-8b-scierc-lora\\nllama3.2-3b-scierc-lora\\nllama_fewnerd_train.log\\nllama_fewnerd_train_4gpu.log\\nqwen3-4b-conll2003-lora\\nqwen3-4b-scierc-lora\\nqwen3-8b-conll2003-lora\\nqwen3-8b-fewnerd-5epoch-lora\\nqwen3-8b-fewnerd-exp021-merged\\nqwen3-8b-scierc-10epoch-lora\\nqwen3-8b-scierc-10epoch-merged\\nqwen3-8b-scierc-3epoch-lora\\nqwen3-8b-scierc-3epoch-merged\\nqwen3-8b-scierc-lora-rank8\\nqwen3-8b-scierc-lora-v2\\nqwen3-8b-scierc-merged-v2\\nqwen3-8b-wnut17-lora\\nwnut17_train.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T15:30:47.072867+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/sampling.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/sampling.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T15:30:47.073204+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Multi-sample inference module for structured IE with vLLM + XGrammar constrained decoding.\\n\\nProvides VLLMSampler for batch sampling, prompt construction for UIE tasks,\\nand a full pipeline that produces SampledInstance dicts.\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport json\\nimport os\\nfrom typing import Any\\n\\n\\n# ---------------------------------------------------------------------------\\n# UIE JSON schema for XGrammar constrained decoding\\n# ---------------------------------------------------------------------------\\n\\nUIE_JSON_SCHEMA: dict[str, Any] = {\\n    \\\"type\\\": \\\"object\\\",\\n    \\\"properties\\\": {\\n        \\\"entities\\\": {\\n            \\\"type\\\": \\\"array\\\",\\n            \\\"items\\\": {\\n                \\\"type\\\": \\\"object\\\",\\n                \\\"properties\\\": {\\n                    \\\"text\\\": {\\\"type\\\": \\\"string\\\"},\\n                    \\\"type\\\": {\\\"type\\\": \\\"string\\\"},\\n                    \\\"start\\\": {\\\"type\\\": \\\"integer\\\"},\\n                    \\\"end\\\": {\\\"type\\\": \\\"integer\\\"},\\n                },\\n                \\\"required\\\": [\\\"text\\\", \\\"type\\\", \\\"start\\\", \\\"end\\\"],\\n            },\\n        },\\n        \\\"relations\\\": {\\n            \\\"type\\\": \\\"array\\\",\\n            \\\"items\\\": {\\n                \\\"type\\\": \\\"object\\\",\\n                \\\"properties\\\": {\\n                    \\\"head\\\": {\\\"type\\\": \\\"string\\\"},\\n                    \\\"tail\\\": {\\\"type\\\": \\\"string\\\"},\\n                    \\\"type\\\": {\\\"type\\\": \\\"string\\\"},\\n                    \\\"head_start\\\": {\\\"type\\\": \\\"integer\\\"},\\n                    \\\"head_end\\\": {\\\"type\\\": \\\"integer\\\"},\\n                    \\\"tail_start\\\": {\\\"type\\\": \\\"integer\\\"},\\n                    \\\"tail_end\\
…[truncated 7663 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T15:30:47.073399+00:00_

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
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
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

_source line 20 · 2026-05-18T15:30:47.073633+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "which python",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "which python",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T15:30:47.073851+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"adalp_analysis_results.json\\nanalysis_epsilon_sweep\\nanalysis_fk_bootstrap_ci.json\\nanalysis_fk_bootstrap_per_instance.json\\nanalysis_lp_range_cdf.json\\nanalysis_lp_range_cdf_n16_3seed.json\\nanalysis_multiseed_selection_f1.json\\nanalysis_round8\\nanalysis_scierc_n16_3seed_selection_f1.json\\nanalysis_scierc_n16_3seed_selection_f1_merged.json\\nanalysis_scierc_re_n16_3seed_selection_f1.json\\nanalysis_unified_rho_full.json\\nbootstrap_ci_nscaling\\nbootstrap_ci_summary.json\\nbootstrap_ci_tables.tex\\ncalibration_baseline_results.json\\nconditional_filter_diagnosis.json\\nd108_greedy_f1\\nd108_lp_vc_combination\\nd108_mbr_within_rho\\nd108_q4q5\\nd110_4b_degeneracy\\nd112_disk_cleanup\\nd112_hybrid_strategy\\nd112_mf3_random_single\\nd112_table2_fix\\nd114_auroc_investigation\\nd140_oracle_gated\\nd141_conditional_decomp\\nd141_degeneracy_scatter\\nd141_entity_merge\\ndals_analysis.json\\ndals_cross_model.json\\ndals_hardening_results.json\\ndeberta_verifier\\ndeberta_verifier_5fold\\nepoch_scierc_textbased_rho.json\\nexp001_n16_seed123\\nexp001_n16_seed123_200only\\nexp001_n16_seed123_200only_backup\\nexp001_n16_seed123_full\\nexp001_n16_seed123_run.log\\nexp001_n16_seed42\\nexp001_n16_seed42_200only_backup\\nexp001_n16_seed42_run.log\\nexp001_n16_seed456\\nexp001_n16_seed456_200only\\nexp001_n16_seed456_run.log\\nexp001_seed123_t10_full\\nexp001_seed123_t10_full.log\\nexp001_seed456_t10_full\\nexp001_seed456_t10_full.log\\nexp002_conll2003\\nexp003_wnut17_dryrun\\nexp003_wnut17_eval\\nexp003_wnut17_eval.log\\nexp003_wnut17_pilot\\nexp003_wnut17_pilot.log\\nexp004_re_diagnostic\\nexp004v2_re_diagnostic\\nexp007_llama_dryrun\\nexp007_llama_inference\\nexp008_re_n16\\nexp008_re_n16_200only\\nexp008_re_n16_t10_full\\nexp008_re_n16_t10_full.log\\nexp009_stratification_results.json\\nexp010_selection_curves\\nexp016_signal_ensemble\\nexp018_3seed_5signal_results.json\\nexp_001_seed123_v2\\nexp_001_seed123_v2_
…[truncated 4155 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T15:30:47.074004+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'which python'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T15:30:47.074183+00:00_

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
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
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

_source line 24 · 2026-05-18T15:30:47.074328+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"all_signals_5signal.json\\nauroc_5signal.json\\ncomparison.json\\nper_type_lp_analysis.csv\\nper_type_lp_table.tex\\nreliability_data_1024.json\\nreport.json\\nrun.log\\nsamples.jsonl\\nsamples_with_logprobs.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T15:30:47.074457+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T15:30:47.074704+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"report.json\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T15:30:47.074837+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T15:30:47.075180+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loaded 551 test instances from scierc\\nINFO 05-16 20:18:53 [utils.py:233] non-default args: {'max_model_len': 4096, 'disable_log_stats': True, 'model': 'checkpoints/qwen3-8b-scierc-merged-v2'}\\nINFO 05-16 20:18:53 [model.py:533] Resolved architecture: Qwen3ForCausalLM\\nINFO 05-16 20:18:53 [model.py:1582] Using max model len 4096\\nINFO 05-16 20:18:53 [scheduler.py:231] Chunked prefill is enabled with max_num_batched_tokens=8192.\\nINFO 05-16 20:18:53 [vllm.py:775] Asynchronous scheduling is enabled.\\n(EngineCore pid=297983) INFO 05-16 20:18:54 [core.py:103] Initializing a V1 LLM engine (v0.18.1) with config: model='checkpoints/qwen3-8b-scierc-merged-v2', speculative_config=None, tokenizer='checkpoints/qwen3-8b-scierc-merged-v2', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, decode_context_parallel_size=1, dcp_comm_backend=ag_rs, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, enable_return_routed_experts=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_plugin='', enable_in_reasoning=False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=False, kv_cache_metrics_sample=0.01, cudagraph_metrics=False, enable_layerwise_nvtx_tracing=False, enable_mfu_metrics=False, enable_mm_processor_stats=False, enable_logging_iteration_details=False), seed=0, served_model_name=checkpoints/qwen3-8b-scierc-merged-v2, enable_prefix_caching=True, enable_chunked_prefill=True, pooler_config=None, compilation_config={'mode': <
…[truncated 6334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T15:30:47.075476+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T15:30:47.075751+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\nadapter_config.json\\nadapter_model.safetensors\\nadded_tokens.json\\nall_results.json\\nchat_template.jinja\\ncheckpoint-400\\ncheckpoint-500\\ncheckpoint-585\\neval_results.json\\nmerges.txt\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\ntrain_results.json\\ntrainer_log.jsonl\\ntrainer_state.json\\ntraining_args.bin\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T15:30:47.075899+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "which python3 && python3 --version",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "which python3 && python3 --version",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T15:30:47.076030+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'which python3 && python3 --version'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T15:30:47.076228+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-18T15:30:47.076378+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-18T15:30:47.076509+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"report.json\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.16}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-18T15:30:47.076634+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_026_T05/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_026_T05/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-18T15:30:47.076756+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"report.json\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T15:30:47.076874+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"report.json\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T15:30:47.076998+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -50 /root/autodl-tmp/struct_self_consist_ie/code/run_mvp_pilot.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -50 /root/autodl-tmp/struct_self_consist_ie/code/run_mvp_pilot.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T15:30:47.077204+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"MVP pilot experiment script for structured self-consistency IE.\\n\\nIntegrates data loading, vLLM sampling, consistency scoring, and evaluation\\ninto a single CLI-driven pipeline. Outputs a verdict (PASS/MARGINAL/FAIL)\\nbased on the correlation between structural consistency and per-instance F1.\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport os\\nimport random\\nimport sys\\n\\nimport numpy as np\\n\\nfrom data_utils import load_scierc, load_ace05, load_conll2003, load_wnut17, load_fewnerd\\nfrom sampling import (\\n    VLLMSampler,\\n    run_sampling_pipeline,\\n    save_sampled_results,\\n    load_sampled_results,\\n    realign_spans,\\n    SCIERC_SCHEMA_HINT,\\n    CONLL2003_SCHEMA_HINT,\\n    WNUT17_SCHEMA_HINT,\\n    FEWNERD_SCHEMA_HINT,\\n)\\nfrom consistency import compute_all_consistency_scores\\nfrom evaluation import (\\n    per_instance_f1,\\n    compute_ner_f1,\\n    compute_re_f1,\\n    compute_eae_f1,\\n    spearman_correlation,\\n    kendall_correlation,\\n    compute_auroc,\\n    compute_sample_f1_distribution,\\n)\\n\\n\\ndef parse_args() -> argparse.Namespace:\\n    \\\"\\\"\\\"Parse command-line arguments.\\\"\\\"\\\"\\n    p = argparse.ArgumentParser(description=\\\"MVP pilot for structured self-consistency IE\\\")\\n    p.add_argument(\\\"--model_path\\\", type=str, required=True, help=\\\"Path to the fine-tuned model\\\")\\n    p.add_argument(\\\"--data_dir\\\", type=str, required=True, help=\\\"Dataset directory (SciERC or ACE05)\\\")\\n    p.add_argument(\\\"--dataset\\\", type=str, default=\\\"scierc\\\", choices=[\\\"scierc\\\", \\\"ace05\\\", \\\"conll2003\\\", \\\"wnut17\\\", \\\"fewnerd\\\"],\\n                   help=\\\"Dataset name (default: scierc)\\\")\\n    p.add_argument(\\\"--subtask\\\", type=str, default=\\\"ner\\\", choices=[\\\"ner\\\", \\\"re\\\", \\\"eae\\\", \\\"joint\\\"],\\n\", \"stderr\": \"\", \"re
…[truncated 78 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-18T15:30:47.077358+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "conda run -n base which python",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "conda run -n base which python",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T15:30:47.077484+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'conda run -n base which python'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: conda: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-18T15:30:47.077635+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-18T15:30:47.077982+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"X96-1059_sent000\\\", \\\"text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\", \\\"start\\\": 15, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 0, \\\"head_end\\\": 27, \\\"tail_start\\\": 103, \\\"tail_end\\\": 125}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 15, \\\"head_end\\\": 27, \\\"tail_start\\\": 31, \\\"tail_end\\\": 44}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"USED-FOR\\\", \\\"head_start\\\": 103, \\\"head_end\\\": 125, \\\"tail_start\\\": 129, \\\"tail_end\\\": 153}], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"
…[truncated 8970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-18T15:30:47.078163+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -c \"logprobs\" /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -c \"logprobs\" /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-18T15:30:47.078305+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-18T15:30:47.078429+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -c \"logprobs\" /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -c \"logprobs\" /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-18T15:30:47.078560+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-18T15:30:47.078681+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -c \"logprobs\" /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -c \"logprobs\" /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-18T15:30:47.078803+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-18T15:30:47.078920+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-18T15:30:47.079081+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"scierc\\\",\\n  \\\"subtask\\\": \\\"ner\\\",\\n  \\\"n_samples\\\": 8,\\n  \\\"temperature\\\": 0.5,\\n  \\\"num_instances\\\": 551,\\n  \\\"use_train_format\\\": true,\\n  \\\"greedy_f1\\\": 0.6646866646866646,\\n  \\\"oracle_f1\\\": 0.7423167848699763,\\n  \\\"oracle_headroom\\\": 0.07763012018331172,\\n  \\\"fleiss_kappa_mean\\\": 0.5768944047623729,\\n  \\\"soft_jaccard_mean\\\": 0.8333504281499606,\\n  \\\"correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.2562729944979881,\\n    \\\"p_value\\\": 2.2246018886526807e-09,\\n    \\\"n\\\": 529\\n  },\\n  \\\"correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.2970104220289181,\\n    \\\"p_value\\\": 3.101588697922607e-12,\\n    \\\"n\\\": 529\\n  },\\n  \\\"correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.23101526459064237,\\n    \\\"p_value\\\": 3.1856837449231265e-07,\\n    \\\"n\\\": 479\\n  },\\n  \\\"correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.2781284141706589,\\n    \\\"p_value\\\": 5.870932916256781e-10,\\n    \\\"n\\\": 479\\n  },\\n  \\\"n_gold_empty_filtered\\\": 22,\\n  \\\"n_greedy_f1_zero_filtered\\\": 50,\\n  \\\"structural_beats_surface\\\": true,\\n  \\\"rho_advantage\\\": 0.04073742753092996,\\n  \\\"sample_f1_mean\\\": 0.6358160799616321,\\n  \\\"sample_f1_std\\\": 0.3087691195817718,\\n  \\\"sample_f1_pct_zero\\\": 10.326086956521738,\\n  \\\"logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.21781651832605584,\\n      \\\"p_rho\\\": 4.2191798011736937e-07,\\n      \\\"tau\\\": 0.15754657878338615,\\n      \\\"p_tau\\\": 2.3394729435169404e-07,\\n      \\\"auroc\\\": 0.5781432748538011,\\n      \\\"n\\\": 529\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.15563076800416717,\\n      \\\"p_rho\\\": 0.0006306098990388763,\\n      \\\"tau\\\": 0.11177590784221654,\\n      \\\"p_tau\\\": 0.000512367664145719,\\n      \\\"auroc\
…[truncated 335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-18T15:30:47.079295+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -80 /root/autodl-tmp/struct_self_consist_ie/code/exp026_temp_ablation_metrics.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -80 /root/autodl-tmp/struct_self_consist_ie/code/exp026_temp_ablation_metrics.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-18T15:30:47.079472+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Compute missing metrics for exp-026 Temperature Ablation.\\n\\nMetrics per temperature:\\n1. Degeneracy rate (exact duplicate KeySet: text+type)\\n2. LP within-instance range (mean/std of max-min across N=8)\\n3. LP selection F1 (+ greedy/oracle/random baselines)\\n4. All 5 signals selection F1 (SJ, FK, EM, VC, LP)\\n5. QE metrics: rho(signal, F1) and AUROC for all 5 signals\\n\\\"\\\"\\\"\\n\\nimport json\\nimport sys\\nimport os\\nimport numpy as np\\nfrom collections import Counter\\nfrom itertools import combinations\\nfrom scipy.stats import spearmanr\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom evaluation import per_instance_f1, entity_strict_match\\n\\nBASE = \\\"/root/autodl-tmp/struct_self_consist_ie\\\"\\nN = 8\\n\\nTEMP_CONFIGS = {\\n    \\\"T=0.5\\\": f\\\"{BASE}/output/exp_026_T05/samples.jsonl\\\",\\n    \\\"T=0.8\\\": f\\\"{BASE}/output/exp_026_T08/samples.jsonl\\\",\\n    \\\"T=1.0\\\": f\\\"{BASE}/output/exp_012_logprob/samples_with_logprobs.jsonl\\\",\\n    \\\"T=1.2\\\": f\\\"{BASE}/output/exp_026_T12/samples.jsonl\\\",\\n}\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f]\\n\\ndef entity_surface_set(ext):\\n    return frozenset((e[\\\"text\\\"], e[\\\"type\\\"]) for e in ext.get(\\\"entities\\\", []))\\n\\ndef compute_degeneracy(data, n_samples=N):\\n    \\\"\\\"\\\"Fraction of instances where all N samples have identical KeySet.\\\"\\\"\\\"\\n    degenerate = 0\\n    total = 0\\n    for inst in data:\\n        samples = inst.get(\\\"samples\\\", [])[:n_samples]\\n        if len(samples) < n_samples:\\n            continue\\n        total += 1\\n        keys = [entity_surface_set(s) for s in samples]\\n        unique_keys = set(keys)\\n        if len(unique_keys) == 1:\\n            degenerate += 1\\n    return degenerate / total if total else 0.0, degenerate, total\\n
…[truncated 1309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-18T15:30:47.079620+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -80 /root/autodl-tmp/struct_self_consist_ie/code/exp026_degeneracy_rho.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -80 /root/autodl-tmp/struct_self_consist_ie/code/exp026_degeneracy_rho.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-18T15:30:47.079786+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Task 1: Correct degeneracy (Constant F1, gold-filtered)\\n   Task 2: Within-instance Spearman rho(LP, F1)\\n\\\"\\\"\\\"\\nimport json\\nimport numpy as np\\nfrom scipy.stats import spearmanr\\n\\nBASE = \\\"/root/autodl-tmp/struct_self_consist_ie\\\"\\nN = 8\\n\\nTEMP_CONFIGS = {\\n    \\\"T=0.5\\\": f\\\"{BASE}/output/exp_026_T05/samples.jsonl\\\",\\n    \\\"T=0.8\\\": f\\\"{BASE}/output/exp_026_T08/samples.jsonl\\\",\\n    \\\"T=1.0\\\": f\\\"{BASE}/output/exp_012_logprob/samples_with_logprobs.jsonl\\\",\\n    \\\"T=1.2\\\": f\\\"{BASE}/output/exp_026_T12/samples.jsonl\\\",\\n}\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f]\\n\\ndef entity_strict_f1(pred_entities, gold_entities):\\n    pred_set = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in pred_entities}\\n    gold_set = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in gold_entities}\\n    tp = len(pred_set & gold_set)\\n    fp = len(pred_set - gold_set)\\n    fn = len(gold_set - pred_set)\\n    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0\\n    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0\\n    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0\\n    return f1\\n\\ndef get_sample_lp(sample, inst_logprobs, idx):\\n    \\\"\\\"\\\"Get mean logprob for a sample, trying multiple field names.\\\"\\\"\\\"\\n    if \\\"mean_logprob\\\" in sample:\\n        return sample[\\\"mean_logprob\\\"]\\n    if inst_logprobs is not None and idx < len(inst_logprobs):\\n        return inst_logprobs[idx]\\n    return None\\n\\ndef analyze(name, path):\\n    data = load_data(path)\\n    \\n    # Task 1: Constant F1, gold-filtered degeneracy\\n    gold_filtered_total = 0\\n    constant_f1_count = 0\\n    \\n    # Task 2: Within-instance rho\\n    rho_values = []\\n    \\n    for inst in data:\\n        gold 
…[truncated 1182 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-18T15:30:47.079941+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -100 /root/autodl-tmp/struct_self_consist_ie/code/analyze_exp012_rerun_5signal.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -100 /root/autodl-tmp/struct_self_consist_ie/code/analyze_exp012_rerun_5signal.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-18T15:30:47.080114+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"exp_012_rerun_1024: Full 5-signal metrics for NER + RE.\\\"\\\"\\\"\\n\\nimport json\\nimport sys\\nfrom collections import Counter\\n\\nimport numpy as np\\nfrom scipy.stats import spearmanr, kendalltau, rankdata\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import compute_all_consistency_scores\\nfrom evaluation import per_instance_f1\\n\\nDATA_PATH = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl\\\"\\nOUTPUT_PATH = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/all_signals_5signal.json\\\"\\nSUBTASKS = [\\\"ner\\\", \\\"re\\\"]\\n\\n\\ndef load_data(path):\\n    records = []\\n    with open(path) as f:\\n        for line in f:\\n            if line.strip():\\n                records.append(json.loads(line))\\n    return records\\n\\n\\ndef compute_exact_match_rate(samples, subtask):\\n    if subtask == \\\"ner\\\":\\n        keys = [frozenset((e[\\\"text\\\"], e[\\\"type\\\"]) for e in s.get(\\\"entities\\\", [])) for s in samples]\\n    else:\\n        keys = [frozenset((r[\\\"head\\\"], r[\\\"tail\\\"], r[\\\"type\\\"]) for r in s.get(\\\"relations\\\", [])) for s in samples]\\n    if not keys:\\n        return 0.0\\n    counter = Counter(keys)\\n    return counter.most_common(1)[0][1] / len(samples)\\n\\n\\ndef compute_voting_confidence(samples, subtask):\\n    N = len(samples)\\n    if N == 0:\\n        return 0.0\\n    counter = Counter()\\n    if subtask == \\\"ner\\\":\\n        for s in samples:\\n            for e in s.get(\\\"entities\\\", []):\\n                counter[(e[\\\"text\\\"], e[\\\"type\\\"])] += 1\\n    else:\\n        for s in samples:\\n            for r in s.get(\\\"relations\\\", []):\\n                counter[(r[\\\"head\\\"], r[\\\"tail\\\"], r[\\\"type\\\"])] += 1\\n    if not counter:\\n        return 0.0\\n    rates = [v / N for v in co
…[truncated 1592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-18T15:30:47.080293+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -50 /root/autodl-tmp/struct_self_consist_ie/code/eval_n8_5signal.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -50 /root/autodl-tmp/struct_self_consist_ie/code/eval_n8_5signal.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-18T15:30:47.080454+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"5-signal evaluation for N=8 experiments (baseline for N=8 vs N=16 comparison).\\\"\\\"\\\"\\nimport json, sys\\nimport numpy as np\\nfrom scipy.stats import spearmanr, rankdata\\nfrom collections import Counter\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import compute_all_consistency_scores\\nfrom evaluation import per_instance_f1\\n\\nEXPERIMENTS = {\\n    \\\"exp_002_conll_n8\\\": {\\n        \\\"path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/samples.jsonl\\\",\\n        \\\"subtask\\\": \\\"ner\\\",\\n        \\\"dataset\\\": \\\"conll2003\\\",\\n    },\\n    \\\"exp_007_llama_n8\\\": {\\n        \\\"path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/samples.jsonl\\\",\\n        \\\"subtask\\\": \\\"ner\\\",\\n        \\\"dataset\\\": \\\"scierc\\\",\\n    },\\n}\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\ndef compute_exact_match_rate(samples, subtask):\\n    if subtask == \\\"ner\\\":\\n        keys = [frozenset((e[\\\"text\\\"], e[\\\"type\\\"]) for e in s.get(\\\"entities\\\", [])) for s in samples]\\n    else:\\n        keys = [frozenset((r[\\\"head\\\"], r[\\\"tail\\\"], r[\\\"type\\\"]) for r in s.get(\\\"relations\\\", [])) for s in samples]\\n    if not keys: return 0.0\\n    c = Counter(keys)\\n    return c.most_common(1)[0][1] / len(samples)\\n\\ndef compute_voting_confidence(samples, subtask):\\n    N = len(samples)\\n    if N == 0: return 0.0\\n    counter = Counter()\\n    if subtask == \\\"ner\\\":\\n        for s in samples:\\n            for e in s.get(\\\"entities\\\", []):\\n                counter[(e[\\\"text\\\"], e[\\\"type\\\"])] += 1\\n    else:\\n        for s in samples:\\n            for r in s.get(\\\"relations\\\", []):\\n                counter[(r[\\\"he
…[truncated 188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-18T15:30:47.080599+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_026_T05/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_026_T05/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-18T15:30:47.080743+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"report.json\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-18T15:30:47.080957+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/miniconda3/bin/python 2>/dev/null || ls /root/miniconda3/envs/*/bin/python 2>/dev/null || find /root -maxdepth 4 -name python3 -type f 2>/dev/null | head -5",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/miniconda3/bin/python 2>/dev/null || ls /root/miniconda3/envs/*/bin/python 2>/dev/null || find /root -maxdepth 4 -name python3 -type f 2>/dev/null | head -5",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-18T15:30:47.081123+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-18T15:30:47.081309+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -30 /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -30 /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-18T15:30:47.081466+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Train format:   True\\n------------------------------------------------------------\\n  Greedy F1:      0.6633\\n  Oracle F1:      0.7684\\n  Oracle headroom:+0.1051\\n------------------------------------------------------------\\n  Fleiss' kappa (mean):    0.4514\\n  Soft Jaccard (mean):     0.7491\\n------------------------------------------------------------\\n  Sample F1 (mean):        0.6222\\n  Sample F1 (std):         0.3120\\n  Sample F1=0 (%):         11.2%\\n------------------------------------------------------------\\n  Gold-empty filtered:     22\\n  All-samples-F1=0 filtered: 52\\n------------------------------------------------------------\\n  Full ρ(κ,F1):   +0.2498  p=5.7701e-09  n=529\\n  Full ρ(SJ,F1):  +0.3589  p=1.5946e-17  n=529\\n  Cond ρ(κ,F1):   +0.1871  p=3.9231e-05  n=477\\n  Cond ρ(SJ,F1):  +0.3123  p=2.9811e-12  n=477\\n  Structural > Surface:    YES  (delta=+0.1091)\\n------------------------------------------------------------\\n  Logprob (full):  ρ=+0.2526  τ=+0.1823  AUROC=0.5890\\n  Logprob (cond):  ρ=+0.1808  τ=+0.1307  AUROC=0.5509\\n------------------------------------------------------------\\n  Verdict:        MARGINAL\\n  Note:           MVP verdict on single subtask; final pass requires at least one of NER/RE/EAE to meet threshold\\n============================================================\\n\\nReport saved to output/exp_026_t08/report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-18T15:30:47.081606+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -30 /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -30 /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-18T15:30:47.081761+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Train format:   True\\n------------------------------------------------------------\\n  Greedy F1:      0.6615\\n  Oracle F1:      0.7914\\n  Oracle headroom:+0.1299\\n------------------------------------------------------------\\n  Fleiss' kappa (mean):    0.3559\\n  Soft Jaccard (mean):     0.6451\\n------------------------------------------------------------\\n  Sample F1 (mean):        0.5938\\n  Sample F1 (std):         0.3250\\n  Sample F1=0 (%):         13.9%\\n------------------------------------------------------------\\n  Gold-empty filtered:     22\\n  All-samples-F1=0 filtered: 52\\n------------------------------------------------------------\\n  Full ρ(κ,F1):   +0.3377  p=1.4079e-15  n=529\\n  Full ρ(SJ,F1):  +0.3771  p=2.5337e-19  n=529\\n  Cond ρ(κ,F1):   +0.2668  p=3.2289e-09  n=477\\n  Cond ρ(SJ,F1):  +0.3551  p=1.2829e-15  n=477\\n  Structural > Surface:    YES  (delta=+0.0394)\\n------------------------------------------------------------\\n  Logprob (full):  ρ=+0.1963  τ=+0.1389  AUROC=0.5720\\n  Logprob (cond):  ρ=+0.1745  τ=+0.1235  AUROC=0.5569\\n------------------------------------------------------------\\n  Verdict:        MARGINAL\\n  Note:           MVP verdict on single subtask; final pass requires at least one of NER/RE/EAE to meet threshold\\n============================================================\\n\\nReport saved to output/exp_026_t12/report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-18T15:30:47.081901+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/all_signals_5signal.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/all_signals_5signal.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-18T15:30:47.082223+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"ner\\\": {\\n    \\\"full\\\": {\\n      \\\"n\\\": 529,\\n      \\\"pct_perfect\\\": 0.2495274102079395,\\n      \\\"metrics\\\": {\\n        \\\"SJ\\\": {\\n          \\\"rho\\\": {\\n            \\\"value\\\": 0.3598905669976535,\\n            \\\"ci_95\\\": [\\n              0.2732249154962052,\\n              0.4389387695378309\\n            ]\\n          },\\n          \\\"tau\\\": {\\n            \\\"value\\\": 0.26461187931901686\\n          },\\n          \\\"AUROC\\\": {\\n            \\\"value\\\": 0.6917410884665293,\\n            \\\"ci_95\\\": [\\n              0.6303734201016633,\\n              0.74057642792587\\n            ]\\n          },\\n          \\\"ECE\\\": {\\n            \\\"value\\\": 0.4530916055268938\\n          }\\n        },\\n        \\\"FK\\\": {\\n          \\\"rho\\\": {\\n            \\\"value\\\": 0.2665109373463269,\\n            \\\"ci_95\\\": [\\n              0.1742613109914005,\\n              0.3486237484303476\\n            ]\\n          },\\n          \\\"tau\\\": {\\n            \\\"value\\\": 0.19742423874169443\\n          },\\n          \\\"AUROC\\\": {\\n            \\\"value\\\": 0.6289977864285169,\\n            \\\"ci_95\\\": [\\n              0.5612201516175135,\\n              0.6882363040668321\\n            ]\\n          },\\n          \\\"ECE\\\": {\\n            \\\"value\\\": 0.4512460702104627\\n          }\\n        },\\n        \\\"logprob\\\": {\\n          \\\"rho\\\": {\\n            \\\"value\\\": 0.20517413101613924,\\n            \\\"ci_95\\\": [\\n              0.11711193891033023,\\n              0.29041687549583595\\n            ]\\n          },\\n          \\\"tau\\\": {\\n            \\\"value\\\": 0.14782758668777154\\n          },\\n          \\\"AUROC\\\": {\\n            \\\"value\\\": 0.578333714983589,\\n            \\\"ci_95\\\": [\\n              0.5179122379711025,\\n              0.6387157727851094\\n            ]\\n
…[truncated 7909 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-18T15:30:47.082440+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/analyze_exp012_rerun_5signal.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/analyze_exp012_rerun_5signal.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-18T15:30:47.082717+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"exp_012_rerun_1024: Full 5-signal metrics for NER + RE.\\\"\\\"\\\"\\n\\nimport json\\nimport sys\\nfrom collections import Counter\\n\\nimport numpy as np\\nfrom scipy.stats import spearmanr, kendalltau, rankdata\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import compute_all_consistency_scores\\nfrom evaluation import per_instance_f1\\n\\nDATA_PATH = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl\\\"\\nOUTPUT_PATH = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/all_signals_5signal.json\\\"\\nSUBTASKS = [\\\"ner\\\", \\\"re\\\"]\\n\\n\\ndef load_data(path):\\n    records = []\\n    with open(path) as f:\\n        for line in f:\\n            if line.strip():\\n                records.append(json.loads(line))\\n    return records\\n\\n\\ndef compute_exact_match_rate(samples, subtask):\\n    if subtask == \\\"ner\\\":\\n        keys = [frozenset((e[\\\"text\\\"], e[\\\"type\\\"]) for e in s.get(\\\"entities\\\", [])) for s in samples]\\n    else:\\n        keys = [frozenset((r[\\\"head\\\"], r[\\\"tail\\\"], r[\\\"type\\\"]) for r in s.get(\\\"relations\\\", [])) for s in samples]\\n    if not keys:\\n        return 0.0\\n    counter = Counter(keys)\\n    return counter.most_common(1)[0][1] / len(samples)\\n\\n\\ndef compute_voting_confidence(samples, subtask):\\n    N = len(samples)\\n    if N == 0:\\n        return 0.0\\n    counter = Counter()\\n    if subtask == \\\"ner\\\":\\n        for s in samples:\\n            for e in s.get(\\\"entities\\\", []):\\n                counter[(e[\\\"text\\\"], e[\\\"type\\\"])] += 1\\n    else:\\n        for s in samples:\\n            for r in s.get(\\\"relations\\\", []):\\n                counter[(r[\\\"head\\\"], r[\\\"tail\\\"], r[\\\"type\\\"])] += 1\\n    if not counter:\\n        return 0.0\\n    rates = [v / N for v in co
…[truncated 7141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-18T15:30:47.082915+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/samples.jsonl /root/autodl-tmp/struct_self_consist_ie/output/exp_026_T05/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/samples.jsonl /root/autodl-tmp/struct_self_consist_ie/output/exp_026_T05/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-18T15:30:47.083502+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     551 /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/samples.jsonl\\n     551 /root/autodl-tmp/struct_self_consist_ie/output/exp_026_T05/samples.jsonl\\n    1102 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-18T15:30:47.083673+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_026_T05/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_026_T05/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-18T15:30:47.084059+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"X96-1059_sent000\\\", \\\"text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\", \\\"start\\\": 15, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 0, \\\"head_end\\\": 27, \\\"tail_start\\\": 103, \\\"tail_end\\\": 125}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 15, \\\"head_end\\\": 27, \\\"tail_start\\\": 31, \\\"tail_end\\\": 44}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"USED-FOR\\\", \\\"head_start\\\": 103, \\\"head_end\\\": 125, \\\"tail_start\\\": 129, \\\"tail_end\\\": 153}], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis in Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\
…[truncated 9678 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-18T15:30:47.084346+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/autodl-tmp/struct_self_consist_ie/code/analyze_exp026_temp_5signal.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"5-signal analysis for exp-026 temperature ablation (parameterized).\"\"\"\n\nimport argparse\nimport json\nimport sys\nfrom collections import Counter\n\nimport numpy as np\nfrom scipy.stats import spearmanr, kendalltau, rankdata\n\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\nfrom consistency import compute_all_consistency_scores\nfrom evaluation import per_instance_f1\n\n\ndef load_data(path):\n    records = []\n    with open(path) as f:\n        for line in f:\n            if line.strip():\n                records.append(json.loads(line))\n    return records\n\n\ndef compute_exact_match_rate(samples, subtask):\n    if subtask == \"ner\":\n        keys = [frozenset((e[\"text\"], e[\"type\"]) for e in s.get(\"entities\", [])) for s in samples]\n    else:\n        keys = [frozenset((r[\"head\"], r[\"tail\"], r[\"type\"]) for r in s.get(\"relations\", [])) for s in samples]\n    if not keys:\n        return 0.0\n    counter = Counter(keys)\n    return counter.most_common(1)[0][1] / len(samples)\n\n\ndef compute_voting_confidence(samples, subtask):\n    N = len(samples)\n    if N == 0:\n        return 0.0\n    counter = Counter()\n    if subtask == \"ner\":\n        for s in samples:\n            for e in s.get(\"entities\", []):\n                counter[(e[\"text\"], e[\"type\"])] += 1\n    else:\n        for s in samples:\n            for r in s.get(\"relations\", []):\n                counter[(r[\"head\"], r[\"tail\"], r[\"type\"])] += 1\n    if not counter:\n        return 0.0\n    rates = [v / N for v in counter.values()]\n    return float(np.mean(rates))\n\n\ndef compute_mean_logprob(samples):\n    logprobs = [s.get(\"mean_logprob\") for s in samples if s.get(\"mean_logprob\") is not None]\n    logprobs = [lp for lp in logprobs if np.isfinite(lp)]\n    if not logprobs:\n        return float(\"nan\")\n    return float(np.mean(logprobs))\n\n\ndef safe_auroc(scores, labels):\n    scores = np.asarray(scores, dtype=float)\n    labels = np.asarray(labels, dtype=int)\n    if len(np.unique(labels)) < 2:\n        return float(\"nan\")\n    n_pos = np.sum(labels == 1)\n    n_neg = np.sum(labels == 0)\n    if n_pos == 0 or n_neg == 0:\n        return float(\"nan\")\n    ranks = rankdata(scores)\n    u = ranks[labels == 1].sum() - n_pos * (n_pos + 1) / 2\n    return float(u / (n_pos * n_neg))\n\n\ndef safe_spearman(x, y):\n    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)\n    mask = np.isfinite(x) & np.isfinite(y)\n    x, y = x[mask], y[mask]\n    if len(x) < 3:\n        return float(\"nan\")\n    return float(spearmanr(x, y).statistic)\n\n\ndef safe_kendall(x, y):\n    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)\n    mask = np.isfinite(x) & np.isfinite(y)\n    x, y = x[mask], y[mask]\n    if len(x) < 3:\n        return float(\"nan\")\n    return float(kendalltau(x, y).statistic)\n\n\ndef normalize_for_ece(signal_name, values):\n    v = np.asarray(values, dtype=float)\n    if signal_name in (\"SJ\", \"EM\", \"voting_conf\"):\n        return np.clip(v, 0, 1)\n    elif signal_name == \"FK\":\n        return np.clip((v + 1) / 2, 0, 1)\n    elif signal_name == \"logprob\":\n        return np.clip(np.exp(v), 0, 1)\n    return v\n\n\ndef compute_ece(confidences, correctness, n_bins=10):\n    conf = np.asarray(confidences, dtype=float)\n    corr = np.asarray(correctness, dtype=float)\n    mask = np.isfinite(conf)\n    conf, corr = conf[mask], corr[mask]\n    if len(conf) == 0:\n        return float(\"nan\")\n    bin_edges = np.linspace(0, 1, n_bins + 1)\n    ece = 0.0\n    total = len(conf)\n    for i in range(n_bins):\n        lo, hi = bin_edges[i], bin_edges[i + 1]\n        in_bin = (conf >= lo) & (conf <= hi if i == n_bins - 1 else conf < hi)\n        if in_bin.sum() == 0:\n            continue\n        bin_conf = conf[in_bin].mean()\n        bin_acc = corr[in_bin].mean()\n        ece += in_bin.sum() / total * abs(bin_acc - bin_conf)\n    return float(ece)\n\n\ndef bootstrap_metric(metric_fn, x, y, n_boot=1000, seed=42):\n    rng = np.random.RandomState(seed)\n    n = len(x)\n    boot_vals = []\n    for _ in range(n_boot):\n        idx = rng.choice(n, n, replace=True)\n        val = metric_fn(x[idx], y[idx])\n        if np.isfinite(val):\n            boot_vals.append(val)\n    if not boot_vals:\n        return [float(\"nan\"), float(\"nan\")]\n    return [float(np.percentile(boot_vals, 2.5)), float(np.percentile(boot_vals, 97.5))]\n\n\ndef compute_degeneracy(data, n_samples=8):\n    degenerate = 0\n    total = 0\n    for inst in data:\n        samples = inst.get(\"samples\", [])[:n_samples]\n        if len(samples) < n_samples:\n            continue\n        gold_entities = inst[\"gold\"].get(\"entities\", [])\n        if len(gold_entities) == 0:\n            continue\n        total += 1\n        keys = [frozenset((e[\"text\"], e[\"type\"]) for e in s.get(\"entities\", [])) for s in samples]\n        if len(set(keys)) == 1:\n            degenerate += 1\n    return degenerate / total if total else 0.0, degenerate, total\n\n\ndef compute_lp_range(data, n_samples=8):\n    ranges = []\n    for inst in data:\n        samples = inst.get(\"samples\", [])[:n_samples]\n        if len(samples) < n_samples:\n            continue\n        lps = [s[\"mean_logprob\"] for s in samples if \"mean_logprob\" in s]\n        if len(lps) >= 2:\n            ranges.append(max(lps) - min(lps))\n    return float(np.mean(ranges)), float(np.std(ranges)), len(ranges)\n\n\ndef evaluate_subtask(instances, subtask):\n    if subtask == \"ner\":\n        valid = [inst for inst in instances if len(inst[\"gold\"].get(\"entities\", [])) > 0]\n    else:\n        valid = [inst for inst in instances if len(inst[\"gold\"].get(\"relations\", [])) > 0]\n    print(f\"\\n=== {subtask.upper()} === Valid: {len(valid)}\")\n\n    greedy_f1s_all = []\n    for inst in valid:\n        greedy = inst.get(\"greedy\", inst[\"samples\"][0])\n        greedy_f1s_all.append(per_instance_f1(greedy, inst[\"gold\"], subtask=subtask))\n    conditional = [inst for inst, f1 in zip(valid, greedy_f1s_all) if f1 > 0]\n    print(f\"Conditional (greedy F1 > 0): {len(conditional)}\")\n\n    results = {}\n    for split_name, split_instances in [(\"full\", valid), (\"conditional\", conditional)]:\n        print(f\"\\n--- {split_name} ({len(split_instances)} instances) ---\")\n        consistency = compute_all_consistency_scores(split_instances, subtask=subtask)\n        sj_vals = consistency[\"soft_jaccard\"]\n        fk_vals = consistency[\"fleiss_kappa\"]\n\n        lp_vals, em_vals, vc_vals, f1_vals = [], [], [], []\n        for inst in split_instances:\n            samples = inst[\"samples\"]\n            gold = inst[\"gold\"]\n            greedy = inst.get(\"greedy\", samples[0])\n            lp_vals.append(compute_mean_logprob(samples))\n            em_vals.append(compute_exact_match_rate(samples, subtask))\n            vc_vals.append(compute_voting_confidence(samples, subtask))\n            f1_vals.append(per_instance_f1(greedy, gold, subtask=subtask))\n\n        signals = {\n            \"SJ\": np.array(sj_vals, dtype=float),\n            \"FK\": np.array(fk_vals, dtype=float),\n            \"logprob\": np.array(lp_vals, dtype=float),\n            \"EM\": np.array(em_vals, dtype=float),\n            \"voting_conf\": np.array(vc_vals, dtype=float),\n        }\n        f1_arr = np.array(f1_vals, dtype=float)\n        binary_correct = (f1_arr >= 1.0).astype(int)\n\n        split_results = {\"n\": len(split_instances), \"pct_perfect\": float(binary_correct.mean())}\n        metrics = {}\n        for sig_name, sig_vals in signals.items():\n            m = {}\n            rho = safe_spearman(sig_vals, f1_arr)\n            rho_ci = bootstrap_metric(safe_spearman, sig_vals, f1_arr)\n            m[\"rho\"] = {\"value\": rho, \"ci_95\": rho_ci}\n\n            tau = safe_kendall(sig_vals, f1_arr)\n            m[\"tau\"] = {\"value\": tau}\n\n            auroc = safe_auroc(sig_vals, binary_correct)\n            auroc_ci = bootstrap_metric(safe_auroc, sig_vals, binary_correct.astype(float))\n            m[\"AUROC\"] = {\"value\": auroc, \"ci_95\": auroc_ci}\n\n            ece_conf = normalize_for_ece(sig_name, sig_vals)\n            m[\"ECE\"] = {\"value\": compute_ece(ece_conf, binary_correct)}\n\n            metrics[sig_name] = m\n            print(f\"  {sig_name:>12}: rho={rho:.4f}  tau={tau:.4f}  AUROC={auroc:.4f}  ECE={m['ECE']['value']:.4f}\")\n\n        split_results[\"metrics\"] = metrics\n        results[split_name] = split_results\n\n    return results\n\n\ndef json_default(obj):\n    if isinstance(obj, (np.floating, np.float64, np.float32)):\n        return float(obj)\n    if isinstance(obj, (np.integer, np.int64, np.int32)):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    return str(obj)\n\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--data_path\", required=True)\n    parser.add_argument(\"--output_dir\", required=True)\n    parser.add_argument(\"--subtasks\", default=\"ner,re\", help=\"Comma-separated subtasks\")\n    args = parser.parse_args()\n\n    subtasks = [s.strip() for s in args.subtasks.split(\",\")]\n    instances = load_data(args.data_path)\n    print(f\"Loaded {len(instances)} instances, N={len(instances[0]['samples'])}\")\n\n    # Degeneracy and LP range\n    deg_rate, deg_count, deg_total = compute_degeneracy(instances)\n    lp_mean, lp_std, lp_n = compute_lp_range(instances)\n    print(f\"\\nDegeneracy rate: {deg_rate:.4f} ({deg_count}/{deg_total})\")\n    print(f\"LP range: mean={lp_mean:.6f}, std={lp_std:.6f}, n={lp_n}\")\n\n    # 5-signal per subtask\n    all_results = {}\n    for subtask in subtasks:\n        all_results[subtask] = evaluate_subtask(instances, subtask)\n\n    all_results[\"degeneracy\"] = {\"rate\": deg_rate, \"count\": deg_count, \"total\": deg_total}\n    all_results[\"lp_range\"] = {\"mean\": lp_mean, \"std\": lp_std, \"n\": lp_n}\n\n    import os\n    os.makedirs(args.output_dir, exist_ok=True)\n    out_path = os.path.join(args.output_dir, \"all_signals_5signal.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(all_results, f, indent=2, default=json_default)\n    print(f\"\\nSaved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/autodl-tmp/struct_self_consist_ie/code/analyze_exp026_temp_5signal.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"5-signal analysis for exp-026 temperature ablation (parameterized).\"\"\"\n\nimport argparse\nimport json\nimport sys\nfrom collections import Counter\n\nimport numpy as np\nfrom scipy.stats import spearmanr, kendalltau, rankdata\n\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\nfrom consistency import compute_all_consistency_scores\nfrom evaluation import per_instance_f1\n\n\ndef load_data(path):\n    records = []\n    with open(path) as f:\n        for line in f:\n            if line.strip():\n                records.append(json.loads(line))\n    return records\n\n\ndef compute_exact_match_rate(samples, subtask):\n    if subtask == \"ner\":\n        keys = [frozenset((e[\"text\"], e[\"type\"]) for e in s.get(\"entities\", [])) for s in samples]\n    else:\n        keys = [frozenset((r[\"head\"], r[\"tail\"], r[\"type\"]) for r in s.get(\"relations\", [])) for s in samples]\n    if not keys:\n        return 0.0\n    counter = Counter(keys)\n    return counter.most_common(1)[0][1] / len(samples)\n\n\ndef compute_voting_confidence(samples, subtask):\n    N = len(samples)\n    if N == 0:\n        return 0.0\n    counter = Counter()\n    if subtask == \"ner\":\n        for s in samples:\n            for e in s.get(\"entities\", []):\n                counter[(e[\"text\"], e[\"type\"])] += 1\n    else:\n        for s in samples:\n            for r in s.get(\"relations\", []):\n                counter[(r[\"head\"], r[\"tail\"], r[\"type\"])] += 1\n    if not counter:\n        return 0.0\n    rates = [v / N for v in counter.values()]\n    return float(np.mean(rates))\n\n\ndef compute_mean_logprob(samples):\n    logprobs = [s.get(\"mean_logprob\") for s in samples if s.get(\"mean_logprob\") is not None]\n    logprobs = [lp for lp in logprobs if np.isfinite(lp)]\n    if not logprobs:\n        return float(\"nan\")\n    return float(np.mean(logprobs))\n\n\ndef safe_auroc(scores, labels):\n    scores = np.asarray(scores, dtype=float)\n    labels = np.asarray(labels, dtype=int)\n    if len(np.unique(labels)) < 2:\n        return float(\"nan\")\n    n_pos = np.sum(labels == 1)\n    n_neg = np.sum(labels == 0)\n    if n_pos == 0 or n_neg == 0:\n        return float(\"nan\")\n    ranks = rankdata(scores)\n    u = ranks[labels == 1].sum() - n_pos * (n_pos + 1) / 2\n    return float(u / (n_pos * n_neg))\n\n\ndef safe_spearman(x, y):\n    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)\n    mask = np.isfinite(x) & np.isfinite(y)\n    x, y = x[mask], y[mask]\n    if len(x) < 3:\n        return float(\"nan\")\n    return float(spearmanr(x, y).statistic)\n\n\ndef safe_kendall(x, y):\n    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)\n    mask = np.isfinite(x) & np.isfinite(y)\n    x, y = x[mask], y[mask]\n    if len(x) < 3:\n        return float(\"nan\")\n    return float(kendalltau(x, y).statistic)\n\n\ndef normalize_for_ece(signal_name, values):\n    v = np.asarray(values, dtype=float)\n    if signal_name in (\"SJ\", \"EM\", \"voting_conf\"):\n        return np.clip(v, 0, 1)\n    elif signal_name == \"FK\":\n        return np.clip((v + 1) / 2, 0, 1)\n    elif signal_name == \"logprob\":\n        return np.clip(np.exp(v), 0, 1)\n    return v\n\n\ndef compute_ece(confidences, correctness, n_bins=10):\n    conf = np.asarray(confidences, dtype=float)\n    corr = np.asarray(correctness, dtype=float)\n    mask = np.isfinite(conf)\n    conf, corr = conf[mask], corr[mask]\n    if len(conf) == 0:\n        return float(\"nan\")\n    bin_edges = np.linspace(0, 1, n_bins + 1)\n    ece = 0.0\n    total = len(conf)\n    for i in range(n_bins):\n        lo, hi = bin_edges[i], bin_edges[i + 1]\n        in_bin = (conf >= lo) & (conf <= hi if i == n_bins - 1 else conf < hi)\n        if in_bin.sum() == 0:\n            continue\n        bin_conf = conf[in_bin].mean()\n        bin_acc = corr[in_bin].mean()\n        ece += in_bin.sum() / total * abs(bin_acc - bin_conf)\n    return float(ece)\n\n\ndef bootstrap_metric(metric_fn, x, y, n_boot=1000, seed=42):\n    rng = np.random.RandomState(seed)\n    n = len(x)\n    boot_vals = []\n    for _ in range(n_boot):\n        idx = rng.choice(n, n, replace=True)\n        val = metric_fn(x[idx], y[idx])\n        if np.isfinite(val):\n            boot_vals.append(val)\n    if not boot_vals:\n        return [float(\"nan\"), float(\"nan\")]\n    return [float(np.percentile(boot_vals, 2.5)), float(np.percentile(boot_vals, 97.5))]\n\n\ndef compute_degeneracy(data, n_samples=8):\n    degenerate = 0\n    total = 0\n    for inst in data:\n        samples = inst.get(\"samples\", [])[:n_samples]\n        if len(samples) < n_samples:\n            continue\n        gold_entities = inst[\"gold\"].get(\"entities\", [])\n        if len(gold_entities) == 0:\n            continue\n        total += 1\n        keys = [frozenset((e[\"text\"], e[\"type\"]) for e in s.get(\"entities\", [])) for s in samples]\n        if len(set(keys)) == 1:\n            degenerate += 1\n    return degenerate / total if total else 0.0, degenerate, total\n\n\ndef compute_lp_range(data, n_samples=8):\n    ranges = []\n    for inst in data:\n        samples = inst.get(\"samples\", [])[:n_samples]\n        if len(samples) < n_samples:\n            continue\n        lps = [s[\"mean_logprob\"] for s in samples if \"mean_logprob\" in s]\n        if len(lps) >= 2:\n            ranges.append(max(lps) - min(lps))\n    return float(np.mean(ranges)), float(np.std(ranges)), len(ranges)\n\n\ndef evaluate_subtask(instances, subtask):\n    if subtask == \"ner\":\n        valid = [inst for inst in instances if len(inst[\"gold\"].get(\"entities\", [])) > 0]\n    else:\n        valid = [inst for inst in instances if len(inst[\"gold\"].get(\"relations\", [])) > 0]\n    print(f\"\\n=== {subtask.upper()} === Valid: {len(valid)}\")\n\n    greedy_f1s_all = []\n    for inst in valid:\n        greedy = inst.get(\"greedy\", inst[\"samples\"][0])\n        greedy_f1s_all.append(per_instance_f1(greedy, inst[\"gold\"], subtask=subtask))\n    conditional = [inst for inst, f1 in zip(valid, greedy_f1s_all) if f1 > 0]\n    print(f\"Conditional (greedy F1 > 0): {len(conditional)}\")\n\n    results = {}\n    for split_name, split_instances in [(\"full\", valid), (\"conditional\", conditional)]:\n        print(f\"\\n--- {split_name} ({len(split_instances)} instances) ---\")\n        consistency = compute_all_consistency_scores(split_instances, subtask=subtask)\n        sj_vals = consistency[\"soft_jaccard\"]\n        fk_vals = consistency[\"fleiss_kappa\"]\n\n        lp_vals, em_vals, vc_vals, f1_vals = [], [], [], []\n        for inst in split_instances:\n            samples = inst[\"samples\"]\n            gold = inst[\"gold\"]\n            greedy = inst.get(\"greedy\", samples[0])\n            lp_vals.append(compute_mean_logprob(samples))\n            em_vals.append(compute_exact_match_rate(samples, subtask))\n            vc_vals.append(compute_voting_confidence(samples, subtask))\n            f1_vals.append(per_instance_f1(greedy, gold, subtask=subtask))\n\n        signals = {\n            \"SJ\": np.array(sj_vals, dtype=float),\n            \"FK\": np.array(fk_vals, dtype=float),\n            \"logprob\": np.array(lp_vals, dtype=float),\n            \"EM\": np.array(em_vals, dtype=float),\n            \"voting_conf\": np.array(vc_vals, dtype=float),\n        }\n        f1_arr = np.array(f1_vals, dtype=float)\n        binary_correct = (f1_arr >= 1.0).astype(int)\n\n        split_results = {\"n\": len(split_instances), \"pct_perfect\": float(binary_correct.mean())}\n        metrics = {}\n        for sig_name, sig_vals in signals.items():\n            m = {}\n            rho = safe_spearman(sig_vals, f1_arr)\n            rho_ci = bootstrap_metric(safe_spearman, sig_vals, f1_arr)\n            m[\"rho\"] = {\"value\": rho, \"ci_95\": rho_ci}\n\n            tau = safe_kendall(sig_vals, f1_arr)\n            m[\"tau\"] = {\"value\": tau}\n\n            auroc = safe_auroc(sig_vals, binary_correct)\n            auroc_ci = bootstrap_metric(safe_auroc, sig_vals, binary_correct.astype(float))\n            m[\"AUROC\"] = {\"value\": auroc, \"ci_95\": auroc_ci}\n\n            ece_conf = normalize_for_ece(sig_name, sig_vals)\n            m[\"ECE\"] = {\"value\": compute_ece(ece_conf, binary_correct)}\n\n            metrics[sig_name] = m\n            print(f\"  {sig_name:>12}: rho={rho:.4f}  tau={tau:.4f}  AUROC={auroc:.4f}  ECE={m['ECE']['value']:.4f}\")\n\n        split_results[\"metrics\"] = metrics\n        results[split_name] = split_results\n\n    return results\n\n\ndef json_default(obj):\n    if isinstance(obj, (np.floating, np.float64, np.float32)):\n        return float(obj)\n    if isinstance(obj, (np.integer, np.int64, np.int32)):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    return str(obj)\n\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--data_path\", required=True)\n    parser.add_argument(\"--output_dir\", required=True)\n    parser.add_argument(\"--subtasks\", default=\"ner,re\", help=\"Comma-separated subtasks\")\n    args = parser.parse_args()\n\n    subtasks = [s.strip() for s in args.subtasks.split(\",\")]\n    instances = load_data(args.data_path)\n    print(f\"Loaded {len(instances)} instances, N={len(instances[0]['samples'])}\")\n\n    # Degeneracy and LP range\n    deg_rate, deg_count, deg_total = compute_degeneracy(instances)\n    lp_mean, lp_std, lp_n = compute_lp_range(instances)\n    print(f\"\\nDegeneracy rate: {deg_rate:.4f} ({deg_count}/{deg_total})\")\n    print(f\"LP range: mean={lp_mean:.6f}, std={lp_std:.6f}, n={lp_n}\")\n\n    # 5-signal per subtask\n    all_results = {}\n    for subtask in subtasks:\n        all_results[subtask] = evaluate_subtask(instances, subtask)\n\n    all_results[\"degeneracy\"] = {\"rate\": deg_rate, \"count\": deg_count, \"total\": deg_total}\n    all_results[\"lp_range\"] = {\"mean\": lp_mean, \"std\": lp_std, \"n\": lp_n}\n\n    import os\n    os.makedirs(args.output_dir, exist_ok=True)\n    out_path = os.path.join(args.output_dir, \"all_signals_5signal.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(all_results, f, indent=2, default=json_default)\n    print(f\"\\nSaved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-18T15:30:47.084581+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-18T15:30:47.084732+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t05_scierc",
  "field": "hypothesis",
  "value": "Lower temperature (T=0.5) increases degeneracy rate and reduces LP range on SciERC NER, as reduced sampling diversity causes more identical outputs",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t05_scierc",
    "field": "hypothesis",
    "value": "Lower temperature (T=0.5) increases degeneracy rate and reduces LP range on SciERC NER, as reduced sampling diversity causes more identical outputs",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-18T15:30:47.084869+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_026_t05_scierc\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:34.135Z\", \"updated_at\": \"2026-05-18T15:28:34.135Z\", \"hypothesis\": \"Lower temperature (T=0.5) increases degeneracy rate and reduces LP range on SciERC NER, as reduced sampling diversity causes more identical outputs\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6139}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-18T15:30:47.084999+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t08_scierc",
  "field": "hypothesis",
  "value": "Moderate temperature (T=0.8) provides intermediate degeneracy/LP-range tradeoff on SciERC NER, testing sensitivity of structural signals to temperature",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t08_scierc",
    "field": "hypothesis",
    "value": "Moderate temperature (T=0.8) provides intermediate degeneracy/LP-range tradeoff on SciERC NER, testing sensitivity of structural signals to temperature",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-18T15:30:47.085193+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_026_t08_scierc\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.084Z\", \"updated_at\": \"2026-05-18T15:28:36.084Z\", \"hypothesis\": \"Moderate temperature (T=0.8) provides intermediate degeneracy/LP-range tradeoff on SciERC NER, testing sensitivity of structural signals to temperature\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6361}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-18T15:30:47.085322+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t12_scierc",
  "field": "hypothesis",
  "value": "Higher temperature (T=1.2) reduces degeneracy rate and increases LP range on SciERC NER, but may degrade absolute generation quality",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t12_scierc",
    "field": "hypothesis",
    "value": "Higher temperature (T=1.2) reduces degeneracy rate and increases LP range on SciERC NER, but may degrade absolute generation quality",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-18T15:30:47.085449+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_026_t12_scierc\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.812Z\", \"updated_at\": \"2026-05-18T15:28:36.812Z\", \"hypothesis\": \"Higher temperature (T=1.2) reduces degeneracy rate and increases LP range on SciERC NER, but may degrade absolute generation quality\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6445}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-18T15:30:47.085606+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "autodl-5090",
  "gpu_ids": "['cuda:0']",
  "command": "bash -c \"cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/ --subtasks ner,re\"",
  "exp_id": "exp_026_t05_scierc",
  "timeout_hours": "3",
  "account": "root",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "autodl-5090",
    "gpu_ids": "['cuda:0']",
    "command": "bash -c \"cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/ --subtasks ner,re\"",
    "exp_id": "exp_026_t05_scierc",
    "timeout_hours": "3",
    "account": "root",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-18T15:30:47.085739+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "autodl-5090",
  "gpu_ids": "['cuda:2']",
  "command": "bash -c \"cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/ --subtasks ner,re\"",
  "exp_id": "exp_026_t08_scierc",
  "timeout_hours": "3",
  "account": "root",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "autodl-5090",
    "gpu_ids": "['cuda:2']",
    "command": "bash -c \"cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/ --subtasks ner,re\"",
    "exp_id": "exp_026_t08_scierc",
    "timeout_hours": "3",
    "account": "root",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-18T15:30:47.085873+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "autodl-5090",
  "gpu_ids": "['cuda:3']",
  "command": "bash -c \"cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/ --subtasks ner,re\"",
  "exp_id": "exp_026_t12_scierc",
  "timeout_hours": "3",
  "account": "root",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "autodl-5090",
    "gpu_ids": "['cuda:3']",
    "command": "bash -c \"cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/ --subtasks ner,re\"",
    "exp_id": "exp_026_t12_scierc",
    "timeout_hours": "3",
    "account": "root",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-18T15:30:47.086005+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"665248\", \"log_file\": \"~/runs/struct_self_consist_ie/exp_026_t05_scierc.log\", \"gpu_ids\": [\"cuda:0\"], \"server\": \"autodl-5090\", \"account\": \"root\", \"cuda_visible_devices\": \"0\", \"backend\": \"tmux\", \"tmux_session\": \"exp_026_t05_scierc\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.63}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-18T15:30:47.086148+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"665386\", \"log_file\": \"~/runs/struct_self_consist_ie/exp_026_t08_scierc.log\", \"gpu_ids\": [\"cuda:2\"], \"server\": \"autodl-5090\", \"account\": \"root\", \"cuda_visible_devices\": \"2\", \"backend\": \"tmux\", \"tmux_session\": \"exp_026_t08_scierc\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.62}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-18T15:30:47.086277+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"665522\", \"log_file\": \"~/runs/struct_self_consist_ie/exp_026_t12_scierc.log\", \"gpu_ids\": [\"cuda:3\"], \"server\": \"autodl-5090\", \"account\": \"root\", \"cuda_visible_devices\": \"3\", \"backend\": \"tmux\", \"tmux_session\": \"exp_026_t12_scierc\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.57}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-18T15:30:47.086410+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -5 /root/runs/struct_self_consist_ie/exp_026_t05_scierc.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -5 /root/runs/struct_self_consist_ie/exp_026_t05_scierc.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-18T15:30:47.086532+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-18T15:30:47.086648+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -5 /root/runs/struct_self_consist_ie/exp_026_t08_scierc.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -5 /root/runs/struct_self_consist_ie/exp_026_t08_scierc.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-18T15:30:47.086764+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-18T15:30:47.086883+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -5 /root/runs/struct_self_consist_ie/exp_026_t12_scierc.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -5 /root/runs/struct_self_consist_ie/exp_026_t12_scierc.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-18T15:30:47.087001+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-18T15:30:47.087159+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -20 /root/runs/struct_self_consist_ie/exp_026_t05_scierc.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -20 /root/runs/struct_self_consist_ie/exp_026_t05_scierc.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-18T15:30:47.087300+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n=== RE === Valid: 397\\nConditional (greedy F1 > 0): 240\\n\\n--- full (397 instances) ---\\n            SJ: rho=0.1823  tau=0.1443  AUROC=0.6227  ECE=0.5667\\n            FK: rho=0.1315  tau=0.1064  AUROC=0.5943  ECE=0.5448\\n       logprob: rho=0.2764  tau=0.2042  AUROC=0.5781  ECE=0.7819\\n            EM: rho=0.1045  tau=0.0831  AUROC=0.6435  ECE=0.5167\\n   voting_conf: rho=0.2824  tau=0.2185  AUROC=0.6533  ECE=0.4352\\n\\n--- conditional (240 instances) ---\\n            SJ: rho=0.2473  tau=0.1825  AUROC=0.6212  ECE=0.4730\\n            FK: rho=0.1901  tau=0.1422  AUROC=0.5975  ECE=0.4419\\n       logprob: rho=0.0027  tau=0.0035  AUROC=0.4891  ECE=0.6600\\n            EM: rho=0.3511  tau=0.2702  AUROC=0.6806  ECE=0.3854\\n   voting_conf: rho=0.2595  tau=0.1907  AUROC=0.6189  ECE=0.3622\\n\\nSaved to output/exp_026_t05/all_signals_5signal.json\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-18T15:30:47.087425+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -20 /root/runs/struct_self_consist_ie/exp_026_t08_scierc.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -20 /root/runs/struct_self_consist_ie/exp_026_t08_scierc.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-18T15:30:47.087553+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n=== RE === Valid: 397\\nConditional (greedy F1 > 0): 238\\n\\n--- full (397 instances) ---\\n            SJ: rho=0.2740  tau=0.2091  AUROC=0.6791  ECE=0.4450\\n            FK: rho=0.1955  tau=0.1578  AUROC=0.5758  ECE=0.4742\\n       logprob: rho=0.3300  tau=0.2425  AUROC=0.6178  ECE=0.7750\\n            EM: rho=0.2000  tau=0.1564  AUROC=0.7282  ECE=0.4166\\n   voting_conf: rho=0.4047  tau=0.3139  AUROC=0.7396  ECE=0.3295\\n\\n--- conditional (238 instances) ---\\n            SJ: rho=0.3294  tau=0.2415  AUROC=0.6618  ECE=0.3587\\n            FK: rho=0.1348  tau=0.1052  AUROC=0.5497  ECE=0.3993\\n       logprob: rho=0.0557  tau=0.0386  AUROC=0.5198  ECE=0.6515\\n            EM: rho=0.4393  tau=0.3381  AUROC=0.7561  ECE=0.2973\\n   voting_conf: rho=0.4055  tau=0.3014  AUROC=0.7050  ECE=0.2679\\n\\nSaved to output/exp_026_t08/all_signals_5signal.json\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-18T15:30:47.087696+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -20 /root/runs/struct_self_consist_ie/exp_026_t12_scierc.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -20 /root/runs/struct_self_consist_ie/exp_026_t12_scierc.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-18T15:30:47.087832+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n=== RE === Valid: 397\\nConditional (greedy F1 > 0): 237\\n\\n--- full (397 instances) ---\\n            SJ: rho=0.2622  tau=0.1974  AUROC=0.6764  ECE=0.3433\\n            FK: rho=0.3450  tau=0.2755  AUROC=0.6232  ECE=0.4245\\n       logprob: rho=0.2939  tau=0.2148  AUROC=0.5848  ECE=0.7662\\n            EM: rho=0.1226  tau=0.0946  AUROC=0.7313  ECE=0.3202\\n   voting_conf: rho=0.3973  tau=0.3044  AUROC=0.7431  ECE=0.2390\\n\\n--- conditional (237 instances) ---\\n            SJ: rho=0.2972  tau=0.2161  AUROC=0.6595  ECE=0.2532\\n            FK: rho=0.1899  tau=0.1495  AUROC=0.5720  ECE=0.3489\\n       logprob: rho=-0.0088  tau=-0.0051  AUROC=0.4853  ECE=0.6463\\n            EM: rho=0.5071  tau=0.3901  AUROC=0.7926  ECE=0.1809\\n   voting_conf: rho=0.3585  tau=0.2639  AUROC=0.7040  ECE=0.1717\\n\\nSaved to output/exp_026_t12/all_signals_5signal.json\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-18T15:30:47.087977+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t05_scierc",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/ --subtasks ner,re', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t05/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t05_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t05_scierc",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/ --subtasks ner,re', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t05/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t05_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-18T15:30:47.088114+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.416}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-18T15:30:47.088477+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t08_scierc",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/ --subtasks ner,re', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t08/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t08_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t08_scierc",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/ --subtasks ner,re', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t08/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t08_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-18T15:30:47.088704+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.4486}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-18T15:30:47.088877+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t12_scierc",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/ --subtasks ner,re', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t12/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t12_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t12_scierc",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/ --subtasks ner,re', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t12/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t12_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-18T15:30:47.089099+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.4124}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-18T15:30:47.089377+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t05_scierc",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/ --subtasks ner,re', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t05/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t05_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t05_scierc",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/ --subtasks ner,re', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t05/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t05_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-18T15:30:47.089547+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3687}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-18T15:30:47.089700+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t08_scierc",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/ --subtasks ner,re', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t08/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t08_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t08_scierc",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/ --subtasks ner,re', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t08/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t08_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-18T15:30:47.089861+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3749}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-18T15:30:47.090007+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t12_scierc",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/ --subtasks ner,re', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t12/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t12_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t12_scierc",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/ --subtasks ner,re', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t12/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t12_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-18T15:30:47.090183+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3799}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-18T15:30:47.090321+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t05_scierc",
  "field": "status",
  "value": "PENDING",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t05_scierc",
    "field": "status",
    "value": "PENDING",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-18T15:30:47.090461+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t08_scierc",
  "field": "status",
  "value": "PENDING",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t08_scierc",
    "field": "status",
    "value": "PENDING",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-18T15:30:47.090586+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t12_scierc",
  "field": "status",
  "value": "PENDING",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t12_scierc",
    "field": "status",
    "value": "PENDING",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-18T15:30:47.090726+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_026_t05_scierc\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:34.135Z\", \"updated_at\": \"2026-05-18T15:29:39.157Z\", \"hypothesis\": \"Lower temperature (T=0.5) increases degeneracy rate and reduces LP range on SciERC NER, as reduced sampling diversity causes more identical outputs\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/ --subtasks ner,re\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"665248\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t05_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:53.787Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.6616}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-18T15:30:47.090877+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_026_t08_scierc\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.084Z\", \"updated_at\": \"2026-05-18T15:29:40.820Z\", \"hypothesis\": \"Moderate temperature (T=0.8) provides intermediate degeneracy/LP-range tradeoff on SciERC NER, testing sensitivity of structural signals to temperature\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/ --subtasks ner,re\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"665386\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t08_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:55.394Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.6087}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-18T15:30:47.091287+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_026_t12_scierc\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.812Z\", \"updated_at\": \"2026-05-18T15:29:42.432Z\", \"hypothesis\": \"Higher temperature (T=1.2) reduces degeneracy rate and increases LP range on SciERC NER, but may degrade absolute generation quality\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/ --subtasks ner,re\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"665522\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t12_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:56.997Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.6018}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-18T15:30:47.091824+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t05_scierc",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t05/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t05_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t05_scierc",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t05/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t05_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
  }
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-18T15:30:47.092059+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3664}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-18T15:30:47.092244+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t08_scierc",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t08/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t08_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t08_scierc",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t08/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t08_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-18T15:30:47.092412+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3694}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-18T15:30:47.092591+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t12_scierc",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t12/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t12_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t12_scierc",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t12/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t12_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-18T15:30:47.092832+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.4253}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-18T15:30:47.092998+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t05_scierc",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t05/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t05_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t05_scierc",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t05/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t05_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-18T15:30:47.093234+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.418}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-18T15:30:47.093373+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t08_scierc",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t08/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t08_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t08_scierc",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t08/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t08_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-18T15:30:47.093521+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.3987}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-18T15:30:47.093649+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t12_scierc",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t12/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t12_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t12_scierc",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t12/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t12_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-18T15:30:47.093791+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.3853}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-18T15:30:47.093987+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t05_scierc",
  "field": "conclusion",
  "value": "T=0.5 shows highest degeneracy among temps. NER: SJ rho=0.26, FK rho=0.23, LP rho=0.22, EM rho=0.29, VC rho=0.38. Structural signals weaker than T=1.0 baseline. RE: LP rho=0.28 but conditional LP near zero (0.003). Confirms hypothesis that lower temp reduces signal discriminability.",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t05_scierc",
    "field": "conclusion",
    "value": "T=0.5 shows highest degeneracy among temps. NER: SJ rho=0.26, FK rho=0.23, LP rho=0.22, EM rho=0.29, VC rho=0.38. Structural signals weaker than T=1.0 baseline. RE: LP rho=0.28 but conditional LP near zero (0.003). Confirms hypothesis that lower temp reduces signal discriminability.",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-18T15:30:47.094224+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'T=0.5 shows highest degeneracy among temps. NER: SJ rho=0.26, FK rho=0.23, LP rho=0.22, EM rho=0.29, VC rho=0.38. Structural signals weaker than T=1.0 baseline. RE: LP rho=0.28 but conditional LP near zero (0.003). Confirms hypothesis that lower temp reduces signal discriminability.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.3798}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-18T15:30:47.094429+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t08_scierc",
  "field": "conclusion",
  "value": "T=0.8 intermediate between T=0.5 and T=1.0. NER: SJ rho=0.36, FK rho=0.25, EM rho=0.29, VC rho=0.38. RE structural signals stronger than T=0.5 (SJ rho=0.27, VC rho=0.40, EM rho=0.44 conditional). Confirms intermediate tradeoff hypothesis.",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t08_scierc",
    "field": "conclusion",
    "value": "T=0.8 intermediate between T=0.5 and T=1.0. NER: SJ rho=0.36, FK rho=0.25, EM rho=0.29, VC rho=0.38. RE structural signals stronger than T=0.5 (SJ rho=0.27, VC rho=0.40, EM rho=0.44 conditional). Confirms intermediate tradeoff hypothesis.",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-18T15:30:47.094632+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'T=0.8 intermediate between T=0.5 and T=1.0. NER: SJ rho=0.36, FK rho=0.25, EM rho=0.29, VC rho=0.38. RE structural signals stronger than T=0.5 (SJ rho=0.27, VC rho=0.40, EM rho=0.44 conditional). Confirms intermediate tradeoff hypothesis.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.3758}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-18T15:30:47.094834+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t12_scierc",
  "field": "conclusion",
  "value": "T=1.2 shows strongest structural signal correlations. NER: SJ rho=0.38, FK rho=0.34, EM rho=0.34, VC rho=0.40. RE: EM conditional rho=0.51 (best across temps). LP degrades at high temp (conditional near zero). Higher diversity improves structural consistency signals at cost of LP utility.",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t12_scierc",
    "field": "conclusion",
    "value": "T=1.2 shows strongest structural signal correlations. NER: SJ rho=0.38, FK rho=0.34, EM rho=0.34, VC rho=0.40. RE: EM conditional rho=0.51 (best across temps). LP degrades at high temp (conditional near zero). Higher diversity improves structural consistency signals at cost of LP utility.",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-18T15:30:47.095040+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'T=1.2 shows strongest structural signal correlations. NER: SJ rho=0.38, FK rho=0.34, EM rho=0.34, VC rho=0.40. RE: EM conditional rho=0.51 (best across temps). LP degrades at high temp (conditional near zero). Higher diversity improves structural consistency signals at cost of LP utility.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.426}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-18T15:30:47.095258+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t05_scierc",
  "field": "conclusion",
  "value": "success",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t05_scierc",
    "field": "conclusion",
    "value": "success",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-18T15:30:47.095449+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t08_scierc",
  "field": "conclusion",
  "value": "success",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t08_scierc",
    "field": "conclusion",
    "value": "success",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-18T15:30:47.095663+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_026_t05_scierc\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:34.135Z\", \"updated_at\": \"2026-05-18T15:30:21.854Z\", \"hypothesis\": \"Lower temperature (T=0.5) increases degeneracy rate and reduces LP range on SciERC NER, as reduced sampling diversity causes more identical outputs\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/ --subtasks ner,re\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"665248\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t05_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:53.787Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6559}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-18T15:30:47.095868+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t12_scierc",
  "field": "conclusion",
  "value": "success",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t12_scierc",
    "field": "conclusion",
    "value": "success",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-18T15:30:47.096076+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_026_t08_scierc\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.084Z\", \"updated_at\": \"2026-05-18T15:30:22.527Z\", \"hypothesis\": \"Moderate temperature (T=0.8) provides intermediate degeneracy/LP-range tradeoff on SciERC NER, testing sensitivity of structural signals to temperature\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/ --subtasks ner,re\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"665386\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t08_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:55.394Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6638}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-18T15:30:47.096321+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_026_t12_scierc\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.812Z\", \"updated_at\": \"2026-05-18T15:30:23.205Z\", \"hypothesis\": \"Higher temperature (T=1.2) reduces degeneracy rate and increases LP range on SciERC NER, but may degrade absolute generation quality\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/ --subtasks ner,re\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"665522\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t12_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:56.997Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6463}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-18T15:30:47.096516+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t05_scierc",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t05/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t05_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t05_scierc",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t05/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t05_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
  }
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-18T15:30:47.096764+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_026_t05_scierc\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:34.135Z\", \"updated_at\": \"2026-05-18T15:30:28.965Z\", \"hypothesis\": \"Lower temperature (T=0.5) increases degeneracy rate and reduces LP range on SciERC NER, as reduced sampling diversity causes more identical outputs\", \"spec\": {\"command\": \"python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"665248\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t05_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:53.787Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/exp_026_t05/samples.jsonl\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"checkpoint_source\": \"ft_002_v2\", \"eval_data\": \"scierc_test_551\", \"wall_clock_seconds\": 95.2, \"gpu_hours\": 0.03}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:30:28.965Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.6445}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-18T15:30:47.096973+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t08_scierc",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t08/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t08_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t08_scierc",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t08/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t08_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
  }
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-18T15:30:47.097239+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_026_t08_scierc\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.084Z\", \"updated_at\": \"2026-05-18T15:30:31.219Z\", \"hypothesis\": \"Moderate temperature (T=0.8) provides intermediate degeneracy/LP-range tradeoff on SciERC NER, testing sensitivity of structural signals to temperature\", \"spec\": {\"command\": \"python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"665386\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t08_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:55.394Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/exp_026_t08/samples.jsonl\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"checkpoint_source\": \"ft_002_v2\", \"eval_data\": \"scierc_test_551\", \"wall_clock_seconds\": 95.8, \"gpu_hours\": 0.03}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:30:31.219Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.6168}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-18T15:30:47.097430+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_026_t12_scierc",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t12/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t12_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_026_t12_scierc",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t12/samples.jsonl', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 42, 'checkpoint_path': 'checkpoints/qwen3-8b-scierc-merged-v2', 'log_path': '~/runs/struct_self_consist_ie/exp_026_t12_scierc.log', 'checkpoint_source': 'ft_002_v2', 'eval_data': 'scierc_test_551'}"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-18T15:30:47.097609+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_026_t12_scierc\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.812Z\", \"updated_at\": \"2026-05-18T15:30:33.407Z\", \"hypothesis\": \"Higher temperature (T=1.2) reduces degeneracy rate and increases LP range on SciERC NER, but may degrade absolute generation quality\", \"spec\": {\"command\": \"python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"665522\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t12_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:56.997Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/exp_026_t12/samples.jsonl\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"checkpoint_source\": \"ft_002_v2\", \"eval_data\": \"scierc_test_551\", \"wall_clock_seconds\": 96.4, \"gpu_hours\": 0.03}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:30:33.407Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.6422}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 151 · 2026-05-18T15:30:47.097852+00:00_

3 个实验全部完成，registry 已更新为 DONE。

## 结果摘要

推理已有（`output/exp_026_t05/t08/t12/samples.jsonl`，每个 551 instances x N=8 + logprobs，模型 `qwen3-8b-scierc-merged-v2` = ft_002_v2）。5-signal 分析已跑完，输出到各目录的 `all_signals_5signal.json`。

**NER 5-signal（full split, rho）**

| Signal | T=0.5 | T=0.8 | T=1.2 |
|--------|-------|-------|-------|
| SJ | 0.26 | 0.36 | 0.38 |
| FK | 0.23 | 0.25 | 0.34 |
| LP | 0.22 | 0.25 | 0.20 |
| EM | 0.29 | 0.29 | 0.34 |
| VC | 0.38 | 0.38 | 0.40 |

**RE 5-signal（full split, rho）**

| Signal | T=0.5 | T=0.8 | T=1.2 |
|--------|-------|-------|-------|
| SJ | 0.18 | 0.27 | 0.26 |
| FK | 0.13 | 0.20 | 0.35 |
| LP | 0.28 | 0.33 | 0.29 |
| EM | 0.10 | 0.20 | 0.12 |
| VC | 0.28 | 0.40 | 0.40 |

趋势：结构信号（SJ, FK, EM）随温度升高而增强（更多样本多样性 → 更好的信号区分度），LP 信号相对稳定但 conditional 下高温退化。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_exp026_t_ablation_submit_20260518T152445"
}
```

</details>

---
