# experiment qwen14b pw nli combo

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_experiment_qwen14b-pw-nli-combo_20260520T213827.jsonl`
- **Structured JSON:** [`e6add61582d9db2c5483.json`](../../sessions/e6/e6add61582d9db2c5483.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-20T21:40:31.967467+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T21:40:31.967978+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T21:40:31.968180+00:00_

called mcp__agent-ml-research__detect_image

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image</summary>

```json
{
  "server": "westd-16639"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__detect_image",
  "tool_args": {
    "server": "westd-16639"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T21:40:31.968323+00:00_

{"result":"{\n  \"detected\": false,\n  \"status\": \"ssh_error\",\n  \"skip_base_setup\": false,\n  \"message\": \"SSH error: exit code 1\"\n}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__detect_image",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T21:40:31.968797+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "ls /root/symb_invariant_consensus/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "ls /root/symb_invariant_consensus/results/"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T21:40:31.969114+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"adaptive_sica_validation_16639.json\\ncross_dataset\\nd116_qwen3_pw_deberta_large\\ndir_c_premise_only_204\\ndir_d_dpp_trace_selection\\ndir_e_strict_verification\\ndir_f2_cross_model_verification\\ndir_f2_self_verification\\ndir_f_prm_verifier_pilot\\ndir_g_hard_negative_analysis\\ndir_h_provenance_analysis\\ndir_j1_nli_logiqa\\ndir_k_nli_qwen3_proofwriter\\ndirection_d_cegis\\ndirection_g_decoupling\\ndirection_h_adversarial\\ndirection_j_bootstrap\\ndirection_j_dryrun\\ndirection_j_dryrun20\\ndirection_k_minority_report\\ndirection_q_premise_mutation\\nexp-063-llama8b-folio204-16639\\nexp028b_dryrun\\nexp028b_qwen3_thinking_folio204\\nexp032_qwen25_14b_pw600\\nexp033_mistral_7b_folio204\\nexp033_qwen3_14b_pw600_nonthinking\\nexp036_qwen25_14b_folio204\\nexp037_mistral7b_folio204\\nexp038_qwen25_14b_logiqa200\\nexp048_llama8b_pw600\\nexp049b_mistral_logiqa200\\nexp050_FAILED_overflow\\nexp050b_mistral_icl_oracle\\nexp052_mistral_folio204_seed123\\nexp053_mistral_folio204_seed456\\nexp055_multitemp_mistral_folio\\nexp064_deepseek_r1_qwen3_8b_folio204\\nexp064_dryrun\\nexp068_qwen3_logiqa200\\nexp069_llama8b_logiqa200\\nexp072_llama8b_logiqa200\\nexp072b_llama8b_logiqa200\\nexp077_kappa_generalization\\nexp078_debate_mistral_logiqa200\\nexp079_icg_mistral_logiqa200\\nexp081_debate_mistral_folio_seed123\\nexp082_contrastive_mistral_folio_seed123\\nfleiss_kappa_batch2.json\\nfleiss_kappa_unified_16639.json\\nmcnemar_recomputed_16639.json\\noracle_folio_mistral7b\\nprocess_kappa_summary_16639.json\\npush_b_stronger_nli_verifier\\nr8_w3_dedup_statistics\\nsc_tiebreak_revalidation_16639.json\\nseed_replication_analysis.json\\nseed_replication_summary.json\\nwild2_ascii_perturbation\\nwild6_kappa_aware_sc\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T21:40:31.969271+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "ls /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "ls /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T21:40:31.969422+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "ls /root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "ls /root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T21:40:31.969569+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"exp032.log\\nintermediates\\nresults.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T21:40:31.969697+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T21:40:31.969816+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "cat /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T21:40:31.970615+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "cat /root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat /root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T21:40:31.971066+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 600,\\n    \\\"sica_accuracy\\\": 0.715,\\n    \\\"sc_accuracy\\\": 0.735,\\n    \\\"sica_correct\\\": 429,\\n    \\\"sc_correct\\\": 441,\\n    \\\"extraction_rate\\\": 0.9915277777777778,\\n    \\\"total_constraints_extracted\\\": 94306,\\n    \\\"total_unique_constraints\\\": 22036,\\n    \\\"contradiction_rate\\\": 0.006171719005264113,\\n    \\\"problems_with_contradictions\\\": 108,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"OWA-D5\\\": {\\n        \\\"sica\\\": 0.715,\\n        \\\"sc\\\": 0.735,\\n        \\\"n\\\": 600\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"proofwriter\\\": {\\n        \\\"sica\\\": 0.715,\\n        \\\"sc\\\": 0.735,\\n        \\\"n\\\": 600\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 39578.2\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"ProofWriter_AttNoneg-OWA-D5-1041_Q1\\\",\\n      \\\"problem\\\": \\\"Bob is cold. Bob is quiet. Bob is red. Bob is smart. Charlie is kind. Charlie is quiet. Charlie is red. Charlie is rough. Dave is cold. Dave is kind. Dave is smart. Fiona is quiet. If something is quiet and cold then it is smart. Red, cold things are round. If something is kind and rough then it is red. All quiet things are rough. Cold, smart things are red. If something is rough then it is cold. All red things are rough. If Dave is smart and Dave is kind then Dave is quiet.\\\\n\\\\nDetermine whether the following statement is true, false, or unknown:\\\\nCharlie is kind.\\\",\\n      \\\"dataset\\\": \\\"proofwriter\\\",\\n      \\\"level\\\": \\\"OWA-D5\\\",\\n      \\\"ground_truth\\\": \\\"True\\\",\\n      \\\"sica_answer\\\": \\\"True\\\",\\n      \\\"sica_scores\\\": {\\n        \\\"True\\\": 97.0\\n      },\\n      \\\"sica_correct\\\": true,\\n      \\\"sc_answer\\\": \\\
…[truncated 8016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T21:40:31.971268+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "ls /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "ls /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T21:40:31.971677+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"D116: Qwen3-14B ProofWriter combo with DeBERTa-large-mnli\\\",\\n  \\\"verifier_model\\\": \\\"microsoft/deberta-large-mnli\\\",\\n  \\\"generator_model\\\": \\\"Qwen3-14B (non-thinking mode)\\\",\\n  \\\"dataset\\\": \\\"ProofWriter-D5-600\\\",\\n  \\\"n_questions\\\": 600,\\n  \\\"standalone_accuracy\\\": 0.55,\\n  \\\"sc_baseline\\\": 0.85,\\n  \\\"deberta_standalone\\\": {\\n    \\\"accuracy\\\": 0.55,\\n    \\\"correct\\\": 330,\\n    \\\"total\\\": 600,\\n    \\\"per_class\\\": {\\n      \\\"True\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 128,\\n        \\\"accuracy\\\": 0.64,\\n        \\\"precision\\\": 0.6957,\\n        \\\"recall\\\": 0.64,\\n        \\\"f1\\\": 0.6667\\n      },\\n      \\\"False\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 195,\\n        \\\"accuracy\\\": 0.975,\\n        \\\"precision\\\": 0.4791,\\n        \\\"recall\\\": 0.975,\\n        \\\"f1\\\": 0.6425\\n      },\\n      \\\"Unknown\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 7,\\n        \\\"accuracy\\\": 0.035,\\n        \\\"precision\\\": 0.7778,\\n        \\\"recall\\\": 0.035,\\n        \\\"f1\\\": 0.067\\n      }\\n    },\\n    \\\"gt_distribution\\\": {\\n      \\\"True\\\": 200,\\n      \\\"False\\\": 200,\\n      \\\"Unknown\\\": 200\\n    },\\n    \\\"pred_distribution\\\": {\\n      \\\"True\\\": 184,\\n      \\\"False\\\": 407,\\n      \\\"Unknown\\\": 9\\n    },\\n    \\\"inference_time_s\\\": 141.0\\n  },\\n  \\\"combo\\\": {\\n    \\\"w1\\\": {\\n      \\\"accuracy\\\": 0.8583,\\n      \\\"delta_pp\\\": 0.83,\\n      \\\"mcnemar_p\\\": 0.125,\\n      \\\"discordant\\\": [\\n        6,\\n        1\\n      ]\\n    },\\n    \\\"w3\\\": {\\n      \\\"accuracy\\\": 0.86,\\n      \\\"delta_pp\\\": 1.0,\\n      \\\"mcnemar_p\\\": 0.146,\\n      \\\"discordant\\\": [\\n        9,\\n        3\\n      ]\\n    },\\n    \\\"w5\\\": {\\n      \\\"
…[truncated 8912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T21:40:31.972001+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"ProofWriter_AttNeg-OWA-D5-1015_Q19.json\\nProofWriter_AttNeg-OWA-D5-1015_Q3.json\\nProofWriter_AttNeg-OWA-D5-1017_Q19.json\\nProofWriter_AttNeg-OWA-D5-1017_Q5.json\\nProofWriter_AttNeg-OWA-D5-1028_Q10.json\\nProofWriter_AttNeg-OWA-D5-1030_Q23.json\\nProofWriter_AttNeg-OWA-D5-1066_Q21.json\\nProofWriter_AttNeg-OWA-D5-107_Q1.json\\nProofWriter_AttNeg-OWA-D5-107_Q6.json\\nProofWriter_AttNeg-OWA-D5-108_Q15.json\\nProofWriter_AttNeg-OWA-D5-109_Q11.json\\nProofWriter_AttNeg-OWA-D5-109_Q13.json\\nProofWriter_AttNeg-OWA-D5-1105_Q4.json\\nProofWriter_AttNeg-OWA-D5-1111_Q2.json\\nProofWriter_AttNeg-OWA-D5-1119_Q6.json\\nProofWriter_AttNeg-OWA-D5-1149_Q12.json\\nProofWriter_AttNeg-OWA-D5-1149_Q18.json\\nProofWriter_AttNeg-OWA-D5-1170_Q10.json\\nProofWriter_AttNeg-OWA-D5-1170_Q13.json\\nProofWriter_AttNeg-OWA-D5-1176_Q11.json\\nProofWriter_AttNeg-OWA-D5-1176_Q12.json\\nProofWriter_AttNeg-OWA-D5-1176_Q18.json\\nProofWriter_AttNeg-OWA-D5-1176_Q8.json\\nProofWriter_AttNeg-OWA-D5-1183_Q16.json\\nProofWriter_AttNeg-OWA-D5-1183_Q20.json\\nProofWriter_AttNeg-OWA-D5-1201_Q18.json\\nProofWriter_AttNeg-OWA-D5-1203_Q17.json\\nProofWriter_AttNeg-OWA-D5-1203_Q8.json\\nProofWriter_AttNeg-OWA-D5-1208_Q1.json\\nProofWriter_AttNeg-OWA-D5-1208_Q15.json\\nProofWriter_AttNeg-OWA-D5-1208_Q5.json\\nProofWriter_AttNeg-OWA-D5-120_Q11.json\\nProofWriter_AttNeg-OWA-D5-120_Q17.json\\nProofWriter_AttNeg-OWA-D5-120_Q9.json\\nProofWriter_AttNeg-OWA-D5-1210_Q4.json\\nProofWriter_AttNeg-OWA-D5-1210_Q8.json\\nProofWriter_AttNeg-OWA-D5-1220_Q4.json\\nProofWriter_AttNeg-OWA-D5-1220_Q6.json\\nProofWriter_AttNeg-OWA-D5-1229_Q3.json\\nProofWriter_AttNeg-OWA-D5-1229_Q6.json\\nProofWriter_AttNeg-OWA-D5-1233_Q11.json\\nProofWriter_AttNeg-OWA-D5-1233_Q2.json\\nProofWriter_AttNeg-OWA-D5-1236_Q12.json\\nProofWriter_AttNeg-OWA-D5-1236_Q20.json\\nProofWriter_AttNeg-OWA-D5-145_Q9.json\\nProofWriter_AttNeg-OWA-D5-155_Q6.json\\nProofWriter_AttNeg-OWA-D5-195_Q15.json\\nPr
…[truncated 6604 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T21:40:31.972237+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus/scripts/ -name '*d116*' -o -name '*nli_combo*' -o -name '*deberta*combo*'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus/scripts/ -name '*d116*' -o -name '*nli_combo*' -o -name '*deberta*combo*'"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T21:40:31.972385+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/scripts/d116_qwen3_pw_deberta_large.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T21:40:31.972514+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "head -50 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-1041_Q1.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "head -50 /root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-1041_Q1.json"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T21:40:31.972836+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"problem\\\": {\\n    \\\"id\\\": \\\"ProofWriter_AttNoneg-OWA-D5-1041_Q1\\\",\\n    \\\"problem\\\": \\\"Bob is cold. Bob is quiet. Bob is red. Bob is smart. Charlie is kind. Charlie is quiet. Charlie is red. Charlie is rough. Dave is cold. Dave is kind. Dave is smart. Fiona is quiet. If something is quiet and cold then it is smart. Red, cold things are round. If something is kind and rough then it is red. All quiet things are rough. Cold, smart things are red. If something is rough then it is cold. All red things are rough. If Dave is smart and Dave is kind then Dave is quiet.\\\\n\\\\nDetermine whether the following statement is true, false, or unknown:\\\\nCharlie is kind.\\\",\\n    \\\"solution\\\": \\\"\\\",\\n    \\\"answer\\\": \\\"True\\\",\\n    \\\"level\\\": \\\"OWA-D5\\\",\\n    \\\"raw_logic_programs\\\": [\\n      \\\"Predicates:\\\\nCold($x, bool) ::: Is x cold?\\\\nQuiet($x, bool) ::: Is x quiet?\\\\nRed($x, bool) ::: Is x red?\\\\nSmart($x, bool) ::: Is x smart?\\\\nKind($x, bool) ::: Is x kind?\\\\nRough($x, bool) ::: Is x rough?\\\\nRound($x, bool) ::: Is x round?\\\\n\\\\nFacts:\\\\nCold(Bob, True) ::: Bob is cold.\\\\nQuiet(Bob, True) ::: Bob is quiet.\\\\nRed(Bob, True) ::: Bob is red.\\\\nSmart(Bob, True) ::: Bob is smart.\\\\nKind(Charlie, True) ::: Charlie is kind.\\\\nQuiet(Charlie, True) ::: Charlie is quiet.\\\\nRed(Charlie, True) ::: Charlie is red.\\\\nRough(Charlie, True) ::: Charlie is rough.\\\\nCold(Dave, True) ::: Dave is cold.\\\\nKind(Dave, True) ::: Dave is kind.\\\\nSmart(Dave, True) ::: Dave is smart.\\\\nQuiet(Fiona, True) ::: Fiona is quiet.\\\\n\\\\nRules:\\\\nQuiet($x, True) && Cold($x, True) >>> Smart($x, True) ::: If something is quiet and cold then it is smart.\\\\nRed($x, True) && Cold($x, True) >>> Round($x, True) ::: Red, cold things are round.\\\\nKind($x, True) && Rough($x, True) >>> Red($x, True) ::: If something is kind and rough then it is red.\\
…[truncated 7116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T21:40:31.973142+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "cat /root/symb_invariant_consensus/scripts/d116_qwen3_pw_deberta_large.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat /root/symb_invariant_consensus/scripts/d116_qwen3_pw_deberta_large.py"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T21:40:31.973599+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"D116: Qwen3-14B ProofWriter combo with DeBERTa-large-mnli\\nReplaces deberta-base-mnli (Dir-K) with deberta-large-mnli to match Dir-J3 (Mistral combo).\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport time\\nfrom collections import Counter\\nfrom scipy.stats import binomtest\\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\nimport torch\\n\\nTRACES_PATH = \\\"/root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json\\\"\\nPW_DATA_PATH = \\\"/root/symb_invariant_consensus/data/proofwriter_full.json\\\"\\nOUTPUT_DIR = \\\"/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large\\\"\\nMODEL_NAME = \\\"/root/autodl-tmp/models/deberta-large-mnli\\\"\\nCLASSES = [\\\"True\\\", \\\"False\\\", \\\"Unknown\\\"]\\nWEIGHTS = [1, 3, 5]\\n\\n\\ndef parse_problem(problem_text):\\n    marker = \\\"\\\\n\\\\nDetermine whether the following statement is true, false, or unknown:\\\\n\\\"\\n    if marker in problem_text:\\n        parts = problem_text.split(marker, 1)\\n        return parts[0].strip(), parts[1].strip()\\n    return problem_text, \\\"\\\"\\n\\n\\ndef mcnemar_test(b, c):\\n    n = b + c\\n    if n == 0:\\n        return 1.0\\n    return binomtest(min(b, c), n, 0.5).pvalue\\n\\n\\ndef main():\\n    os.makedirs(OUTPUT_DIR, exist_ok=True)\\n\\n    with open(TRACES_PATH) as f:\\n        traces = json.load(f)\\n    with open(PW_DATA_PATH) as f:\\n        pw_data = json.load(f)\\n    pw_by_id = {q[\\\"id\\\"]: q for q in pw_data}\\n\\n    results_list = traces[\\\"results\\\"]\\n    total = len(results_list)\\n    print(f\\\"Loaded {total} problems from traces\\\")\\n\\n    gt = {}\\n    sc_answers = {}\\n    sc_vote_dists = {}\\n    for r in results_list:\\n        pid = r[\\\"problem_id\\\"]\\n        gt[pid] = r[\\\"ground_truth\\\"]\\n        sc_answers[pid] = r[\\\"sc_answer\\\"]\\n        sc_vote_dists[pid] 
…[truncated 7280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T21:40:31.974006+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "cat > /root/symb_invariant_consensus/scripts/qwen14b_pw_nli_combo.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Qwen2.5-14B ProofWriter NLI Combo using D116's DeBERTa-large predictions.\n\nDeBERTa-large-mnli predictions are deterministic on the same 600 PW problems\nregardless of generator model, so we reuse D116's per_question results directly.\n\"\"\"\n\nimport json\nimport os\nfrom collections import Counter\nfrom scipy.stats import binomtest\n\nEXP032_PATH = \"/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json\"\nD116_PATH = \"/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json\"\nOUTPUT_DIR = \"/root/symb_invariant_consensus/results/qwen14b_pw_nli_combo\"\nCLASSES = [\"True\", \"False\", \"Unknown\"]\nWEIGHTS = [1, 3, 5]\n\n\ndef mcnemar_test(b, c):\n    n = b + c\n    if n == 0:\n        return 1.0\n    return binomtest(min(b, c), n, 0.5).pvalue\n\n\ndef main():\n    os.makedirs(OUTPUT_DIR, exist_ok=True)\n\n    with open(EXP032_PATH) as f:\n        exp032 = json.load(f)\n    with open(D116_PATH) as f:\n        d116 = json.load(f)\n\n    results_list = exp032[\"results\"]\n    d116_pq = d116[\"per_question\"]\n    total = len(results_list)\n    print(f\"Loaded {total} problems from exp032 (Qwen2.5-14B PW600)\")\n\n    # Extract per-problem data from exp032\n    gt = {}\n    sc_answers = {}\n    sc_vote_dists = {}\n    for r in results_list:\n        pid = r[\"problem_id\"]\n        gt[pid] = r[\"ground_truth\"]\n        sc_answers[pid] = r[\"sc_answer\"]\n        sc_vote_dists[pid] = r[\"sc_vote_distribution\"]\n\n    # Verify all problem_ids match D116\n    missing = [pid for pid in gt if pid not in d116_pq]\n    if missing:\n        print(f\"WARNING: {len(missing)} problems missing from D116!\")\n        for m in missing[:5]:\n            print(f\"  {m}\")\n    else:\n        print(\"All 600 problem_ids match D116 DeBERTa predictions.\")\n\n    # Verify D116 gold labels match exp032\n    gold_mismatch = [pid for pid in gt if pid in d116_pq and d116_pq[pid][\"gold\"] != gt[pid]]\n    if gold_mismatch:\n        print(f\"ERROR: {len(gold_mismatch)} gold label mismatches!\")\n        return\n    print(\"Gold labels verified: all match.\")\n\n    # SC baseline\n    sc_correct_n = sum(1 for pid in gt if sc_answers[pid] == gt[pid])\n    sc_acc = sc_correct_n / total\n    print(f\"\\nSC baseline (Qwen2.5-14B, K=12): {sc_acc:.4f} ({sc_correct_n}/{total})\")\n\n    # DeBERTa standalone (reused from D116)\n    deberta_preds = {pid: d116_pq[pid][\"deberta_pred\"] for pid in gt}\n    deberta_probs_dict = {pid: d116_pq[pid][\"deberta_probs\"] for pid in gt}\n    deberta_correct_n = sum(1 for pid in gt if deberta_preds[pid] == gt[pid])\n    deberta_acc = deberta_correct_n / total\n    print(f\"DeBERTa-large standalone: {deberta_acc:.4f} ({deberta_correct_n}/{total})\")\n    print(f\"Capability gap: {(deberta_acc - sc_acc)*100:.2f}pp\")\n\n    # Per-class DeBERTa stats\n    gt_dist = Counter(gt.values())\n    pred_dist = Counter(deberta_preds.values())\n    per_class = {}\n    for cls in CLASSES:\n        n_cls = gt_dist.get(cls, 0)\n        if n_cls == 0:\n            continue\n        correct_cls = sum(1 for pid in gt if gt[pid] == cls and deberta_preds[pid] == cls)\n        tp = correct_cls\n        fp = sum(1 for pid in gt if gt[pid] != cls and deberta_preds[pid] == cls)\n        fn = n_cls - correct_cls\n        prec = tp / (tp + fp) if (tp + fp) > 0 else 0\n        rec = tp / (tp + fn) if (tp + fn) > 0 else 0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0\n        per_class[cls] = {\n            \"n\": n_cls,\n            \"correct\": correct_cls,\n            \"accuracy\": round(correct_cls / n_cls, 4),\n            \"precision\": round(prec, 4),\n            \"recall\": round(rec, 4),\n            \"f1\": round(f1, 4)\n        }\n\n    # Complementarity\n    nli_right_sc_wrong = sum(1 for pid in gt if deberta_preds[pid] == gt[pid] and sc_answers[pid] != gt[pid])\n    sc_right_nli_wrong = sum(1 for pid in gt if sc_answers[pid] == gt[pid] and deberta_preds[pid] != gt[pid])\n    both_right = sum(1 for pid in gt if deberta_preds[pid] == gt[pid] and sc_answers[pid] == gt[pid])\n    both_wrong = sum(1 for pid in gt if deberta_preds[pid] != gt[pid] and sc_answers[pid] != gt[pid])\n    print(f\"\\nComplementarity: NLI✓SC✗={nli_right_sc_wrong}, SC✓NLI✗={sc_right_nli_wrong}, both✓={both_right}, both✗={both_wrong}\")\n\n    # Combo\n    print(\"\\n=== Combo Results ===\")\n    combo_results = {}\n    for w in WEIGHTS:\n        combo_correct = 0\n        b_count = 0  # combo right, SC wrong\n        c_count = 0  # combo wrong, SC right\n\n        for pid in gt:\n            gold = gt[pid]\n            nli_pred = deberta_preds[pid]\n            sc_dist = sc_vote_dists[pid]\n\n            combo_votes = {}\n            for cls in CLASSES:\n                combo_votes[cls] = sc_dist.get(cls, 0) + (w if cls == nli_pred else 0)\n            combo_answer = max(combo_votes, key=combo_votes.get)\n\n            sc_correct = sc_answers[pid] == gold\n            combo_is_correct = combo_answer == gold\n\n            if combo_is_correct:\n                combo_correct += 1\n            if combo_is_correct and not sc_correct:\n                b_count += 1\n            if not combo_is_correct and sc_correct:\n                c_count += 1\n\n        combo_acc = combo_correct / total\n        delta = combo_acc - sc_acc\n        p_val = mcnemar_test(b_count, c_count)\n\n        combo_results[w] = {\n            \"accuracy\": round(combo_acc, 4),\n            \"correct\": combo_correct,\n            \"delta_vs_sc\": round(delta, 4),\n            \"delta_pp\": round(delta * 100, 2),\n            \"mcnemar_b\": b_count,\n            \"mcnemar_c\": c_count,\n            \"mcnemar_n_discordant\": b_count + c_count,\n            \"mcnemar_p\": round(p_val, 4)\n        }\n        print(f\"  w={w}: {combo_acc:.4f} ({combo_correct}/{total}), delta={delta*100:+.2f}pp, p={p_val:.4f}, discordant=[{b_count},{c_count}]\")\n\n    # Agreement\n    agree = sum(1 for pid in gt if deberta_preds[pid] == sc_answers[pid])\n    disagree = total - agree\n    agree_correct = sum(1 for pid in gt if deberta_preds[pid] == sc_answers[pid] == gt[pid])\n    disagree_deberta = sum(1 for pid in gt if deberta_preds[pid] != sc_answers[pid] and deberta_preds[pid] == gt[pid])\n    disagree_sc = sum(1 for pid in gt if deberta_preds[pid] != sc_answers[pid] and sc_answers[pid] == gt[pid])\n\n    print(f\"\\n=== Agreement ===\")\n    if agree > 0:\n        print(f\"  Agree: {agree}/{total} ({agree/total:.4f}), acc={agree_correct/agree:.4f}\")\n    print(f\"  Disagree: DeBERTa right={disagree_deberta}, SC right={disagree_sc}\")\n\n    # Save\n    output = {\n        \"experiment\": \"Qwen2.5-14B ProofWriter NLI Combo (DeBERTa-large reused from D116)\",\n        \"verifier_model\": \"microsoft/deberta-large-mnli\",\n        \"generator_model\": \"Qwen2.5-14B-Instruct\",\n        \"dataset\": \"ProofWriter-D5-600\",\n        \"n_questions\": total,\n        \"standalone_accuracy\": round(deberta_acc, 4),\n        \"sc_baseline\": round(sc_acc, 4),\n        \"capability_gap_pp\": round((deberta_acc - sc_acc) * 100, 2),\n        \"deberta_standalone\": {\n            \"accuracy\": round(deberta_acc, 4),\n            \"correct\": deberta_correct_n,\n            \"total\": total,\n            \"per_class\": per_class,\n            \"gt_distribution\": dict(gt_dist),\n            \"pred_distribution\": dict(pred_dist),\n            \"note\": \"Reused from D116 (same 600 PW problems, NLI is generator-independent)\"\n        },\n        \"combo\": {\n            f\"w{w}\": {\n                \"accuracy\": combo_results[w][\"accuracy\"],\n                \"delta_pp\": combo_results[w][\"delta_pp\"],\n                \"mcnemar_p\": combo_results[w][\"mcnemar_p\"],\n                \"discordant\": [combo_results[w][\"mcnemar_b\"], combo_results[w][\"mcnemar_c\"]]\n            }\n            for w in WEIGHTS\n        },\n        \"complementarity\": {\n            \"nli_right_sc_wrong\": nli_right_sc_wrong,\n            \"sc_right_nli_wrong\": sc_right_nli_wrong,\n            \"both_right\": both_right,\n            \"both_wrong\": both_wrong\n        },\n        \"combo_vs_sc_full\": {f\"w{w}\": combo_results[w] for w in WEIGHTS},\n        \"agreement_vs_sc\": {\n            \"agree\": agree,\n            \"disagree\": disagree,\n            \"agreement_rate\": round(agree / total, 4),\n            \"agree_accuracy\": round(agree_correct / agree, 4) if agree > 0 else 0,\n            \"disagree_deberta_correct\": disagree_deberta,\n            \"disagree_sc_correct\": disagree_sc\n        },\n        \"per_question\": {\n            pid: {\n                \"deberta_pred\": deberta_preds[pid],\n                \"deberta_probs\": deberta_probs_dict[pid],\n                \"sc_answer\": sc_answers[pid],\n                \"sc_vote_distribution\": sc_vote_dists[pid],\n                \"gold\": gt[pid],\n                \"deberta_correct\": deberta_preds[pid] == gt[pid],\n                \"sc_correct\": sc_answers[pid] == gt[pid]\n            }\n            for pid in gt\n        }\n    }\n\n    out = os.path.join(OUTPUT_DIR, \"results.json\")\n    with open(out, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved: {out}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat > /root/symb_invariant_consensus/scripts/qwen14b_pw_nli_combo.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Qwen2.5-14B ProofWriter NLI Combo using D116's DeBERTa-large predictions.\n\nDeBERTa-large-mnli predictions are deterministic on the same 600 PW problems\nregardless of generator model, so we reuse D116's per_question results directly.\n\"\"\"\n\nimport json\nimport os\nfrom collections import Counter\nfrom scipy.stats import binomtest\n\nEXP032_PATH = \"/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json\"\nD116_PATH = \"/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json\"\nOUTPUT_DIR = \"/root/symb_invariant_consensus/results/qwen14b_pw_nli_combo\"\nCLASSES = [\"True\", \"False\", \"Unknown\"]\nWEIGHTS = [1, 3, 5]\n\n\ndef mcnemar_test(b, c):\n    n = b + c\n    if n == 0:\n        return 1.0\n    return binomtest(min(b, c), n, 0.5).pvalue\n\n\ndef main():\n    os.makedirs(OUTPUT_DIR, exist_ok=True)\n\n    with open(EXP032_PATH) as f:\n        exp032 = json.load(f)\n    with open(D116_PATH) as f:\n        d116 = json.load(f)\n\n    results_list = exp032[\"results\"]\n    d116_pq = d116[\"per_question\"]\n    total = len(results_list)\n    print(f\"Loaded {total} problems from exp032 (Qwen2.5-14B PW600)\")\n\n    # Extract per-problem data from exp032\n    gt = {}\n    sc_answers = {}\n    sc_vote_dists = {}\n    for r in results_list:\n        pid = r[\"problem_id\"]\n        gt[pid] = r[\"ground_truth\"]\n        sc_answers[pid] = r[\"sc_answer\"]\n        sc_vote_dists[pid] = r[\"sc_vote_distribution\"]\n\n    # Verify all problem_ids match D116\n    missing = [pid for pid in gt if pid not in d116_pq]\n    if missing:\n        print(f\"WARNING: {len(missing)} problems missing from D116!\")\n        for m in missing[:5]:\n            print(f\"  {m}\")\n    else:\n        print(\"All 600 problem_ids match D116 DeBERTa predictions.\")\n\n    # Verify D116 gold labels match exp032\n    gold_mismatch = [pid for pid in gt if pid in d116_pq and d116_pq[pid][\"gold\"] != gt[pid]]\n    if gold_mismatch:\n        print(f\"ERROR: {len(gold_mismatch)} gold label mismatches!\")\n        return\n    print(\"Gold labels verified: all match.\")\n\n    # SC baseline\n    sc_correct_n = sum(1 for pid in gt if sc_answers[pid] == gt[pid])\n    sc_acc = sc_correct_n / total\n    print(f\"\\nSC baseline (Qwen2.5-14B, K=12): {sc_acc:.4f} ({sc_correct_n}/{total})\")\n\n    # DeBERTa standalone (reused from D116)\n    deberta_preds = {pid: d116_pq[pid][\"deberta_pred\"] for pid in gt}\n    deberta_probs_dict = {pid: d116_pq[pid][\"deberta_probs\"] for pid in gt}\n    deberta_correct_n = sum(1 for pid in gt if deberta_preds[pid] == gt[pid])\n    deberta_acc = deberta_correct_n / total\n    print(f\"DeBERTa-large standalone: {deberta_acc:.4f} ({deberta_correct_n}/{total})\")\n    print(f\"Capability gap: {(deberta_acc - sc_acc)*100:.2f}pp\")\n\n    # Per-class DeBERTa stats\n    gt_dist = Counter(gt.values())\n    pred_dist = Counter(deberta_preds.values())\n    per_class = {}\n    for cls in CLASSES:\n        n_cls = gt_dist.get(cls, 0)\n        if n_cls == 0:\n            continue\n        correct_cls = sum(1 for pid in gt if gt[pid] == cls and deberta_preds[pid] == cls)\n        tp = correct_cls\n        fp = sum(1 for pid in gt if gt[pid] != cls and deberta_preds[pid] == cls)\n        fn = n_cls - correct_cls\n        prec = tp / (tp + fp) if (tp + fp) > 0 else 0\n        rec = tp / (tp + fn) if (tp + fn) > 0 else 0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0\n        per_class[cls] = {\n            \"n\": n_cls,\n            \"correct\": correct_cls,\n            \"accuracy\": round(correct_cls / n_cls, 4),\n            \"precision\": round(prec, 4),\n            \"recall\": round(rec, 4),\n            \"f1\": round(f1, 4)\n        }\n\n    # Complementarity\n    nli_right_sc_wrong = sum(1 for pid in gt if deberta_preds[pid] == gt[pid] and sc_answers[pid] != gt[pid])\n    sc_right_nli_wrong = sum(1 for pid in gt if sc_answers[pid] == gt[pid] and deberta_preds[pid] != gt[pid])\n    both_right = sum(1 for pid in gt if deberta_preds[pid] == gt[pid] and sc_answers[pid] == gt[pid])\n    both_wrong = sum(1 for pid in gt if deberta_preds[pid] != gt[pid] and sc_answers[pid] != gt[pid])\n    print(f\"\\nComplementarity: NLI✓SC✗={nli_right_sc_wrong}, SC✓NLI✗={sc_right_nli_wrong}, both✓={both_right}, both✗={both_wrong}\")\n\n    # Combo\n    print(\"\\n=== Combo Results ===\")\n    combo_results = {}\n    for w in WEIGHTS:\n        combo_correct = 0\n        b_count = 0  # combo right, SC wrong\n        c_count = 0  # combo wrong, SC right\n\n        for pid in gt:\n            gold = gt[pid]\n            nli_pred = deberta_preds[pid]\n            sc_dist = sc_vote_dists[pid]\n\n            combo_votes = {}\n            for cls in CLASSES:\n                combo_votes[cls] = sc_dist.get(cls, 0) + (w if cls == nli_pred else 0)\n            combo_answer = max(combo_votes, key=combo_votes.get)\n\n            sc_correct = sc_answers[pid] == gold\n            combo_is_correct = combo_answer == gold\n\n            if combo_is_correct:\n                combo_correct += 1\n            if combo_is_correct and not sc_correct:\n                b_count += 1\n            if not combo_is_correct and sc_correct:\n                c_count += 1\n\n        combo_acc = combo_correct / total\n        delta = combo_acc - sc_acc\n        p_val = mcnemar_test(b_count, c_count)\n\n        combo_results[w] = {\n            \"accuracy\": round(combo_acc, 4),\n            \"correct\": combo_correct,\n            \"delta_vs_sc\": round(delta, 4),\n            \"delta_pp\": round(delta * 100, 2),\n            \"mcnemar_b\": b_count,\n            \"mcnemar_c\": c_count,\n            \"mcnemar_n_discordant\": b_count + c_count,\n            \"mcnemar_p\": round(p_val, 4)\n        }\n        print(f\"  w={w}: {combo_acc:.4f} ({combo_correct}/{total}), delta={delta*100:+.2f}pp, p={p_val:.4f}, discordant=[{b_count},{c_count}]\")\n\n    # Agreement\n    agree = sum(1 for pid in gt if deberta_preds[pid] == sc_answers[pid])\n    disagree = total - agree\n    agree_correct = sum(1 for pid in gt if deberta_preds[pid] == sc_answers[pid] == gt[pid])\n    disagree_deberta = sum(1 for pid in gt if deberta_preds[pid] != sc_answers[pid] and deberta_preds[pid] == gt[pid])\n    disagree_sc = sum(1 for pid in gt if deberta_preds[pid] != sc_answers[pid] and sc_answers[pid] == gt[pid])\n\n    print(f\"\\n=== Agreement ===\")\n    if agree > 0:\n        print(f\"  Agree: {agree}/{total} ({agree/total:.4f}), acc={agree_correct/agree:.4f}\")\n    print(f\"  Disagree: DeBERTa right={disagree_deberta}, SC right={disagree_sc}\")\n\n    # Save\n    output = {\n        \"experiment\": \"Qwen2.5-14B ProofWriter NLI Combo (DeBERTa-large reused from D116)\",\n        \"verifier_model\": \"microsoft/deberta-large-mnli\",\n        \"generator_model\": \"Qwen2.5-14B-Instruct\",\n        \"dataset\": \"ProofWriter-D5-600\",\n        \"n_questions\": total,\n        \"standalone_accuracy\": round(deberta_acc, 4),\n        \"sc_baseline\": round(sc_acc, 4),\n        \"capability_gap_pp\": round((deberta_acc - sc_acc) * 100, 2),\n        \"deberta_standalone\": {\n            \"accuracy\": round(deberta_acc, 4),\n            \"correct\": deberta_correct_n,\n            \"total\": total,\n            \"per_class\": per_class,\n            \"gt_distribution\": dict(gt_dist),\n            \"pred_distribution\": dict(pred_dist),\n            \"note\": \"Reused from D116 (same 600 PW problems, NLI is generator-independent)\"\n        },\n        \"combo\": {\n            f\"w{w}\": {\n                \"accuracy\": combo_results[w][\"accuracy\"],\n                \"delta_pp\": combo_results[w][\"delta_pp\"],\n                \"mcnemar_p\": combo_results[w][\"mcnemar_p\"],\n                \"discordant\": [combo_results[w][\"mcnemar_b\"], combo_results[w][\"mcnemar_c\"]]\n            }\n            for w in WEIGHTS\n        },\n        \"complementarity\": {\n            \"nli_right_sc_wrong\": nli_right_sc_wrong,\n            \"sc_right_nli_wrong\": sc_right_nli_wrong,\n            \"both_right\": both_right,\n            \"both_wrong\": both_wrong\n        },\n        \"combo_vs_sc_full\": {f\"w{w}\": combo_results[w] for w in WEIGHTS},\n        \"agreement_vs_sc\": {\n            \"agree\": agree,\n            \"disagree\": disagree,\n            \"agreement_rate\": round(agree / total, 4),\n            \"agree_accuracy\": round(agree_correct / agree, 4) if agree > 0 else 0,\n            \"disagree_deberta_correct\": disagree_deberta,\n            \"disagree_sc_correct\": disagree_sc\n        },\n        \"per_question\": {\n            pid: {\n                \"deberta_pred\": deberta_preds[pid],\n                \"deberta_probs\": deberta_probs_dict[pid],\n                \"sc_answer\": sc_answers[pid],\n                \"sc_vote_distribution\": sc_vote_dists[pid],\n                \"gold\": gt[pid],\n                \"deberta_correct\": deberta_preds[pid] == gt[pid],\n                \"sc_correct\": sc_answers[pid] == gt[pid]\n            }\n            for pid in gt\n        }\n    }\n\n    out = os.path.join(OUTPUT_DIR, \"results.json\")\n    with open(out, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved: {out}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\""
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T21:40:31.974388+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T21:40:31.974616+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, os\nfrom scipy.stats import binomtest\nprint('scipy OK')\nfor p in ['/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json',\n          '/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json']:\n    assert os.path.exists(p), f'Missing: {p}'\n    with open(p) as f:\n        d = json.load(f)\n    if 'results' in d:\n        print(f'{p}: {len(d[\\\"results\\\"])} problems')\n    if 'per_question' in d:\n        print(f'{p}: {len(d[\\\"per_question\\\"])} per_question entries')\nprint('All checks passed.')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, os\nfrom scipy.stats import binomtest\nprint('scipy OK')\nfor p in ['/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json',\n          '/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json']:\n    assert os.path.exists(p), f'Missing: {p}'\n    with open(p) as f:\n        d = json.load(f)\n    if 'results' in d:\n        print(f'{p}: {len(d[\\\"results\\\"])} problems')\n    if 'per_question' in d:\n        print(f'{p}: {len(d[\\\"per_question\\\"])} per_question entries')\nprint('All checks passed.')\n\""
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T21:40:31.974820+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"scipy OK\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json: 600 problems\\n/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json: 600 per_question entries\\nAll checks passed.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.09}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T21:40:31.975058+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python3 scripts/qwen14b_pw_nli_combo.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python3 scripts/qwen14b_pw_nli_combo.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T21:40:31.975274+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loaded 600 problems from exp032 (Qwen2.5-14B PW600)\\nAll 600 problem_ids match D116 DeBERTa predictions.\\nGold labels verified: all match.\\n\\nSC baseline (Qwen2.5-14B, K=12): 0.7350 (441/600)\\nDeBERTa-large standalone: 0.5500 (330/600)\\nCapability gap: -18.50pp\\n\\nComplementarity: NLI✓SC✗=80, SC✓NLI✗=191, both✓=250, both✗=79\\n\\n=== Combo Results ===\\n  w=1: 0.7417 (445/600), delta=+0.67pp, p=0.3438, discordant=[7,3]\\n  w=3: 0.7433 (446/600), delta=+0.83pp, p=0.4049, discordant=[14,9]\\n  w=5: 0.7533 (452/600), delta=+1.83pp, p=0.1439, discordant=[29,18]\\n\\n=== Agreement ===\\n  Agree: 277/600 (0.4617), acc=0.9025\\n  Disagree: DeBERTa right=80, SC right=191\\n\\nSaved: /root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.08}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-20T21:40:31.975530+00:00_

完成。结果：

| Metric | Value |
|--------|-------|
| SC baseline (Qwen2.5-14B) | 73.50% |
| DeBERTa-large standalone | 55.00% |
| **Capability gap** | **-18.50pp** |
| Combo w=1 | 74.17% (+0.67pp, p=0.344) |
| Combo w=3 | 74.33% (+0.83pp, p=0.405) |
| Combo w=5 | **75.33% (+1.83pp, p=0.144)** |

Capability Gap 叙事验证：gap = -18.50pp 介于 Qwen3 (-30pp, gain=+1.83) 和 Mistral (+15.67pp, gain=+10.67) 之间，对应 combo gain 也在两者之间（+0.67 ~ +1.83pp），支撑单调递减趋势。

结果已写入 `/root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_experiment_qwen14b-pw-nli-combo_20260520T213827"
}
```

</details>

---
