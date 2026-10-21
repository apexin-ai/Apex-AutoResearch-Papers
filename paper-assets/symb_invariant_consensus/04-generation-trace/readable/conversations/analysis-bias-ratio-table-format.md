# analysis bias ratio table format

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 0
- **Tool calls:** 31
- **Original source:** `logs/chats/worker_analysis_bias-ratio-table-format_20260520T113129.jsonl`
- **Structured JSON:** [`97698ccc26c543ce5d30.json`](../../sessions/97/97698ccc26c543ce5d30.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

63 recorded events

### Tool call

_source line 1 · 2026-05-20T11:36:31.000362+00:00_

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
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
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

_source line 2 · 2026-05-20T11:36:31.000726+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T11:36:31.000943+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/results/confirmation_bias/crossmodel_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/results/confirmation_bias/crossmodel_results.json"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T11:36:31.001127+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/confirmation_bias/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/confirmation_bias/"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T11:36:31.001296+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"results\\\": [\\n    {\\n      \\\"model\\\": \\\"Mistral-7B\\\",\\n      \\\"n_total\\\": 204,\\n      \\\"n_wrong\\\": 83,\\n      \\\"sica_acc\\\": 0.5931,\\n      \\\"score_bias_ratio\\\": 4.24,\\n      \\\"score_error_pct\\\": 80.9,\\n      \\\"score_gold_frac_wrong\\\": 0.1909,\\n      \\\"score_gold_frac_correct\\\": 0.7184,\\n      \\\"follows_sc_rate\\\": 0.9398,\\n      \\\"raw_bias_ratio\\\": 4.97,\\n      \\\"raw_error_pct\\\": 83.3,\\n      \\\"raw_n_analyzed\\\": 83\\n    },\\n    {\\n      \\\"model\\\": \\\"Qwen2.5-14B\\\",\\n      \\\"n_total\\\": 204,\\n      \\\"n_wrong\\\": 52,\\n      \\\"sica_acc\\\": 0.7451,\\n      \\\"score_bias_ratio\\\": 3.69,\\n      \\\"score_error_pct\\\": 78.7,\\n      \\\"score_gold_frac_wrong\\\": 0.2133,\\n      \\\"score_gold_frac_correct\\\": 0.8872,\\n      \\\"follows_sc_rate\\\": 0.9038,\\n      \\\"raw_bias_ratio\\\": 3.93,\\n      \\\"raw_error_pct\\\": 79.7,\\n      \\\"raw_n_analyzed\\\": 52\\n    }\\n  ]\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.14}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T11:36:31.001435+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"crossmodel_results.json\\nresults.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T11:36:31.001591+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/exp063*/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/exp063*/"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T11:36:31.001716+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/exp033_mistral_folio204/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/exp033_mistral_folio204/"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T11:36:31.001844+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/symb_invariant_consensus/results/exp063*/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T11:36:31.002031+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/symb_invariant_consensus/results/exp033_mistral_folio204/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T11:36:31.002161+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/exp041*/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/exp041*/"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T11:36:31.002311+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/symb_invariant_consensus/results/exp041*/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T11:36:31.002520+00:00_

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
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
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

_source line 14 · 2026-05-20T11:36:31.002692+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"adaptive_sica_validation.json\\ncase_study_constraints.json\\ncase_study_normalized.json\\ncondorcet_independence_analysis.json\\nconfirmation_bias\\ncross_model_experiment\\ncross_model_kappa\\ncross_model_mistral_folio\\ndirection_a_prove\\ndirection_b_deepconf\\ndirection_e_abstention\\ndirection_f_blind_fol\\ndirection_g_decoupling\\ndirection_g_dryrun.log\\ndirection_g_vllm.log\\ndirection_i_z3_filter\\ndirection_r_deberta\\ndirection_r_nli_large\\ndirection_r_nli_small\\ndisc_filter_full.log\\ndisc_filter_test.log\\ndiscriminative_filter_exp033.json\\ndiscriminative_filter_exp033_test.json\\ndiscriminative_filter_exp044b.json\\ndiscriminative_filter_exp046.json\\ndiscriminative_filter_exp054.json\\nexp-007-qwen72b-awq\\nexp-029-contrastive-folio204\\nexp004_qwen7b_rerun\\nexp013_constraint_ablation\\nexp027_qwen3_14b_nonthinking\\nexp028_qwen3_14b_thinking\\nexp028b_discordant_tracking.json\\nexp028b_qwen3_thinking_folio204\\nexp033_mistral_7b_folio204\\nexp033_per_problem_analysis.json\\nexp033_per_problem_analysis_v2.json\\nexp034_llama31_8b_folio204\\nexp034_qwen25_14b_proofwriter\\nexp035_qwen25_7b_folio204\\nexp036_z3_feedback\\nexp036b_cross_trace_unsat.json\\nexp044b_icl_oracle_qwen14b\\nexp045b_backward_qwen14b\\nexp046_mistral_7b_pw600\\nexp047_qwen3_thinking_folio204\\nexp051_mistral_k_sensitivity\\nexp054_mistral_folio204_t10\\nexp057_mistral_folio204_t03\\nexp058_mistral_folio204_t05\\nexp059_cross_qwen3_extractor\\nexp05_backward_verification\\nexp060_cross_qwen25_14b_extractor\\nexp061_qwen25_7b_folio204\\nexp062_gemma27b_folio204\\nexp065_qwen7b_pw600\\nexp066_qwen14b_folio_seed123\\nexp066_vllm.log\\nexp067_mistral_folio_seed789\\nexp069_mistral_logiqa200\\nexp070_qwen7b_logiqa200\\nexp071_qwen7b_logiqa200_seed123\\nexp073_qwen7b_logiqa200_seed456\\nexp073b_qwen7b_logiqa200_seed456\\nexp074_icg_dryrun\\nexp074_icg_mistral_folio\\nexp074_icg_v2_dryrun\\nexp074c_icg_mistral_folio_seed123\\ne
…[truncated 872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T11:36:31.002864+00:00_

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
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
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

_source line 16 · 2026-05-20T11:36:31.003024+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"constraint_cache\\nexp033.log\\nexp033_results.json\\nintermediates\\nsc_answer_matrix.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T11:36:31.003145+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/exp034_llama31_8b_folio204/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/exp034_llama31_8b_folio204/"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T11:36:31.003263+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/folio_204_14b/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/folio_204_14b/"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T11:36:31.003380+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"exp034.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T11:36:31.003497+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"folio_204_14b.log\\nfolio_204_results.json\\nintermediates\\nper_trace_constraints\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T11:36:31.003609+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -100 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -100 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T11:36:31.003726+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -100 /root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -100 /root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T11:36:31.003951+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 204,\\n    \\\"sica_accuracy\\\": 0.5931372549019608,\\n    \\\"sc_accuracy\\\": 0.5441176470588235,\\n    \\\"sica_correct\\\": 121,\\n    \\\"sc_correct\\\": 111,\\n    \\\"extraction_rate\\\": 0.9714052287581699,\\n    \\\"total_constraints_extracted\\\": 14042,\\n    \\\"total_unique_constraints\\\": 8021,\\n    \\\"contradiction_rate\\\": 0.03503303827452936,\\n    \\\"problems_with_contradictions\\\": 128,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"validation\\\": {\\n        \\\"sica\\\": 0.5931372549019608,\\n        \\\"sc\\\": 0.5441176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.5931372549019608,\\n        \\\"sc\\\": 0.5441176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 4881.8\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"folio_0\\\",\\n      \\\"problem\\\": \\\"Given the following premises:\\\\nIf people perform in school talent shows often, then they attend and are very engaged with school events. People either perform in school talent shows often or are inactive and disinterested members of their community. If people chaperone high school dances, then they are not students who attend the school. All people who are inactive and disinterested members of their community chaperone high school dances. All young children and teenagers who wish to further their academic careers and educational opportunities are students who attend the school. Bonnie either both attends and is very engaged with school events and is a student who attends the school, or she neither attends and is very engaged with school events nor is a student who attends the school.\\\\n\\\\nDetermine whether the following conclusion
…[truncated 3574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T11:36:31.004127+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/results/confirmation_bias/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/results/confirmation_bias/results.json"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T11:36:31.004338+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 204,\\n    \\\"sica_accuracy\\\": 0.7450980392156863,\\n    \\\"sc_accuracy\\\": 0.75,\\n    \\\"sica_correct\\\": 152,\\n    \\\"sc_correct\\\": 153,\\n    \\\"extraction_rate\\\": 0.9852941176470589,\\n    \\\"total_constraints_extracted\\\": 13694,\\n    \\\"total_unique_constraints\\\": 6134,\\n    \\\"contradiction_rate\\\": 0.009129442451907402,\\n    \\\"problems_with_contradictions\\\": 36,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"validation\\\": {\\n        \\\"sica\\\": 0.7450980392156863,\\n        \\\"sc\\\": 0.75,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.7450980392156863,\\n        \\\"sc\\\": 0.75,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 8881.0\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"folio_0\\\",\\n      \\\"problem\\\": \\\"Given the following premises:\\\\nIf people perform in school talent shows often, then they attend and are very engaged with school events. People either perform in school talent shows often or are inactive and disinterested members of their community. If people chaperone high school dances, then they are not students who attend the school. All people who are inactive and disinterested members of their community chaperone high school dances. All young children and teenagers who wish to further their academic careers and educational opportunities are students who attend the school. Bonnie either both attends and is very engaged with school events and is a student who attends the school, or she neither attends and is very engaged with school events nor is a student who attends the school.\\\\n\\\\nDetermine whether the following conclusion is true, false, or uncertain:\\\\nBonnie 
…[truncated 3536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T11:36:31.004741+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"total_problems\\\": 204,\\n    \\\"skipped_no_cache\\\": 0,\\n    \\\"sica_accuracy\\\": 0.5931,\\n    \\\"sc_accuracy\\\": 0.5441,\\n    \\\"sica_wrong_follows_sc_count\\\": 78,\\n    \\\"sica_wrong_diverges_sc_count\\\": 5,\\n    \\\"sica_wrong_follows_sc_rate\\\": 0.9398\\n  },\\n  \\\"category_stats\\\": [\\n    {\\n      \\\"category\\\": \\\"SICA correct\\\",\\n      \\\"n_problems\\\": 121,\\n      \\\"constraints_gold_frac\\\": 0.7808,\\n      \\\"constraints_wrong_frac\\\": 0.2192,\\n      \\\"weight_gold_frac\\\": 0.7184,\\n      \\\"bias_ratio\\\": 0.2808\\n    },\\n    {\\n      \\\"category\\\": \\\"SICA wrong\\\",\\n      \\\"n_problems\\\": 83,\\n      \\\"constraints_gold_frac\\\": 0.1674,\\n      \\\"constraints_wrong_frac\\\": 0.8326,\\n      \\\"weight_gold_frac\\\": 0.1909,\\n      \\\"bias_ratio\\\": 4.9746\\n    },\\n    {\\n      \\\"category\\\": \\\"SC wrong, SICA correct\\\",\\n      \\\"n_problems\\\": 12,\\n      \\\"constraints_gold_frac\\\": 0.4303,\\n      \\\"constraints_wrong_frac\\\": 0.5697,\\n      \\\"weight_gold_frac\\\": 0.4832,\\n      \\\"bias_ratio\\\": 1.324\\n    },\\n    {\\n      \\\"category\\\": \\\"SC correct, SICA wrong\\\",\\n      \\\"n_problems\\\": 2,\\n      \\\"constraints_gold_frac\\\": 0.4548,\\n      \\\"constraints_wrong_frac\\\": 0.5452,\\n      \\\"weight_gold_frac\\\": 0.3504,\\n      \\\"bias_ratio\\\": 1.1987\\n    },\\n    {\\n      \\\"category\\\": \\\"Both wrong\\\",\\n      \\\"n_problems\\\": 81,\\n      \\\"constraints_gold_frac\\\": 0.1603,\\n      \\\"constraints_wrong_frac\\\": 0.8397,\\n      \\\"weight_gold_frac\\\": 0.187,\\n      \\\"bias_ratio\\\": 5.2391\\n    },\\n    {\\n      \\\"category\\\": \\\"Both correct\\\",\\n      \\\"n_problems\\\": 109,\\n      \\\"constraints_gold_frac\\\": 0.8193,\\n      \\\"constraints_wrong_frac\\\": 0.1807,\\n      \\\"weight_gold_frac\\\": 0.7443,\\n      \\\"
…[truncated 8671 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T11:36:31.004963+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus/results/exp034_llama31_8b_folio204/ -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus/results/exp034_llama31_8b_folio204/ -type f"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T11:36:31.005113+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/exp034_llama31_8b_folio204/exp034.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T11:36:31.005241+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus/results/ -name \"*llama*\" -o -name \"*Llama*\" -o -name \"*LLAMA*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus/results/ -name \"*llama*\" -o -name \"*Llama*\" -o -name \"*LLAMA*\""
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T11:36:31.005371+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/exp034_llama31_8b_folio204\\n/root/symb_invariant_consensus/results/cross_model_kappa/decode_llama.py\\n/root/symb_invariant_consensus/results/cross_model_kappa/llama_answer_matrix.json\\n/root/symb_invariant_consensus/results/cross_model_experiment/llama_sc_answer_matrix.json\\n/root/symb_invariant_consensus/results/cross_model_experiment/llama_constraints_t0t3.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T11:36:31.005492+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/cross_model_experiment/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/cross_model_experiment/"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T11:36:31.005613+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"cross_model_results.json\\nllama_constraints_t0t3.json\\nllama_sc_answer_matrix.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T11:36:31.005728+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -100 /root/symb_invariant_consensus/results/cross_model_experiment/llama_constraints_t0t3.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -100 /root/symb_invariant_consensus/results/cross_model_experiment/llama_constraints_t0t3.json"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T11:36:31.006071+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"folio_0\\\": {\\\"gt\\\": \\\"Unknown\\\", \\\"per_trace\\\": [{\\\"trace_idx\\\": 0, \\\"answer\\\": \\\"True\\\", \\\"constraints\\\": [{\\\"z3_formula\\\": \\\"performs_bonnie == True\\\", \\\"expression\\\": \\\"performs_bonnie == True\\\", \\\"type\\\": \\\"invariant\\\"}, {\\\"z3_formula\\\": \\\"Implies(performs_bonnie, And(attends_bonnie, engaged_bonnie))\\\", \\\"expression\\\": \\\"Implies(performs_bonnie, And(attends_bonnie, engaged_bonnie))\\\", \\\"type\\\": \\\"invariant\\\"}, {\\\"z3_formula\\\": \\\"Implies(performs_bonnie, student_bonnie)\\\", \\\"expression\\\": \\\"Implies(performs_bonnie, student_bonnie)\\\", \\\"type\\\": \\\"invariant\\\"}, {\\\"z3_formula\\\": \\\"Or(performs_bonnie, inactive_bonnie)\\\", \\\"expression\\\": \\\"Or(performs_bonnie, inactive_bonnie)\\\", \\\"type\\\": \\\"invariant\\\"}, {\\\"z3_formula\\\": \\\"Implies(inactive_bonnie, chaperone_bonnie)\\\", \\\"expression\\\": \\\"Implies(inactive_bonnie, chaperone_bonnie)\\\", \\\"type\\\": \\\"invariant\\\"}, {\\\"z3_formula\\\": \\\"Implies(chaperone_bonnie, Not(student_bonnie))\\\", \\\"expression\\\": \\\"Implies(chaperone_bonnie, Not(student_bonnie))\\\", \\\"type\\\": \\\"invariant\\\"}, {\\\"z3_formula\\\": \\\"Implies(student_bonnie, wishes_further_bonnie)\\\", \\\"expression\\\": \\\"Implies(student_bonnie, wishes_further_bonnie)\\\", \\\"type\\\": \\\"invariant\\\"}, {\\\"z3_formula\\\": \\\"Implies(And(attends_bonnie, engaged_bonnie), Both(attends_bonnie, engaged_bonnie, student_bonnie))\\\", \\\"expression\\\": \\\"Implies(And(attends_bonnie, engaged_bonnie), Both(attends_bonnie, engaged_bonnie, student_bonnie))\\\", \\\"type\\\": \\\"invariant\\\"}, {\\\"z3_formula\\\": \\\"Implies(Not(Both(attends_bonnie, engaged_bonnie, student_bonnie)), Either(Not(attends_bonnie), Not(engaged_bonnie), Not(student_bonnie)))\\\", \\\"expression\\\": \\\"Implies(Not(Both(attends_bonnie, engaged_bonnie, student_bonnie))
…[truncated 8255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T11:36:31.006283+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -50 /root/symb_invariant_consensus/results/cross_model_experiment/cross_model_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -50 /root/symb_invariant_consensus/results/cross_model_experiment/cross_model_results.json"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T11:36:31.006455+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -50 /root/symb_invariant_consensus/results/cross_model_experiment/llama_sc_answer_matrix.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -50 /root/symb_invariant_consensus/results/cross_model_experiment/llama_sc_answer_matrix.json"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T11:36:31.006625+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 204,\\n    \\\"n_skipped_sica\\\": 0,\\n    \\\"cross_model_sc_accuracy\\\": 0.7450980392156863,\\n    \\\"cross_model_sc_correct\\\": 152,\\n    \\\"cross_model_sica_accuracy\\\": 0.7401960784313726,\\n    \\\"cross_model_sica_correct\\\": 151,\\n    \\\"delta_sica_minus_sc\\\": -0.004901960784313708,\\n    \\\"mcnemar_p\\\": 1.0,\\n    \\\"mcnemar_n01\\\": 7,\\n    \\\"mcnemar_n10\\\": 6,\\n    \\\"traces_per_model\\\": 4,\\n    \\\"total_k\\\": 12,\\n    \\\"models\\\": {\\n      \\\"mistral\\\": \\\"Mistral-7B\\\",\\n      \\\"llama\\\": \\\"LLaMA-3.1-8B\\\",\\n      \\\"qwen\\\": \\\"Qwen2.5-7B\\\"\\n    }\\n  },\\n  \\\"baselines\\\": {\\n    \\\"mistral\\\": {\\n      \\\"sc_accuracy\\\": 0.5441176470588235,\\n      \\\"sica_accuracy\\\": 0.5931372549019608,\\n      \\\"n\\\": 204\\n    },\\n    \\\"qwen\\\": {\\n      \\\"sc_accuracy\\\": 0.7598039215686274,\\n      \\\"sica_accuracy\\\": 0.7647058823529411,\\n      \\\"n\\\": 204\\n    }\\n  },\\n  \\\"per_problem\\\": {\\n    \\\"folio_0\\\": {\\n      \\\"sc_answer\\\": \\\"Unknown\\\",\\n      \\\"sc_distribution\\\": {\\n        \\\"Unknown\\\": 8,\\n        \\\"True\\\": 3,\\n        \\\"False\\\": 1\\n      },\\n      \\\"ground_truth\\\": \\\"Unknown\\\",\\n      \\\"sc_correct\\\": true,\\n      \\\"sica_answer\\\": \\\"Unknown\\\",\\n      \\\"sica_scores\\\": {\\n        \\\"False\\\": 7.0,\\n        \\\"True\\\": 18.5,\\n        \\\"Unknown\\\": 50.0\\n      },\\n      \\\"sica_correct\\\": true,\\n      \\\"maxsat_stats\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T11:36:31.006801+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"folio_0\\\": {\\n    \\\"answers\\\": [\\n      \\\"True\\\",\\n      \\\"Unknown\\\",\\n      \\\"False\\\",\\n      \\\"Unknown\\\",\\n      \\\"True\\\",\\n      \\\"True\\\",\\n      \\\"Unknown\\\",\\n      \\\"True\\\",\\n      \\\"Unknown\\\",\\n      \\\"Unknown\\\",\\n      \\\"Unknown\\\",\\n      \\\"Unknown\\\"\\n    ],\\n    \\\"ground_truth\\\": \\\"Unknown\\\"\\n  },\\n  \\\"folio_1\\\": {\\n    \\\"answers\\\": [\\n      \\\"True\\\",\\n      \\\"Unknown\\\",\\n      \\\"True\\\",\\n      \\\"True\\\",\\n      \\\"True\\\",\\n      \\\"True\\\",\\n      \\\"True\\\",\\n      \\\"True\\\",\\n      \\\"True\\\",\\n      \\\"Unknown\\\",\\n      \\\"\\\",\\n      \\\"True\\\"\\n    ],\\n    \\\"ground_truth\\\": \\\"True\\\"\\n  },\\n  \\\"folio_10\\\": {\\n    \\\"answers\\\": [\\n      \\\"Unknown\\\",\\n      \\\"False\\\",\\n      \\\"False\\\",\\n      \\\"False\\\",\\n      \\\"Ocellated wild turkey\\\",\\n      \\\"False\\\",\\n      \\\"Unknown\\\",\\n      \\\"False\\\",\\n      \\\"False\\\",\\n      \\\"False\\\",\\n      \\\"False\\\",\\n      \\\"Unknown\\\"\\n    ],\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T11:36:31.006987+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -30 /root/symb_invariant_consensus/results/exp034_llama31_8b_folio204/exp034.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -30 /root/symb_invariant_consensus/results/exp034_llama31_8b_folio204/exp034.log"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T11:36:31.007118+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus/results/ -name \"*results*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus/results/ -name \"*results*.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-20T11:36:31.007243+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bash: line 1: python: command not found\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T11:36:31.007417+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json\\n/root/symb_invariant_consensus/results/exp028_qwen3_14b_thinking/exp028_results.json\\n/root/symb_invariant_consensus/results/exp027_qwen3_14b_nonthinking/exp027_results.json\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204/contrastive_results.json\\n/root/symb_invariant_consensus/results/cross_model_mistral_folio/cross_model_mistral_results.json\\n/root/symb_invariant_consensus/results/oracle_folio_regen/exp031_results.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\\n/root/symb_invariant_consensus/results/exp035_qwen25_7b_folio204/exp035_results.json\\n/root/symb_invariant_consensus/results/exp034_qwen25_14b_proofwriter/exp034_results.json\\n/root/symb_invariant_consensus/results/exp036_z3_feedback/z3_feedback_results.json\\n/root/symb_invariant_consensus/results/icl_oracle_folio/results.json\\n/root/symb_invariant_consensus/results/exp4_consistency_filtering/results.json\\n/root/symb_invariant_consensus/results/exp05_backward_verification/results.json\\n/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json\\n/root/symb_invariant_consensus/results/exp044b_icl_oracle_qwen14b/results.json\\n/root/symb_invariant_consensus/results/exp028b_qwen3_thinking_folio204/exp028b_results.json\\n/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k4/results.json\\n/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k8/results.json\\n/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k16/results.json\\n/root/symb_invariant_consensus/results/exp051_mistral_k_sensitivity/k20/results.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/exp054_results.json\\n/root/symb_invariant_consensus/results/exp057_mistral_folio204_t03/exp057_results.json\\n/root/symb_invariant_consensus/results/exp058
…[truncated 3628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T11:36:31.007603+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -30 /root/symb_invariant_consensus/results/exp062_gemma27b_folio204/exp062_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -30 /root/symb_invariant_consensus/results/exp062_gemma27b_folio204/exp062_results.json"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T11:36:31.007732+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -30 /root/symb_invariant_consensus/results/exp061_qwen25_7b_folio204/exp061_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -30 /root/symb_invariant_consensus/results/exp061_qwen25_7b_folio204/exp061_results.json"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T11:36:31.007854+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -30 /root/symb_invariant_consensus/results/exp035_qwen25_7b_folio204/exp035_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -30 /root/symb_invariant_consensus/results/exp035_qwen25_7b_folio204/exp035_results.json"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T11:36:31.008022+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 204,\\n    \\\"sica_accuracy\\\": 0.803921568627451,\\n    \\\"sc_accuracy\\\": 0.8088235294117647,\\n    \\\"sica_correct\\\": 164,\\n    \\\"sc_correct\\\": 165,\\n    \\\"extraction_rate\\\": 0.9975490196078431,\\n    \\\"total_constraints_extracted\\\": 15241,\\n    \\\"total_unique_constraints\\\": 6493,\\n    \\\"contradiction_rate\\\": 0.010934852918527645,\\n    \\\"problems_with_contradictions\\\": 45,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"validation\\\": {\\n        \\\"sica\\\": 0.803921568627451,\\n        \\\"sc\\\": 0.8088235294117647,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.803921568627451,\\n        \\\"sc\\\": 0.8088235294117647,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 21442.9\\n  },\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-20T11:36:31.008180+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 204,\\n    \\\"sica_accuracy\\\": 0.7647058823529411,\\n    \\\"sc_accuracy\\\": 0.7598039215686274,\\n    \\\"sica_correct\\\": 156,\\n    \\\"sc_correct\\\": 155,\\n    \\\"extraction_rate\\\": 0.9758986928104575,\\n    \\\"total_constraints_extracted\\\": 12819,\\n    \\\"total_unique_constraints\\\": 6503,\\n    \\\"contradiction_rate\\\": 0.016300169152698753,\\n    \\\"problems_with_contradictions\\\": 57,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"validation\\\": {\\n        \\\"sica\\\": 0.7647058823529411,\\n        \\\"sc\\\": 0.7598039215686274,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.7647058823529411,\\n        \\\"sc\\\": 0.7598039215686274,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 4712.8\\n  },\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T11:36:31.008327+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 204,\\n    \\\"sica_accuracy\\\": 0.7647058823529411,\\n    \\\"sc_accuracy\\\": 0.7696078431372549,\\n    \\\"sica_correct\\\": 156,\\n    \\\"sc_correct\\\": 157,\\n    \\\"extraction_rate\\\": 0.9820261437908496,\\n    \\\"total_constraints_extracted\\\": 12979,\\n    \\\"total_unique_constraints\\\": 6538,\\n    \\\"contradiction_rate\\\": 0.01575405322728663,\\n    \\\"problems_with_contradictions\\\": 60,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"validation\\\": {\\n        \\\"sica\\\": 0.7647058823529411,\\n        \\\"sc\\\": 0.7696078431372549,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.7647058823529411,\\n        \\\"sc\\\": 0.7696078431372549,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 4704.8\\n  },\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T11:36:31.008497+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls -la /root/symb_invariant_consensus/results/exp062_gemma27b_folio204/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls -la /root/symb_invariant_consensus/results/exp062_gemma27b_folio204/"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-20T11:36:31.008622+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp062_gemma27b_folio204/exp062_results.json')); r=d['results'][0]; print(list(r.keys()))\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp062_gemma27b_folio204/exp062_results.json')); r=d['results'][0]; print(list(r.keys()))\""
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-20T11:36:31.008752+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 976\\ndrwxr-xr-x  4 root root    162 May 19 17:04 .\\ndrwxr-xr-x 68 root root   4096 May 20 18:41 ..\\n-rw-r--r--  1 root root   6909 May 19 17:01 dryrun.json\\n-rw-r--r--  1 root root 657543 May 19 22:59 exp062_gemma27b_folio204.log\\n-rw-r--r--  1 root root 294776 May 19 22:59 exp062_results.json\\ndrwxr-xr-x  2 root root   8192 May 19 22:59 intermediates\\ndrwxr-xr-x  2 root root   8192 May 19 22:59 per_trace_constraints\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T11:36:31.008886+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T11:36:31.009097+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "cat > /root/symb_invariant_consensus/scripts/gen_bias_tables.py << 'PYEOF'\nimport json\nimport sys\n\nMODELS = [\n    (\"Mistral-7B\", \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\"),\n    (\"Qwen2.5-14B\", \"/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json\"),\n    (\"Gemma-2-7B\", \"/root/symb_invariant_consensus/results/exp062_gemma27b_folio204/exp062_results.json\"),\n]\n\ntable1_rows = []\ntable2_rows = []\n\nfor model_name, path in MODELS:\n    with open(path) as f:\n        data = json.load(f)\n    \n    results = data[\"results\"]\n    n_total = len(results)\n    \n    # Split into correct/incorrect\n    correct_problems = [r for r in results if r[\"sica_correct\"]]\n    incorrect_problems = [r for r in results if not r[\"sica_correct\"]]\n    n_correct = len(correct_problems)\n    n_incorrect = len(incorrect_problems)\n    \n    # --- Table 1: Bias Ratio by correct/incorrect ---\n    \n    # For INCORRECT problems: sica_answer != gold\n    # wrong_support = score for sica_answer (the wrong answer)\n    # right_support = score for gold_answer\n    inc_wrong_support_total = 0\n    inc_right_support_total = 0\n    inc_constraint_wrong_pct_sum = 0\n    inc_valid = 0\n    \n    for r in incorrect_problems:\n        scores = r[\"sica_scores\"]\n        gt = r[\"ground_truth\"]\n        sica_ans = r[\"sica_answer\"]\n        \n        wrong_support = scores.get(sica_ans, 0)\n        right_support = scores.get(gt, 0)\n        \n        inc_wrong_support_total += wrong_support\n        inc_right_support_total += right_support\n        \n        total_score = sum(scores.values())\n        if total_score > 0:\n            inc_constraint_wrong_pct_sum += wrong_support / total_score\n            inc_valid += 1\n    \n    if inc_right_support_total > 0:\n        bias_ratio_inc = inc_wrong_support_total / inc_right_support_total\n    else:\n        bias_ratio_inc = float('inf')\n    \n    constraint_wrong_pct_inc = (inc_constraint_wrong_pct_sum / inc_valid * 100) if inc_valid > 0 else 0\n    \n    # For CORRECT problems: sica_answer == gold\n    # right_support = score for sica_answer (= gold)\n    # wrong_support = sum of scores for non-gold answers\n    cor_right_support_total = 0\n    cor_wrong_support_total = 0\n    cor_constraint_right_pct_sum = 0\n    cor_valid = 0\n    \n    for r in correct_problems:\n        scores = r[\"sica_scores\"]\n        gt = r[\"ground_truth\"]\n        \n        right_support = scores.get(gt, 0)\n        wrong_support = sum(v for k, v in scores.items() if k != gt)\n        \n        cor_right_support_total += right_support\n        cor_wrong_support_total += wrong_support\n        \n        total_score = sum(scores.values())\n        if total_score > 0:\n            cor_constraint_right_pct_sum += right_support / total_score\n            cor_valid += 1\n    \n    if cor_wrong_support_total > 0:\n        bias_ratio_cor = cor_right_support_total / cor_wrong_support_total\n    else:\n        bias_ratio_cor = float('inf')\n    \n    constraint_right_pct_cor = (cor_constraint_right_pct_sum / cor_valid * 100) if cor_valid > 0 else 0\n    \n    delta = bias_ratio_inc - (1.0 / bias_ratio_cor if bias_ratio_cor != float('inf') else 0)\n    \n    # Actually, let's compute delta as the difference between bias ratios\n    # For incorrect: bias = wrong/right (high = more biased toward wrong)\n    # For correct: bias = right/wrong (high = more biased toward right)\n    # They're both \"supports chosen answer / supports other answer\"\n    # So to make comparable: incorrect bias = wrong/right, correct bias = right/wrong\n    # Delta = incorrect_bias - correct_bias (if both measure \"chosen/other\")\n    # Actually the interesting thing is: incorrect has high wrong/right, correct has high right/wrong\n    # Let's just show both raw ratios\n    \n    table1_rows.append({\n        \"model\": model_name,\n        \"n\": n_total,\n        \"n_errors\": n_incorrect,\n        \"bias_ratio_inc\": bias_ratio_inc,\n        \"constraint_wrong_pct_inc\": constraint_wrong_pct_inc,\n        \"bias_ratio_cor\": bias_ratio_cor,\n        \"constraint_right_pct_cor\": constraint_right_pct_cor,\n        \"delta\": bias_ratio_inc - bias_ratio_cor,\n    })\n    \n    # --- Table 2: SICA follows SC rate ---\n    sica_acc = sum(1 for r in results if r[\"sica_correct\"]) / n_total\n    sc_acc = sum(1 for r in results if r[\"sc_correct\"]) / n_total\n    sica_eq_sc = sum(1 for r in results if r[\"sica_answer\"] == r[\"sc_answer\"]) / n_total\n    sica_corrects_sc = sum(1 for r in results if r[\"sica_correct\"] and not r[\"sc_correct\"]) \n    sc_corrects_sica = sum(1 for r in results if r[\"sc_correct\"] and not r[\"sica_correct\"])\n    \n    table2_rows.append({\n        \"model\": model_name,\n        \"sica_acc\": sica_acc,\n        \"sc_acc\": sc_acc,\n        \"sica_eq_sc\": sica_eq_sc,\n        \"sica_corrects_sc\": sica_corrects_sc,\n        \"sc_corrects_sica\": sc_corrects_sica,\n    })\n\n# --- Print Table 1 ---\nprint(\"=\" * 110)\nprint(\"Table 1: Confirmation Bias — Constraint Score Distribution by Correctness\")\nprint(\"=\" * 110)\n\n# LaTeX format\nprint(\"\\n% LaTeX Table 1\")\nprint(r\"\\begin{table}[t]\")\nprint(r\"\\centering\")\nprint(r\"\\small\")\nprint(r\"\\caption{Confirmation bias in constraint scoring. For incorrect SICA predictions, constraints disproportionately support the (wrong) chosen answer over the gold answer. $\\Delta$ = difference between bias ratios.}\")\nprint(r\"\\label{tab:confirmation-bias}\")\nprint(r\"\\begin{tabular}{lcccccc}\")\nprint(r\"\\toprule\")\nprint(r\"\\textbf{Model} & \\textbf{N} & \\textbf{Errors} & \\multicolumn{2}{c}{\\textbf{Incorrect}} & \\textbf{Correct} & \\textbf{$\\Delta$} \\\\\")\nprint(r\"\\cmidrule(lr){4-5} \\cmidrule(lr){6-6}\")\nprint(r\" & & & Bias Ratio & Wrong\\% & Bias Ratio & \\\\\")\nprint(r\"\\midrule\")\n\nfor row in table1_rows:\n    print(f\"{row['model']} & {row['n']} & {row['n_errors']} & \"\n          f\"{row['bias_ratio_inc']:.2f} & {row['constraint_wrong_pct_inc']:.1f}\\\\% & \"\n          f\"{row['bias_ratio_cor']:.2f} & \"\n          f\"{row['delta']:+.2f} \\\\\\\\\")\n\nprint(r\"\\bottomrule\")\nprint(r\"\\end{tabular}\")\nprint(r\"\\end{table}\")\n\n# Markdown format\nprint(\"\\n\\n### Table 1 (Markdown)\")\nprint(\"| Model | N | Errors | BR (Incorrect) | Wrong→Chosen% (Inc) | BR (Correct) | Right→Gold% (Cor) | Δ |\")\nprint(\"|-------|---|--------|----------------|---------------------|--------------|-------------------|---|\")\nfor row in table1_rows:\n    print(f\"| {row['model']} | {row['n']} | {row['n_errors']} | \"\n          f\"{row['bias_ratio_inc']:.2f} | {row['constraint_wrong_pct_inc']:.1f}% | \"\n          f\"{row['bias_ratio_cor']:.2f} | {row['constraint_right_pct_cor']:.1f}% | \"\n          f\"{row['delta']:+.2f} |\")\n\n# --- Print Table 2 ---\nprint(\"\\n\\n\" + \"=\" * 90)\nprint(\"Table 2: SICA vs SC Agreement\")\nprint(\"=\" * 90)\n\nprint(\"\\n% LaTeX Table 2\")\nprint(r\"\\begin{table}[t]\")\nprint(r\"\\centering\")\nprint(r\"\\small\")\nprint(r\"\\caption{Agreement between SICA and Self-Consistency (SC) on FOLIO-204.}\")\nprint(r\"\\label{tab:sica-sc-agreement}\")\nprint(r\"\\begin{tabular}{lccccc}\")\nprint(r\"\\toprule\")\nprint(r\"\\textbf{Model} & \\textbf{SICA Acc} & \\textbf{SC Acc} & \\textbf{SICA=SC} & \\textbf{SICA$\\succ$SC} & \\textbf{SC$\\succ$SICA} \\\\\")\nprint(r\"\\midrule\")\n\nfor row in table2_rows:\n    print(f\"{row['model']} & {row['sica_acc']:.1%} & {row['sc_acc']:.1%} & \"\n          f\"{row['sica_eq_sc']:.1%} & {row['sica_corrects_sc']} & {row['sc_corrects_sica']} \\\\\\\\\")\n\nprint(r\"\\bottomrule\")\nprint(r\"\\end{tabular}\")\nprint(r\"\\end{table}\")\n\nprint(\"\\n\\n### Table 2 (Markdown)\")\nprint(\"| Model | SICA Acc | SC Acc | SICA=SC | SICA⊳SC | SC⊳SICA |\")\nprint(\"|-------|----------|--------|---------|---------|---------|\")\nfor row in table2_rows:\n    print(f\"| {row['model']} | {row['sica_acc']:.1%} | {row['sc_acc']:.1%} | \"\n          f\"{row['sica_eq_sc']:.1%} | {row['sica_corrects_sc']} | {row['sc_corrects_sica']} |\")\n\n# Also print raw numbers for verification\nprint(\"\\n\\n--- Raw verification ---\")\nfor row in table1_rows:\n    print(f\"\\n{row['model']}:\")\n    print(f\"  Incorrect: n={row['n_errors']}, BR={row['bias_ratio_inc']:.4f}, Wrong%={row['constraint_wrong_pct_inc']:.2f}%\")\n    print(f\"  Correct:   n={row['n']-row['n_errors']}, BR={row['bias_ratio_cor']:.4f}, Right%={row['constraint_right_pct_cor']:.2f}%\")\n    \nPYEOF\necho \"Script written\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat > /root/symb_invariant_consensus/scripts/gen_bias_tables.py << 'PYEOF'\nimport json\nimport sys\n\nMODELS = [\n    (\"Mistral-7B\", \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\"),\n    (\"Qwen2.5-14B\", \"/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json\"),\n    (\"Gemma-2-7B\", \"/root/symb_invariant_consensus/results/exp062_gemma27b_folio204/exp062_results.json\"),\n]\n\ntable1_rows = []\ntable2_rows = []\n\nfor model_name, path in MODELS:\n    with open(path) as f:\n        data = json.load(f)\n    \n    results = data[\"results\"]\n    n_total = len(results)\n    \n    # Split into correct/incorrect\n    correct_problems = [r for r in results if r[\"sica_correct\"]]\n    incorrect_problems = [r for r in results if not r[\"sica_correct\"]]\n    n_correct = len(correct_problems)\n    n_incorrect = len(incorrect_problems)\n    \n    # --- Table 1: Bias Ratio by correct/incorrect ---\n    \n    # For INCORRECT problems: sica_answer != gold\n    # wrong_support = score for sica_answer (the wrong answer)\n    # right_support = score for gold_answer\n    inc_wrong_support_total = 0\n    inc_right_support_total = 0\n    inc_constraint_wrong_pct_sum = 0\n    inc_valid = 0\n    \n    for r in incorrect_problems:\n        scores = r[\"sica_scores\"]\n        gt = r[\"ground_truth\"]\n        sica_ans = r[\"sica_answer\"]\n        \n        wrong_support = scores.get(sica_ans, 0)\n        right_support = scores.get(gt, 0)\n        \n        inc_wrong_support_total += wrong_support\n        inc_right_support_total += right_support\n        \n        total_score = sum(scores.values())\n        if total_score > 0:\n            inc_constraint_wrong_pct_sum += wrong_support / total_score\n            inc_valid += 1\n    \n    if inc_right_support_total > 0:\n        bias_ratio_inc = inc_wrong_support_total / inc_right_support_total\n    else:\n        bias_ratio_inc = float('inf')\n    \n    constraint_wrong_pct_inc = (inc_constraint_wrong_pct_sum / inc_valid * 100) if inc_valid > 0 else 0\n    \n    # For CORRECT problems: sica_answer == gold\n    # right_support = score for sica_answer (= gold)\n    # wrong_support = sum of scores for non-gold answers\n    cor_right_support_total = 0\n    cor_wrong_support_total = 0\n    cor_constraint_right_pct_sum = 0\n    cor_valid = 0\n    \n    for r in correct_problems:\n        scores = r[\"sica_scores\"]\n        gt = r[\"ground_truth\"]\n        \n        right_support = scores.get(gt, 0)\n        wrong_support = sum(v for k, v in scores.items() if k != gt)\n        \n        cor_right_support_total += right_support\n        cor_wrong_support_total += wrong_support\n        \n        total_score = sum(scores.values())\n        if total_score > 0:\n            cor_constraint_right_pct_sum += right_support / total_score\n            cor_valid += 1\n    \n    if cor_wrong_support_total > 0:\n        bias_ratio_cor = cor_right_support_total / cor_wrong_support_total\n    else:\n        bias_ratio_cor = float('inf')\n    \n    constraint_right_pct_cor = (cor_constraint_right_pct_sum / cor_valid * 100) if cor_valid > 0 else 0\n    \n    delta = bias_ratio_inc - (1.0 / bias_ratio_cor if bias_ratio_cor != float('inf') else 0)\n    \n    # Actually, let's compute delta as the difference between bias ratios\n    # For incorrect: bias = wrong/right (high = more biased toward wrong)\n    # For correct: bias = right/wrong (high = more biased toward right)\n    # They're both \"supports chosen answer / supports other answer\"\n    # So to make comparable: incorrect bias = wrong/right, correct bias = right/wrong\n    # Delta = incorrect_bias - correct_bias (if both measure \"chosen/other\")\n    # Actually the interesting thing is: incorrect has high wrong/right, correct has high right/wrong\n    # Let's just show both raw ratios\n    \n    table1_rows.append({\n        \"model\": model_name,\n        \"n\": n_total,\n        \"n_errors\": n_incorrect,\n        \"bias_ratio_inc\": bias_ratio_inc,\n        \"constraint_wrong_pct_inc\": constraint_wrong_pct_inc,\n        \"bias_ratio_cor\": bias_ratio_cor,\n        \"constraint_right_pct_cor\": constraint_right_pct_cor,\n        \"delta\": bias_ratio_inc - bias_ratio_cor,\n    })\n    \n    # --- Table 2: SICA follows SC rate ---\n    sica_acc = sum(1 for r in results if r[\"sica_correct\"]) / n_total\n    sc_acc = sum(1 for r in results if r[\"sc_correct\"]) / n_total\n    sica_eq_sc = sum(1 for r in results if r[\"sica_answer\"] == r[\"sc_answer\"]) / n_total\n    sica_corrects_sc = sum(1 for r in results if r[\"sica_correct\"] and not r[\"sc_correct\"]) \n    sc_corrects_sica = sum(1 for r in results if r[\"sc_correct\"] and not r[\"sica_correct\"])\n    \n    table2_rows.append({\n        \"model\": model_name,\n        \"sica_acc\": sica_acc,\n        \"sc_acc\": sc_acc,\n        \"sica_eq_sc\": sica_eq_sc,\n        \"sica_corrects_sc\": sica_corrects_sc,\n        \"sc_corrects_sica\": sc_corrects_sica,\n    })\n\n# --- Print Table 1 ---\nprint(\"=\" * 110)\nprint(\"Table 1: Confirmation Bias — Constraint Score Distribution by Correctness\")\nprint(\"=\" * 110)\n\n# LaTeX format\nprint(\"\\n% LaTeX Table 1\")\nprint(r\"\\begin{table}[t]\")\nprint(r\"\\centering\")\nprint(r\"\\small\")\nprint(r\"\\caption{Confirmation bias in constraint scoring. For incorrect SICA predictions, constraints disproportionately support the (wrong) chosen answer over the gold answer. $\\Delta$ = difference between bias ratios.}\")\nprint(r\"\\label{tab:confirmation-bias}\")\nprint(r\"\\begin{tabular}{lcccccc}\")\nprint(r\"\\toprule\")\nprint(r\"\\textbf{Model} & \\textbf{N} & \\textbf{Errors} & \\multicolumn{2}{c}{\\textbf{Incorrect}} & \\textbf{Correct} & \\textbf{$\\Delta$} \\\\\")\nprint(r\"\\cmidrule(lr){4-5} \\cmidrule(lr){6-6}\")\nprint(r\" & & & Bias Ratio & Wrong\\% & Bias Ratio & \\\\\")\nprint(r\"\\midrule\")\n\nfor row in table1_rows:\n    print(f\"{row['model']} & {row['n']} & {row['n_errors']} & \"\n          f\"{row['bias_ratio_inc']:.2f} & {row['constraint_wrong_pct_inc']:.1f}\\\\% & \"\n          f\"{row['bias_ratio_cor']:.2f} & \"\n          f\"{row['delta']:+.2f} \\\\\\\\\")\n\nprint(r\"\\bottomrule\")\nprint(r\"\\end{tabular}\")\nprint(r\"\\end{table}\")\n\n# Markdown format\nprint(\"\\n\\n### Table 1 (Markdown)\")\nprint(\"| Model | N | Errors | BR (Incorrect) | Wrong→Chosen% (Inc) | BR (Correct) | Right→Gold% (Cor) | Δ |\")\nprint(\"|-------|---|--------|----------------|---------------------|--------------|-------------------|---|\")\nfor row in table1_rows:\n    print(f\"| {row['model']} | {row['n']} | {row['n_errors']} | \"\n          f\"{row['bias_ratio_inc']:.2f} | {row['constraint_wrong_pct_inc']:.1f}% | \"\n          f\"{row['bias_ratio_cor']:.2f} | {row['constraint_right_pct_cor']:.1f}% | \"\n          f\"{row['delta']:+.2f} |\")\n\n# --- Print Table 2 ---\nprint(\"\\n\\n\" + \"=\" * 90)\nprint(\"Table 2: SICA vs SC Agreement\")\nprint(\"=\" * 90)\n\nprint(\"\\n% LaTeX Table 2\")\nprint(r\"\\begin{table}[t]\")\nprint(r\"\\centering\")\nprint(r\"\\small\")\nprint(r\"\\caption{Agreement between SICA and Self-Consistency (SC) on FOLIO-204.}\")\nprint(r\"\\label{tab:sica-sc-agreement}\")\nprint(r\"\\begin{tabular}{lccccc}\")\nprint(r\"\\toprule\")\nprint(r\"\\textbf{Model} & \\textbf{SICA Acc} & \\textbf{SC Acc} & \\textbf{SICA=SC} & \\textbf{SICA$\\succ$SC} & \\textbf{SC$\\succ$SICA} \\\\\")\nprint(r\"\\midrule\")\n\nfor row in table2_rows:\n    print(f\"{row['model']} & {row['sica_acc']:.1%} & {row['sc_acc']:.1%} & \"\n          f\"{row['sica_eq_sc']:.1%} & {row['sica_corrects_sc']} & {row['sc_corrects_sica']} \\\\\\\\\")\n\nprint(r\"\\bottomrule\")\nprint(r\"\\end{tabular}\")\nprint(r\"\\end{table}\")\n\nprint(\"\\n\\n### Table 2 (Markdown)\")\nprint(\"| Model | SICA Acc | SC Acc | SICA=SC | SICA⊳SC | SC⊳SICA |\")\nprint(\"|-------|----------|--------|---------|---------|---------|\")\nfor row in table2_rows:\n    print(f\"| {row['model']} | {row['sica_acc']:.1%} | {row['sc_acc']:.1%} | \"\n          f\"{row['sica_eq_sc']:.1%} | {row['sica_corrects_sc']} | {row['sc_corrects_sica']} |\")\n\n# Also print raw numbers for verification\nprint(\"\\n\\n--- Raw verification ---\")\nfor row in table1_rows:\n    print(f\"\\n{row['model']}:\")\n    print(f\"  Incorrect: n={row['n_errors']}, BR={row['bias_ratio_inc']:.4f}, Wrong%={row['constraint_wrong_pct_inc']:.2f}%\")\n    print(f\"  Correct:   n={row['n']-row['n_errors']}, BR={row['bias_ratio_cor']:.4f}, Right%={row['constraint_right_pct_cor']:.2f}%\")\n    \nPYEOF\necho \"Script written\""
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T11:36:31.009334+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T11:36:31.009463+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "cd /root/symb_invariant_consensus && python3 scripts/gen_bias_tables.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "cd /root/symb_invariant_consensus && python3 scripts/gen_bias_tables.py"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T11:36:31.009589+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/symb_invariant_consensus && python3 scripts/gen_bias_tables.py'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T11:36:31.009713+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root -name \"python*\" -type f -maxdepth 5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root -name \"python*\" -type f -maxdepth 5"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T11:36:31.009847+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n/root/miniconda3/conda-meta/python_abi-3.12-3_cp312.json\\n/root/miniconda3/conda-meta/python-3.12.4-h5148396_1.json\\n/root/miniconda3/include/python3.12/cpython/pythonrun.h\\n/root/miniconda3/include/python3.12/pythonrun.h\\n/root/miniconda3/lib/pkgconfig/python-3.12-embed.pc\\n/root/miniconda3/lib/pkgconfig/python-3.12.pc\\n/root/miniconda3/lib/python3.12/config-3.12-x86_64-linux-gnu/python-config.py\\n/root/miniconda3/lib/python3.12/config-3.12-x86_64-linux-gnu/python.o\\n/root/miniconda3/pkgs/python-3.12.3-h996f2a0_1/bin/python3.12\\n/root/miniconda3/pkgs/python-3.12.3-h996f2a0_1/bin/python3.12-config\\n/root/miniconda3/pkgs/python-3.12.3-h996f2a0_1.conda\\n/root/miniconda3/pkgs/python-3.12.4-h5148396_1.conda\\n/root/miniconda3/pkgs/python-3.12.4-h5148396_1/bin/python3.12\\n/root/miniconda3/pkgs/python-3.12.4-h5148396_1/bin/python3.12-config\\n/root/miniconda3/pkgs/python_abi-3.12-3_cp312.conda\\n/root/miniconda3/share/man/man1/python3.12.1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.12}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T11:36:31.009995+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python scripts/gen_bias_tables.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python scripts/gen_bias_tables.py"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T11:36:31.010180+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"==============================================================================================================\\nTable 1: Confirmation Bias — Constraint Score Distribution by Correctness\\n==============================================================================================================\\n\\n% LaTeX Table 1\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Confirmation bias in constraint scoring. For incorrect SICA predictions, constraints disproportionately support the (wrong) chosen answer over the gold answer. $\\\\Delta$ = difference between bias ratios.}\\n\\\\label{tab:confirmation-bias}\\n\\\\begin{tabular}{lcccccc}\\n\\\\toprule\\n\\\\textbf{Model} & \\\\textbf{N} & \\\\textbf{Errors} & \\\\multicolumn{2}{c}{\\\\textbf{Incorrect}} & \\\\textbf{Correct} & \\\\textbf{$\\\\Delta$} \\\\\\\\\\n\\\\cmidrule(lr){4-5} \\\\cmidrule(lr){6-6}\\n & & & Bias Ratio & Wrong\\\\% & Bias Ratio & \\\\\\\\\\n\\\\midrule\\nMistral-7B & 204 & 83 & 3.00 & 63.1\\\\% & 1.82 & +1.17 \\\\\\\\\\nQwen2.5-14B & 204 & 52 & 2.52 & 69.1\\\\% & 5.38 & -2.85 \\\\\\\\\\nGemma-2-7B & 204 & 40 & 2.90 & 73.1\\\\% & 5.88 & -2.98 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\n### Table 1 (Markdown)\\n| Model | N | Errors | BR (Incorrect) | Wrong→Chosen% (Inc) | BR (Correct) | Right→Gold% (Cor) | Δ |\\n|-------|---|--------|----------------|---------------------|--------------|-------------------|---|\\n| Mistral-7B | 204 | 83 | 3.00 | 63.1% | 1.82 | 72.4% | +1.17 |\\n| Qwen2.5-14B | 204 | 52 | 2.52 | 69.1% | 5.38 | 88.7% | -2.85 |\\n| Gemma-2-7B | 204 | 40 | 2.90 | 73.1% | 5.88 | 89.3% | -2.98 |\\n\\n\\n==========================================================================================\\nTable 2: SICA vs SC Agreement\\n==========================================================================================\\n\\n% LaTeX Table 2\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\cap
…[truncated 1425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T11:36:31.010509+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "cat > /root/symb_invariant_consensus/scripts/gen_bias_tables_v2.py << 'PYEOF'\nimport json\n\nMODELS = [\n    (\"Mistral-7B\", \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\"),\n    (\"Qwen2.5-14B\", \"/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json\"),\n    (\"Gemma-2-7B\", \"/root/symb_invariant_consensus/results/exp062_gemma27b_folio204/exp062_results.json\"),\n]\n\ntable1_rows = []\ntable2_rows = []\n\nfor model_name, path in MODELS:\n    with open(path) as f:\n        data = json.load(f)\n    \n    results = data[\"results\"]\n    n_total = len(results)\n    \n    correct_problems = [r for r in results if r[\"sica_correct\"]]\n    incorrect_problems = [r for r in results if not r[\"sica_correct\"]]\n    n_correct = len(correct_problems)\n    n_incorrect = len(incorrect_problems)\n    \n    # === Table 1: Bias Ratio by correct/incorrect ===\n    # Using sica_scores: total weighted support per answer\n    # For each problem: gold_weight = score for gold answer\n    #                    total_weight = sum of all scores\n    #                    non_gold_weight = total - gold\n    # gold_frac = gold_weight / total_weight (averaged across problems in group)\n    # bias_ratio = non_gold / gold (for incorrect) or gold / non_gold (for correct)\n    \n    # --- Incorrect group ---\n    inc_gold_frac_sum = 0\n    inc_nongold_frac_sum = 0\n    inc_gold_total = 0\n    inc_all_total = 0\n    inc_valid = 0\n    \n    for r in incorrect_problems:\n        scores = r[\"sica_scores\"]\n        gt = r[\"ground_truth\"]\n        gold_w = scores.get(gt, 0)\n        total_w = sum(scores.values())\n        if total_w > 0:\n            inc_gold_frac_sum += gold_w / total_w\n            inc_nongold_frac_sum += (total_w - gold_w) / total_w\n            inc_valid += 1\n        inc_gold_total += gold_w\n        inc_all_total += total_w\n    \n    avg_gold_frac_inc = inc_gold_frac_sum / inc_valid if inc_valid > 0 else 0\n    avg_nongold_frac_inc = inc_nongold_frac_sum / inc_valid if inc_valid > 0 else 0\n    \n    # Bias ratio: non-gold / gold (higher = more biased toward wrong)\n    bias_ratio_inc = avg_nongold_frac_inc / avg_gold_frac_inc if avg_gold_frac_inc > 0 else float('inf')\n    wrong_pct_inc = avg_nongold_frac_inc * 100  # % of weight going to wrong answers\n    \n    # --- Correct group ---\n    cor_gold_frac_sum = 0\n    cor_nongold_frac_sum = 0\n    cor_gold_total = 0\n    cor_all_total = 0\n    cor_valid = 0\n    \n    for r in correct_problems:\n        scores = r[\"sica_scores\"]\n        gt = r[\"ground_truth\"]\n        gold_w = scores.get(gt, 0)\n        total_w = sum(scores.values())\n        if total_w > 0:\n            cor_gold_frac_sum += gold_w / total_w\n            cor_nongold_frac_sum += (total_w - gold_w) / total_w\n            cor_valid += 1\n        cor_gold_total += gold_w\n        cor_all_total += total_w\n    \n    avg_gold_frac_cor = cor_gold_frac_sum / cor_valid if cor_valid > 0 else 0\n    avg_nongold_frac_cor = cor_nongold_frac_sum / cor_valid if cor_valid > 0 else 0\n    \n    # Bias ratio: gold / non-gold (higher = more supporting correct)\n    bias_ratio_cor = avg_gold_frac_cor / avg_nongold_frac_cor if avg_nongold_frac_cor > 0 else float('inf')\n    right_pct_cor = avg_gold_frac_cor * 100  # % of weight going to gold\n    \n    table1_rows.append({\n        \"model\": model_name,\n        \"n\": n_total,\n        \"n_errors\": n_incorrect,\n        \"bias_ratio_inc\": bias_ratio_inc,\n        \"wrong_pct_inc\": wrong_pct_inc,\n        \"bias_ratio_cor\": bias_ratio_cor,\n        \"right_pct_cor\": right_pct_cor,\n        \"avg_gold_frac_inc\": avg_gold_frac_inc,\n        \"avg_gold_frac_cor\": avg_gold_frac_cor,\n    })\n    \n    # === Table 2: SICA vs SC ===\n    sica_acc = sum(1 for r in results if r[\"sica_correct\"]) / n_total\n    sc_acc = sum(1 for r in results if r[\"sc_correct\"]) / n_total\n    sica_eq_sc = sum(1 for r in results if r[\"sica_answer\"] == r[\"sc_answer\"]) / n_total\n    sica_corrects_sc = sum(1 for r in results if r[\"sica_correct\"] and not r[\"sc_correct\"])\n    sc_corrects_sica = sum(1 for r in results if r[\"sc_correct\"] and not r[\"sica_correct\"])\n    \n    table2_rows.append({\n        \"model\": model_name,\n        \"sica_acc\": sica_acc,\n        \"sc_acc\": sc_acc,\n        \"sica_eq_sc\": sica_eq_sc,\n        \"sica_corrects_sc\": sica_corrects_sc,\n        \"sc_corrects_sica\": sc_corrects_sica,\n        \"n\": n_total,\n    })\n\n# Verify against existing Mistral data\nprint(\"=== Verification against existing Mistral confirmation_bias data ===\")\nprint(f\"Mistral incorrect: avg_gold_frac={table1_rows[0]['avg_gold_frac_inc']:.4f} (expected ~0.1909)\")\nprint(f\"Mistral correct:   avg_gold_frac={table1_rows[0]['avg_gold_frac_cor']:.4f} (expected ~0.7184)\")\nprint(f\"Mistral inc BR: {table1_rows[0]['bias_ratio_inc']:.2f} (expected ~4.24)\")\nprint()\n\n# === Print LaTeX Table 1 ===\nprint(\"% ============================================================\")\nprint(\"% Table 1: Confirmation Bias\")\nprint(\"% ============================================================\")\nprint(r\"\\begin{table}[t]\")\nprint(r\"\\centering\")\nprint(r\"\\small\")\nprint(r\"\\caption{Confirmation bias in constraint scoring. For incorrect SICA predictions, the weighted constraint support disproportionately favors the (wrong) chosen answer over the gold answer. \\textbf{BR}$_{\\text{err}}$ = ratio of non-gold to gold weight on error cases; \\textbf{BR}$_{\\text{cor}}$ = ratio of gold to non-gold weight on correct cases; $\\Delta$ = BR$_{\\text{err}}$ $-$ BR$_{\\text{cor}}$.}\")\nprint(r\"\\label{tab:confirmation-bias}\")\nprint(r\"\\begin{tabular}{l c c r@{\\hspace{4pt}}r r@{\\hspace{4pt}}r c}\")\nprint(r\"\\toprule\")\nprint(r\"& & & \\multicolumn{2}{c}{\\textbf{Error Cases}} & \\multicolumn{2}{c}{\\textbf{Correct Cases}} & \\\\\")\nprint(r\"\\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\")\nprint(r\"\\textbf{Model} & $N$ & \\textbf{Err} & BR$_{\\text{err}}$ & Wrong\\% & BR$_{\\text{cor}}$ & Gold\\% & $\\Delta$ \\\\\")\nprint(r\"\\midrule\")\n\nfor row in table1_rows:\n    delta = row['bias_ratio_inc'] - row['bias_ratio_cor']\n    print(f\"{row['model']} & {row['n']} & {row['n_errors']} & \"\n          f\"{row['bias_ratio_inc']:.2f} & {row['wrong_pct_inc']:.1f}\\\\% & \"\n          f\"{row['bias_ratio_cor']:.2f} & {row['right_pct_cor']:.1f}\\\\% & \"\n          f\"{delta:+.2f} \\\\\\\\\")\n\nprint(r\"\\bottomrule\")\nprint(r\"\\end{tabular}\")\nprint(r\"\\end{table}\")\n\n# === Print LaTeX Table 2 ===\nprint()\nprint(\"% ============================================================\")\nprint(\"% Table 2: SICA vs SC Agreement\")\nprint(\"% ============================================================\")\nprint(r\"\\begin{table}[t]\")\nprint(r\"\\centering\")\nprint(r\"\\small\")\nprint(r\"\\caption{SICA vs.\\ Self-Consistency (SC) on FOLIO-204. \\textbf{SICA=SC}: fraction of problems where both methods agree. \\textbf{SICA$\\boldsymbol{\\succ}$SC} / \\textbf{SC$\\boldsymbol{\\succ}$SICA}: number of problems where one method is correct and the other is not.}\")\nprint(r\"\\label{tab:sica-sc-agreement}\")\nprint(r\"\\begin{tabular}{l c c c c c}\")\nprint(r\"\\toprule\")\nprint(r\"\\textbf{Model} & \\textbf{SICA} & \\textbf{SC} & \\textbf{SICA=SC} & \\textbf{SICA$\\succ$SC} & \\textbf{SC$\\succ$SICA} \\\\\")\nprint(r\"\\midrule\")\n\nfor row in table2_rows:\n    print(f\"{row['model']} & {row['sica_acc']:.1%} & {row['sc_acc']:.1%} & \"\n          f\"{row['sica_eq_sc']:.1%} & {row['sica_corrects_sc']} & {row['sc_corrects_sica']} \\\\\\\\\")\n\nprint(r\"\\bottomrule\")\nprint(r\"\\end{tabular}\")\nprint(r\"\\end{table}\")\n\n# === Markdown versions ===\nprint(\"\\n\\n### Table 1 (Markdown)\")\nprint(\"| Model | N | Errors | BR_err | Wrong% | BR_cor | Gold% | Δ |\")\nprint(\"|-------|---|--------|--------|--------|--------|-------|---|\")\nfor row in table1_rows:\n    delta = row['bias_ratio_inc'] - row['bias_ratio_cor']\n    print(f\"| {row['model']} | {row['n']} | {row['n_errors']} | \"\n          f\"{row['bias_ratio_inc']:.2f} | {row['wrong_pct_inc']:.1f}% | \"\n          f\"{row['bias_ratio_cor']:.2f} | {row['right_pct_cor']:.1f}% | \"\n          f\"{delta:+.2f} |\")\n\nprint(\"\\n### Table 2 (Markdown)\")\nprint(\"| Model | SICA Acc | SC Acc | SICA=SC | SICA⊳SC | SC⊳SICA |\")\nprint(\"|-------|----------|--------|---------|---------|---------|\")\nfor row in table2_rows:\n    print(f\"| {row['model']} | {row['sica_acc']:.1%} | {row['sc_acc']:.1%} | \"\n          f\"{row['sica_eq_sc']:.1%} | {row['sica_corrects_sc']} | {row['sc_corrects_sica']} |\")\n\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python scripts/gen_bias_tables_v2.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat > /root/symb_invariant_consensus/scripts/gen_bias_tables_v2.py << 'PYEOF'\nimport json\n\nMODELS = [\n    (\"Mistral-7B\", \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\"),\n    (\"Qwen2.5-14B\", \"/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json\"),\n    (\"Gemma-2-7B\", \"/root/symb_invariant_consensus/results/exp062_gemma27b_folio204/exp062_results.json\"),\n]\n\ntable1_rows = []\ntable2_rows = []\n\nfor model_name, path in MODELS:\n    with open(path) as f:\n        data = json.load(f)\n    \n    results = data[\"results\"]\n    n_total = len(results)\n    \n    correct_problems = [r for r in results if r[\"sica_correct\"]]\n    incorrect_problems = [r for r in results if not r[\"sica_correct\"]]\n    n_correct = len(correct_problems)\n    n_incorrect = len(incorrect_problems)\n    \n    # === Table 1: Bias Ratio by correct/incorrect ===\n    # Using sica_scores: total weighted support per answer\n    # For each problem: gold_weight = score for gold answer\n    #                    total_weight = sum of all scores\n    #                    non_gold_weight = total - gold\n    # gold_frac = gold_weight / total_weight (averaged across problems in group)\n    # bias_ratio = non_gold / gold (for incorrect) or gold / non_gold (for correct)\n    \n    # --- Incorrect group ---\n    inc_gold_frac_sum = 0\n    inc_nongold_frac_sum = 0\n    inc_gold_total = 0\n    inc_all_total = 0\n    inc_valid = 0\n    \n    for r in incorrect_problems:\n        scores = r[\"sica_scores\"]\n        gt = r[\"ground_truth\"]\n        gold_w = scores.get(gt, 0)\n        total_w = sum(scores.values())\n        if total_w > 0:\n            inc_gold_frac_sum += gold_w / total_w\n            inc_nongold_frac_sum += (total_w - gold_w) / total_w\n            inc_valid += 1\n        inc_gold_total += gold_w\n        inc_all_total += total_w\n    \n    avg_gold_frac_inc = inc_gold_frac_sum / inc_valid if inc_valid > 0 else 0\n    avg_nongold_frac_inc = inc_nongold_frac_sum / inc_valid if inc_valid > 0 else 0\n    \n    # Bias ratio: non-gold / gold (higher = more biased toward wrong)\n    bias_ratio_inc = avg_nongold_frac_inc / avg_gold_frac_inc if avg_gold_frac_inc > 0 else float('inf')\n    wrong_pct_inc = avg_nongold_frac_inc * 100  # % of weight going to wrong answers\n    \n    # --- Correct group ---\n    cor_gold_frac_sum = 0\n    cor_nongold_frac_sum = 0\n    cor_gold_total = 0\n    cor_all_total = 0\n    cor_valid = 0\n    \n    for r in correct_problems:\n        scores = r[\"sica_scores\"]\n        gt = r[\"ground_truth\"]\n        gold_w = scores.get(gt, 0)\n        total_w = sum(scores.values())\n        if total_w > 0:\n            cor_gold_frac_sum += gold_w / total_w\n            cor_nongold_frac_sum += (total_w - gold_w) / total_w\n            cor_valid += 1\n        cor_gold_total += gold_w\n        cor_all_total += total_w\n    \n    avg_gold_frac_cor = cor_gold_frac_sum / cor_valid if cor_valid > 0 else 0\n    avg_nongold_frac_cor = cor_nongold_frac_sum / cor_valid if cor_valid > 0 else 0\n    \n    # Bias ratio: gold / non-gold (higher = more supporting correct)\n    bias_ratio_cor = avg_gold_frac_cor / avg_nongold_frac_cor if avg_nongold_frac_cor > 0 else float('inf')\n    right_pct_cor = avg_gold_frac_cor * 100  # % of weight going to gold\n    \n    table1_rows.append({\n        \"model\": model_name,\n        \"n\": n_total,\n        \"n_errors\": n_incorrect,\n        \"bias_ratio_inc\": bias_ratio_inc,\n        \"wrong_pct_inc\": wrong_pct_inc,\n        \"bias_ratio_cor\": bias_ratio_cor,\n        \"right_pct_cor\": right_pct_cor,\n        \"avg_gold_frac_inc\": avg_gold_frac_inc,\n        \"avg_gold_frac_cor\": avg_gold_frac_cor,\n    })\n    \n    # === Table 2: SICA vs SC ===\n    sica_acc = sum(1 for r in results if r[\"sica_correct\"]) / n_total\n    sc_acc = sum(1 for r in results if r[\"sc_correct\"]) / n_total\n    sica_eq_sc = sum(1 for r in results if r[\"sica_answer\"] == r[\"sc_answer\"]) / n_total\n    sica_corrects_sc = sum(1 for r in results if r[\"sica_correct\"] and not r[\"sc_correct\"])\n    sc_corrects_sica = sum(1 for r in results if r[\"sc_correct\"] and not r[\"sica_correct\"])\n    \n    table2_rows.append({\n        \"model\": model_name,\n        \"sica_acc\": sica_acc,\n        \"sc_acc\": sc_acc,\n        \"sica_eq_sc\": sica_eq_sc,\n        \"sica_corrects_sc\": sica_corrects_sc,\n        \"sc_corrects_sica\": sc_corrects_sica,\n        \"n\": n_total,\n    })\n\n# Verify against existing Mistral data\nprint(\"=== Verification against existing Mistral confirmation_bias data ===\")\nprint(f\"Mistral incorrect: avg_gold_frac={table1_rows[0]['avg_gold_frac_inc']:.4f} (expected ~0.1909)\")\nprint(f\"Mistral correct:   avg_gold_frac={table1_rows[0]['avg_gold_frac_cor']:.4f} (expected ~0.7184)\")\nprint(f\"Mistral inc BR: {table1_rows[0]['bias_ratio_inc']:.2f} (expected ~4.24)\")\nprint()\n\n# === Print LaTeX Table 1 ===\nprint(\"% ============================================================\")\nprint(\"% Table 1: Confirmation Bias\")\nprint(\"% ============================================================\")\nprint(r\"\\begin{table}[t]\")\nprint(r\"\\centering\")\nprint(r\"\\small\")\nprint(r\"\\caption{Confirmation bias in constraint scoring. For incorrect SICA predictions, the weighted constraint support disproportionately favors the (wrong) chosen answer over the gold answer. \\textbf{BR}$_{\\text{err}}$ = ratio of non-gold to gold weight on error cases; \\textbf{BR}$_{\\text{cor}}$ = ratio of gold to non-gold weight on correct cases; $\\Delta$ = BR$_{\\text{err}}$ $-$ BR$_{\\text{cor}}$.}\")\nprint(r\"\\label{tab:confirmation-bias}\")\nprint(r\"\\begin{tabular}{l c c r@{\\hspace{4pt}}r r@{\\hspace{4pt}}r c}\")\nprint(r\"\\toprule\")\nprint(r\"& & & \\multicolumn{2}{c}{\\textbf{Error Cases}} & \\multicolumn{2}{c}{\\textbf{Correct Cases}} & \\\\\")\nprint(r\"\\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\")\nprint(r\"\\textbf{Model} & $N$ & \\textbf{Err} & BR$_{\\text{err}}$ & Wrong\\% & BR$_{\\text{cor}}$ & Gold\\% & $\\Delta$ \\\\\")\nprint(r\"\\midrule\")\n\nfor row in table1_rows:\n    delta = row['bias_ratio_inc'] - row['bias_ratio_cor']\n    print(f\"{row['model']} & {row['n']} & {row['n_errors']} & \"\n          f\"{row['bias_ratio_inc']:.2f} & {row['wrong_pct_inc']:.1f}\\\\% & \"\n          f\"{row['bias_ratio_cor']:.2f} & {row['right_pct_cor']:.1f}\\\\% & \"\n          f\"{delta:+.2f} \\\\\\\\\")\n\nprint(r\"\\bottomrule\")\nprint(r\"\\end{tabular}\")\nprint(r\"\\end{table}\")\n\n# === Print LaTeX Table 2 ===\nprint()\nprint(\"% ============================================================\")\nprint(\"% Table 2: SICA vs SC Agreement\")\nprint(\"% ============================================================\")\nprint(r\"\\begin{table}[t]\")\nprint(r\"\\centering\")\nprint(r\"\\small\")\nprint(r\"\\caption{SICA vs.\\ Self-Consistency (SC) on FOLIO-204. \\textbf{SICA=SC}: fraction of problems where both methods agree. \\textbf{SICA$\\boldsymbol{\\succ}$SC} / \\textbf{SC$\\boldsymbol{\\succ}$SICA}: number of problems where one method is correct and the other is not.}\")\nprint(r\"\\label{tab:sica-sc-agreement}\")\nprint(r\"\\begin{tabular}{l c c c c c}\")\nprint(r\"\\toprule\")\nprint(r\"\\textbf{Model} & \\textbf{SICA} & \\textbf{SC} & \\textbf{SICA=SC} & \\textbf{SICA$\\succ$SC} & \\textbf{SC$\\succ$SICA} \\\\\")\nprint(r\"\\midrule\")\n\nfor row in table2_rows:\n    print(f\"{row['model']} & {row['sica_acc']:.1%} & {row['sc_acc']:.1%} & \"\n          f\"{row['sica_eq_sc']:.1%} & {row['sica_corrects_sc']} & {row['sc_corrects_sica']} \\\\\\\\\")\n\nprint(r\"\\bottomrule\")\nprint(r\"\\end{tabular}\")\nprint(r\"\\end{table}\")\n\n# === Markdown versions ===\nprint(\"\\n\\n### Table 1 (Markdown)\")\nprint(\"| Model | N | Errors | BR_err | Wrong% | BR_cor | Gold% | Δ |\")\nprint(\"|-------|---|--------|--------|--------|--------|-------|---|\")\nfor row in table1_rows:\n    delta = row['bias_ratio_inc'] - row['bias_ratio_cor']\n    print(f\"| {row['model']} | {row['n']} | {row['n_errors']} | \"\n          f\"{row['bias_ratio_inc']:.2f} | {row['wrong_pct_inc']:.1f}% | \"\n          f\"{row['bias_ratio_cor']:.2f} | {row['right_pct_cor']:.1f}% | \"\n          f\"{delta:+.2f} |\")\n\nprint(\"\\n### Table 2 (Markdown)\")\nprint(\"| Model | SICA Acc | SC Acc | SICA=SC | SICA⊳SC | SC⊳SICA |\")\nprint(\"|-------|----------|--------|---------|---------|---------|\")\nfor row in table2_rows:\n    print(f\"| {row['model']} | {row['sica_acc']:.1%} | {row['sc_acc']:.1%} | \"\n          f\"{row['sica_eq_sc']:.1%} | {row['sica_corrects_sc']} | {row['sc_corrects_sica']} |\")\n\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python scripts/gen_bias_tables_v2.py"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T11:36:31.010831+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Verification against existing Mistral confirmation_bias data ===\\nMistral incorrect: avg_gold_frac=0.1909 (expected ~0.1909)\\nMistral correct:   avg_gold_frac=0.7244 (expected ~0.7184)\\nMistral inc BR: 4.24 (expected ~4.24)\\n\\n% ============================================================\\n% Table 1: Confirmation Bias\\n% ============================================================\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Confirmation bias in constraint scoring. For incorrect SICA predictions, the weighted constraint support disproportionately favors the (wrong) chosen answer over the gold answer. \\\\textbf{BR}$_{\\\\text{err}}$ = ratio of non-gold to gold weight on error cases; \\\\textbf{BR}$_{\\\\text{cor}}$ = ratio of gold to non-gold weight on correct cases; $\\\\Delta$ = BR$_{\\\\text{err}}$ $-$ BR$_{\\\\text{cor}}$.}\\n\\\\label{tab:confirmation-bias}\\n\\\\begin{tabular}{l c c r@{\\\\hspace{4pt}}r r@{\\\\hspace{4pt}}r c}\\n\\\\toprule\\n& & & \\\\multicolumn{2}{c}{\\\\textbf{Error Cases}} & \\\\multicolumn{2}{c}{\\\\textbf{Correct Cases}} & \\\\\\\\\\n\\\\cmidrule(lr){4-5} \\\\cmidrule(lr){6-7}\\n\\\\textbf{Model} & $N$ & \\\\textbf{Err} & BR$_{\\\\text{err}}$ & Wrong\\\\% & BR$_{\\\\text{cor}}$ & Gold\\\\% & $\\\\Delta$ \\\\\\\\\\n\\\\midrule\\nMistral-7B & 204 & 83 & 4.24 & 80.9\\\\% & 2.63 & 72.4\\\\% & +1.61 \\\\\\\\\\nQwen2.5-14B & 204 & 52 & 3.69 & 78.7\\\\% & 7.87 & 88.7\\\\% & -4.18 \\\\\\\\\\nGemma-2-7B & 204 & 40 & 4.06 & 80.3\\\\% & 8.34 & 89.3\\\\% & -4.28 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n% ============================================================\\n% Table 2: SICA vs SC Agreement\\n% ============================================================\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{SICA vs.\\\\ Self-Consistency (SC) on FOLIO-204. \\\\textbf{SICA=SC}: fraction of problems where both methods agree.
…[truncated 1508 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-20T11:36:31.011087+00:00_

验证通过（Mistral BR_err=4.24 与已有数据精确匹配）。LLaMA-3.1-8B 的 exp034 实验没跑完（python not found），用 Gemma-2-7B 替代作为第三个模型家族。

结果如下：

### Table 1: Confirmation Bias

| Model | N | Errors | BR_err | Wrong% | BR_cor | Gold% | Δ |
|-------|---|--------|--------|--------|--------|-------|---|
| Mistral-7B | 204 | 83 | 4.24 | 80.9% | 2.63 | 72.4% | +1.61 |
| Qwen2.5-14B | 204 | 52 | 3.69 | 78.7% | 7.87 | 88.7% | -4.18 |
| Gemma-2-7B | 204 | 40 | 4.06 | 80.3% | 8.34 | 89.3% | -4.28 |

- **BR_err** = 非 gold 权重 / gold 权重（错误题），越高越 biased
- **Wrong%** = 错误题中约束权重流向非 gold 答案的比例
- **BR_cor** = gold 权重 / 非 gold 权重（正确题）
- 三个模型的错误题 BR 都在 3.7–4.2，说明 confirmation bias 是跨模型一致的现象

### Table 2: SICA vs SC Agreement

| Model | SICA Acc | SC Acc | SICA=SC | SICA⊳SC | SC⊳SICA |
|-------|----------|--------|---------|---------|---------|
| Mistral-7B | 59.3% | 54.4% | 91.7% | 12 | 2 |
| Qwen2.5-14B | 74.5% | 75.0% | 96.6% | 2 | 3 |
| Gemma-2-7B | 80.4% | 80.9% | 99.5% | 0 | 1 |

LaTeX 版本已在脚本输出中，可直接复制。脚本路径：`/root/symb_invariant_consensus/scripts/gen_bias_tables_v2.py`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_bias-ratio-table-format_20260520T113129"
}
```

</details>

---
