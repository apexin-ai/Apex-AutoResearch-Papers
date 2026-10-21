# analysis 23config regression

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/chats/worker_analysis_23config_regression_20260519T072221.jsonl`
- **Structured JSON:** [`7ddf361413a886e5cdb9.json`](../../sessions/7d/7ddf361413a886e5cdb9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

67 recorded events

### Tool call

_source line 1 · 2026-05-19T07:29:17.589417+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T07:29:17.589732+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T07:29:17.589900+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && find output/ artifacts/ -name \"*23*config*\" -o -name \"*decomposition*\" -o -name \"*regression*\" -o -name \"*figure3*\" -o -name \"*fig3*\" 2>/dev/null | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && find output/ artifacts/ -name \"*23*config*\" -o -name \"*decomposition*\" -o -name \"*regression*\" -o -name \"*figure3*\" -o -name \"*fig3*\" 2>/dev/null | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T07:29:17.590048+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"output/mvp_pilot_004/e1_component_decomposition.json\\noutput/unified_metrics_regression\\noutput/unified_metrics_regression/regression_report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T07:29:17.590235+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && cat output/unified_metrics_regression/regression_report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && cat output/unified_metrics_regression/regression_report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T07:29:17.590449+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"metadata\\\": {\\n    \\\"source\\\": \\\"unified_metrics (single truth source)\\\",\\n    \\\"gold_filter\\\": true,\\n    \\\"n_samples\\\": 8,\\n    \\\"n_bootstrap\\\": 10000,\\n    \\\"seed\\\": 42,\\n    \\\"f1_definition\\\": \\\"span-based (start, end, type) exact match micro-F1\\\",\\n    \\\"degeneracy_definition\\\": \\\"constant-F1 gold-filtered\\\"\\n  },\\n  \\\"datasets\\\": {\\n    \\\"SciERC\\\": {\\n      \\\"n_instances\\\": 529,\\n      \\\"n_degen\\\": 94,\\n      \\\"degen_pct\\\": 17.77,\\n      \\\"greedy\\\": {\\n        \\\"mean\\\": 0.6439219990259687,\\n        \\\"ci_lo\\\": 0.6180475688982305,\\n        \\\"ci_hi\\\": 0.6692473667898999\\n      },\\n      \\\"lp_all\\\": {\\n        \\\"mean\\\": 0.6500718843902431,\\n        \\\"ci_lo\\\": 0.6245690161179985,\\n        \\\"ci_hi\\\": 0.6749655320154598\\n      },\\n      \\\"dgs\\\": {\\n        \\\"mean\\\": 0.6513321238357378,\\n        \\\"ci_lo\\\": 0.6259400720731756,\\n        \\\"ci_hi\\\": 0.6760374227376341\\n      },\\n      \\\"oracle\\\": {\\n        \\\"mean\\\": 0.7758023559647044,\\n        \\\"ci_lo\\\": 0.7540692550589138,\\n        \\\"ci_hi\\\": 0.7968803038023543\\n      },\\n      \\\"delta_dgs_minus_greedy\\\": {\\n        \\\"delta\\\": 0.007410124809769103,\\n        \\\"ci_lo\\\": -0.006005775609912112,\\n        \\\"ci_hi\\\": 0.021087603106951347\\n      }\\n    },\\n    \\\"CoNLL\\\": {\\n      \\\"n_instances\\\": 2756,\\n      \\\"n_degen\\\": 1597,\\n      \\\"degen_pct\\\": 57.95,\\n      \\\"greedy\\\": {\\n        \\\"mean\\\": 0.9069619201150406,\\n        \\\"ci_lo\\\": 0.8976105091489706,\\n        \\\"ci_hi\\\": 0.9158281466155198\\n      },\\n      \\\"lp_all\\\": {\\n        \\\"mean\\\": 0.8988964753682902,\\n        \\\"ci_lo\\\": 0.8891507200010481,\\n        \\\"ci_hi\\\": 0.9082347494759536\\n      },\\n      \\\"dgs\\\": {\\n        \\\"mean\\\": 0.8988964753682902,\\n       
…[truncated 1575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T07:29:17.590634+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && cat output/mvp_pilot_004/e1_component_decomposition.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && cat output/mvp_pilot_004/e1_component_decomposition.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T07:29:17.590811+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"n_full\\\": 397,\\n  \\\"n_conditional\\\": 313,\\n  \\\"full\\\": {\\n    \\\"head_sj\\\": {\\n      \\\"rho\\\": 0.20963672137052117,\\n      \\\"p_value\\\": 2.54590861868317e-05,\\n      \\\"mean\\\": 0.6553448389570243\\n    },\\n    \\\"tail_sj\\\": {\\n      \\\"rho\\\": 0.20100368637123048,\\n      \\\"p_value\\\": 5.4932807005587235e-05,\\n      \\\"mean\\\": 0.6381347569871075\\n    },\\n    \\\"type_match\\\": {\\n      \\\"rho\\\": 0.20066238285813504,\\n      \\\"p_value\\\": 5.659135228562417e-05,\\n      \\\"mean\\\": 0.6706424497896251\\n    },\\n    \\\"multiplicative\\\": {\\n      \\\"rho\\\": 0.2440702831280834,\\n      \\\"p_value\\\": 8.550224511243979e-07,\\n      \\\"mean\\\": 0.5806075772493355\\n    },\\n    \\\"additive\\\": {\\n      \\\"rho\\\": 0.24296994832030042,\\n      \\\"p_value\\\": 9.608671577562469e-07,\\n      \\\"mean\\\": 0.6053451123428257\\n    },\\n    \\\"fleiss_kappa\\\": {\\n      \\\"rho\\\": 0.2782151188817765,\\n      \\\"p_value\\\": 1.7243205365720716e-08,\\n      \\\"mean\\\": 0.27323279256680094\\n    }\\n  },\\n  \\\"conditional\\\": {\\n    \\\"head_sj\\\": {\\n      \\\"rho\\\": 0.2700948820524552,\\n      \\\"p_value\\\": 1.2359812977339843e-06,\\n      \\\"mean\\\": 0.6591563594691062\\n    },\\n    \\\"tail_sj\\\": {\\n      \\\"rho\\\": 0.25851142783449954,\\n      \\\"p_value\\\": 3.582394378277026e-06,\\n      \\\"mean\\\": 0.6417942951859777\\n    },\\n    \\\"type_match\\\": {\\n      \\\"rho\\\": 0.25178655623399226,\\n      \\\"p_value\\\": 6.4950766741894395e-06,\\n      \\\"mean\\\": 0.6756402866113044\\n    },\\n    \\\"multiplicative\\\": {\\n      \\\"rho\\\": 0.31612432525905776,\\n      \\\"p_value\\\": 1.0795971808906936e-08,\\n      \\\"mean\\\": 0.5840519989820876\\n    },\\n    \\\"additive\\\": {\\n      \\\"rho\\\": 0.30625134008871885,\\n      \\\"p_value\\\": 3.204204105068383e-08,\\n      \\\"mean\\\": 0.61027086203722
…[truncated 293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T07:29:17.590985+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && find output/ -name \"report*.json\" -o -name \"*analysis*.json\" | sort | head -40",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && find output/ -name \"report*.json\" -o -name \"*analysis*.json\" | sort | head -40",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T07:29:17.591161+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"output/adalp_analysis_results.json\\noutput/analysis_fk_bootstrap_ci.json\\noutput/analysis_fk_bootstrap_per_instance.json\\noutput/analysis_lp_range_cdf.json\\noutput/analysis_lp_range_cdf_n16_3seed.json\\noutput/analysis_mbr_selection.json\\noutput/analysis_multiseed_selection_f1.json\\noutput/analysis_scierc_n16_3seed_selection_f1.json\\noutput/analysis_scierc_n16_3seed_selection_f1_merged.json\\noutput/analysis_scierc_re_n16_3seed_selection_f1.json\\noutput/analysis_unified_rho_full.json\\noutput/d108_q4q5/q4_entity_lp_analysis.json\\noutput/dals_analysis.json\\noutput/dgs_epoch_rank_analysis.json\\noutput/exp001_n16_seed123/report.json\\noutput/exp001_n16_seed123_200only/report.json\\noutput/exp001_n16_seed42/report.json\\noutput/exp001_n16_seed42_200only_backup/report.json\\noutput/exp001_n16_seed456/report.json\\noutput/exp001_n16_seed456_200only/report.json\\noutput/exp001_seed123_t10_full/report.json\\noutput/exp001_seed456_t10_full/report.json\\noutput/exp002_conll2003/full_signal_analysis.json\\noutput/exp002_conll2003/report.json\\noutput/exp003_wnut17_dryrun/report.json\\noutput/exp003_wnut17_eval/report.json\\noutput/exp003_wnut17_pilot/report.json\\noutput/exp007_llama_dryrun/report.json\\noutput/exp007_llama_inference/report.json\\noutput/exp008_re_n16/report.json\\noutput/exp008_re_n16_200only/report.json\\noutput/exp008_re_n16_t10_full/report.json\\noutput/exp_001_seed123_v2/report.json\\noutput/exp_001_seed42_v2/report.json\\noutput/exp_001_seed42_v2_r1024/report.json\\noutput/exp_001_seed456_v2/report.json\\noutput/exp_001_seed456_v2_ner/report.json\\noutput/exp_002_conll_n16/report.json\\noutput/exp_002_conll_n16_r1024/report.json\\noutput/exp_002_conll_n16_seed123/report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T07:29:17.591309+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && find output/ -name \"report*.json\" -o -name \"*analysis*.json\" | sort | tail -40",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && find output/ -name \"report*.json\" -o -name \"*analysis*.json\" | sort | tail -40",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T07:29:17.591458+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"output/exp_027_fewnerd_n16/shard_3/report.json\\noutput/exp_028_entity_token_lp/analysis_results.json\\noutput/exp_028_fewnerd_5epoch/analysis_results.json\\noutput/exp_028_fewnerd_5epoch/report.json\\noutput/exp_029a_scierc_3epoch/analysis_results.json\\noutput/exp_029a_scierc_3epoch/report.json\\noutput/exp_029b_scierc_10epoch/analysis_results.json\\noutput/exp_029b_scierc_10epoch/report.json\\noutput/exp_030_conll_t12/report.json\\noutput/exp_031_fewnerd_t12/report.json\\noutput/exp_entity_token_lp/conll/report.json\\noutput/exp_entity_token_lp/scierc/report.json\\noutput/exp_entity_token_lp_pilot/report.json\\noutput/exp_entity_token_lp_smoke/report.json\\noutput/exp_lp_scierc_t07/report.json\\noutput/exp_qwen3_4b_conll_scs_inference/report.json\\noutput/exp_qwen3_4b_conll_scs_inference_v2/report.json\\noutput/exp_qwen3_4b_scierc_scs_inference/report.json\\noutput/exp_re_scierc_seed123/report.json\\noutput/exp_re_scierc_seed456/report.json\\noutput/exp_scale_qwen3_4b_conll/report.json\\noutput/fewnerd_seed789_merged/analysis.json\\noutput/fewnerd_seed789_merged/full_signal_analysis.json\\noutput/gate0_ft002v2/report.json\\noutput/gate0_ft002v2_ckpt400/report.json\\noutput/llama_fewnerd_s123/report.json\\noutput/llama_fewnerd_s42/report.json\\noutput/llama_fewnerd_s456/report.json\\noutput/mvp_pilot_001/report.json\\noutput/mvp_pilot_003/report.json\\noutput/mvp_pilot_004/report.json\\noutput/mvp_pilot_005/report.json\\noutput/review_round2/diversity_analysis.json\\noutput/review_round2/re_conditional_analysis.json\\noutput/review_round2/sj_threshold_analysis.json\\noutput/review_round2/wnut17_full_signal_analysis.json\\noutput/review_round8/r8w2_thinking_token_analysis.json\\noutput/review_round8/r8w4_lp_range_analysis.json\\noutput/review_round9_experiments/llama3b_scierc/report.json\\noutput/vc_quartile_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_se
…[truncated 17 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T07:29:17.591625+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && grep -rl \"23\\|figure.3\\|fig.3\\|scatter\\|decompos\" code/ | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && grep -rl \"23\\|figure.3\\|fig.3\\|scatter\\|decompos\" code/ | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T07:29:17.591765+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"code/__pycache__/exp_006_v2_selection.cpython-312.pyc\\ncode/__pycache__/statistical_hardening.cpython-312.pyc\\ncode/__pycache__/diagnostic_calibration.cpython-312.pyc\\ncode/__pycache__/adaptive_temperature_analysis.cpython-312.pyc\\ncode/analyze_component_wise_re.py\\ncode/analyze_exp016_ensemble.py\\ncode/diagnose_logprob_rho.py\\ncode/_backup_cond_fix/analyze_component_wise_re.py\\ncode/analyze_exp015_v2_metrics.py\\ncode/exp_006_v2_selection.py\\ncode/exp_009_v2_stratification.py\\ncode/exp_016_v2_ensemble.py\\ncode/analyze_3seed_5signal.py\\ncode/analyze_exp017_llama_conll_n16_s123.py\\ncode/exp001_3seed_all_signals.py\\ncode/compute_re_conditional.py\\ncode/exp018_5signal_analysis.py\\ncode/analysis_multiseed_selection_f1.py\\ncode/fk_bootstrap_ci.py\\ncode/compute_selection_f1.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T07:29:17.591892+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && grep -rl \"delta_oracle\\|headroom\\|rho_within\\|selection_gain\\|degeneracy.*oracle\\|decomposition_formula\" code/ | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && grep -rl \"delta_oracle\\|headroom\\|rho_within\\|selection_gain\\|degeneracy.*oracle\\|decomposition_formula\" code/ | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T07:29:17.592023+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"code/__pycache__/run_mvp_pilot.cpython-312.pyc\\ncode/__pycache__/statistical_hardening.cpython-312.pyc\\ncode/__pycache__/analyze_fewnerd_results.cpython-312.pyc\\ncode/run_mvp_pilot.py\\ncode/mvp_pilot.py\\ncode/analyze_exp002_conll2003.py\\ncode/_backup_cond_fix/run_mvp_pilot.py\\ncode/_backup_cond_fix/analyze_exp002_conll2003.py\\ncode/diversity_stratified_selection.py\\ncode/oracle_improvable.py\\ncode/vc_quartile_analysis.py\\ncode/analyze_exp023_rank8_full.py\\ncode/analyze_fewnerd_results.py\\ncode/run_mvp_pilot.py.bak\\ncode/exp021_fewnerd_full_analysis.py\\ncode/analyze_per_type_lp.py\\ncode/analyze_per_type_lp_scierc.py\\ncode/exp017_full_signal_analysis.py\\ncode/recompute_table_fewnerd.py\\ncode/recompute_table_metrics.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T07:29:17.592194+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && grep -rl \"figure_3\\|fig_3\\|scatter.*decomp\\|plot.*regress\\|23.*config\" code/ docs/ | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && grep -rl \"figure_3\\|fig_3\\|scatter.*decomp\\|plot.*regress\\|23.*config\" code/ docs/ | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T07:29:17.592348+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T07:29:17.592477+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && find docs/paper/ -name \"*.tex\" | head -10 && grep -l \"decompos\\|ΔF1\\|delta.*F1\\|selection.*gain\\|oracle.*headroom\\|rho.*within\" docs/paper/sections/*.tex 2>/dev/null | head -10",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && find docs/paper/ -name \"*.tex\" | head -10 && grep -l \"decompos\\|ΔF1\\|delta.*F1\\|selection.*gain\\|oracle.*headroom\\|rho.*within\" docs/paper/sections/*.tex 2>/dev/null | head -10",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T07:29:17.592612+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T07:29:17.592734+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && find docs/ -type f -name \"*.tex\" | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && find docs/ -type f -name \"*.tex\" | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T07:29:17.592857+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T07:29:17.592972+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && ls docs/ 2>/dev/null && ls artifacts/_project/paper/ 2>/dev/null | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && ls docs/ 2>/dev/null && ls artifacts/_project/paper/ 2>/dev/null | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T07:29:17.593115+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"paper\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T07:29:17.593278+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && ls docs/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && ls docs/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T07:29:17.593405+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"figures\\nreferences.bib\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T07:29:17.593529+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && ls docs/paper/figures/ && find . -name \"*.tex\" -path \"*/paper/*\" | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && ls docs/paper/figures/ && find . -name \"*.tex\" -path \"*/paper/*\" | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T07:29:17.593657+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"fig_degeneracy_lp_scatter.pdf\\nfig_degeneracy_lp_scatter.png\\nfig_overview.pdf\\nfig_overview.png\\nfig_selection_gap.pdf\\nfig_selection_gap.png\\nfig_selection_gap_dual_panel.pdf\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T07:29:17.593795+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && grep -rl \"scatter\\|degeneracy_lp_scatter\\|selection_gap\" code/ | head -10",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && grep -rl \"scatter\\|degeneracy_lp_scatter\\|selection_gap\" code/ | head -10",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T07:29:17.593922+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"code/__pycache__/diagnostic_calibration.cpython-312.pyc\\ncode/analyze_exp016_ensemble.py\\ncode/plot_selection_gap_1024.py\\ncode/diversity_stratified_selection.py\\ncode/plot_selection_gap_3seed.py\\ncode/plot_selection_gap_n8.py\\ncode/diagnostic_calibration.py\\ncode/scatter_v2_data.py\\ncode/plot_scatter_v2.py\\ncode/plot_selection_gap_single.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T07:29:17.594059+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && cat code/scatter_v2_data.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && cat code/scatter_v2_data.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T07:29:17.594358+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Compute unified (degen%, LP_delta) for all experiments at N=8.\\\"\\\"\\\"\\nimport json\\nimport sys\\nimport os\\nsys.path.insert(0, \\\"/root/autodl-tmp/struct_self_consist_ie/code\\\")\\nfrom unified_metrics import compute_entity_f1, compute_degeneracy\\n\\nBASE = \\\"/root/autodl-tmp/struct_self_consist_ie/output\\\"\\n\\nEXPERIMENTS = [\\n    # Cross-dataset canonical (Qwen3-8B, T=1.0, seed=42)\\n    {\\\"dir\\\": \\\"exp_012_rerun_1024\\\", \\\"label\\\": \\\"SciERC\\\", \\\"category\\\": \\\"cross-dataset\\\", \\\"model\\\": \\\"Qwen3-8B\\\", \\\"dataset\\\": \\\"SciERC\\\", \\\"T\\\": 1.0, \\\"seed\\\": 42},\\n    {\\\"dir\\\": \\\"exp_002_conll_n16_r1024\\\", \\\"label\\\": \\\"CoNLL\\\", \\\"category\\\": \\\"cross-dataset\\\", \\\"model\\\": \\\"Qwen3-8B\\\", \\\"dataset\\\": \\\"CoNLL\\\", \\\"T\\\": 1.0, \\\"seed\\\": 42},\\n    {\\\"dir\\\": \\\"exp_027_fewnerd_n16\\\", \\\"label\\\": \\\"FewNERD\\\", \\\"category\\\": \\\"cross-dataset\\\", \\\"model\\\": \\\"Qwen3-8B\\\", \\\"dataset\\\": \\\"FewNERD\\\", \\\"T\\\": 1.0, \\\"seed\\\": 42},\\n    # Multi-seed Qwen SciERC\\n    {\\\"dir\\\": \\\"exp_018_qwen_scierc_seed123\\\", \\\"label\\\": \\\"SciERC s123\\\", \\\"category\\\": \\\"multi-seed\\\", \\\"model\\\": \\\"Qwen3-8B\\\", \\\"dataset\\\": \\\"SciERC\\\", \\\"T\\\": 1.0, \\\"seed\\\": 123},\\n    {\\\"dir\\\": \\\"exp_018_qwen_scierc_seed456\\\", \\\"label\\\": \\\"SciERC s456\\\", \\\"category\\\": \\\"multi-seed\\\", \\\"model\\\": \\\"Qwen3-8B\\\", \\\"dataset\\\": \\\"SciERC\\\", \\\"T\\\": 1.0, \\\"seed\\\": 456},\\n    # Multi-seed Qwen CoNLL N=8\\n    {\\\"dir\\\": \\\"exp_002_conll_n8_seed123\\\", \\\"label\\\": \\\"CoNLL s123\\\", \\\"category\\\": \\\"multi-seed\\\", \\\"model\\\": \\\"Qwen3-8B\\\", \\\"dataset\\\": \\\"CoNLL\\\", \\\"T\\\": 1.0, \\\"seed\\\": 123},\\n    {\\\"dir\\\": \\\"exp_002_conll_n8_seed456\\\", \\\"label\\\": \\\"Co
…[truncated 7123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T07:29:17.594549+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && cat output/scatter_v2_data.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && cat output/scatter_v2_data.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T07:29:17.594860+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"label\\\": \\\"SciERC\\\",\\n    \\\"category\\\": \\\"cross-dataset\\\",\\n    \\\"model\\\": \\\"Qwen3-8B\\\",\\n    \\\"dataset\\\": \\\"SciERC\\\",\\n    \\\"T\\\": 1.0,\\n    \\\"seed\\\": 42,\\n    \\\"degen_pct\\\": 17.77,\\n    \\\"greedy_f1\\\": 0.6439,\\n    \\\"lp_f1\\\": 0.6501,\\n    \\\"lp_delta_pp\\\": 0.61,\\n    \\\"n_used\\\": 529,\\n    \\\"n_degen\\\": 94\\n  },\\n  {\\n    \\\"label\\\": \\\"CoNLL\\\",\\n    \\\"category\\\": \\\"cross-dataset\\\",\\n    \\\"model\\\": \\\"Qwen3-8B\\\",\\n    \\\"dataset\\\": \\\"CoNLL\\\",\\n    \\\"T\\\": 1.0,\\n    \\\"seed\\\": 42,\\n    \\\"degen_pct\\\": 57.95,\\n    \\\"greedy_f1\\\": 0.907,\\n    \\\"lp_f1\\\": 0.8989,\\n    \\\"lp_delta_pp\\\": -0.81,\\n    \\\"n_used\\\": 2756,\\n    \\\"n_degen\\\": 1597\\n  },\\n  {\\n    \\\"label\\\": \\\"FewNERD\\\",\\n    \\\"category\\\": \\\"cross-dataset\\\",\\n    \\\"model\\\": \\\"Qwen3-8B\\\",\\n    \\\"dataset\\\": \\\"FewNERD\\\",\\n    \\\"T\\\": 1.0,\\n    \\\"seed\\\": 42,\\n    \\\"degen_pct\\\": 14.43,\\n    \\\"greedy_f1\\\": 0.7478,\\n    \\\"lp_f1\\\": 0.761,\\n    \\\"lp_delta_pp\\\": 1.32,\\n    \\\"n_used\\\": 4351,\\n    \\\"n_degen\\\": 628\\n  },\\n  {\\n    \\\"label\\\": \\\"SciERC s123\\\",\\n    \\\"category\\\": \\\"multi-seed\\\",\\n    \\\"model\\\": \\\"Qwen3-8B\\\",\\n    \\\"dataset\\\": \\\"SciERC\\\",\\n    \\\"T\\\": 1.0,\\n    \\\"seed\\\": 123,\\n    \\\"degen_pct\\\": 17.2,\\n    \\\"greedy_f1\\\": 0.6457,\\n    \\\"lp_f1\\\": 0.6436,\\n    \\\"lp_delta_pp\\\": -0.21,\\n    \\\"n_used\\\": 529,\\n    \\\"n_degen\\\": 91\\n  },\\n  {\\n    \\\"label\\\": \\\"SciERC s456\\\",\\n    \\\"category\\\": \\\"multi-seed\\\",\\n    \\\"model\\\": \\\"Qwen3-8B\\\",\\n    \\\"dataset\\\": \\\"SciERC\\\",\\n    \\\"T\\\": 1.0,\\n    \\\"seed\\\": 456,\\n    \\\"degen_pct\\\": 20.42,\\n    \\\"greedy_f1\\\": 0.6478,\\n    \\\"lp_f1\\\": 0.645,\\n    \\\"lp_delta_pp
…[truncated 7572 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T07:29:17.595039+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && head -80 code/unified_metrics.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && head -80 code/unified_metrics.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T07:29:17.595227+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Unified F1 / degeneracy / data-loading module.\\n\\nThis is the single source of truth for entity F1, degeneracy detection,\\nand data loading across all analysis scripts. All analysis scripts must\\nimport from this module instead of defining their own implementations.\\n\\nConventions:\\n  - Entity = (start, end, type) tuple, exact match\\n  - F1 = micro per-instance: 2*P*R/(P+R)\\n  - Degeneracy = constant-F1 gold-filtered (all N sample F1s identical)\\n  - gold_filter = skip instances where gold entities list is empty\\n\\\"\\\"\\\"\\n\\nimport json\\nimport numpy as np\\n\\n\\ndef compute_entity_f1(pred_entities, gold_entities):\\n    \\\"\\\"\\\"Span-based entity F1 for a single instance.\\n\\n    Args:\\n        pred_entities: list of dicts with keys start, end, type.\\n        gold_entities: list of dicts with keys start, end, type.\\n\\n    Returns:\\n        float F1 in [0, 1].\\n    \\\"\\\"\\\"\\n    pred_set = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in pred_entities}\\n    gold_set = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in gold_entities}\\n    if not gold_set and not pred_set:\\n        return 1.0\\n    if not gold_set or not pred_set:\\n        return 0.0\\n    tp = len(pred_set & gold_set)\\n    if tp == 0:\\n        return 0.0\\n    p = tp / len(pred_set)\\n    r = tp / len(gold_set)\\n    return 2 * p * r / (p + r)\\n\\n\\ndef compute_degeneracy(sample_f1_list):\\n    \\\"\\\"\\\"Check if an instance is degenerate (constant-F1 gold-filtered).\\n\\n    All N sample F1 values are identical (after rounding to 10 decimals\\n    to avoid float noise) -> degenerate.\\n\\n    Args:\\n        sample_f1_list: list of float F1 values, one per sample.\\n\\n    Returns:\\n        bool, True if degenerate.\\n    \\\"\\\"\\\"\\n    return len(set(round(f, 10) for f in sample_f1_list)) <= 1\\n\\n\\ndef load_and_filter(path, gold_filter=True):\\n    \\\"\\\"
…[truncated 831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T07:29:17.595380+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && sed -n '80,160p' code/unified_metrics.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && sed -n '80,160p' code/unified_metrics.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T07:29:17.595554+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    \\\"\\\"\\\"Compute per-sample F1 list for an instance.\\n\\n    Args:\\n        inst: instance dict with keys gold, samples.\\n        n_samples: if set, only use first n_samples.\\n\\n    Returns:\\n        list of float F1 values.\\n    \\\"\\\"\\\"\\n    gold_ents = inst[\\\"gold\\\"][\\\"entities\\\"]\\n    samples = inst[\\\"samples\\\"][:n_samples] if n_samples else inst[\\\"samples\\\"]\\n    return [compute_entity_f1(s.get(\\\"entities\\\", []), gold_ents) for s in samples]\\n\\n\\ndef compute_greedy_f1(inst):\\n    \\\"\\\"\\\"Compute greedy F1 for an instance.\\\"\\\"\\\"\\n    gold_ents = inst[\\\"gold\\\"][\\\"entities\\\"]\\n    greedy = inst.get(\\\"greedy\\\", inst[\\\"samples\\\"][0])\\n    return compute_entity_f1(greedy.get(\\\"entities\\\", []), gold_ents)\\n\\n\\ndef get_lp_selection_idx(inst, n_samples=None):\\n    \\\"\\\"\\\"Get the index of the sample with highest mean_logprob.\\\"\\\"\\\"\\n    samples = inst[\\\"samples\\\"][:n_samples] if n_samples else inst[\\\"samples\\\"]\\n    best_idx = 0\\n    best_lp = -float(\\\"inf\\\")\\n    for i, s in enumerate(samples):\\n        lp = s.get(\\\"mean_logprob\\\", None)\\n        if lp is None and \\\"logprobs\\\" in inst and i < len(inst[\\\"logprobs\\\"]):\\n            lp = inst[\\\"logprobs\\\"][i]\\n        if lp is not None and np.isfinite(lp) and lp > best_lp:\\n            best_lp = lp\\n            best_idx = i\\n    return best_idx\\n\\n\\ndef bootstrap_ci(values, n_boot=2000, ci=0.95, seed=42):\\n    \\\"\\\"\\\"Bootstrap confidence interval for the mean.\\\"\\\"\\\"\\n    arr = np.array(values)\\n    n = len(arr)\\n    if n == 0:\\n        return {\\\"mean\\\": 0.0, \\\"ci_lo\\\": 0.0, \\\"ci_hi\\\": 0.0}\\n    rng = np.random.RandomState(seed)\\n    boot_means = np.array([arr[rng.randint(0, n, n)].mean() for _ in range(n_boot)])\\n    boot_means.sort()\\n    lo = boot_means[int((1 - ci) / 2 * n_boot)]\\n    hi = boot_means
…[truncated 963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T07:29:17.595778+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat << 'PYEOF' > /tmp/decomposition_regression.py\n#!/usr/bin/env python3\n\"\"\"Compute decomposition formula regression: ΔF1 ≈ (1-d) × Δ_oracle × ρ_within for 23 configs.\"\"\"\nimport json\nimport sys\nimport os\nimport numpy as np\nfrom scipy.stats import spearmanr\nfrom sklearn.metrics import r2_score\nfrom sklearn.linear_model import LinearRegression\n\nsys.path.insert(0, \"/root/autodl-tmp/struct_self_consist_ie/code\")\nfrom unified_metrics import compute_entity_f1, compute_degeneracy, get_lp_selection_idx\n\nBASE = \"/root/autodl-tmp/struct_self_consist_ie/output\"\n\n# Load experiment definitions from scatter_v2_data.py\nEXPERIMENTS = [\n    {\"dir\": \"exp_012_rerun_1024\", \"label\": \"SciERC\", \"category\": \"cross-dataset\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 42},\n    {\"dir\": \"exp_002_conll_n16_r1024\", \"label\": \"CoNLL\", \"category\": \"cross-dataset\", \"model\": \"Qwen3-8B\", \"dataset\": \"CoNLL\", \"T\": 1.0, \"seed\": 42},\n    {\"dir\": \"exp_027_fewnerd_n16\", \"label\": \"FewNERD\", \"category\": \"cross-dataset\", \"model\": \"Qwen3-8B\", \"dataset\": \"FewNERD\", \"T\": 1.0, \"seed\": 42},\n    {\"dir\": \"exp_018_qwen_scierc_seed123\", \"label\": \"SciERC s123\", \"category\": \"multi-seed\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 123},\n    {\"dir\": \"exp_018_qwen_scierc_seed456\", \"label\": \"SciERC s456\", \"category\": \"multi-seed\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 456},\n    {\"dir\": \"exp_002_conll_n8_seed123\", \"label\": \"CoNLL s123\", \"category\": \"multi-seed\", \"model\": \"Qwen3-8B\", \"dataset\": \"CoNLL\", \"T\": 1.0, \"seed\": 123},\n    {\"dir\": \"exp_002_conll_n8_seed456\", \"label\": \"CoNLL s456\", \"category\": \"multi-seed\", \"model\": \"Qwen3-8B\", \"dataset\": \"CoNLL\", \"T\": 1.0, \"seed\": 456},\n    {\"dir\": \"exp_021_fewnerd_n8_seed123\", \"label\": \"FewNERD s123\", \"category\": \"multi-seed\", \"model\": \"Qwen3-8B\", \"dataset\": \"FewNERD\", \"T\": 1.0, \"seed\": 123},\n    {\"dir\": \"exp_021_fewnerd_n8_seed456\", \"label\": \"FewNERD s456\", \"category\": \"multi-seed\", \"model\": \"Qwen3-8B\", \"dataset\": \"FewNERD\", \"T\": 1.0, \"seed\": 456},\n    {\"dir\": \"exp_018_llama_scierc_seed42_r1024\", \"label\": \"LLaMA SciERC s42\", \"category\": \"LLaMA3.1-8B\", \"model\": \"LLaMA3.1-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 42},\n    {\"dir\": \"exp_018_llama_scierc_seed123\", \"label\": \"LLaMA SciERC s123\", \"category\": \"LLaMA3.1-8B\", \"model\": \"LLaMA3.1-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 123},\n    {\"dir\": \"exp_018_llama_scierc_seed456_r1024\", \"label\": \"LLaMA SciERC s456\", \"category\": \"LLaMA3.1-8B\", \"model\": \"LLaMA3.1-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 456},\n    {\"dir\": \"exp_017_llama_conll_n16_r1024\", \"label\": \"LLaMA CoNLL s42\", \"category\": \"LLaMA3.1-8B\", \"model\": \"LLaMA3.1-8B\", \"dataset\": \"CoNLL\", \"T\": 1.0, \"seed\": 42},\n    {\"dir\": \"exp_017_llama_conll_n16_s123_r1024\", \"label\": \"LLaMA CoNLL s123\", \"category\": \"LLaMA3.1-8B\", \"model\": \"LLaMA3.1-8B\", \"dataset\": \"CoNLL\", \"T\": 1.0, \"seed\": 123},\n    {\"dir\": \"exp_017_llama_conll_n16_s456_r1024\", \"label\": \"LLaMA CoNLL s456\", \"category\": \"LLaMA3.1-8B\", \"model\": \"LLaMA3.1-8B\", \"dataset\": \"CoNLL\", \"T\": 1.0, \"seed\": 456},\n    {\"dir\": \"exp_029a_scierc_3epoch\", \"label\": \"3-epoch\", \"category\": \"epoch\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 42, \"note\": \"3ep\"},\n    {\"dir\": \"exp_029b_scierc_10epoch\", \"label\": \"10-epoch\", \"category\": \"epoch\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 42, \"note\": \"10ep\"},\n    {\"dir\": \"exp_023_rank8_inference\", \"label\": \"rank=8\", \"category\": \"rank\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 42, \"note\": \"rank8\"},\n    {\"dir\": \"exp_026_t05\", \"label\": \"T=0.5\", \"category\": \"temperature\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 0.5, \"seed\": 42},\n    {\"dir\": \"exp_026_t08\", \"label\": \"T=0.8\", \"category\": \"temperature\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 0.8, \"seed\": 42},\n    {\"dir\": \"exp_026_t12\", \"label\": \"T=1.2\", \"category\": \"temperature\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 1.2, \"seed\": 42},\n    {\"dir\": \"exp_qwen3_4b_scierc_scs_inference\", \"label\": \"4B SciERC\", \"category\": \"Qwen3-4B\", \"model\": \"Qwen3-4B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 42},\n    {\"dir\": \"exp_qwen3_4b_conll_scs_inference_v2\", \"label\": \"4B CoNLL\", \"category\": \"Qwen3-4B\", \"model\": \"Qwen3-4B\", \"dataset\": \"CoNLL\", \"T\": 1.0, \"seed\": 42},\n]\n\nN_SAMPLES = 8\n\ndef analyze_config(path, n_samples=N_SAMPLES):\n    \"\"\"For a single config, compute d, delta_oracle, rho_within, actual_delta_f1.\"\"\"\n    greedy_f1s = []\n    lp_f1s = []\n    oracle_f1s = []\n    n_degen = 0\n    n_used = 0\n    \n    # For rho_within: collect per-instance (mean_logprob, f1) pairs across non-degenerate instances\n    # rho_within = avg of per-instance Spearman(LP, F1) across non-degen instances with variance\n    # Actually the formula uses dataset-level within-instance correlation\n    # We compute: for each non-degen instance, Spearman(sample_logprobs, sample_f1s), then average\n    instance_rhos = []\n    \n    with open(path) as f:\n        for line in f:\n            if not line.strip():\n                continue\n            inst = json.loads(line)\n            gold_ents = inst[\"gold\"].get(\"entities\", [])\n            if not gold_ents:\n                continue\n            \n            samples = inst[\"samples\"][:n_samples]\n            if len(samples) < n_samples:\n                continue\n            \n            greedy = inst.get(\"greedy\", samples[0])\n            \n            sample_f1s = [compute_entity_f1(s.get(\"entities\", []), gold_ents) for s in samples]\n            g_f1 = compute_entity_f1(greedy.get(\"entities\", []), gold_ents)\n            \n            # Oracle: best sample F1\n            oracle_f1 = max(sample_f1s)\n            \n            # LP selection\n            lp_idx = get_lp_selection_idx(inst, n_samples=n_samples)\n            lp_f1 = sample_f1s[lp_idx]\n            \n            is_degen = compute_degeneracy(sample_f1s)\n            if is_degen:\n                n_degen += 1\n            \n            greedy_f1s.append(g_f1)\n            lp_f1s.append(lp_f1)\n            oracle_f1s.append(oracle_f1)\n            n_used += 1\n            \n            # Within-instance correlation (only for non-degen instances with F1 variance)\n            if not is_degen:\n                sample_lps = []\n                for i, s in enumerate(samples):\n                    lp = s.get(\"mean_logprob\", None)\n                    if lp is None and \"logprobs\" in inst and i < len(inst[\"logprobs\"]):\n                        lp = inst[\"logprobs\"][i]\n                    sample_lps.append(lp if lp is not None else 0.0)\n                \n                # Check variance in both\n                if len(set(round(x, 10) for x in sample_f1s)) > 1 and len(set(round(x, 10) for x in sample_lps)) > 1:\n                    rho, _ = spearmanr(sample_lps, sample_f1s)\n                    if np.isfinite(rho):\n                        instance_rhos.append(rho)\n    \n    if n_used == 0:\n        return None\n    \n    d = n_degen / n_used  # degeneracy rate (fraction)\n    mean_greedy = np.mean(greedy_f1s)\n    mean_lp = np.mean(lp_f1s)\n    mean_oracle = np.mean(oracle_f1s)\n    \n    delta_oracle = (mean_oracle - mean_greedy) * 100  # in pp\n    actual_delta_f1 = (mean_lp - mean_greedy) * 100  # in pp\n    rho_within = np.mean(instance_rhos) if instance_rhos else 0.0\n    \n    # Predicted: (1-d) * delta_oracle * rho_within\n    predicted = (1 - d) * delta_oracle * rho_within\n    \n    return {\n        \"d\": round(d, 4),\n        \"degen_pct\": round(d * 100, 2),\n        \"greedy_f1\": round(float(mean_greedy), 4),\n        \"oracle_f1\": round(float(mean_oracle), 4),\n        \"lp_f1\": round(float(mean_lp), 4),\n        \"delta_oracle_pp\": round(delta_oracle, 2),\n        \"actual_delta_f1_pp\": round(actual_delta_f1, 2),\n        \"rho_within\": round(rho_within, 4),\n        \"predicted_delta_f1_pp\": round(predicted, 2),\n        \"n_used\": n_used,\n        \"n_degen\": n_degen,\n        \"n_rho_instances\": len(instance_rhos),\n    }\n\n\n# Process all configs\nconfigs = []\nfor exp in EXPERIMENTS:\n    path = os.path.join(BASE, exp[\"dir\"], \"samples.jsonl\")\n    if not os.path.exists(path):\n        print(f\"SKIP: {exp['dir']} - no samples.jsonl\", file=sys.stderr)\n        continue\n    \n    metrics = analyze_config(path)\n    if metrics is None:\n        print(f\"SKIP: {exp['dir']} - no valid instances\", file=sys.stderr)\n        continue\n    \n    entry = {\n        \"label\": exp[\"label\"],\n        \"category\": exp[\"category\"],\n        \"model\": exp[\"model\"],\n        \"dataset\": exp[\"dataset\"],\n        \"T\": exp[\"T\"],\n        \"seed\": exp[\"seed\"],\n    }\n    if \"note\" in exp:\n        entry[\"note\"] = exp[\"note\"]\n    entry.update(metrics)\n    configs.append(entry)\n    \n    print(f\"{exp['label']:25s}  d={metrics['degen_pct']:5.1f}%  Δ_oracle={metrics['delta_oracle_pp']:+6.2f}  ρ_within={metrics['rho_within']:+.4f}  pred={metrics['predicted_delta_f1_pp']:+6.2f}  actual={metrics['actual_delta_f1_pp']:+6.2f}\")\n\nprint(f\"\\n=== {len(configs)} configs processed ===\\n\")\n\n# Extract arrays\npredicted = np.array([c[\"predicted_delta_f1_pp\"] for c in configs])\nactual = np.array([c[\"actual_delta_f1_pp\"] for c in configs])\n\n# (a) Full-sample statistics\nrho_full, p_full = spearmanr(predicted, actual)\nr2_full = r2_score(actual, predicted)\n\n# Pearson correlation too\nfrom scipy.stats import pearsonr\npearson_full, pearson_p = pearsonr(predicted, actual)\n\nprint(f\"Full-sample Spearman ρ = {rho_full:.4f} (p = {p_full:.2e})\")\nprint(f\"Full-sample Pearson r  = {pearson_full:.4f} (p = {pearson_p:.2e})\")\nprint(f\"Full-sample R²         = {r2_full:.4f}\")\n\n# MAE\nmae = np.mean(np.abs(predicted - actual))\nprint(f\"Full-sample MAE        = {mae:.2f} pp\")\n\n# (b) Leave-one-dataset-out CV\n# Group by a \"dataset_group\" that combines model+dataset for grouping\n# Actually group by dataset only for the LODO CV\ndataset_groups = {}\nfor i, c in enumerate(configs):\n    # Create group key: for LLaMA configs, use \"llama_&lt;dataset>\"\n    if c[\"model\"] == \"LLaMA3.1-8B\":\n        gkey = f\"llama_{c['dataset'].lower()}\"\n    elif c[\"model\"] == \"Qwen3-4B\":\n        gkey = f\"4b_{c['dataset'].lower()}\"\n    else:\n        gkey = c[\"dataset\"].lower()\n    \n    if gkey not in dataset_groups:\n        dataset_groups[gkey] = []\n    dataset_groups[gkey].append(i)\n\nprint(f\"\\nDataset groups: {list(dataset_groups.keys())}\")\nfor gk, gv in dataset_groups.items():\n    print(f\"  {gk}: {len(gv)} configs\")\n\n# LODO CV with linear regression: fit actual ~ α * predicted + β\nlodo_results = {}\nall_test_preds = np.zeros_like(actual)\nall_test_actual = np.zeros_like(actual)\ntest_count = 0\n\nfor held_out, test_idx in dataset_groups.items():\n    train_idx = [i for i in range(len(configs)) if i not in test_idx]\n    \n    if len(train_idx) < 3 or len(test_idx) < 1:\n        continue\n    \n    X_train = predicted[train_idx].reshape(-1, 1)\n    y_train = actual[train_idx]\n    X_test = predicted[test_idx].reshape(-1, 1)\n    y_test = actual[test_idx]\n    \n    reg = LinearRegression()\n    reg.fit(X_train, y_train)\n    y_pred = reg.predict(X_test)\n    \n    if len(test_idx) > 1:\n        r2_cv = r2_score(y_test, y_pred)\n        rho_cv, _ = spearmanr(y_pred, y_test) if len(test_idx) >= 3 else (float('nan'), float('nan'))\n    else:\n        r2_cv = float('nan')\n        rho_cv = float('nan')\n    \n    lodo_results[held_out] = {\n        \"r2\": round(r2_cv, 4) if np.isfinite(r2_cv) else None,\n        \"spearman\": round(rho_cv, 4) if np.isfinite(rho_cv) else None,\n        \"n_test\": len(test_idx),\n        \"n_train\": len(train_idx),\n        \"coef\": round(float(reg.coef_[0]), 4),\n        \"intercept\": round(float(reg.intercept_), 4),\n    }\n    print(f\"  LODO {held_out:20s}: R²={r2_cv:.4f}, n_test={len(test_idx)}, coef={reg.coef_[0]:.4f}, intercept={reg.intercept_:.4f}\")\n\n# Save results\nout_dir = os.path.join(BASE, \"decomposition_regression\")\nos.makedirs(out_dir, exist_ok=True)\n\nresult = {\n    \"n_configs\": len(configs),\n    \"formula\": \"predicted_ΔF1 = (1-d) × Δ_oracle × ρ_within\",\n    \"configs\": configs,\n    \"full_sample\": {\n        \"spearman_rho\": round(rho_full, 4),\n        \"spearman_p\": float(p_full),\n        \"pearson_r\": round(pearson_full, 4),\n        \"pearson_p\": float(pearson_p),\n        \"r2\": round(r2_full, 4),\n        \"mae_pp\": round(mae, 2),\n    },\n    \"leave_one_dataset_out_cv\": lodo_results,\n    \"scatter_data\": [\n        {\n            \"label\": c[\"label\"],\n            \"category\": c[\"category\"],\n            \"dataset\": c[\"dataset\"],\n            \"model\": c[\"model\"],\n            \"predicted\": c[\"predicted_delta_f1_pp\"],\n            \"actual\": c[\"actual_delta_f1_pp\"],\n        }\n        for c in configs\n    ],\n}\n\nout_path = os.path.join(out_dir, \"regression_results.json\")\nwith open(out_path, \"w\") as f:\n    json.dump(result, f, indent=2)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF\necho \"Script written\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat << 'PYEOF' > /tmp/decomposition_regression.py\n#!/usr/bin/env python3\n\"\"\"Compute decomposition formula regression: ΔF1 ≈ (1-d) × Δ_oracle × ρ_within for 23 configs.\"\"\"\nimport json\nimport sys\nimport os\nimport numpy as np\nfrom scipy.stats import spearmanr\nfrom sklearn.metrics import r2_score\nfrom sklearn.linear_model import LinearRegression\n\nsys.path.insert(0, \"/root/autodl-tmp/struct_self_consist_ie/code\")\nfrom unified_metrics import compute_entity_f1, compute_degeneracy, get_lp_selection_idx\n\nBASE = \"/root/autodl-tmp/struct_self_consist_ie/output\"\n\n# Load experiment definitions from scatter_v2_data.py\nEXPERIMENTS = [\n    {\"dir\": \"exp_012_rerun_1024\", \"label\": \"SciERC\", \"category\": \"cross-dataset\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 42},\n    {\"dir\": \"exp_002_conll_n16_r1024\", \"label\": \"CoNLL\", \"category\": \"cross-dataset\", \"model\": \"Qwen3-8B\", \"dataset\": \"CoNLL\", \"T\": 1.0, \"seed\": 42},\n    {\"dir\": \"exp_027_fewnerd_n16\", \"label\": \"FewNERD\", \"category\": \"cross-dataset\", \"model\": \"Qwen3-8B\", \"dataset\": \"FewNERD\", \"T\": 1.0, \"seed\": 42},\n    {\"dir\": \"exp_018_qwen_scierc_seed123\", \"label\": \"SciERC s123\", \"category\": \"multi-seed\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 123},\n    {\"dir\": \"exp_018_qwen_scierc_seed456\", \"label\": \"SciERC s456\", \"category\": \"multi-seed\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 456},\n    {\"dir\": \"exp_002_conll_n8_seed123\", \"label\": \"CoNLL s123\", \"category\": \"multi-seed\", \"model\": \"Qwen3-8B\", \"dataset\": \"CoNLL\", \"T\": 1.0, \"seed\": 123},\n    {\"dir\": \"exp_002_conll_n8_seed456\", \"label\": \"CoNLL s456\", \"category\": \"multi-seed\", \"model\": \"Qwen3-8B\", \"dataset\": \"CoNLL\", \"T\": 1.0, \"seed\": 456},\n    {\"dir\": \"exp_021_fewnerd_n8_seed123\", \"label\": \"FewNERD s123\", \"category\": \"multi-seed\", \"model\": \"Qwen3-8B\", \"dataset\": \"FewNERD\", \"T\": 1.0, \"seed\": 123},\n    {\"dir\": \"exp_021_fewnerd_n8_seed456\", \"label\": \"FewNERD s456\", \"category\": \"multi-seed\", \"model\": \"Qwen3-8B\", \"dataset\": \"FewNERD\", \"T\": 1.0, \"seed\": 456},\n    {\"dir\": \"exp_018_llama_scierc_seed42_r1024\", \"label\": \"LLaMA SciERC s42\", \"category\": \"LLaMA3.1-8B\", \"model\": \"LLaMA3.1-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 42},\n    {\"dir\": \"exp_018_llama_scierc_seed123\", \"label\": \"LLaMA SciERC s123\", \"category\": \"LLaMA3.1-8B\", \"model\": \"LLaMA3.1-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 123},\n    {\"dir\": \"exp_018_llama_scierc_seed456_r1024\", \"label\": \"LLaMA SciERC s456\", \"category\": \"LLaMA3.1-8B\", \"model\": \"LLaMA3.1-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 456},\n    {\"dir\": \"exp_017_llama_conll_n16_r1024\", \"label\": \"LLaMA CoNLL s42\", \"category\": \"LLaMA3.1-8B\", \"model\": \"LLaMA3.1-8B\", \"dataset\": \"CoNLL\", \"T\": 1.0, \"seed\": 42},\n    {\"dir\": \"exp_017_llama_conll_n16_s123_r1024\", \"label\": \"LLaMA CoNLL s123\", \"category\": \"LLaMA3.1-8B\", \"model\": \"LLaMA3.1-8B\", \"dataset\": \"CoNLL\", \"T\": 1.0, \"seed\": 123},\n    {\"dir\": \"exp_017_llama_conll_n16_s456_r1024\", \"label\": \"LLaMA CoNLL s456\", \"category\": \"LLaMA3.1-8B\", \"model\": \"LLaMA3.1-8B\", \"dataset\": \"CoNLL\", \"T\": 1.0, \"seed\": 456},\n    {\"dir\": \"exp_029a_scierc_3epoch\", \"label\": \"3-epoch\", \"category\": \"epoch\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 42, \"note\": \"3ep\"},\n    {\"dir\": \"exp_029b_scierc_10epoch\", \"label\": \"10-epoch\", \"category\": \"epoch\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 42, \"note\": \"10ep\"},\n    {\"dir\": \"exp_023_rank8_inference\", \"label\": \"rank=8\", \"category\": \"rank\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 42, \"note\": \"rank8\"},\n    {\"dir\": \"exp_026_t05\", \"label\": \"T=0.5\", \"category\": \"temperature\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 0.5, \"seed\": 42},\n    {\"dir\": \"exp_026_t08\", \"label\": \"T=0.8\", \"category\": \"temperature\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 0.8, \"seed\": 42},\n    {\"dir\": \"exp_026_t12\", \"label\": \"T=1.2\", \"category\": \"temperature\", \"model\": \"Qwen3-8B\", \"dataset\": \"SciERC\", \"T\": 1.2, \"seed\": 42},\n    {\"dir\": \"exp_qwen3_4b_scierc_scs_inference\", \"label\": \"4B SciERC\", \"category\": \"Qwen3-4B\", \"model\": \"Qwen3-4B\", \"dataset\": \"SciERC\", \"T\": 1.0, \"seed\": 42},\n    {\"dir\": \"exp_qwen3_4b_conll_scs_inference_v2\", \"label\": \"4B CoNLL\", \"category\": \"Qwen3-4B\", \"model\": \"Qwen3-4B\", \"dataset\": \"CoNLL\", \"T\": 1.0, \"seed\": 42},\n]\n\nN_SAMPLES = 8\n\ndef analyze_config(path, n_samples=N_SAMPLES):\n    \"\"\"For a single config, compute d, delta_oracle, rho_within, actual_delta_f1.\"\"\"\n    greedy_f1s = []\n    lp_f1s = []\n    oracle_f1s = []\n    n_degen = 0\n    n_used = 0\n    \n    # For rho_within: collect per-instance (mean_logprob, f1) pairs across non-degenerate instances\n    # rho_within = avg of per-instance Spearman(LP, F1) across non-degen instances with variance\n    # Actually the formula uses dataset-level within-instance correlation\n    # We compute: for each non-degen instance, Spearman(sample_logprobs, sample_f1s), then average\n    instance_rhos = []\n    \n    with open(path) as f:\n        for line in f:\n            if not line.strip():\n                continue\n            inst = json.loads(line)\n            gold_ents = inst[\"gold\"].get(\"entities\", [])\n            if not gold_ents:\n                continue\n            \n            samples = inst[\"samples\"][:n_samples]\n            if len(samples) < n_samples:\n                continue\n            \n            greedy = inst.get(\"greedy\", samples[0])\n            \n            sample_f1s = [compute_entity_f1(s.get(\"entities\", []), gold_ents) for s in samples]\n            g_f1 = compute_entity_f1(greedy.get(\"entities\", []), gold_ents)\n            \n            # Oracle: best sample F1\n            oracle_f1 = max(sample_f1s)\n            \n            # LP selection\n            lp_idx = get_lp_selection_idx(inst, n_samples=n_samples)\n            lp_f1 = sample_f1s[lp_idx]\n            \n            is_degen = compute_degeneracy(sample_f1s)\n            if is_degen:\n                n_degen += 1\n            \n            greedy_f1s.append(g_f1)\n            lp_f1s.append(lp_f1)\n            oracle_f1s.append(oracle_f1)\n            n_used += 1\n            \n            # Within-instance correlation (only for non-degen instances with F1 variance)\n            if not is_degen:\n                sample_lps = []\n                for i, s in enumerate(samples):\n                    lp = s.get(\"mean_logprob\", None)\n                    if lp is None and \"logprobs\" in inst and i < len(inst[\"logprobs\"]):\n                        lp = inst[\"logprobs\"][i]\n                    sample_lps.append(lp if lp is not None else 0.0)\n                \n                # Check variance in both\n                if len(set(round(x, 10) for x in sample_f1s)) > 1 and len(set(round(x, 10) for x in sample_lps)) > 1:\n                    rho, _ = spearmanr(sample_lps, sample_f1s)\n                    if np.isfinite(rho):\n                        instance_rhos.append(rho)\n    \n    if n_used == 0:\n        return None\n    \n    d = n_degen / n_used  # degeneracy rate (fraction)\n    mean_greedy = np.mean(greedy_f1s)\n    mean_lp = np.mean(lp_f1s)\n    mean_oracle = np.mean(oracle_f1s)\n    \n    delta_oracle = (mean_oracle - mean_greedy) * 100  # in pp\n    actual_delta_f1 = (mean_lp - mean_greedy) * 100  # in pp\n    rho_within = np.mean(instance_rhos) if instance_rhos else 0.0\n    \n    # Predicted: (1-d) * delta_oracle * rho_within\n    predicted = (1 - d) * delta_oracle * rho_within\n    \n    return {\n        \"d\": round(d, 4),\n        \"degen_pct\": round(d * 100, 2),\n        \"greedy_f1\": round(float(mean_greedy), 4),\n        \"oracle_f1\": round(float(mean_oracle), 4),\n        \"lp_f1\": round(float(mean_lp), 4),\n        \"delta_oracle_pp\": round(delta_oracle, 2),\n        \"actual_delta_f1_pp\": round(actual_delta_f1, 2),\n        \"rho_within\": round(rho_within, 4),\n        \"predicted_delta_f1_pp\": round(predicted, 2),\n        \"n_used\": n_used,\n        \"n_degen\": n_degen,\n        \"n_rho_instances\": len(instance_rhos),\n    }\n\n\n# Process all configs\nconfigs = []\nfor exp in EXPERIMENTS:\n    path = os.path.join(BASE, exp[\"dir\"], \"samples.jsonl\")\n    if not os.path.exists(path):\n        print(f\"SKIP: {exp['dir']} - no samples.jsonl\", file=sys.stderr)\n        continue\n    \n    metrics = analyze_config(path)\n    if metrics is None:\n        print(f\"SKIP: {exp['dir']} - no valid instances\", file=sys.stderr)\n        continue\n    \n    entry = {\n        \"label\": exp[\"label\"],\n        \"category\": exp[\"category\"],\n        \"model\": exp[\"model\"],\n        \"dataset\": exp[\"dataset\"],\n        \"T\": exp[\"T\"],\n        \"seed\": exp[\"seed\"],\n    }\n    if \"note\" in exp:\n        entry[\"note\"] = exp[\"note\"]\n    entry.update(metrics)\n    configs.append(entry)\n    \n    print(f\"{exp['label']:25s}  d={metrics['degen_pct']:5.1f}%  Δ_oracle={metrics['delta_oracle_pp']:+6.2f}  ρ_within={metrics['rho_within']:+.4f}  pred={metrics['predicted_delta_f1_pp']:+6.2f}  actual={metrics['actual_delta_f1_pp']:+6.2f}\")\n\nprint(f\"\\n=== {len(configs)} configs processed ===\\n\")\n\n# Extract arrays\npredicted = np.array([c[\"predicted_delta_f1_pp\"] for c in configs])\nactual = np.array([c[\"actual_delta_f1_pp\"] for c in configs])\n\n# (a) Full-sample statistics\nrho_full, p_full = spearmanr(predicted, actual)\nr2_full = r2_score(actual, predicted)\n\n# Pearson correlation too\nfrom scipy.stats import pearsonr\npearson_full, pearson_p = pearsonr(predicted, actual)\n\nprint(f\"Full-sample Spearman ρ = {rho_full:.4f} (p = {p_full:.2e})\")\nprint(f\"Full-sample Pearson r  = {pearson_full:.4f} (p = {pearson_p:.2e})\")\nprint(f\"Full-sample R²         = {r2_full:.4f}\")\n\n# MAE\nmae = np.mean(np.abs(predicted - actual))\nprint(f\"Full-sample MAE        = {mae:.2f} pp\")\n\n# (b) Leave-one-dataset-out CV\n# Group by a \"dataset_group\" that combines model+dataset for grouping\n# Actually group by dataset only for the LODO CV\ndataset_groups = {}\nfor i, c in enumerate(configs):\n    # Create group key: for LLaMA configs, use \"llama_&lt;dataset>\"\n    if c[\"model\"] == \"LLaMA3.1-8B\":\n        gkey = f\"llama_{c['dataset'].lower()}\"\n    elif c[\"model\"] == \"Qwen3-4B\":\n        gkey = f\"4b_{c['dataset'].lower()}\"\n    else:\n        gkey = c[\"dataset\"].lower()\n    \n    if gkey not in dataset_groups:\n        dataset_groups[gkey] = []\n    dataset_groups[gkey].append(i)\n\nprint(f\"\\nDataset groups: {list(dataset_groups.keys())}\")\nfor gk, gv in dataset_groups.items():\n    print(f\"  {gk}: {len(gv)} configs\")\n\n# LODO CV with linear regression: fit actual ~ α * predicted + β\nlodo_results = {}\nall_test_preds = np.zeros_like(actual)\nall_test_actual = np.zeros_like(actual)\ntest_count = 0\n\nfor held_out, test_idx in dataset_groups.items():\n    train_idx = [i for i in range(len(configs)) if i not in test_idx]\n    \n    if len(train_idx) < 3 or len(test_idx) < 1:\n        continue\n    \n    X_train = predicted[train_idx].reshape(-1, 1)\n    y_train = actual[train_idx]\n    X_test = predicted[test_idx].reshape(-1, 1)\n    y_test = actual[test_idx]\n    \n    reg = LinearRegression()\n    reg.fit(X_train, y_train)\n    y_pred = reg.predict(X_test)\n    \n    if len(test_idx) > 1:\n        r2_cv = r2_score(y_test, y_pred)\n        rho_cv, _ = spearmanr(y_pred, y_test) if len(test_idx) >= 3 else (float('nan'), float('nan'))\n    else:\n        r2_cv = float('nan')\n        rho_cv = float('nan')\n    \n    lodo_results[held_out] = {\n        \"r2\": round(r2_cv, 4) if np.isfinite(r2_cv) else None,\n        \"spearman\": round(rho_cv, 4) if np.isfinite(rho_cv) else None,\n        \"n_test\": len(test_idx),\n        \"n_train\": len(train_idx),\n        \"coef\": round(float(reg.coef_[0]), 4),\n        \"intercept\": round(float(reg.intercept_), 4),\n    }\n    print(f\"  LODO {held_out:20s}: R²={r2_cv:.4f}, n_test={len(test_idx)}, coef={reg.coef_[0]:.4f}, intercept={reg.intercept_:.4f}\")\n\n# Save results\nout_dir = os.path.join(BASE, \"decomposition_regression\")\nos.makedirs(out_dir, exist_ok=True)\n\nresult = {\n    \"n_configs\": len(configs),\n    \"formula\": \"predicted_ΔF1 = (1-d) × Δ_oracle × ρ_within\",\n    \"configs\": configs,\n    \"full_sample\": {\n        \"spearman_rho\": round(rho_full, 4),\n        \"spearman_p\": float(p_full),\n        \"pearson_r\": round(pearson_full, 4),\n        \"pearson_p\": float(pearson_p),\n        \"r2\": round(r2_full, 4),\n        \"mae_pp\": round(mae, 2),\n    },\n    \"leave_one_dataset_out_cv\": lodo_results,\n    \"scatter_data\": [\n        {\n            \"label\": c[\"label\"],\n            \"category\": c[\"category\"],\n            \"dataset\": c[\"dataset\"],\n            \"model\": c[\"model\"],\n            \"predicted\": c[\"predicted_delta_f1_pp\"],\n            \"actual\": c[\"actual_delta_f1_pp\"],\n        }\n        for c in configs\n    ],\n}\n\nout_path = os.path.join(out_dir, \"regression_results.json\")\nwith open(out_path, \"w\") as f:\n    json.dump(result, f, indent=2)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF\necho \"Script written\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T07:29:17.596066+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T07:29:17.596223+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && python /tmp/decomposition_regression.py",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && python /tmp/decomposition_regression.py",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T07:29:17.596356+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python: command not found\\n\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T07:29:17.596479+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && python3 /tmp/decomposition_regression.py",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && python3 /tmp/decomposition_regression.py",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T07:29:17.596602+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python3: command not found\\n\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 0.63}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T07:29:17.596722+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "which python3.* 2>/dev/null; ls /usr/bin/python* /usr/local/bin/python* /root/miniconda*/bin/python* /root/anaconda*/bin/python* 2>/dev/null; conda info --envs 2>/dev/null | head -10",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "which python3.* 2>/dev/null; ls /usr/bin/python* /usr/local/bin/python* /root/miniconda*/bin/python* /root/anaconda*/bin/python* 2>/dev/null; conda info --envs 2>/dev/null | head -10",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T07:29:17.596847+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n/root/miniconda3/bin/python3\\n/root/miniconda3/bin/python3-config\\n/root/miniconda3/bin/python3.1\\n/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T07:29:17.596965+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python /tmp/decomposition_regression.py",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python /tmp/decomposition_regression.py",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T07:29:17.597113+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python /tmp/decomposition_regression.py'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T07:29:17.597285+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && wc -l output/exp_021_fewnerd_n8_seed123/samples.jsonl output/exp_021_fewnerd_n8_seed456/samples.jsonl output/exp_027_fewnerd_n16/samples.jsonl 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && wc -l output/exp_021_fewnerd_n8_seed123/samples.jsonl output/exp_021_fewnerd_n8_seed456/samples.jsonl output/exp_027_fewnerd_n16/samples.jsonl 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T07:29:17.597422+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     37648 output/exp_021_fewnerd_n8_seed123/samples.jsonl\\n     37648 output/exp_021_fewnerd_n8_seed456/samples.jsonl\\n      5000 output/exp_027_fewnerd_n16/samples.jsonl\\n     80296 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T07:29:17.597562+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && nohup /root/miniconda3/bin/python /tmp/decomposition_regression.py > /tmp/decomp_output.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && nohup /root/miniconda3/bin/python /tmp/decomposition_regression.py > /tmp/decomp_output.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T07:29:17.597687+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/autodl-tmp/struct_self_consist_ie && nohup /root/miniconda3/bin/python /tmp/decomposition_regression.py > /tmp/decomp_output.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=770146\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T07:29:17.597822+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "ps -p 770146 -o pid,state,etime 2>/dev/null; tail -5 /tmp/decomp_output.log 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ps -p 770146 -o pid,state,etime 2>/dev/null; tail -5 /tmp/decomp_output.log 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T07:29:17.597995+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID S     ELAPSED\\n770146 S       00:35\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.88}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T07:29:17.598167+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "ps -p 770146 -o pid,state,etime 2>/dev/null; wc -l /tmp/decomp_output.log 2>/dev/null; tail -20 /tmp/decomp_output.log 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ps -p 770146 -o pid,state,etime 2>/dev/null; wc -l /tmp/decomp_output.log 2>/dev/null; tail -20 /tmp/decomp_output.log 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T07:29:17.598313+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID S     ELAPSED\\n770146 S       00:39\\n0 /tmp/decomp_output.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T07:29:17.598452+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "sleep 30 && ps -p 770146 -o pid,state,etime 2>/dev/null; wc -l /tmp/decomp_output.log 2>/dev/null; cat /tmp/decomp_output.log 2>/dev/null",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "sleep 30 && ps -p 770146 -o pid,state,etime 2>/dev/null; wc -l /tmp/decomp_output.log 2>/dev/null; cat /tmp/decomp_output.log 2>/dev/null",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T07:29:17.598579+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'sleep 30 && ps -p 770146 -o pid,state,etime 2>/dev/null; wc -l /tmp/decomp_output.log 2>/dev/null; cat /tmp/decomp_output.log 2>/dev/null'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T07:29:17.598697+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "ps -p 770146 -o pid,state,etime 2>/dev/null; wc -l /tmp/decomp_output.log 2>/dev/null; head -30 /tmp/decomp_output.log 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ps -p 770146 -o pid,state,etime 2>/dev/null; wc -l /tmp/decomp_output.log 2>/dev/null; head -30 /tmp/decomp_output.log 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T07:29:17.598844+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID S     ELAPSED\\n50 /tmp/decomp_output.log\\n/tmp/decomposition_regression.py:233: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho_cv, _ = spearmanr(y_pred, y_test) if len(test_idx) >= 3 else (float('nan'), float('nan'))\\nSciERC                     d= 17.8%  Δ_oracle=+13.19  ρ_within=+0.1795  pred= +1.95  actual= +0.61\\nCoNLL                      d= 58.0%  Δ_oracle= +4.24  ρ_within=+0.3540  pred= +0.63  actual= -0.81\\nFewNERD                    d= 14.4%  Δ_oracle=+12.09  ρ_within=+0.5241  pred= +5.42  actual= +1.32\\nSciERC s123                d= 17.2%  Δ_oracle=+13.48  ρ_within=+0.1760  pred= +1.96  actual= -0.21\\nSciERC s456                d= 20.4%  Δ_oracle=+12.50  ρ_within=+0.1893  pred= +1.88  actual= -0.28\\nCoNLL s123                 d= 63.0%  Δ_oracle= +3.99  ρ_within=+0.3095  pred= +0.46  actual= -0.77\\nCoNLL s456                 d= 62.9%  Δ_oracle= +3.84  ρ_within=+0.3158  pred= +0.45  actual= -0.73\\nFewNERD s123               d= 13.1%  Δ_oracle=+12.92  ρ_within=+0.5080  pred= +5.70  actual= +1.44\\nFewNERD s456               d= 12.1%  Δ_oracle=+12.65  ρ_within=+0.5078  pred= +5.65  actual= +1.37\\nLLaMA SciERC s42           d= 24.9%  Δ_oracle=+12.88  ρ_within=+0.1542  pred= +1.49  actual= +0.19\\nLLaMA SciERC s123          d= 26.6%  Δ_oracle=+12.04  ρ_within=+0.1595  pred= +1.41  actual= -0.38\\nLLaMA SciERC s456          d= 27.4%  Δ_oracle=+11.73  ρ_within=+0.1765  pred= +1.50  actual= +0.10\\nLLaMA CoNLL s42            d= 89.4%  Δ_oracle= +2.11  ρ_within=+0.2032  pred= +0.05  actual= +0.14\\nLLaMA CoNLL s123           d= 89.3%  Δ_oracle= +2.00  ρ_within=+0.2313  pred= +0.05  actual= +0.11\\nLLaMA CoNLL s456           d= 89.4%  Δ_oracle= +2.06  ρ_within=+0.2329  pred= +0.05  actual= +0.02\\n3-epoch                    d=  6.4%  Δ_oracle=+14.97  ρ_within=+0.2727  pred= +3.82  actual= -1.18\\n10-epoch                   d= 47.8%  Δ_oracle
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-19T07:29:17.599008+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -30 /tmp/decomp_output.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -30 /tmp/decomp_output.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T07:29:17.599171+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"T=0.5                      d= 41.4%  Δ_oracle= +9.05  ρ_within=+0.1321  pred= +0.70  actual= -0.23\\nT=0.8                      d= 23.8%  Δ_oracle=+12.51  ρ_within=+0.1648  pred= +1.57  actual= +0.03\\nT=1.2                      d= 14.9%  Δ_oracle=+14.63  ρ_within=+0.2278  pred= +2.84  actual= -0.61\\n4B SciERC                  d= 10.4%  Δ_oracle=+13.02  ρ_within=+0.1894  pred= +2.21  actual= -2.23\\n4B CoNLL                   d= 90.6%  Δ_oracle= +1.70  ρ_within=+0.2423  pred= +0.04  actual= +0.09\\n\\n=== 23 configs processed ===\\n\\nFull-sample Spearman ρ = 0.0742 (p = 7.37e-01)\\nFull-sample Pearson r  = 0.3575 (p = 9.40e-02)\\nFull-sample R²         = -8.5316\\nFull-sample MAE        = 2.04 pp\\n\\nDataset groups: ['scierc', 'conll', 'fewnerd', 'llama_scierc', 'llama_conll', '4b_scierc', '4b_conll']\\n  scierc: 9 configs\\n  conll: 3 configs\\n  fewnerd: 3 configs\\n  llama_scierc: 3 configs\\n  llama_conll: 3 configs\\n  4b_scierc: 1 configs\\n  4b_conll: 1 configs\\n  LODO scierc              : R²=-1.2018, n_test=9, coef=0.2815, intercept=-0.5149\\n  LODO conll               : R²=-334.4859, n_test=3, coef=0.1341, intercept=-0.2422\\n  LODO fewnerd             : R²=-2932.6055, n_test=3, coef=-0.2375, intercept=0.0396\\n  LODO llama_scierc        : R²=-0.1986, n_test=3, coef=0.1700, intercept=-0.4047\\n  LODO llama_conll         : R²=-157.9217, n_test=3, coef=0.2172, intercept=-0.5616\\n  LODO 4b_scierc           : R²=nan, n_test=1, coef=0.1780, intercept=-0.3026\\n  LODO 4b_conll            : R²=nan, n_test=1, coef=0.1814, intercept=-0.4323\\n\\nSaved to /root/autodl-tmp/struct_self_consist_ie/output/decomposition_regression/regression_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T07:29:17.599381+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python -c \"\nimport json\nwith open('output/decomposition_regression/regression_results.json') as f:\n    d = json.load(f)\nprint('n_configs:', d['n_configs'])\nprint('full_sample:', json.dumps(d['full_sample'], indent=2))\nprint()\n# Also compute: if we use (1-d)*delta_oracle*rho_within as a SINGLE feature in OLS, what R2?\nimport numpy as np\nfrom sklearn.linear_model import LinearRegression\nfrom scipy.stats import spearmanr, pearsonr\n\npredicted = np.array([c['predicted_delta_f1_pp'] for c in d['configs']])\nactual = np.array([c['actual_delta_f1_pp'] for c in d['configs']])\n\n# Calibrated regression: actual = a * predicted + b\nreg = LinearRegression()\nreg.fit(predicted.reshape(-1,1), actual)\ny_hat = reg.predict(predicted.reshape(-1,1))\nss_res = np.sum((actual - y_hat)**2)\nss_tot = np.sum((actual - actual.mean())**2)\nr2_calibrated = 1 - ss_res / ss_tot\nprint(f'Calibrated R² (OLS: actual ~ predicted): {r2_calibrated:.4f}')\nprint(f'OLS coef: {reg.coef_[0]:.4f}, intercept: {reg.intercept_:.4f}')\n\n# Multi-factor regression: actual ~ (1-d)*delta_oracle, (1-d)*rho_within, etc.\nd_arr = np.array([c['d'] for c in d['configs']])\ndelta_oracle = np.array([c['delta_oracle_pp'] for c in d['configs']])\nrho_within = np.array([c['rho_within'] for c in d['configs']])\none_minus_d = 1 - d_arr\n\nX_multi = np.column_stack([one_minus_d, delta_oracle, rho_within])\nreg2 = LinearRegression()\nreg2.fit(X_multi, actual)\ny_hat2 = reg2.predict(X_multi)\nr2_multi = 1 - np.sum((actual - y_hat2)**2) / ss_tot\nprint(f'\\nMulti-factor R² (actual ~ (1-d), Δ_oracle, ρ_within): {r2_multi:.4f}')\nprint(f'Coefs: (1-d)={reg2.coef_[0]:.4f}, Δ_oracle={reg2.coef_[1]:.4f}, ρ_within={reg2.coef_[2]:.4f}, intercept={reg2.intercept_:.4f}')\n\n# Also try: actual ~ (1-d)*Δ_oracle (without rho_within)\nX_headroom = ((1-d_arr) * delta_oracle).reshape(-1, 1)\nreg3 = LinearRegression()\nreg3.fit(X_headroom, actual)\ny_hat3 = reg3.predict(X_headroom)\nr2_headroom = 1 - np.sum((actual - y_hat3)**2) / ss_tot\nrho_headroom, p_headroom = spearmanr(X_headroom.ravel(), actual)\nprint(f'\\nHeadroom-only R² (actual ~ (1-d)*Δ_oracle): {r2_headroom:.4f}')\nprint(f'Headroom-only Spearman ρ: {rho_headroom:.4f} (p={p_headroom:.4f})')\n\n# Spearman for individual factors\nfor name, vals in [('(1-d)', one_minus_d), ('Δ_oracle', delta_oracle), ('ρ_within', rho_within), ('(1-d)*Δ_oracle', (1-d_arr)*delta_oracle), ('predicted', predicted)]:\n    rho, p = spearmanr(vals, actual)\n    pr, pp_ = pearsonr(vals, actual)\n    print(f'{name:25s}: Spearman ρ={rho:+.4f} (p={p:.4f}), Pearson r={pr:+.4f} (p={pp_:.4f})')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python -c \"\nimport json\nwith open('output/decomposition_regression/regression_results.json') as f:\n    d = json.load(f)\nprint('n_configs:', d['n_configs'])\nprint('full_sample:', json.dumps(d['full_sample'], indent=2))\nprint()\n# Also compute: if we use (1-d)*delta_oracle*rho_within as a SINGLE feature in OLS, what R2?\nimport numpy as np\nfrom sklearn.linear_model import LinearRegression\nfrom scipy.stats import spearmanr, pearsonr\n\npredicted = np.array([c['predicted_delta_f1_pp'] for c in d['configs']])\nactual = np.array([c['actual_delta_f1_pp'] for c in d['configs']])\n\n# Calibrated regression: actual = a * predicted + b\nreg = LinearRegression()\nreg.fit(predicted.reshape(-1,1), actual)\ny_hat = reg.predict(predicted.reshape(-1,1))\nss_res = np.sum((actual - y_hat)**2)\nss_tot = np.sum((actual - actual.mean())**2)\nr2_calibrated = 1 - ss_res / ss_tot\nprint(f'Calibrated R² (OLS: actual ~ predicted): {r2_calibrated:.4f}')\nprint(f'OLS coef: {reg.coef_[0]:.4f}, intercept: {reg.intercept_:.4f}')\n\n# Multi-factor regression: actual ~ (1-d)*delta_oracle, (1-d)*rho_within, etc.\nd_arr = np.array([c['d'] for c in d['configs']])\ndelta_oracle = np.array([c['delta_oracle_pp'] for c in d['configs']])\nrho_within = np.array([c['rho_within'] for c in d['configs']])\none_minus_d = 1 - d_arr\n\nX_multi = np.column_stack([one_minus_d, delta_oracle, rho_within])\nreg2 = LinearRegression()\nreg2.fit(X_multi, actual)\ny_hat2 = reg2.predict(X_multi)\nr2_multi = 1 - np.sum((actual - y_hat2)**2) / ss_tot\nprint(f'\\nMulti-factor R² (actual ~ (1-d), Δ_oracle, ρ_within): {r2_multi:.4f}')\nprint(f'Coefs: (1-d)={reg2.coef_[0]:.4f}, Δ_oracle={reg2.coef_[1]:.4f}, ρ_within={reg2.coef_[2]:.4f}, intercept={reg2.intercept_:.4f}')\n\n# Also try: actual ~ (1-d)*Δ_oracle (without rho_within)\nX_headroom = ((1-d_arr) * delta_oracle).reshape(-1, 1)\nreg3 = LinearRegression()\nreg3.fit(X_headroom, actual)\ny_hat3 = reg3.predict(X_headroom)\nr2_headroom = 1 - np.sum((actual - y_hat3)**2) / ss_tot\nrho_headroom, p_headroom = spearmanr(X_headroom.ravel(), actual)\nprint(f'\\nHeadroom-only R² (actual ~ (1-d)*Δ_oracle): {r2_headroom:.4f}')\nprint(f'Headroom-only Spearman ρ: {rho_headroom:.4f} (p={p_headroom:.4f})')\n\n# Spearman for individual factors\nfor name, vals in [('(1-d)', one_minus_d), ('Δ_oracle', delta_oracle), ('ρ_within', rho_within), ('(1-d)*Δ_oracle', (1-d_arr)*delta_oracle), ('predicted', predicted)]:\n    rho, p = spearmanr(vals, actual)\n    pr, pp_ = pearsonr(vals, actual)\n    print(f'{name:25s}: Spearman ρ={rho:+.4f} (p={p:.4f}), Pearson r={pr:+.4f} (p={pp_:.4f})')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T07:29:17.599565+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"n_configs: 23\\nfull_sample: {\\n  \\\"spearman_rho\\\": 0.0742,\\n  \\\"spearman_p\\\": 0.736570958697109,\\n  \\\"pearson_r\\\": 0.3575,\\n  \\\"pearson_p\\\": 0.09400623987020823,\\n  \\\"r2\\\": -8.5316,\\n  \\\"mae_pp\\\": 2.04\\n}\\n\\nCalibrated R² (OLS: actual ~ predicted): 0.1278\\nOLS coef: 0.1682, intercept: -0.3848\\n\\nMulti-factor R² (actual ~ (1-d), Δ_oracle, ρ_within): 0.3129\\nCoefs: (1-d)=-7.3025, Δ_oracle=0.4350, ρ_within=5.0734, intercept=-0.9946\\n\\nHeadroom-only R² (actual ~ (1-d)*Δ_oracle): 0.0000\\nHeadroom-only Spearman ρ: -0.1077 (p=0.6247)\\n(1-d)                    : Spearman ρ=-0.0519 (p=0.8141), Pearson r=+0.0074 (p=0.9733)\\nΔ_oracle                 : Spearman ρ=-0.1126 (p=0.6088), Pearson r=+0.0234 (p=0.9158)\\nρ_within                 : Spearman ρ=-0.0375 (p=0.8649), Pearson r=+0.3791 (p=0.0745)\\n(1-d)*Δ_oracle           : Spearman ρ=-0.1077 (p=0.6247), Pearson r=-0.0031 (p=0.9888)\\npredicted                : Spearman ρ=+0.0742 (p=0.7366), Pearson r=+0.3575 (p=0.0940)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T07:29:17.599748+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python -c \"\nimport json\nwith open('output/decomposition_regression/regression_results.json') as f:\n    d = json.load(f)\nprint(f'Keys: {list(d.keys())}')\nprint(f'n_configs: {d[\\\"n_configs\\\"]}')\nprint(f'scatter_data has {len(d[\\\"scatter_data\\\"])} items')\nprint(f'LODO keys: {list(d[\\\"leave_one_dataset_out_cv\\\"].keys())}')\n# Quick check all configs have all fields\nfor c in d['configs']:\n    assert all(k in c for k in ['d', 'delta_oracle_pp', 'rho_within', 'actual_delta_f1_pp', 'predicted_delta_f1_pp']), f'Missing field in {c[\\\"label\\\"]}'\nprint('All configs have all required fields.')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && /root/miniconda3/bin/python -c \"\nimport json\nwith open('output/decomposition_regression/regression_results.json') as f:\n    d = json.load(f)\nprint(f'Keys: {list(d.keys())}')\nprint(f'n_configs: {d[\\\"n_configs\\\"]}')\nprint(f'scatter_data has {len(d[\\\"scatter_data\\\"])} items')\nprint(f'LODO keys: {list(d[\\\"leave_one_dataset_out_cv\\\"].keys())}')\n# Quick check all configs have all fields\nfor c in d['configs']:\n    assert all(k in c for k in ['d', 'delta_oracle_pp', 'rho_within', 'actual_delta_f1_pp', 'predicted_delta_f1_pp']), f'Missing field in {c[\\\"label\\\"]}'\nprint('All configs have all required fields.')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T07:29:17.599894+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Keys: ['n_configs', 'formula', 'configs', 'full_sample', 'leave_one_dataset_out_cv', 'scatter_data']\\nn_configs: 23\\nscatter_data has 23 items\\nLODO keys: ['scierc', 'conll', 'fewnerd', 'llama_scierc', 'llama_conll', '4b_scierc', '4b_conll']\\nAll configs have all required fields.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_23config_regression_20260519T072221",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-19T07:29:17.600066+00:00_

结果保存在 `output/decomposition_regression/regression_results.json`。

---

## 汇报

### 23 Configs 完整列表

| Config | d (%) | Δ_oracle (pp) | ρ_within | Predicted (pp) | Actual (pp) |
|--------|------:|------:|------:|------:|------:|
| SciERC s42 | 17.8 | +13.19 | +0.18 | +1.95 | +0.61 |
| CoNLL s42 | 58.0 | +4.24 | +0.35 | +0.63 | -0.81 |
| FewNERD s42 | 14.4 | +12.09 | +0.52 | +5.42 | +1.32 |
| SciERC s123 | 17.2 | +13.48 | +0.18 | +1.96 | -0.21 |
| SciERC s456 | 20.4 | +12.50 | +0.19 | +1.88 | -0.28 |
| CoNLL s123 | 63.0 | +3.99 | +0.31 | +0.46 | -0.77 |
| CoNLL s456 | 62.9 | +3.84 | +0.32 | +0.45 | -0.73 |
| FewNERD s123 | 13.1 | +12.92 | +0.51 | +5.70 | +1.44 |
| FewNERD s456 | 12.1 | +12.65 | +0.51 | +5.65 | +1.37 |
| LLaMA SciERC s42 | 24.9 | +12.88 | +0.15 | +1.49 | +0.19 |
| LLaMA SciERC s123 | 26.6 | +12.04 | +0.16 | +1.41 | -0.38 |
| LLaMA SciERC s456 | 27.4 | +11.73 | +0.18 | +1.50 | +0.10 |
| LLaMA CoNLL s42 | 89.4 | +2.11 | +0.20 | +0.05 | +0.14 |
| LLaMA CoNLL s123 | 89.3 | +2.00 | +0.23 | +0.05 | +0.11 |
| LLaMA CoNLL s456 | 89.4 | +2.06 | +0.23 | +0.05 | +0.02 |
| 3-epoch | 6.4 | +14.97 | +0.27 | +3.82 | -1.18 |
| 10-epoch | 47.8 | +8.64 | +0.07 | +0.31 | +0.99 |
| rank=8 | 7.2 | +16.01 | +0.24 | +3.63 | -0.47 |
| T=0.5 | 41.4 | +9.05 | +0.13 | +0.70 | -0.23 |
| T=0.8 | 23.8 | +12.51 | +0.16 | +1.57 | +0.03 |
| T=1.2 | 14.9 | +14.63 | +0.23 | +2.84 | -0.61 |
| 4B SciERC | 10.4 | +13.02 | +0.19 | +2.21 | -2.23 |
| 4B CoNLL | 90.6 | +1.70 | +0.24 | +0.04 | +0.09 |

### Full-sample 统计

| Metric | Value |
|--------|-------|
| Spearman ρ | 0.074 (p=0.737) |
| Pearson r | 0.358 (p=0.094) |
| R² (raw formula) | **-8.53** |
| R² (calibrated OLS) | 0.128 |
| MAE | 2.04 pp |

### Leave-one-dataset-out CV R²

全部为大幅负值（-1.2 到 -2933），公式在交叉验证中完全无预测力。

### 各因子单独与 actual ΔF1 的相关性

- (1-d): Spearman ρ = -0.05 (p=0.81)
- Δ_oracle: Spearman ρ = -0.11 (p=0.61)
- ρ_within: Spearman ρ = -0.04 (p=0.86), Pearson r = +0.38 (p=0.07)
- (1-d)×Δ_oracle: Spearman ρ = -0.11 (p=0.62)

### 结论

**分解公式 ΔF1 ≈ (1-d) × Δ_oracle × ρ_within 不具备预测力。**

核心问题：
1. **系统性高估**：predicted 始终为正（因 ρ_within > 0），但 23 configs 中 13 个 actual ΔF1 为负
2. **FewNERD 极端过估**：predicted ~5.5 pp vs actual ~1.4 pp（4x 偏差）
3. **极端失配**：3-epoch (pred +3.82, actual -1.18)、rank=8 (pred +3.63, actual -0.47)、4B SciERC (pred +2.21, actual -2.23)
4. **三因子无单独预测力**：没有任何一个因子与 actual ΔF1 有显著 Spearman 相关
5. 唯一略有信号的是 ρ_within 的 Pearson r = 0.38 (p=0.07)，但这不足以支撑公式

根本原因：within-instance Spearman ρ（仅 8 samples）的正均值不代表 LP 选择能有效捕获 oracle gap。ρ_within 作为乘法因子的假设在小样本下不成立。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_23config_regression_20260519T072221"
}
```

</details>

---
