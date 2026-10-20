# experiment d126 drc folio

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/chats/worker_experiment_d126-drc-folio_20260521T082219.jsonl`
- **Structured JSON:** [`e49f2b9a1aafc2db0871.json`](../../sessions/e4/e49f2b9a1aafc2db0871.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

39 recorded events

### Tool call

_source line 1 · 2026-05-21T08:25:31.222083+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T08:25:31.223034+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T08:25:31.223298+00:00_

called mcp__agent-ml-research__detect_image

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image</summary>

```json
{
  "server": "westd-25068"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__detect_image",
  "tool_args": {
    "server": "westd-25068"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T08:25:31.223444+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T08:25:31.223585+00:00_

{"result":"{\n  \"detected\": false,\n  \"status\": \"ssh_error\",\n  \"skip_base_setup\": false,\n  \"message\": \"SSH error: exit code 1\"\n}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__detect_image",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T08:25:31.223712+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus/ -name \"*drc*\" -o -name \"*cascade*\" -o -name \"*disagreement*\" "
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus/ -name \"*drc*\" -o -name \"*cascade*\" -o -name \"*disagreement*\" "
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T08:25:31.223918+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"adaptive_sica_validation.json\\nalpha_recompute_25068.json\\nalpha_sensitivity_exp033.json\\nanalysis_tasks_356.json\\ncase_study_constraints.json\\ncase_study_normalized.json\\ncondorcet_independence_analysis.json\\nconfirmation_bias\\ncross_model_experiment\\ncross_model_kappa\\ncross_model_mistral_folio\\ndir_f3_cross_model_verification\\ndir_i2_single_model_baselines\\ndir_i3_sica_qwen3_14b\\ndir_i_hge_pilot\\ndir_j2_nli_qwen3\\ndir_j3_nli_multi_verifier\\ndir_l2_single_trace_n204\\ndir_l_single_trace\\ndir_n_oracle_bestofk\\ndir_n_oracle_qwen3t_n204\\ndirection_a_atom_pilot20.json\\ndirection_a_prove\\ndirection_b_deepconf\\ndirection_c_counterfactual_pilot.json\\ndirection_e_abstention\\ndirection_f_blind_fol\\ndirection_g_decoupling\\ndirection_g_dryrun.log\\ndirection_g_vllm.log\\ndirection_i_z3_filter\\ndirection_r_deberta\\ndirection_r_nli_large\\ndirection_r_nli_pw600\\ndirection_r_nli_small\\ndirection_rg_combo\\ndisc_filter_full.log\\ndisc_filter_test.log\\ndiscriminative_filter_exp033.json\\ndiscriminative_filter_exp033_test.json\\ndiscriminative_filter_exp044b.json\\ndiscriminative_filter_exp046.json\\ndiscriminative_filter_exp054.json\\ndrc_cascade_pilot\\nexp-007-qwen72b-awq\\nexp-029-contrastive-folio204\\nexp004_qwen7b_rerun\\nexp013_constraint_ablation\\nexp027_qwen3_14b_nonthinking\\nexp028_qwen3_14b_thinking\\nexp028b_discordant_tracking.json\\nexp028b_qwen3_thinking_folio204\\nexp033_mistral_7b_folio204\\nexp033_per_problem_analysis.json\\nexp033_per_problem_analysis_v2.json\\nexp034_llama31_8b_folio204\\nexp034_qwen25_14b_proofwriter\\nexp035_qwen25_7b_folio204\\nexp036_z3_feedback\\nexp036b_cross_trace_unsat.json\\nexp044b_icl_oracle_qwen14b\\nexp045b_backward_qwen14b\\nexp046_mistral_7b_pw600\\nexp047_qwen3_thinking_folio204\\nexp051_mistral_k_sensitivity\\nexp054_mistral_folio204_t10\\nexp057_mistral_folio204_t03\\nexp058_mistral_folio204_t05\\nexp059_cross_qwen3_extractor\\nexp05_bac
…[truncated 1842 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T08:25:31.224100+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/scripts/drc_cascade_pilot.py\\n/root/symb_invariant_consensus/results/drc_cascade_pilot\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T08:25:31.224251+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/scripts/drc_cascade_pilot.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/scripts/drc_cascade_pilot.py"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T08:25:31.224474+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"DRC (Disagreement-Routed Cascade) pilot: Mistral-7B ProofWriter 600.\\\"\\\"\\\"\\nimport json\\nimport os\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\n\\nRESULTS_DIR = \\\"/root/symb_invariant_consensus/results\\\"\\nSC_PATH = f\\\"{RESULTS_DIR}/exp046_mistral_7b_pw600/exp046_results.json\\\"\\nNLI_PATH = f\\\"{RESULTS_DIR}/direction_r_nli_pw600/results.json\\\"\\nOUT_DIR = f\\\"{RESULTS_DIR}/drc_cascade_pilot\\\"\\nVALID_ANSWERS = {\\\"True\\\", \\\"False\\\", \\\"Unknown\\\"}\\nK = 12\\nW = 3\\nTAUS = [0.3, 0.5, 0.7, 0.9]\\n\\n\\ndef majority_vote(vote_dist, tiebreak_alpha=True):\\n    if not vote_dist:\\n        return \\\"Unknown\\\"\\n    max_count = max(vote_dist.values())\\n    winners = [k for k, v in vote_dist.items() if v == max_count]\\n    if tiebreak_alpha:\\n        winners.sort()\\n    return winners[0]\\n\\n\\ndef filter_valid(vote_dist):\\n    return {k: v for k, v in vote_dist.items() if k in VALID_ANSWERS}\\n\\n\\ndef combo_answer(sc_dist, nli_pred, w):\\n    combined = dict(filter_valid(sc_dist))\\n    combined[nli_pred] = combined.get(nli_pred, 0) + w\\n    return majority_vote(combined)\\n\\n\\ndef main():\\n    with open(SC_PATH) as f:\\n        sc_data = json.load(f)\\n    with open(NLI_PATH) as f:\\n        nli_data = json.load(f)\\n\\n    sc_results = sc_data[\\\"results\\\"]\\n    nli_per_q = nli_data[\\\"per_question\\\"]\\n\\n    questions = []\\n    for r in sc_results:\\n        pid = r[\\\"problem_id\\\"]\\n        if pid not in nli_per_q:\\n            continue\\n        nli_q = nli_per_q[pid]\\n        valid_dist = filter_valid(r[\\\"sc_vote_distribution\\\"])\\n        total_valid = sum(valid_dist.values())\\n        if total_valid == 0:\\n            agreement = 0.0\\n        else:\\n            agreement = max(valid_dist.values()) / total_valid\\n        sc_ans = majority_vote(valid_dist)\\n        questions.append({\\n  
…[truncated 4236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T08:25:31.224682+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/drc_cascade_pilot/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/drc_cascade_pilot/"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T08:25:31.224906+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"agreement_distribution.png\\npareto_front.pdf\\npareto_front.png\\nresults.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T08:25:31.225091+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/direction_r_nli_large/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/direction_r_nli_large/"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T08:25:31.225227+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/nli_combo_full_table_bh/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/nli_combo_full_table_bh/"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T08:25:31.225356+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T08:25:31.225481+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T08:25:31.225616+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T08:25:31.225743+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"constraint_cache\\nexp033.log\\nexp033_results.json\\nintermediates\\nsc_answer_matrix.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T08:25:31.225861+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/results/direction_r_nli_large/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/results/direction_r_nli_large/results.json"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T08:25:31.226284+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_r1_deberta_standalone\\\": {\\n    \\\"accuracy\\\": 0.4951,\\n    \\\"correct\\\": 101,\\n    \\\"total\\\": 204,\\n    \\\"per_class\\\": {\\n      \\\"True\\\": {\\n        \\\"n\\\": 72,\\n        \\\"correct\\\": 43,\\n        \\\"accuracy\\\": 0.5972,\\n        \\\"precision\\\": 0.5181,\\n        \\\"recall\\\": 0.5972,\\n        \\\"f1\\\": 0.5548\\n      },\\n      \\\"False\\\": {\\n        \\\"n\\\": 63,\\n        \\\"correct\\\": 45,\\n        \\\"accuracy\\\": 0.7143,\\n        \\\"precision\\\": 0.4545,\\n        \\\"recall\\\": 0.7143,\\n        \\\"f1\\\": 0.5556\\n      },\\n      \\\"Unknown\\\": {\\n        \\\"n\\\": 69,\\n        \\\"correct\\\": 13,\\n        \\\"accuracy\\\": 0.1884,\\n        \\\"precision\\\": 0.5909,\\n        \\\"recall\\\": 0.1884,\\n        \\\"f1\\\": 0.2857\\n      }\\n    },\\n    \\\"gt_distribution\\\": {\\n      \\\"Unknown\\\": 69,\\n      \\\"True\\\": 72,\\n      \\\"False\\\": 63\\n    },\\n    \\\"pred_distribution\\\": {\\n      \\\"True\\\": 83,\\n      \\\"False\\\": 99,\\n      \\\"Unknown\\\": 22\\n    },\\n    \\\"inference_time_s\\\": 42.1,\\n    \\\"model\\\": \\\"/root/models/deberta-large-mnli\\\"\\n  },\\n  \\\"exp_r2_verifier\\\": {\\n    \\\"agreement_rate\\\": 0.451,\\n    \\\"agree_count\\\": 92,\\n    \\\"disagree_count\\\": 112,\\n    \\\"agree_accuracy\\\": 0.6848,\\n    \\\"disagree_breakdown\\\": {\\n      \\\"deberta_correct_sc_wrong\\\": 38,\\n      \\\"sc_correct_deberta_wrong\\\": 48,\\n      \\\"both_wrong\\\": 26\\n    },\\n    \\\"strategies\\\": {\\n      \\\"abstain\\\": {\\n        \\\"coverage\\\": 0.451,\\n        \\\"accuracy\\\": 0.6848\\n      },\\n      \\\"deberta_override\\\": {\\n        \\\"accuracy\\\": 0.4951\\n      },\\n      \\\"sc_baseline\\\": {\\n        \\\"accuracy\\\": 0.5441\\n      }\\n    },\\n    \\\"deberta_corrects_sc\\\": [\\n      \\\"folio_2\\\",\\n      \\\"folio_5\\\",\\n      \\\
…[truncated 9202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T08:25:31.226470+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/results/nli_combo_full_table_bh/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/results/nli_combo_full_table_bh/results.json"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T08:25:31.226761+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"description\\\": \\\"NLI Combo Full Table with Benjamini-Hochberg Correction\\\",\\n  \\\"dataset\\\": \\\"ProofWriter-D5-600\\\",\\n  \\\"verifier\\\": \\\"microsoft/deberta-large-mnli\\\",\\n  \\\"deberta_standalone_accuracy\\\": 0.55,\\n  \\\"n_tests\\\": 12,\\n  \\\"alpha\\\": 0.05,\\n  \\\"bh_significant_count\\\": 4,\\n  \\\"source_files\\\": {\\n    \\\"Mistral-7B\\\": \\\"westd-25068:direction_r_nli_pw600 + exp046_mistral_7b_pw600\\\",\\n    \\\"LLaMA-3.1-8B\\\": \\\"westd-16639:exp092_llama8b_pw_nli_combo\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"westd-16639:qwen14b_pw_nli_combo\\\",\\n    \\\"Qwen3-14B\\\": \\\"westd-16639:d116_qwen3_pw_deberta_large\\\",\\n    \\\"LLaMA-SC-baseline\\\": \\\"westd-16639:exp048_llama8b_pw600 (SC=0.70 confirmed)\\\"\\n  },\\n  \\\"generators\\\": {\\n    \\\"Mistral-7B\\\": {\\n      \\\"n\\\": 600,\\n      \\\"sc_accuracy\\\": 0.3933,\\n      \\\"sc_accuracy_pct\\\": 39.33,\\n      \\\"capability_gap_pp\\\": 15.67,\\n      \\\"w1\\\": {\\n        \\\"combo_accuracy\\\": 0.4017,\\n        \\\"combo_accuracy_pct\\\": 40.17,\\n        \\\"delta_pp\\\": 0.83,\\n        \\\"discordant\\\": [\\n          4,\\n          9\\n        ],\\n        \\\"p_raw\\\": 0.2668457031,\\n        \\\"p_bh\\\": 0.3557942708,\\n        \\\"significant_bh_005\\\": false\\n      },\\n      \\\"w3\\\": {\\n        \\\"combo_accuracy\\\": 0.4283,\\n        \\\"combo_accuracy_pct\\\": 42.83,\\n        \\\"delta_pp\\\": 3.5,\\n        \\\"discordant\\\": [\\n          22,\\n          43\\n        ],\\n        \\\"p_raw\\\": 0.0125025461,\\n        \\\"p_bh\\\": 0.0375076384,\\n        \\\"significant_bh_005\\\": true\\n      },\\n      \\\"w5\\\": {\\n        \\\"combo_accuracy\\\": 0.5,\\n        \\\"combo_accuracy_pct\\\": 50.0,\\n        \\\"delta_pp\\\": 10.67,\\n        \\\"discordant\\\": [\\n          35,\\n          99\\n        ],\\n        \\\"p_raw\\\": 2.89e-08,\\n        \\\"p_bh\
…[truncated 7137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T08:25:31.227044+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -80 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -80 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T08:25:31.227269+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 204,\\n    \\\"sica_accuracy\\\": 0.5931372549019608,\\n    \\\"sc_accuracy\\\": 0.5441176470588235,\\n    \\\"sica_correct\\\": 121,\\n    \\\"sc_correct\\\": 111,\\n    \\\"extraction_rate\\\": 0.9714052287581699,\\n    \\\"total_constraints_extracted\\\": 14042,\\n    \\\"total_unique_constraints\\\": 8021,\\n    \\\"contradiction_rate\\\": 0.03503303827452936,\\n    \\\"problems_with_contradictions\\\": 128,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"validation\\\": {\\n        \\\"sica\\\": 0.5931372549019608,\\n        \\\"sc\\\": 0.5441176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.5931372549019608,\\n        \\\"sc\\\": 0.5441176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 4881.8\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"folio_0\\\",\\n      \\\"problem\\\": \\\"Given the following premises:\\\\nIf people perform in school talent shows often, then they attend and are very engaged with school events. People either perform in school talent shows often or are inactive and disinterested members of their community. If people chaperone high school dances, then they are not students who attend the school. All people who are inactive and disinterested members of their community chaperone high school dances. All young children and teenagers who wish to further their academic careers and educational opportunities are students who attend the school. Bonnie either both attends and is very engaged with school events and is a student who attends the school, or she neither attends and is very engaged with school events nor is a student who attends the school.\\\\n\\\\nDetermine whether the following conclusion
…[truncated 2950 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T08:25:31.227568+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "cat > /root/symb_invariant_consensus/scripts/drc_cascade_folio.py << 'PYEOF'\n\"\"\"DRC (Disagreement-Routed Cascade) on FOLIO-204: Mistral-7B + DeBERTa-large-mnli.\"\"\"\nimport json\nimport os\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\nRESULTS_DIR = \"/root/symb_invariant_consensus/results\"\nSC_PATH = f\"{RESULTS_DIR}/exp033_mistral_7b_folio204/exp033_results.json\"\nNLI_PATH = f\"{RESULTS_DIR}/direction_r_nli_large/results.json\"\nOUT_DIR = f\"{RESULTS_DIR}/exp_d126_drc_folio\"\nVALID_ANSWERS = {\"True\", \"False\", \"Unknown\"}\nK = 12\nTAUS = [0.3, 0.5, 0.6, 0.7, 0.8, 0.9]\nWEIGHTS = [1, 3]\n\n\ndef majority_vote(vote_dist, tiebreak_alpha=True):\n    if not vote_dist:\n        return \"Unknown\"\n    max_count = max(vote_dist.values())\n    winners = [k for k, v in vote_dist.items() if v == max_count]\n    if tiebreak_alpha:\n        winners.sort()\n    return winners[0]\n\n\ndef filter_valid(vote_dist):\n    return {k: v for k, v in vote_dist.items() if k in VALID_ANSWERS}\n\n\ndef combo_answer(sc_dist, nli_pred, w):\n    combined = dict(filter_valid(sc_dist))\n    combined[nli_pred] = combined.get(nli_pred, 0) + w\n    return majority_vote(combined)\n\n\ndef main():\n    with open(SC_PATH) as f:\n        sc_data = json.load(f)\n    with open(NLI_PATH) as f:\n        nli_data = json.load(f)\n\n    sc_results = sc_data[\"results\"]\n    nli_per_q = nli_data[\"per_question\"]\n\n    questions = []\n    for r in sc_results:\n        pid = r[\"problem_id\"]\n        if pid not in nli_per_q:\n            continue\n        nli_q = nli_per_q[pid]\n        valid_dist = filter_valid(r[\"sc_vote_distribution\"])\n        total_valid = sum(valid_dist.values())\n        agreement = max(valid_dist.values()) / total_valid if total_valid > 0 else 0.0\n        sc_ans = majority_vote(valid_dist)\n        q = {\n            \"pid\": pid,\n            \"gold\": r[\"ground_truth\"],\n            \"sc_dist\": r[\"sc_vote_distribution\"],\n            \"sc_answer\": sc_ans,\n            \"agreement\": agreement,\n            \"nli_pred\": nli_q[\"deberta_pred\"],\n        }\n        for w in WEIGHTS:\n            q[f\"combo_w{w}\"] = combo_answer(r[\"sc_vote_distribution\"], nli_q[\"deberta_pred\"], w)\n        questions.append(q)\n\n    n = len(questions)\n    sc_correct = sum(1 for q in questions if q[\"sc_answer\"] == q[\"gold\"])\n\n    results = {\n        \"experiment\": \"exp-d126-drc-folio\",\n        \"dataset\": \"FOLIO-204\",\n        \"generator\": \"Mistral-7B\",\n        \"verifier\": \"DeBERTa-large-mnli\",\n        \"K\": K,\n        \"n_questions\": n,\n        \"baselines\": {\n            \"sc_only\": {\"accuracy\": sc_correct / n, \"correct\": sc_correct},\n        },\n        \"full_combo\": {},\n        \"drc\": {},\n    }\n\n    for w in WEIGHTS:\n        key = f\"w{w}\"\n        combo_corr = sum(1 for q in questions if q[f\"combo_{key}\"] == q[\"gold\"])\n        results[\"full_combo\"][key] = {\n            \"accuracy\": combo_corr / n,\n            \"correct\": combo_corr,\n            \"nli_calls\": n,\n            \"cost_ratio\": 1.0,\n        }\n\n    for tau in TAUS:\n        for w in WEIGHTS:\n            wkey = f\"w{w}\"\n            drc_correct = 0\n            nli_invoked = 0\n            per_q_details = []\n            for q in questions:\n                if q[\"agreement\"] > tau:\n                    pred = q[\"sc_answer\"]\n                    used_nli = False\n                else:\n                    pred = q[f\"combo_{wkey}\"]\n                    nli_invoked += 1\n                    used_nli = True\n                correct = pred == q[\"gold\"]\n                if correct:\n                    drc_correct += 1\n                per_q_details.append({\n                    \"pid\": q[\"pid\"],\n                    \"agreement\": round(q[\"agreement\"], 4),\n                    \"used_nli\": used_nli,\n                    \"pred\": pred,\n                    \"gold\": q[\"gold\"],\n                    \"correct\": correct,\n                })\n\n            results[\"drc\"][f\"tau={tau}_{wkey}\"] = {\n                \"tau\": tau,\n                \"weight\": w,\n                \"accuracy\": round(drc_correct / n, 4),\n                \"correct\": drc_correct,\n                \"nli_invoked\": nli_invoked,\n                \"nli_invocation_rate\": round(nli_invoked / n, 4),\n                \"cost_ratio_pct\": round(nli_invoked / n * 100, 1),\n                \"sc_only_count\": n - nli_invoked,\n                \"gain_recovery_pct\": None,\n            }\n            # gain recovery: fraction of full combo gain recovered\n            combo_acc = results[\"full_combo\"][wkey][\"accuracy\"]\n            sc_acc = results[\"baselines\"][\"sc_only\"][\"accuracy\"]\n            full_gain = combo_acc - sc_acc\n            drc_gain = drc_correct / n - sc_acc\n            if full_gain > 0:\n                results[\"drc\"][f\"tau={tau}_{wkey}\"][\"gain_recovery_pct\"] = round(drc_gain / full_gain * 100, 1)\n\n    os.makedirs(OUT_DIR, exist_ok=True)\n    with open(f\"{OUT_DIR}/results.json\", \"w\") as f:\n        json.dump(results, f, indent=2)\n\n    # Pareto front plot (w=3)\n    fig, ax = plt.subplots(1, 1, figsize=(6, 4))\n    for w in WEIGHTS:\n        wkey = f\"w{w}\"\n        xs, ys, labels = [], [], []\n        for tau in TAUS:\n            r = results[\"drc\"][f\"tau={tau}_{wkey}\"]\n            xs.append(r[\"nli_invocation_rate\"] * 100)\n            ys.append(r[\"accuracy\"] * 100)\n            labels.append(f\"τ={tau}\")\n        color = \"#2563eb\" if w == 3 else \"#94a3b8\"\n        ax.plot(xs, ys, \"o-\", color=color, markersize=7, linewidth=2, zorder=3, label=f\"DRC w={w}\")\n        if w == 3:\n            for x, y, label in zip(xs, ys, labels):\n                ax.annotate(label, (x, y), textcoords=\"offset points\", xytext=(8, 6), fontsize=8)\n\n    sc_acc = results[\"baselines\"][\"sc_only\"][\"accuracy\"] * 100\n    combo3_acc = results[\"full_combo\"][\"w3\"][\"accuracy\"] * 100\n    ax.axhline(sc_acc, color=\"gray\", linestyle=\"--\", linewidth=1, label=f\"SC-only ({sc_acc:.1f}%)\")\n    ax.axhline(combo3_acc, color=\"orange\", linestyle=\"--\", linewidth=1, label=f\"Full combo w=3 ({combo3_acc:.1f}%)\")\n\n    ax.set_xlabel(\"NLI Invocation Rate (%)\", fontsize=11)\n    ax.set_ylabel(\"Accuracy (%)\", fontsize=11)\n    ax.set_title(\"DRC Cascade: Mistral-7B FOLIO-204\", fontsize=12)\n    ax.legend(fontsize=8, loc=\"lower right\")\n    ax.set_xlim(-5, 105)\n    ax.grid(True, alpha=0.3)\n    plt.tight_layout()\n    plt.savefig(f\"{OUT_DIR}/pareto_front.pdf\", bbox_inches=\"tight\")\n    plt.savefig(f\"{OUT_DIR}/pareto_front.png\", dpi=150, bbox_inches=\"tight\")\n\n    # Agreement distribution\n    agreements = [q[\"agreement\"] for q in questions]\n    fig2, ax2 = plt.subplots(1, 1, figsize=(6, 3.5))\n    ax2.hist(agreements, bins=20, color=\"#2563eb\", alpha=0.7, edgecolor=\"white\")\n    for tau in TAUS:\n        ax2.axvline(tau, color=\"red\", linestyle=\"--\", alpha=0.5, linewidth=1)\n    ax2.set_xlabel(\"SC Agreement (majority fraction)\", fontsize=11)\n    ax2.set_ylabel(\"Count\", fontsize=11)\n    ax2.set_title(\"FOLIO-204: Per-Question SC Agreement Distribution\", fontsize=12)\n    plt.tight_layout()\n    plt.savefig(f\"{OUT_DIR}/agreement_distribution.png\", dpi=150, bbox_inches=\"tight\")\n\n    print(json.dumps(results, indent=2))\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"DONE\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat > /root/symb_invariant_consensus/scripts/drc_cascade_folio.py << 'PYEOF'\n\"\"\"DRC (Disagreement-Routed Cascade) on FOLIO-204: Mistral-7B + DeBERTa-large-mnli.\"\"\"\nimport json\nimport os\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\nRESULTS_DIR = \"/root/symb_invariant_consensus/results\"\nSC_PATH = f\"{RESULTS_DIR}/exp033_mistral_7b_folio204/exp033_results.json\"\nNLI_PATH = f\"{RESULTS_DIR}/direction_r_nli_large/results.json\"\nOUT_DIR = f\"{RESULTS_DIR}/exp_d126_drc_folio\"\nVALID_ANSWERS = {\"True\", \"False\", \"Unknown\"}\nK = 12\nTAUS = [0.3, 0.5, 0.6, 0.7, 0.8, 0.9]\nWEIGHTS = [1, 3]\n\n\ndef majority_vote(vote_dist, tiebreak_alpha=True):\n    if not vote_dist:\n        return \"Unknown\"\n    max_count = max(vote_dist.values())\n    winners = [k for k, v in vote_dist.items() if v == max_count]\n    if tiebreak_alpha:\n        winners.sort()\n    return winners[0]\n\n\ndef filter_valid(vote_dist):\n    return {k: v for k, v in vote_dist.items() if k in VALID_ANSWERS}\n\n\ndef combo_answer(sc_dist, nli_pred, w):\n    combined = dict(filter_valid(sc_dist))\n    combined[nli_pred] = combined.get(nli_pred, 0) + w\n    return majority_vote(combined)\n\n\ndef main():\n    with open(SC_PATH) as f:\n        sc_data = json.load(f)\n    with open(NLI_PATH) as f:\n        nli_data = json.load(f)\n\n    sc_results = sc_data[\"results\"]\n    nli_per_q = nli_data[\"per_question\"]\n\n    questions = []\n    for r in sc_results:\n        pid = r[\"problem_id\"]\n        if pid not in nli_per_q:\n            continue\n        nli_q = nli_per_q[pid]\n        valid_dist = filter_valid(r[\"sc_vote_distribution\"])\n        total_valid = sum(valid_dist.values())\n        agreement = max(valid_dist.values()) / total_valid if total_valid > 0 else 0.0\n        sc_ans = majority_vote(valid_dist)\n        q = {\n            \"pid\": pid,\n            \"gold\": r[\"ground_truth\"],\n            \"sc_dist\": r[\"sc_vote_distribution\"],\n            \"sc_answer\": sc_ans,\n            \"agreement\": agreement,\n            \"nli_pred\": nli_q[\"deberta_pred\"],\n        }\n        for w in WEIGHTS:\n            q[f\"combo_w{w}\"] = combo_answer(r[\"sc_vote_distribution\"], nli_q[\"deberta_pred\"], w)\n        questions.append(q)\n\n    n = len(questions)\n    sc_correct = sum(1 for q in questions if q[\"sc_answer\"] == q[\"gold\"])\n\n    results = {\n        \"experiment\": \"exp-d126-drc-folio\",\n        \"dataset\": \"FOLIO-204\",\n        \"generator\": \"Mistral-7B\",\n        \"verifier\": \"DeBERTa-large-mnli\",\n        \"K\": K,\n        \"n_questions\": n,\n        \"baselines\": {\n            \"sc_only\": {\"accuracy\": sc_correct / n, \"correct\": sc_correct},\n        },\n        \"full_combo\": {},\n        \"drc\": {},\n    }\n\n    for w in WEIGHTS:\n        key = f\"w{w}\"\n        combo_corr = sum(1 for q in questions if q[f\"combo_{key}\"] == q[\"gold\"])\n        results[\"full_combo\"][key] = {\n            \"accuracy\": combo_corr / n,\n            \"correct\": combo_corr,\n            \"nli_calls\": n,\n            \"cost_ratio\": 1.0,\n        }\n\n    for tau in TAUS:\n        for w in WEIGHTS:\n            wkey = f\"w{w}\"\n            drc_correct = 0\n            nli_invoked = 0\n            per_q_details = []\n            for q in questions:\n                if q[\"agreement\"] > tau:\n                    pred = q[\"sc_answer\"]\n                    used_nli = False\n                else:\n                    pred = q[f\"combo_{wkey}\"]\n                    nli_invoked += 1\n                    used_nli = True\n                correct = pred == q[\"gold\"]\n                if correct:\n                    drc_correct += 1\n                per_q_details.append({\n                    \"pid\": q[\"pid\"],\n                    \"agreement\": round(q[\"agreement\"], 4),\n                    \"used_nli\": used_nli,\n                    \"pred\": pred,\n                    \"gold\": q[\"gold\"],\n                    \"correct\": correct,\n                })\n\n            results[\"drc\"][f\"tau={tau}_{wkey}\"] = {\n                \"tau\": tau,\n                \"weight\": w,\n                \"accuracy\": round(drc_correct / n, 4),\n                \"correct\": drc_correct,\n                \"nli_invoked\": nli_invoked,\n                \"nli_invocation_rate\": round(nli_invoked / n, 4),\n                \"cost_ratio_pct\": round(nli_invoked / n * 100, 1),\n                \"sc_only_count\": n - nli_invoked,\n                \"gain_recovery_pct\": None,\n            }\n            # gain recovery: fraction of full combo gain recovered\n            combo_acc = results[\"full_combo\"][wkey][\"accuracy\"]\n            sc_acc = results[\"baselines\"][\"sc_only\"][\"accuracy\"]\n            full_gain = combo_acc - sc_acc\n            drc_gain = drc_correct / n - sc_acc\n            if full_gain > 0:\n                results[\"drc\"][f\"tau={tau}_{wkey}\"][\"gain_recovery_pct\"] = round(drc_gain / full_gain * 100, 1)\n\n    os.makedirs(OUT_DIR, exist_ok=True)\n    with open(f\"{OUT_DIR}/results.json\", \"w\") as f:\n        json.dump(results, f, indent=2)\n\n    # Pareto front plot (w=3)\n    fig, ax = plt.subplots(1, 1, figsize=(6, 4))\n    for w in WEIGHTS:\n        wkey = f\"w{w}\"\n        xs, ys, labels = [], [], []\n        for tau in TAUS:\n            r = results[\"drc\"][f\"tau={tau}_{wkey}\"]\n            xs.append(r[\"nli_invocation_rate\"] * 100)\n            ys.append(r[\"accuracy\"] * 100)\n            labels.append(f\"τ={tau}\")\n        color = \"#2563eb\" if w == 3 else \"#94a3b8\"\n        ax.plot(xs, ys, \"o-\", color=color, markersize=7, linewidth=2, zorder=3, label=f\"DRC w={w}\")\n        if w == 3:\n            for x, y, label in zip(xs, ys, labels):\n                ax.annotate(label, (x, y), textcoords=\"offset points\", xytext=(8, 6), fontsize=8)\n\n    sc_acc = results[\"baselines\"][\"sc_only\"][\"accuracy\"] * 100\n    combo3_acc = results[\"full_combo\"][\"w3\"][\"accuracy\"] * 100\n    ax.axhline(sc_acc, color=\"gray\", linestyle=\"--\", linewidth=1, label=f\"SC-only ({sc_acc:.1f}%)\")\n    ax.axhline(combo3_acc, color=\"orange\", linestyle=\"--\", linewidth=1, label=f\"Full combo w=3 ({combo3_acc:.1f}%)\")\n\n    ax.set_xlabel(\"NLI Invocation Rate (%)\", fontsize=11)\n    ax.set_ylabel(\"Accuracy (%)\", fontsize=11)\n    ax.set_title(\"DRC Cascade: Mistral-7B FOLIO-204\", fontsize=12)\n    ax.legend(fontsize=8, loc=\"lower right\")\n    ax.set_xlim(-5, 105)\n    ax.grid(True, alpha=0.3)\n    plt.tight_layout()\n    plt.savefig(f\"{OUT_DIR}/pareto_front.pdf\", bbox_inches=\"tight\")\n    plt.savefig(f\"{OUT_DIR}/pareto_front.png\", dpi=150, bbox_inches=\"tight\")\n\n    # Agreement distribution\n    agreements = [q[\"agreement\"] for q in questions]\n    fig2, ax2 = plt.subplots(1, 1, figsize=(6, 3.5))\n    ax2.hist(agreements, bins=20, color=\"#2563eb\", alpha=0.7, edgecolor=\"white\")\n    for tau in TAUS:\n        ax2.axvline(tau, color=\"red\", linestyle=\"--\", alpha=0.5, linewidth=1)\n    ax2.set_xlabel(\"SC Agreement (majority fraction)\", fontsize=11)\n    ax2.set_ylabel(\"Count\", fontsize=11)\n    ax2.set_title(\"FOLIO-204: Per-Question SC Agreement Distribution\", fontsize=12)\n    plt.tight_layout()\n    plt.savefig(f\"{OUT_DIR}/agreement_distribution.png\", dpi=150, bbox_inches=\"tight\")\n\n    print(json.dumps(results, indent=2))\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"DONE\""
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T08:25:31.227824+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T08:25:31.228150+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nsc = json.load(open('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json'))\nnli = json.load(open('/root/symb_invariant_consensus/results/direction_r_nli_large/results.json'))\nprint(f'SC results: {len(sc[\\\"results\\\"])} questions')\nprint(f'NLI per_question: {len(nli[\\\"per_question\\\"])} questions')\n# check overlap\nsc_ids = {r['problem_id'] for r in sc['results']}\nnli_ids = set(nli['per_question'].keys())\noverlap = sc_ids & nli_ids\nprint(f'Overlap: {len(overlap)} questions')\nprint(f'SC acc: {sc[\\\"summary\\\"][\\\"sc_accuracy\\\"]:.4f}')\nprint(f'First SC entry keys: {list(sc[\\\"results\\\"][0].keys())}')\nprint(f'First NLI entry keys: {list(list(nli[\\\"per_question\\\"].values())[0].keys())}')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nsc = json.load(open('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json'))\nnli = json.load(open('/root/symb_invariant_consensus/results/direction_r_nli_large/results.json'))\nprint(f'SC results: {len(sc[\\\"results\\\"])} questions')\nprint(f'NLI per_question: {len(nli[\\\"per_question\\\"])} questions')\n# check overlap\nsc_ids = {r['problem_id'] for r in sc['results']}\nnli_ids = set(nli['per_question'].keys())\noverlap = sc_ids & nli_ids\nprint(f'Overlap: {len(overlap)} questions')\nprint(f'SC acc: {sc[\\\"summary\\\"][\\\"sc_accuracy\\\"]:.4f}')\nprint(f'First SC entry keys: {list(sc[\\\"results\\\"][0].keys())}')\nprint(f'First NLI entry keys: {list(list(nli[\\\"per_question\\\"].values())[0].keys())}')\n\""
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T08:25:31.228325+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"SC results: 204 questions\\nNLI per_question: 204 questions\\nOverlap: 204 questions\\nSC acc: 0.5441\\nFirst SC entry keys: ['problem_idx', 'problem_id', 'problem', 'dataset', 'level', 'ground_truth', 'sica_answer', 'sica_scores', 'sica_correct', 'sc_answer', 'sc_vote_count', 'sc_vote_distribution', 'sc_correct', 'constraints_stats', 'maxsat_stats', 'timing', 'wall_time_s']\\nFirst NLI entry keys: ['deberta_pred', 'deberta_probs', 'sc_answer', 'sica_answer', 'gold', 'deberta_correct', 'sc_correct', 'sica_correct']\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.66}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T08:25:31.228623+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python3 scripts/drc_cascade_folio.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python3 scripts/drc_cascade_folio.py"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T08:25:31.228931+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-d126-drc-folio\\\",\\n  \\\"dataset\\\": \\\"FOLIO-204\\\",\\n  \\\"generator\\\": \\\"Mistral-7B\\\",\\n  \\\"verifier\\\": \\\"DeBERTa-large-mnli\\\",\\n  \\\"K\\\": 12,\\n  \\\"n_questions\\\": 204,\\n  \\\"baselines\\\": {\\n    \\\"sc_only\\\": {\\n      \\\"accuracy\\\": 0.5588235294117647,\\n      \\\"correct\\\": 114\\n    }\\n  },\\n  \\\"full_combo\\\": {\\n    \\\"w1\\\": {\\n      \\\"accuracy\\\": 0.5637254901960784,\\n      \\\"correct\\\": 115,\\n      \\\"nli_calls\\\": 204,\\n      \\\"cost_ratio\\\": 1.0\\n    },\\n    \\\"w3\\\": {\\n      \\\"accuracy\\\": 0.5882352941176471,\\n      \\\"correct\\\": 120,\\n      \\\"nli_calls\\\": 204,\\n      \\\"cost_ratio\\\": 1.0\\n    }\\n  },\\n  \\\"drc\\\": {\\n    \\\"tau=0.3_w1\\\": {\\n      \\\"tau\\\": 0.3,\\n      \\\"weight\\\": 1,\\n      \\\"accuracy\\\": 0.5588,\\n      \\\"correct\\\": 114,\\n      \\\"nli_invoked\\\": 0,\\n      \\\"nli_invocation_rate\\\": 0.0,\\n      \\\"cost_ratio_pct\\\": 0.0,\\n      \\\"sc_only_count\\\": 204,\\n      \\\"gain_recovery_pct\\\": 0.0\\n    },\\n    \\\"tau=0.3_w3\\\": {\\n      \\\"tau\\\": 0.3,\\n      \\\"weight\\\": 3,\\n      \\\"accuracy\\\": 0.5588,\\n      \\\"correct\\\": 114,\\n      \\\"nli_invoked\\\": 0,\\n      \\\"nli_invocation_rate\\\": 0.0,\\n      \\\"cost_ratio_pct\\\": 0.0,\\n      \\\"sc_only_count\\\": 204,\\n      \\\"gain_recovery_pct\\\": 0.0\\n    },\\n    \\\"tau=0.5_w1\\\": {\\n      \\\"tau\\\": 0.5,\\n      \\\"weight\\\": 1,\\n      \\\"accuracy\\\": 0.5588,\\n      \\\"correct\\\": 114,\\n      \\\"nli_invoked\\\": 23,\\n      \\\"nli_invocation_rate\\\": 0.1127,\\n      \\\"cost_ratio_pct\\\": 11.3,\\n      \\\"sc_only_count\\\": 181,\\n      \\\"gain_recovery_pct\\\": 0.0\\n    },\\n    \\\"tau=0.5_w3\\\": {\\n      \\\"tau\\\": 0.5,\\n      \\\"weight\\\": 3,\\n      \\\"accuracy\\\": 0.5588,\\n      \\\"correct\\\": 114,\\n      \
…[truncated 3194 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T08:25:31.229180+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/results/exp_d126_drc_folio/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/results/exp_d126_drc_folio/results.json"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T08:25:31.229428+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-d126-drc-folio\\\",\\n  \\\"dataset\\\": \\\"FOLIO-204\\\",\\n  \\\"generator\\\": \\\"Mistral-7B\\\",\\n  \\\"verifier\\\": \\\"DeBERTa-large-mnli\\\",\\n  \\\"K\\\": 12,\\n  \\\"n_questions\\\": 204,\\n  \\\"baselines\\\": {\\n    \\\"sc_only\\\": {\\n      \\\"accuracy\\\": 0.5588235294117647,\\n      \\\"correct\\\": 114\\n    }\\n  },\\n  \\\"full_combo\\\": {\\n    \\\"w1\\\": {\\n      \\\"accuracy\\\": 0.5637254901960784,\\n      \\\"correct\\\": 115,\\n      \\\"nli_calls\\\": 204,\\n      \\\"cost_ratio\\\": 1.0\\n    },\\n    \\\"w3\\\": {\\n      \\\"accuracy\\\": 0.5882352941176471,\\n      \\\"correct\\\": 120,\\n      \\\"nli_calls\\\": 204,\\n      \\\"cost_ratio\\\": 1.0\\n    }\\n  },\\n  \\\"drc\\\": {\\n    \\\"tau=0.3_w1\\\": {\\n      \\\"tau\\\": 0.3,\\n      \\\"weight\\\": 1,\\n      \\\"accuracy\\\": 0.5588,\\n      \\\"correct\\\": 114,\\n      \\\"nli_invoked\\\": 0,\\n      \\\"nli_invocation_rate\\\": 0.0,\\n      \\\"cost_ratio_pct\\\": 0.0,\\n      \\\"sc_only_count\\\": 204,\\n      \\\"gain_recovery_pct\\\": 0.0\\n    },\\n    \\\"tau=0.3_w3\\\": {\\n      \\\"tau\\\": 0.3,\\n      \\\"weight\\\": 3,\\n      \\\"accuracy\\\": 0.5588,\\n      \\\"correct\\\": 114,\\n      \\\"nli_invoked\\\": 0,\\n      \\\"nli_invocation_rate\\\": 0.0,\\n      \\\"cost_ratio_pct\\\": 0.0,\\n      \\\"sc_only_count\\\": 204,\\n      \\\"gain_recovery_pct\\\": 0.0\\n    },\\n    \\\"tau=0.5_w1\\\": {\\n      \\\"tau\\\": 0.5,\\n      \\\"weight\\\": 1,\\n      \\\"accuracy\\\": 0.5588,\\n      \\\"correct\\\": 114,\\n      \\\"nli_invoked\\\": 23,\\n      \\\"nli_invocation_rate\\\": 0.1127,\\n      \\\"cost_ratio_pct\\\": 11.3,\\n      \\\"sc_only_count\\\": 181,\\n      \\\"gain_recovery_pct\\\": 0.0\\n    },\\n    \\\"tau=0.5_w3\\\": {\\n      \\\"tau\\\": 0.5,\\n      \\\"weight\\\": 3,\\n      \\\"accuracy\\\": 0.5588,\\n      \\\"correct\\\": 114,\\n      \
…[truncated 3075 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T08:25:31.229600+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T08:25:31.229764+00:00_

_extracted
_project
ablation_text.py
aime30_v2_partial_analysis.md
aime_bias_ratio_results.json
analysis_exp045.md
analysis_prove_verify.py
analyze_adaptive_sica.py
analyze_discriminative_rate.py
analyze_expanded.py
analyze_seed_replication.py
appendix_prompt_template.md
backward_verification.py
bootstrap_br.py
br_bootstrap_ci.json
capability_gap_scatter_v2.pdf
capability_gap_scatter_v2.png
case_study_materials.md
citation_verification.md
code_verify_report.md
compute_tost_sensitivity.py
confirmation_bias_results.json
constraint_ablation
constraint_extractor.py
constraint_extractor_fixed.py
constraint_quality_crossmethod.json
crd_audit_report.md
cross_model_kappa_results.json
cross_model_sica_results.json
cross_trace_unsat.py
d016_model_pivot_report.md
d116_qwen3_pw_deberta_large.py
diagnose_exp039.md
diagnose_exp062_exp065.md
dir_c_premise_only.py
dir_d_dpp_trace_selection.py
dir_f2_self_verify.py
dir_f3_cross_model.py
dir_f_prm_verifier_pilot.py
dir_f_prm_verifier_pilot_v2.py
dir_h_provenance_analysis
dir_h_provenance_analysis.py
dir_i2_single_model_baselines.py
dir_j2_nli_qwen3.py
dir_j3_nli_multi_verifier.py
dir_k_nli_qwen3_proofwriter
direction_a_atom_verification.py
direction_a_prove_results.json
direction_b_weighted_maxsat.py
direction_c_counterfactual.py
direction_d_cegis_results_partial.json
direction_e_abstention.py
direction_e_abstention_results.json
direction_gr_combo.py
direction_j
direction_j_results.json
direction_r_deberta_proofwriter.py
direction_r_nli_large
drc_cascade_pilot.py
dream_reports
entropy_breakdown_crossmodel.json
error_categorization.py
error_categorization_discordant.json
exp-001
exp-005
exp-007-qwen72b-awq
exp-009
exp-010-mistral-v2
exp-011
exp-011-llama8b
exp-013-constraint-ablation
exp-014
exp-016
exp-017-strategyqa-v3
exp-017-strategyqa-v3_analysis.md
exp-019
exp-021-oracle-folio
exp-022
exp-022-oracle-proofwriter
exp-023-discriminative-rate
exp-030-crossmodel-mistral-folio204
exp-031-oracle-folio-regen
exp-038
exp-045-backward-ver
…[truncated 2337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T08:25:31.229953+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/drc_folio_results.json",
  "content": "{\n  \"experiment\": \"exp-d126-drc-folio\",\n  \"dataset\": \"FOLIO-204\",\n  \"generator\": \"Mistral-7B\",\n  \"verifier\": \"DeBERTa-large-mnli\",\n  \"K\": 12,\n  \"n_questions\": 204,\n  \"baselines\": {\n    \"sc_only\": {\n      \"accuracy\": 0.5588235294117647,\n      \"correct\": 114\n    }\n  },\n  \"full_combo\": {\n    \"w1\": {\n      \"accuracy\": 0.5637254901960784,\n      \"correct\": 115,\n      \"nli_calls\": 204,\n      \"cost_ratio\": 1.0\n    },\n    \"w3\": {\n      \"accuracy\": 0.5882352941176471,\n      \"correct\": 120,\n      \"nli_calls\": 204,\n      \"cost_ratio\": 1.0\n    }\n  },\n  \"drc\": {\n    \"tau=0.3_w1\": {\n      \"tau\": 0.3,\n      \"weight\": 1,\n      \"accuracy\": 0.5588,\n      \"correct\": 114,\n      \"nli_invoked\": 0,\n      \"nli_invocation_rate\": 0.0,\n      \"cost_ratio_pct\": 0.0,\n      \"sc_only_count\": 204,\n      \"gain_recovery_pct\": 0.0\n    },\n    \"tau=0.3_w3\": {\n      \"tau\": 0.3,\n      \"weight\": 3,\n      \"accuracy\": 0.5588,\n      \"correct\": 114,\n      \"nli_invoked\": 0,\n      \"nli_invocation_rate\": 0.0,\n      \"cost_ratio_pct\": 0.0,\n      \"sc_only_count\": 204,\n      \"gain_recovery_pct\": 0.0\n    },\n    \"tau=0.5_w1\": {\n      \"tau\": 0.5,\n      \"weight\": 1,\n      \"accuracy\": 0.5588,\n      \"correct\": 114,\n      \"nli_invoked\": 23,\n      \"nli_invocation_rate\": 0.1127,\n      \"cost_ratio_pct\": 11.3,\n      \"sc_only_count\": 181,\n      \"gain_recovery_pct\": 0.0\n    },\n    \"tau=0.5_w3\": {\n      \"tau\": 0.5,\n      \"weight\": 3,\n      \"accuracy\": 0.5588,\n      \"correct\": 114,\n      \"nli_invoked\": 23,\n      \"nli_invocation_rate\": 0.1127,\n      \"cost_ratio_pct\": 11.3,\n      \"sc_only_count\": 181,\n      \"gain_recovery_pct\": 0.0\n    },\n    \"tau=0.6_w1\": {\n      \"tau\": 0.6,\n      \"weight\": 1,\n      \"accuracy\": 0.5637,\n      \"correct\": 115,\n      \"nli_invoked\": 49,\n      \"nli_invocation_rate\": 0.2402,\n      \"cost_ratio_pct\": 24.0,\n      \"sc_only_count\": 155,\n      \"gain_recovery_pct\": 100.0\n    },\n    \"tau=0.6_w3\": {\n      \"tau\": 0.6,\n      \"weight\": 3,\n      \"accuracy\": 0.5735,\n      \"correct\": 117,\n      \"nli_invoked\": 49,\n      \"nli_invocation_rate\": 0.2402,\n      \"cost_ratio_pct\": 24.0,\n      \"sc_only_count\": 155,\n      \"gain_recovery_pct\": 50.0\n    },\n    \"tau=0.7_w1\": {\n      \"tau\": 0.7,\n      \"weight\": 1,\n      \"accuracy\": 0.5637,\n      \"correct\": 115,\n      \"nli_invoked\": 71,\n      \"nli_invocation_rate\": 0.348,\n      \"cost_ratio_pct\": 34.8,\n      \"sc_only_count\": 133,\n      \"gain_recovery_pct\": 100.0\n    },\n    \"tau=0.7_w3\": {\n      \"tau\": 0.7,\n      \"weight\": 3,\n      \"accuracy\": 0.5833,\n      \"correct\": 119,\n      \"nli_invoked\": 71,\n      \"nli_invocation_rate\": 0.348,\n      \"cost_ratio_pct\": 34.8,\n      \"sc_only_count\": 133,\n      \"gain_recovery_pct\": 83.3\n    },\n    \"tau=0.8_w1\": {\n      \"tau\": 0.8,\n      \"weight\": 1,\n      \"accuracy\": 0.5637,\n      \"correct\": 115,\n      \"nli_invoked\": 99,\n      \"nli_invocation_rate\": 0.4853,\n      \"cost_ratio_pct\": 48.5,\n      \"sc_only_count\": 105,\n      \"gain_recovery_pct\": 100.0\n    },\n    \"tau=0.8_w3\": {\n      \"tau\": 0.8,\n      \"weight\": 3,\n      \"accuracy\": 0.5882,\n      \"correct\": 120,\n      \"nli_invoked\": 99,\n      \"nli_invocation_rate\": 0.4853,\n      \"cost_ratio_pct\": 48.5,\n      \"sc_only_count\": 105,\n      \"gain_recovery_pct\": 100.0\n    },\n    \"tau=0.9_w1\": {\n      \"tau\": 0.9,\n      \"weight\": 1,\n      \"accuracy\": 0.5637,\n      \"correct\": 115,\n      \"nli_invoked\": 131,\n      \"nli_invocation_rate\": 0.6422,\n      \"cost_ratio_pct\": 64.2,\n      \"sc_only_count\": 73,\n      \"gain_recovery_pct\": 100.0\n    },\n    \"tau=0.9_w3\": {\n      \"tau\": 0.9,\n      \"weight\": 3,\n      \"accuracy\": 0.5882,\n      \"correct\": 120,\n      \"nli_invoked\": 131,\n      \"nli_invocation_rate\": 0.6422,\n      \"cost_ratio_pct\": 64.2,\n      \"sc_only_count\": 73,\n      \"gain_recovery_pct\": 100.0\n    }\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/drc_folio_results.json",
    "content": "{\n  \"experiment\": \"exp-d126-drc-folio\",\n  \"dataset\": \"FOLIO-204\",\n  \"generator\": \"Mistral-7B\",\n  \"verifier\": \"DeBERTa-large-mnli\",\n  \"K\": 12,\n  \"n_questions\": 204,\n  \"baselines\": {\n    \"sc_only\": {\n      \"accuracy\": 0.5588235294117647,\n      \"correct\": 114\n    }\n  },\n  \"full_combo\": {\n    \"w1\": {\n      \"accuracy\": 0.5637254901960784,\n      \"correct\": 115,\n      \"nli_calls\": 204,\n      \"cost_ratio\": 1.0\n    },\n    \"w3\": {\n      \"accuracy\": 0.5882352941176471,\n      \"correct\": 120,\n      \"nli_calls\": 204,\n      \"cost_ratio\": 1.0\n    }\n  },\n  \"drc\": {\n    \"tau=0.3_w1\": {\n      \"tau\": 0.3,\n      \"weight\": 1,\n      \"accuracy\": 0.5588,\n      \"correct\": 114,\n      \"nli_invoked\": 0,\n      \"nli_invocation_rate\": 0.0,\n      \"cost_ratio_pct\": 0.0,\n      \"sc_only_count\": 204,\n      \"gain_recovery_pct\": 0.0\n    },\n    \"tau=0.3_w3\": {\n      \"tau\": 0.3,\n      \"weight\": 3,\n      \"accuracy\": 0.5588,\n      \"correct\": 114,\n      \"nli_invoked\": 0,\n      \"nli_invocation_rate\": 0.0,\n      \"cost_ratio_pct\": 0.0,\n      \"sc_only_count\": 204,\n      \"gain_recovery_pct\": 0.0\n    },\n    \"tau=0.5_w1\": {\n      \"tau\": 0.5,\n      \"weight\": 1,\n      \"accuracy\": 0.5588,\n      \"correct\": 114,\n      \"nli_invoked\": 23,\n      \"nli_invocation_rate\": 0.1127,\n      \"cost_ratio_pct\": 11.3,\n      \"sc_only_count\": 181,\n      \"gain_recovery_pct\": 0.0\n    },\n    \"tau=0.5_w3\": {\n      \"tau\": 0.5,\n      \"weight\": 3,\n      \"accuracy\": 0.5588,\n      \"correct\": 114,\n      \"nli_invoked\": 23,\n      \"nli_invocation_rate\": 0.1127,\n      \"cost_ratio_pct\": 11.3,\n      \"sc_only_count\": 181,\n      \"gain_recovery_pct\": 0.0\n    },\n    \"tau=0.6_w1\": {\n      \"tau\": 0.6,\n      \"weight\": 1,\n      \"accuracy\": 0.5637,\n      \"correct\": 115,\n      \"nli_invoked\": 49,\n      \"nli_invocation_rate\": 0.2402,\n      \"cost_ratio_pct\": 24.0,\n      \"sc_only_count\": 155,\n      \"gain_recovery_pct\": 100.0\n    },\n    \"tau=0.6_w3\": {\n      \"tau\": 0.6,\n      \"weight\": 3,\n      \"accuracy\": 0.5735,\n      \"correct\": 117,\n      \"nli_invoked\": 49,\n      \"nli_invocation_rate\": 0.2402,\n      \"cost_ratio_pct\": 24.0,\n      \"sc_only_count\": 155,\n      \"gain_recovery_pct\": 50.0\n    },\n    \"tau=0.7_w1\": {\n      \"tau\": 0.7,\n      \"weight\": 1,\n      \"accuracy\": 0.5637,\n      \"correct\": 115,\n      \"nli_invoked\": 71,\n      \"nli_invocation_rate\": 0.348,\n      \"cost_ratio_pct\": 34.8,\n      \"sc_only_count\": 133,\n      \"gain_recovery_pct\": 100.0\n    },\n    \"tau=0.7_w3\": {\n      \"tau\": 0.7,\n      \"weight\": 3,\n      \"accuracy\": 0.5833,\n      \"correct\": 119,\n      \"nli_invoked\": 71,\n      \"nli_invocation_rate\": 0.348,\n      \"cost_ratio_pct\": 34.8,\n      \"sc_only_count\": 133,\n      \"gain_recovery_pct\": 83.3\n    },\n    \"tau=0.8_w1\": {\n      \"tau\": 0.8,\n      \"weight\": 1,\n      \"accuracy\": 0.5637,\n      \"correct\": 115,\n      \"nli_invoked\": 99,\n      \"nli_invocation_rate\": 0.4853,\n      \"cost_ratio_pct\": 48.5,\n      \"sc_only_count\": 105,\n      \"gain_recovery_pct\": 100.0\n    },\n    \"tau=0.8_w3\": {\n      \"tau\": 0.8,\n      \"weight\": 3,\n      \"accuracy\": 0.5882,\n      \"correct\": 120,\n      \"nli_invoked\": 99,\n      \"nli_invocation_rate\": 0.4853,\n      \"cost_ratio_pct\": 48.5,\n      \"sc_only_count\": 105,\n      \"gain_recovery_pct\": 100.0\n    },\n    \"tau=0.9_w1\": {\n      \"tau\": 0.9,\n      \"weight\": 1,\n      \"accuracy\": 0.5637,\n      \"correct\": 115,\n      \"nli_invoked\": 131,\n      \"nli_invocation_rate\": 0.6422,\n      \"cost_ratio_pct\": 64.2,\n      \"sc_only_count\": 73,\n      \"gain_recovery_pct\": 100.0\n    },\n    \"tau=0.9_w3\": {\n      \"tau\": 0.9,\n      \"weight\": 3,\n      \"accuracy\": 0.5882,\n      \"correct\": 120,\n      \"nli_invoked\": 131,\n      \"nli_invocation_rate\": 0.6422,\n      \"cost_ratio_pct\": 64.2,\n      \"sc_only_count\": 73,\n      \"gain_recovery_pct\": 100.0\n    }\n  }\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T08:25:31.230140+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/drc_folio_results.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T08:25:31.230273+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "drc_folio_results",
  "type": "data",
  "description": "DRC Cascade results on FOLIO-204 (Mistral-7B + DeBERTa-large-mnli). τ sweep {0.3-0.9}, w={1,3}. Key: τ=0.7/w=3 recovers 83.3% gain at 34.8% cost.",
  "project": "symb_invariant_consensus",
  "exp_id": "exp-d126-drc-folio",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/drc_folio_results.json",
  "tags": "['drc', 'folio', 'cascade', 'nli-combo']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "drc_folio_results",
    "type": "data",
    "description": "DRC Cascade results on FOLIO-204 (Mistral-7B + DeBERTa-large-mnli). τ sweep {0.3-0.9}, w={1,3}. Key: τ=0.7/w=3 recovers 83.3% gain at 34.8% cost.",
    "project": "symb_invariant_consensus",
    "exp_id": "exp-d126-drc-folio",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/drc_folio_results.json",
    "tags": "['drc', 'folio', 'cascade', 'nli-combo']"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T08:25:31.230438+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_b907ed\", \"name\": \"drc_folio_results\", \"type\": \"data\", \"description\": \"DRC Cascade results on FOLIO-204 (Mistral-7B + DeBERTa-large-mnli). τ sweep {0.3-0.9}, w={1,3}. Key: τ=0.7/w=3 recovers 83.3% gain at 34.8% cost.\", \"path\": \"projects/symb_invariant_consensus/artifacts/exp-d126-drc-folio/data/drc_folio_results.json\", \"url\": null, \"project\": \"symb_invariant_consensus\", \"exp_id\": \"exp-d126-drc-folio\", \"skill\": \"\", \"created_at\": \"2026-05-21T08:25:18.354571+00:00\", \"tags\": [\"drc\", \"folio\", \"cascade\", \"nli-combo\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_d126-drc-folio_20260521T082219",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-21T08:25:31.230615+00:00_

实验完成。

**E3 — DRC Cascade on FOLIO-204 结果**:

| Method | Acc | Δ vs SC | NLI Calls | Cost |
|--------|-----|---------|-----------|------|
| SC only | 55.88% | — | 0/204 | 0% |
| Full combo w=1 | 56.37% | +0.49pp | 204/204 | 100% |
| Full combo w=3 | 58.82% | +2.94pp | 204/204 | 100% |
| DRC τ=0.5 w=3 | 55.88% | 0 | 23/204 | 11.3% |
| DRC τ=0.6 w=3 | 57.35% | +1.47pp | 49/204 | 24.0% |
| **DRC τ=0.7 w=3** | **58.33%** | **+2.45pp** | **71/204** | **34.8%** |
| DRC τ=0.8 w=3 | 58.82% | +2.94pp | 99/204 | 48.5% |
| DRC τ=0.9 w=3 | 58.82% | +2.94pp | 131/204 | 64.2% |

**泛化性验证成功**: τ=0.7 在 FOLIO 上恢复 83.3% 的 full combo gain，仅需 34.8% NLI 调用 — 与 ProofWriter (90% gain / 38.8% cost) 高度一致。τ=0.8 达到 100% gain recovery，cost 仅 48.5%。

结果已保存至服务器 `results/exp_d126_drc_folio/results.json` 和本地 `artifacts/drc_folio_results.json`，Pareto front 图和 agreement distribution 图也已生成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_experiment_d126-drc-folio_20260521T082219"
}
```

</details>

---
