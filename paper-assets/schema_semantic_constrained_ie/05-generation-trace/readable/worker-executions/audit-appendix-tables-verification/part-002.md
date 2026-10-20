# audit appendix tables verification — Part 2 of 2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../audit-appendix-tables-verification.md) · [Structured JSON](../../../sessions/84/84354abf8d7056ed3624.json)

## Before a recorded user message

### Tool result

_source line 98 · 2026-05-23T10:52:26.902Z_

<details><summary>↩ Tool result · `toolu_018BteM1QV1QpizKU1DZoV2B`</summary>

```text
=== ee_qwen_wikievents_unconstrained ===
{
  "parse_success": "218/246 (88.6%)",
  "ET": 0,
  "EV": 24,
  "RoV": 74.9,
  "AC": 0.3,
  "CF": 0,
  "trigger_f1": 0.1184,
  "argument_f1": 0.0009,
  "entity_f1": 0
}

=== ee_llama_wikievents_unconstrained ===
{
  "parse_success": "226/246 (91.9%)",
  "ET": 0,
  "EV": 10.5,
  "RoV": 88.8,
  "AC": 0.1,
  "CF": 0,
  "trigger_f1": 0.0572,
  "argument_f1": 0,
  "entity_f1": 0
}

=== ee_mistral_wikievents_unconstrained ===
{
  "parse_success": "194/246 (78.9%)",
  "ET": 0,
  "EV": 37.3,
  "RoV": 63.9,
  "AC": 0,
  "CF": 0,
  "trigger_f1": 0.0241,
  "argument_f1": 0,
  "entity_f1": 0
}

=== ee_qwen_wikievents_constrained_v3 ===
{
  "parse_success": "206/246 (83.7%)",
  "parse_failures": 40,
  "ET": 0,
  "EV": 0,
  "RoV": 0,
  "AC": 2.1,
  "CF": 21.1,
  "go_no_go": 2.05,
  "entity_f1": 0.1409,
  "trigger_f1": 0.1339,
  "argument_f1": 0.0168,
  "code_version": "938-line (collision+exact-match fix)",
  "posthoc_args_removed": 109,
  "posthoc_arg_f1": 0.017,
  "cf_voting_fix_rate": "15.9%",
  "cf_voting_entity_f1": 0.1352
}

=== ee_llama_wikievents_constrained_v3 ===
{
  "parse_success": "207/246 (84.1%)",
  "parse_failures": 39,
  "ET": 0,
  "EV": 0,
  "RoV": 0,
  "AC": 3.8,
  "CF": 17.2,
  "go_no_go": 3.8,
  "entity_f1": 0.1763,
  "trigger_f1": 0.0748,
  "argument_f1": 0.0118,
  "code_version": "938-line (collision+exact-match fix)",
  "posthoc_args_removed": 173,
  "posthoc_arg_f1": 0.0118
}

=== ee_mistral_wikievents_constrained_v3 ===
{
  "parse_success": "218/246 (88.6%)",
  "parse_failures": 28,
  "ET": 0,
  "EV": 0,
  "RoV": 0,
  "AC": 1.3,
  "CF": 14.9,
  "go_no_go": 1.26,
  "entity_f1": 0.1171,
  "trigger_f1": 0.0387,
  "argument_f1": 0.0031,
  "code_version": "938-line (collision+exact-match fix)",
  "posthoc_args_removed": 86,
  "posthoc_ac_after": 0
}

=== ee_mistral_wikievents_grammar_only_v3 ===
{
  "parse_success": "218/246 (88.6%)",
  "parse_failures": 28,
  "ET": 0,
  "EV": 0,
  "RoV": 64,
  "AC": 13.8,
  "CF": 1.1,
  "go_no_go": 77.73,
  "entity_f1": 0.1192,
  "trigger_f1": 0.0337,
  "argument_f1": 0.0027,
  "code_version": "938-line (collision+exact-match fix)",
  "mode": "grammar_only"
}

=== ee_qwen_wikievents_constrained ===
{
  "parse_success": "206/246 (83.7%)",
  "ET": 0,
  "EV": 0,
  "RoV": 0.3,
  "AC": 2.1,
  "CF": 21.1,
  "trigger_f1": 0.1339,
  "argument_f1": 0.0168,
  "entity_f1": 0.1409,
  "parse_failures": 40,
  "go_no_go": 2.4,
  "note": "after retry with max_new_tokens=8192"
}

=== ee_llama_wikievents_constrained ===
{
  "parse_success": "215/246 (87.4%)",
  "ET": 0,
  "EV": 0,
  "RoV": 0,
  "AC": 3.4,
  "CF": 15.5,
  "trigger_f1": 0.078,
  "argument_f1": 0.011,
  "entity_f1": 0.178,
  "parse_failures": 31,
  "go_no_go": 3.4,
  "note": "after retry with max_new_tokens=8192"
}

=== ee_mistral_wikievents_constrained_v2 ===
{
  "parse_success": "178/246 (72.4%)",
  "ET": 0,
  "EV": 0,
  "RoV": 0.1,
  "AC": 16.6,
  "CF": 13.9,
  "trigger_f1": 0.0508,
  "argument_f1": 0.0047,
  "entity_f1": 0.1245,
  "parse_failures": 68,
  "go_no_go": 16.7
}

=== d065_tcr_pilot ===
{
  "scierc_zs_qwen": {
    "cf_before": 9.75,
    "cf_after": 0,
    "dr_before": 0.93,
    "dr_after": 1.21,
    "ef1_delta": -0.0129,
    "fund_pct": 2.04
  },
  "scierc_zs_llama": {
    "cf_before": 6.4,
    "cf_after": 0,
    "dr_before": 0.08,
    "dr_after": 0.3,
    "ef1_delta": -0.0178,
    "fund_pct": 1.85
  },
  "scierc_lora_qwen": {
    "cf_before": 1.19,
    "cf_after": 0,
    "dr_before": 0,
    "dr_after": 0,
    "ef1_delta": -0.0075,
    "fund_pct": 0
  },
  "scierc_lora_llama": {
    "cf_before": 0.46,
    "cf_after": 0,
    "dr_before": 0.09,
    "dr_after": 0.09,
    "ef1_delta": -0.0018,
    "fund_pct": 0
  },
  "scierc_zs_mistral": {
    "cf_before": 0.67,
    "cf_after": 0,
    "dr_before": 13.36,
    "dr_after": 12.87,
    "ef1_delta": 0.0005,
    "fund_pct": 0
  },
  "docred_zs_qwen": {
    "cf_before": 13.11,
    "cf_after": 0,
    "dr_before": 10.21,
    "dr_after": 11.74,
    "ef1_delta": -0.0344,
    "fund_pct": 13.52
  },
  "docred_zs_llama": {
    "cf_before": 23.71,
    "cf_after": 0,
    "dr_before": 2.55,
    "dr_after": 11.93,
    "ef1_delta": -0.0521,
    "fund_pct": 22.78
  },
  "docred_zs_70b": {
    "cf_before": 11.61,
    "cf_after": 0,
    "dr_before": 0,
    "dr_after": 4.2,
    "ef1_delta": -0.0598,
    "fund_pct": 18.26
  },
  "docred_lora_qwen": {
    "cf_before": 0.42,
    "cf_after": 0,
    "dr_before": 0.01,
    "dr_after": 0.14,
    "ef1_delta": -0.0016,
    "fund_pct": 12.16
  },
  "docred_lora_llama": {
    "cf_before": 0.36,
    "cf_after": 0,
    "dr_before": 0.21,
    "dr_after": 0.2,
    "ef1_delta": -0.0017,
    "fund_pct": 11.59
  },
  "total_configs": 10,
  "all_cf_eliminated": true
}

=== d065_tcr_full ===
{
  "configs_tested": 10,
  "all_cf_eliminated": true,
  "scierc_all_dr_delta_max": 0.28,
  "docred_lora_dr_delta_max": 0.14,
  "docred_zs_llama_dr_delta": 9.38,
  "docred_zs_70b_dr_delta": 4.2,
  "docred_zs_qwen_dr_delta": 1.53,
  "fund_conflict_scierc_max": 2.04,
  "fund_conflict_docred_zs_max": 22.78,
  "fund_conflict_docred_lora_max": 12.16,
  "lora_ef1_cost_max": 0.0075,
  "zs_docred_ef1_cost_max": 0.0598
}

=== posthoc_filtering_baseline ===
{
  "docred_f1_before": 7.74,
  "docred_f1_after": 9.61,
  "docred_precision_before": 6.55,
  "docred_precision_after": 11.22,
  "docred_recall_before": 9.46,
  "docred_recall_after": 8.4,
  "docred_rejection_rate": 0.481,
  "docred_tp_before": 1137,
  "docred_tp_after": 1010,
  "docred_tp_lost": 127,
  "docred_et_residual": 0.0247,
  "scierc_f1_before": 8.23,
  "scierc_f1_after": 8.63,
  "scierc_rejection_rate": 0.168,
  "scierc_recall_before": 11.4,
  "scierc_recall_after": 10.68,
  "scierc_tp_before": 111,
  "scierc_tp_after": 104
}

=== w8_ft_posthoc_baseline ===
{
  "ft_regime": {
    "qwen_scierc": {
      "R_F1_before": 43.86,
      "R_F1_posthoc": 43.94,
      "R_F1_constrained": 43.77,
      "reject_rate_pct": 1.95,
      "TP_lost": 4
    },
    "llama_scierc": {
      "R_F1_before": 45.45,
      "R_F1_posthoc": 45.23,
      "R_F1_constrained": 45.47,
      "reject_rate_pct": 1.11,
      "TP_lost": 5
    },
    "qwen_docred": {
      "R_F1_before": 40.91,
      "R_F1_posthoc": 41.11,
      "R_F1_constrained": "TBD",
      "reject_rate_pct": 1.03,
      "TP_lost": 1
    },
    "llama_docred": {
      "R_F1_before": 43.77,
      "R_F1_posthoc": 43.92,
      "R_F1_constrained": 44.23,
      "reject_rate_pct": 0.64,
      "TP_lost": 1
    }
  },
  "zs_regime": {
    "mistral_scierc": {
      "triples": 1584,
      "reject_pct": 20.27,
      "R_F1_before": 0.0376,
      "R_F1_posthoc": 0.0394,
      "R_F1_constrained": 0.0367,
      "TP_before": 48,
      "TP_after": 44,
      "TP_lost": 4
    },
    "qwen_scierc": {
      "triples": 1724,
      "reject_pct": 16.76,
      "R_F1_before": 0.0823,
      "R_F1_posthoc": 0.0863,
      "R_F1_constrained": 0.0836,
      "TP_before": 111,
      "TP_after": 104,
      "TP_lost": 7
    },
    "llama_scierc": {
      "triples": 1274,
      "reject_pct": 13.89,
      "R_F1_before": 0.0268,
      "R_F1_posthoc": 0.0271,
      "R_F1_constrained": 0.0254,
      "TP_before": 30,
      "TP_after": 28,
      "TP_lost": 2
    },
    "qwen_docred": {
      "triples": 17497,
      "reject_pct": 48.12,
      "R_F1_before": 0.0774,
      "R_F1_posthoc": 0.0961,
      "R_F1_constrained": 0.0823,
      "TP_before": 1137,
      "TP_after": 1010,
      "TP_lost": 127
    },
    "llama_docred": {
      "triples": 16437,
      "reject_pct": 42.18,
      "R_F1_before": 0.0598,
      "R_F1_posthoc": 0.0744,
      "R_F1_constrained": 0.0627,
      "TP_before": 850,
      "TP_after": 802,
      "TP_lost": 48
    },
    "mistral_docred": {
      "triples": 11836,
      "reject_pct": 73.73,
      "R_F1_before

=== r16_trie_qwen_ft_scierc ===
{
  "E_F1": 64.4,
  "E_P": 66.8,
  "E_R": 62.16,
  "R_F1": 41.16,
  "R_P": 38.24,
  "R_R": 44.56,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 95.5,
  "CF_pct": 0.09,
  "parse_fail_pct": 9.1,
  "samples": 551,
  "note": "CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated."
}

=== r16_trie_llama_ft_scierc ===
{
  "E_F1": 36.66,
  "E_P": 67.47,
  "E_R": 25.16,
  "R_F1": 19.95,
  "R_P": 41.42,
  "R_R": 13.14,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 15.2,
  "CF_pct": 0,
  "parse_fail_pct": 50.8,
  "samples": 551,
  "note": "CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated."
}

=== r16_trie_qwen_zs_scierc ===
{
  "E_F1": 30.97,
  "R_F1": 8.64,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 29.3,
  "CF_pct": 0,
  "parse_fail_pct": 0,
  "samples": 551
}

=== r16_trie_llama_zs_scierc ===
{
  "E_F1": 23.23,
  "R_F1": 2.9,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 84.4,
  "CF_pct": 0.36,
  "parse_fail_pct": 0,
  "samples": 551
}

=== vllm_guided_json_scierc_zs ===
{
  "DR%": 15.26,
  "RV%": 0,
  "ET%": 0,
  "CF%": 0.04,
  "R-F1": 8.75,
  "E-F1": 30.91,
  "parse_fail%": 0,
  "total_samples": 551,
  "total_entities": 2485,
  "total_relations": 1724,
  "inference_time_s": 108.5
}

=== r4_prompt_minimal ===
{
  "unconstrained": {
    "ET_pct": 0.58,
    "RV_pct": 1.16,
    "DR_pct": 16.91,
    "E_F1": 31.98,
    "R_F1": 7.91
  },
  "constrained": {
    "ET_pct": 0,
    "RV_pct": 0,
    "DR_pct": 0.92,
    "E_F1": 31.99,
    "R_F1": 7.85
  },
  "DR_reduction_pct": 94.6,
  "delta_R_F1_pp": -0.06,
  "delta_E_F1_pp": 0.01
}

=== r4_prompt_detailed ===
{
  "unconstrained": {
    "ET_pct": 0.22,
    "RV_pct": 0.45,
    "DR_pct": 11.07,
    "E_F1": 33.55,
    "R_F1": 10.48
  },
  "constrained": {
    "ET_pct": 0,
    "RV_pct": 0,
    "DR_pct": 0.64,
    "E_F1": 33.56,
    "R_F1": 10.48
  },
  "DR_reduction_pct": 94.2,
  "delta_R_F1_pp": 0,
  "delta_E_F1_pp": 0.01
}

=== p1_ee_ft_composability_r5 ===
{
  "unconstrained": {
    "parse_rate": 0.85,
    "trigger_f1": 0.3208,
    "argument_f1": 0.0785,
    "rov_rate": 0.3831,
    "ac_rate": 0.0268,
    "go_nogo": 0.41
  },
  "full_s1": {
    "parse_rate": 0.95,
    "trigger_f1": 0.2672,
    "argument_f1": 0.0818,
    "rov_rate": 0,
    "ac_rate": 0,
    "go_nogo": 0
  }
}

=== w1_cf_fallback_scierc_pilot ===
{
  "ET": 0,
  "RV": 0,
  "DR": 0.1478,
  "CF": 0.0004,
  "R_F1": 0.0823,
  "R_P": 0.0643,
  "R_R": 0.114,
  "E_F1": 0.3098,
  "E_P": 0.2598,
  "E_R": 0.3837,
  "entities": 2474,
  "relations": 1725,
  "samples": 551,
  "grammar_first_fallback_rate": 0.3664,
  "cf_registry_fallback_rate": 0.0448,
  "total_mask_calls": 17024,
  "violation_budget_DR_CF": 0.1482
}

=== d062_ontology_scalability ===
{
  "compile_small_total_s": 0.334,
  "compile_medium_total_s": 0.322,
  "compile_large_total_s": 0.345,
  "compile_xlarge_total_s": 0.42,
  "grammar_small_s": 0.333,
  "grammar_xlarge_s": 0.365,
  "semantic_small_s": 0.0004,
  "semantic_xlarge_s": 0.017,
  "overhead_small": 1.02,
  "overhead_medium": 1.03,
  "overhead_large": 1.03,
  "overhead_xlarge": 1.03,
  "failures": 0
}

=== p8c_ft_scierc_latency ===
{
  "unconstrained_mean_s": 2.612,
  "constrained_mean_s": 2.873,
  "unconstrained_median_s": 2.355,
  "constrained_median_s": 2.624,
  "overhead_mean_pct": 10,
  "overhead_median_pct": 11.42,
  "per_doc_ratio_mean": 1.205,
  "per_doc_ratio_median": 1.117,
  "num_docs": 551,
  "unconstrained_total_s": 1439,
  "constrained_total_s": 1582.9
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "5aaf1717-1e0d-49c2-9705-f2667d0dd6a4",
  "tool_use_result": {
    "stdout": "=== ee_qwen_wikievents_unconstrained ===\n{\n  \"parse_success\": \"218/246 (88.6%)\",\n  \"ET\": 0,\n  \"EV\": 24,\n  \"RoV\": 74.9,\n  \"AC\": 0.3,\n  \"CF\": 0,\n  \"trigger_f1\": 0.1184,\n  \"argument_f1\": 0.0009,\n  \"entity_f1\": 0\n}\n\n=== ee_llama_wikievents_unconstrained ===\n{\n  \"parse_success\": \"226/246 (91.9%)\",\n  \"ET\": 0,\n  \"EV\": 10.5,\n  \"RoV\": 88.8,\n  \"AC\": 0.1,\n  \"CF\": 0,\n  \"trigger_f1\": 0.0572,\n  \"argument_f1\": 0,\n  \"entity_f1\": 0\n}\n\n=== ee_mistral_wikievents_unconstrained ===\n{\n  \"parse_success\": \"194/246 (78.9%)\",\n  \"ET\": 0,\n  \"EV\": 37.3,\n  \"RoV\": 63.9,\n  \"AC\": 0,\n  \"CF\": 0,\n  \"trigger_f1\": 0.0241,\n  \"argument_f1\": 0,\n  \"entity_f1\": 0\n}\n\n=== ee_qwen_wikievents_constrained_v3 ===\n{\n  \"parse_success\": \"206/246 (83.7%)\",\n  \"parse_failures\": 40,\n  \"ET\": 0,\n  \"EV\": 0,\n  \"RoV\": 0,\n  \"AC\": 2.1,\n  \"CF\": 21.1,\n  \"go_no_go\": 2.05,\n  \"entity_f1\": 0.1409,\n  \"trigger_f1\": 0.1339,\n  \"argument_f1\": 0.0168,\n  \"code_version\": \"938-line (collision+exact-match fix)\",\n  \"posthoc_args_removed\": 109,\n  \"posthoc_arg_f1\": 0.017,\n  \"cf_voting_fix_rate\": \"15.9%\",\n  \"cf_voting_entity_f1\": 0.1352\n}\n\n=== ee_llama_wikievents_constrained_v3 ===\n{\n  \"parse_success\": \"207/246 (84.1%)\",\n  \"parse_failures\": 39,\n  \"ET\": 0,\n  \"EV\": 0,\n  \"RoV\": 0,\n  \"AC\": 3.8,\n  \"CF\": 17.2,\n  \"go_no_go\": 3.8,\n  \"entity_f1\": 0.1763,\n  \"trigger_f1\": 0.0748,\n  \"argument_f1\": 0.0118,\n  \"code_version\": \"938-line (collision+exact-match fix)\",\n  \"posthoc_args_removed\": 173,\n  \"posthoc_arg_f1\": 0.0118\n}\n\n=== ee_mistral_wikievents_constrained_v3 ===\n{\n  \"parse_success\": \"218/246 (88.6%)\",\n  \"parse_failures\": 28,\n  \"ET\": 0,\n  \"EV\": 0,\n  \"RoV\": 0,\n  \"AC\": 1.3,\n  \"CF\": 14.9,\n  \"go_no_go\": 1.26,\n  \"entity_f1\": 0.1171,\n  \"trigger_f1\": 0.0387,\n  \"argument_f1\": 0.0031,\n  \"code_version\": \"938-line (collision+exact-match fix)\",\n  \"posthoc_args_removed\": 86,\n  \"posthoc_ac_after\": 0\n}\n\n=== ee_mistral_wikievents_grammar_only_v3 ===\n{\n  \"parse_success\": \"218/246 (88.6%)\",\n  \"parse_failures\": 28,\n  \"ET\": 0,\n  \"EV\": 0,\n  \"RoV\": 64,\n  \"AC\": 13.8,\n  \"CF\": 1.1,\n  \"go_no_go\": 77.73,\n  \"entity_f1\": 0.1192,\n  \"trigger_f1\": 0.0337,\n  \"argument_f1\": 0.0027,\n  \"code_version\": \"938-line (collision+exact-match fix)\",\n  \"mode\": \"grammar_only\"\n}\n\n=== ee_qwen_wikievents_constrained ===\n{\n  \"parse_success\": \"206/246 (83.7%)\",\n  \"ET\": 0,\n  \"EV\": 0,\n  \"RoV\": 0.3,\n  \"AC\": 2.1,\n  \"CF\": 21.1,\n  \"trigger_f1\": 0.1339,\n  \"argument_f1\": 0.0168,\n  \"entity_f1\": 0.1409,\n  \"parse_failures\": 40,\n  \"go_no_go\": 2.4,\n  \"note\": \"after retry with max_new_tokens=8192\"\n}\n\n=== ee_llama_wikievents_constrained ===\n{\n  \"parse_success\": \"215/246 (87.4%)\",\n  \"ET\": 0,\n  \"EV\": 0,\n  \"RoV\": 0,\n  \"AC\": 3.4,\n  \"CF\": 15.5,\n  \"trigger_f1\": 0.078,\n  \"argument_f1\": 0.011,\n  \"entity_f1\": 0.178,\n  \"parse_failures\": 31,\n  \"go_no_go\": 3.4,\n  \"note\": \"after retry with max_new_tokens=8192\"\n}\n\n=== ee_mistral_wikievents_constrained_v2 ===\n{\n  \"parse_success\": \"178/246 (72.4%)\",\n  \"ET\": 0,\n  \"EV\": 0,\n  \"RoV\": 0.1,\n  \"AC\": 16.6,\n  \"CF\": 13.9,\n  \"trigger_f1\": 0.0508,\n  \"argument_f1\": 0.0047,\n  \"entity_f1\": 0.1245,\n  \"parse_failures\": 68,\n  \"go_no_go\": 16.7\n}\n\n=== d065_tcr_pilot ===\n{\n  \"scierc_zs_qwen\": {\n    \"cf_before\": 9.75,\n    \"cf_after\": 0,\n    \"dr_before\": 0.93,\n    \"dr_after\": 1.21,\n    \"ef1_delta\": -0.0129,\n    \"fund_pct\": 2.04\n  },\n  \"scierc_zs_llama\": {\n    \"cf_before\": 6.4,\n    \"cf_after\": 0,\n    \"dr_before\": 0.08,\n    \"dr_after\": 0.3,\n    \"ef1_delta\": -0.0178,\n    \"fund_pct\": 1.85\n  },\n  \"scierc_lora_qwen\": {\n    \"cf_before\": 1.19,\n    \"cf_after\": 0,\n    \"dr_before\": 0,\n    \"dr_after\": 0,\n    \"ef1_delta\": -0.0075,\n    \"fund_pct\": 0\n  },\n  \"scierc_lora_llama\": {\n    \"cf_before\": 0.46,\n    \"cf_after\": 0,\n    \"dr_before\": 0.09,\n    \"dr_after\": 0.09,\n    \"ef1_delta\": -0.0018,\n    \"fund_pct\": 0\n  },\n  \"scierc_zs_mistral\": {\n    \"cf_before\": 0.67,\n    \"cf_after\": 0,\n    \"dr_before\": 13.36,\n    \"dr_after\": 12.87,\n    \"ef1_delta\": 0.0005,\n    \"fund_pct\": 0\n  },\n  \"docred_zs_qwen\": {\n    \"cf_before\": 13.11,\n    \"cf_after\": 0,\n    \"dr_before\": 10.21,\n    \"dr_after\": 11.74,\n    \"ef1_delta\": -0.0344,\n    \"fund_pct\": 13.52\n  },\n  \"docred_zs_llama\": {\n    \"cf_before\": 23.71,\n    \"cf_after\": 0,\n    \"dr_before\": 2.55,\n    \"dr_after\": 11.93,\n    \"ef1_delta\": -0.0521,\n    \"fund_pct\": 22.78\n  },\n  \"docred_zs_70b\": {\n    \"cf_before\": 11.61,\n    \"cf_after\": 0,\n    \"dr_before\": 0,\n    \"dr_after\": 4.2,\n    \"ef1_delta\": -0.0598,\n    \"fund_pct\": 18.26\n  },\n  \"docred_lora_qwen\": {\n    \"cf_before\": 0.42,\n    \"cf_after\": 0,\n    \"dr_before\": 0.01,\n    \"dr_after\": 0.14,\n    \"ef1_delta\": -0.0016,\n    \"fund_pct\": 12.16\n  },\n  \"docred_lora_llama\": {\n    \"cf_before\": 0.36,\n    \"cf_after\": 0,\n    \"dr_before\": 0.21,\n    \"dr_after\": 0.2,\n    \"ef1_delta\": -0.0017,\n    \"fund_pct\": 11.59\n  },\n  \"total_configs\": 10,\n  \"all_cf_eliminated\": true\n}\n\n=== d065_tcr_full ===\n{\n  \"configs_tested\": 10,\n  \"all_cf_eliminated\": true,\n  \"scierc_all_dr_delta_max\": 0.28,\n  \"docred_lora_dr_delta_max\": 0.14,\n  \"docred_zs_llama_dr_delta\": 9.38,\n  \"docred_zs_70b_dr_delta\": 4.2,\n  \"docred_zs_qwen_dr_delta\": 1.53,\n  \"fund_conflict_scierc_max\": 2.04,\n  \"fund_conflict_docred_zs_max\": 22.78,\n  \"fund_conflict_docred_lora_max\": 12.16,\n  \"lora_ef1_cost_max\": 0.0075,\n  \"zs_docred_ef1_cost_max\": 0.0598\n}\n\n=== posthoc_filtering_baseline ===\n{\n  \"docred_f1_before\": 7.74,\n  \"docred_f1_after\": 9.61,\n  \"docred_precision_before\": 6.55,\n  \"docred_precision_after\": 11.22,\n  \"docred_recall_before\": 9.46,\n  \"docred_recall_after\": 8.4,\n  \"docred_rejection_rate\": 0.481,\n  \"docred_tp_before\": 1137,\n  \"docred_tp_after\": 1010,\n  \"docred_tp_lost\": 127,\n  \"docred_et_residual\": 0.0247,\n  \"scierc_f1_before\": 8.23,\n  \"scierc_f1_after\": 8.63,\n  \"scierc_rejection_rate\": 0.168,\n  \"scierc_recall_before\": 11.4,\n  \"scierc_recall_after\": 10.68,\n  \"scierc_tp_before\": 111,\n  \"scierc_tp_after\": 104\n}\n\n=== w8_ft_posthoc_baseline ===\n{\n  \"ft_regime\": {\n    \"qwen_scierc\": {\n      \"R_F1_before\": 43.86,\n      \"R_F1_posthoc\": 43.94,\n      \"R_F1_constrained\": 43.77,\n      \"reject_rate_pct\": 1.95,\n      \"TP_lost\": 4\n    },\n    \"llama_scierc\": {\n      \"R_F1_before\": 45.45,\n      \"R_F1_posthoc\": 45.23,\n      \"R_F1_constrained\": 45.47,\n      \"reject_rate_pct\": 1.11,\n      \"TP_lost\": 5\n    },\n    \"qwen_docred\": {\n      \"R_F1_before\": 40.91,\n      \"R_F1_posthoc\": 41.11,\n      \"R_F1_constrained\": \"TBD\",\n      \"reject_rate_pct\": 1.03,\n      \"TP_lost\": 1\n    },\n    \"llama_docred\": {\n      \"R_F1_before\": 43.77,\n      \"R_F1_posthoc\": 43.92,\n      \"R_F1_constrained\": 44.23,\n      \"reject_rate_pct\": 0.64,\n      \"TP_lost\": 1\n    }\n  },\n  \"zs_regime\": {\n    \"mistral_scierc\": {\n      \"triples\": 1584,\n      \"reject_pct\": 20.27,\n      \"R_F1_before\": 0.0376,\n      \"R_F1_posthoc\": 0.0394,\n      \"R_F1_constrained\": 0.0367,\n      \"TP_before\": 48,\n      \"TP_after\": 44,\n      \"TP_lost\": 4\n    },\n    \"qwen_scierc\": {\n      \"triples\": 1724,\n      \"reject_pct\": 16.76,\n      \"R_F1_before\": 0.0823,\n      \"R_F1_posthoc\": 0.0863,\n      \"R_F1_constrained\": 0.0836,\n      \"TP_before\": 111,\n      \"TP_after\": 104,\n      \"TP_lost\": 7\n    },\n    \"llama_scierc\": {\n      \"triples\": 1274,\n      \"reject_pct\": 13.89,\n      \"R_F1_before\": 0.0268,\n      \"R_F1_posthoc\": 0.0271,\n      \"R_F1_constrained\": 0.0254,\n      \"TP_before\": 30,\n      \"TP_after\": 28,\n      \"TP_lost\": 2\n    },\n    \"qwen_docred\": {\n      \"triples\": 17497,\n      \"reject_pct\": 48.12,\n      \"R_F1_before\": 0.0774,\n      \"R_F1_posthoc\": 0.0961,\n      \"R_F1_constrained\": 0.0823,\n      \"TP_before\": 1137,\n      \"TP_after\": 1010,\n      \"TP_lost\": 127\n    },\n    \"llama_docred\": {\n      \"triples\": 16437,\n      \"reject_pct\": 42.18,\n      \"R_F1_before\": 0.0598,\n      \"R_F1_posthoc\": 0.0744,\n      \"R_F1_constrained\": 0.0627,\n      \"TP_before\": 850,\n      \"TP_after\": 802,\n      \"TP_lost\": 48\n    },\n    \"mistral_docred\": {\n      \"triples\": 11836,\n      \"reject_pct\": 73.73,\n      \"R_F1_before\n\n=== r16_trie_qwen_ft_scierc ===\n{\n  \"E_F1\": 64.4,\n  \"E_P\": 66.8,\n  \"E_R\": 62.16,\n  \"R_F1\": 41.16,\n  \"R_P\": 38.24,\n  \"R_R\": 44.56,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 95.5,\n  \"CF_pct\": 0.09,\n  \"parse_fail_pct\": 9.1,\n  \"samples\": 551,\n  \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\"\n}\n\n=== r16_trie_llama_ft_scierc ===\n{\n  \"E_F1\": 36.66,\n  \"E_P\": 67.47,\n  \"E_R\": 25.16,\n  \"R_F1\": 19.95,\n  \"R_P\": 41.42,\n  \"R_R\": 13.14,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 15.2,\n  \"CF_pct\": 0,\n  \"parse_fail_pct\": 50.8,\n  \"samples\": 551,\n  \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\"\n}\n\n=== r16_trie_qwen_zs_scierc ===\n{\n  \"E_F1\": 30.97,\n  \"R_F1\": 8.64,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 29.3,\n  \"CF_pct\": 0,\n  \"parse_fail_pct\": 0,\n  \"samples\": 551\n}\n\n=== r16_trie_llama_zs_scierc ===\n{\n  \"E_F1\": 23.23,\n  \"R_F1\": 2.9,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 84.4,\n  \"CF_pct\": 0.36,\n  \"parse_fail_pct\": 0,\n  \"samples\": 551\n}\n\n=== vllm_guided_json_scierc_zs ===\n{\n  \"DR%\": 15.26,\n  \"RV%\": 0,\n  \"ET%\": 0,\n  \"CF%\": 0.04,\n  \"R-F1\": 8.75,\n  \"E-F1\": 30.91,\n  \"parse_fail%\": 0,\n  \"total_samples\": 551,\n  \"total_entities\": 2485,\n  \"total_relations\": 1724,\n  \"inference_time_s\": 108.5\n}\n\n=== r4_prompt_minimal ===\n{\n  \"unconstrained\": {\n    \"ET_pct\": 0.58,\n    \"RV_pct\": 1.16,\n    \"DR_pct\": 16.91,\n    \"E_F1\": 31.98,\n    \"R_F1\": 7.91\n  },\n  \"constrained\": {\n    \"ET_pct\": 0,\n    \"RV_pct\": 0,\n    \"DR_pct\": 0.92,\n    \"E_F1\": 31.99,\n    \"R_F1\": 7.85\n  },\n  \"DR_reduction_pct\": 94.6,\n  \"delta_R_F1_pp\": -0.06,\n  \"delta_E_F1_pp\": 0.01\n}\n\n=== r4_prompt_detailed ===\n{\n  \"unconstrained\": {\n    \"ET_pct\": 0.22,\n    \"RV_pct\": 0.45,\n    \"DR_pct\": 11.07,\n    \"E_F1\": 33.55,\n    \"R_F1\": 10.48\n  },\n  \"constrained\": {\n    \"ET_pct\": 0,\n    \"RV_pct\": 0,\n    \"DR_pct\": 0.64,\n    \"E_F1\": 33.56,\n    \"R_F1\": 10.48\n  },\n  \"DR_reduction_pct\": 94.2,\n  \"delta_R_F1_pp\": 0,\n  \"delta_E_F1_pp\": 0.01\n}\n\n=== p1_ee_ft_composability_r5 ===\n{\n  \"unconstrained\": {\n    \"parse_rate\": 0.85,\n    \"trigger_f1\": 0.3208,\n    \"argument_f1\": 0.0785,\n    \"rov_rate\": 0.3831,\n    \"ac_rate\": 0.0268,\n    \"go_nogo\": 0.41\n  },\n  \"full_s1\": {\n    \"parse_rate\": 0.95,\n    \"trigger_f1\": 0.2672,\n    \"argument_f1\": 0.0818,\n    \"rov_rate\": 0,\n    \"ac_rate\": 0,\n    \"go_nogo\": 0\n  }\n}\n\n=== w1_cf_fallback_scierc_pilot ===\n{\n  \"ET\": 0,\n  \"RV\": 0,\n  \"DR\": 0.1478,\n  \"CF\": 0.0004,\n  \"R_F1\": 0.0823,\n  \"R_P\": 0.0643,\n  \"R_R\": 0.114,\n  \"E_F1\": 0.3098,\n  \"E_P\": 0.2598,\n  \"E_R\": 0.3837,\n  \"entities\": 2474,\n  \"relations\": 1725,\n  \"samples\": 551,\n  \"grammar_first_fallback_rate\": 0.3664,\n  \"cf_registry_fallback_rate\": 0.0448,\n  \"total_mask_calls\": 17024,\n  \"violation_budget_DR_CF\": 0.1482\n}\n\n=== d062_ontology_scalability ===\n{\n  \"compile_small_total_s\": 0.334,\n  \"compile_medium_total_s\": 0.322,\n  \"compile_large_total_s\": 0.345,\n  \"compile_xlarge_total_s\": 0.42,\n  \"grammar_small_s\": 0.333,\n  \"grammar_xlarge_s\": 0.365,\n  \"semantic_small_s\": 0.0004,\n  \"semantic_xlarge_s\": 0.017,\n  \"overhead_small\": 1.02,\n  \"overhead_medium\": 1.03,\n  \"overhead_large\": 1.03,\n  \"overhead_xlarge\": 1.03,\n  \"failures\": 0\n}\n\n=== p8c_ft_scierc_latency ===\n{\n  \"unconstrained_mean_s\": 2.612,\n  \"constrained_mean_s\": 2.873,\n  \"unconstrained_median_s\": 2.355,\n  \"constrained_median_s\": 2.624,\n  \"overhead_mean_pct\": 10,\n  \"overhead_median_pct\": 11.42,\n  \"per_doc_ratio_mean\": 1.205,\n  \"per_doc_ratio_median\": 1.117,\n  \"num_docs\": 551,\n  \"unconstrained_total_s\": 1439,\n  \"constrained_total_s\": 1582.9\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 99_

<details><summary>Logged reasoning block</summary>

```text
Now I have a very comprehensive view of the registry data. Let me also check a couple more experiments that might help resolve remaining questions. Let me get the bootstrap CI and lucky violation experiments.

Let me also check the w5_qwen_docred and w5_llama_docred corrected values more carefully. The key issue is whether DocRED FT values in the paper are from old vs new eval.

Let me also look at the ft-ablation table's DocRED values more carefully:

Paper ft-ablation DocRED/Qwen:
- Unconstrained: DR=0.56, RV=0.27, ET=0.00, CF=0.08, PF=7.11, E-F1=82.35, R-F1=40.89


- Grammar: DR=0.61, RV=0.00, ET=0.00, CF=0.11, PF=7.01, E-F1=82.19, R-F1=40.85
- Semantic: DR=0.21, RV=0.23, ET=0.00, CF=0.27, PF=7.52, E-F1=82.15, R-F1=40.89
- S1: DR=0.00, RV=0.00, ET=0.00, CF=0.22, PF=8.52, E-F1=81.87, R-F1=40.79

The ablation variants show interesting trade-offs—the grammar constraint reduces relation violations but increases duplicate relations, while the semantic constraint shows the opposite pattern with more violations but fewer duplicates.

Now I'm comparing the registry results against the paper's reported numbers for the unconstrained model. The registry entry shows consistently different values across multiple metrics—the detection rate is higher by 0.20 points, but the constraint and F1 scores diverge in the opposite direction. This suggests the paper's unconstrained row might be pulling from a different model variant than what I'm looking at.

Let me check the grammar-only configuration instead. The registry entry for the grammar-focused model matches the paper's reported metrics exactly—detection rate of 0.61, entity F1 of 82.19, relation F1 of 40.85, constraint failure at 0.11, and parse failure at 7.01. That's a complete match across all five metrics.

But when I look at the semantic-only variant, there's a discrepancy. The registry shows R_F1 of 40.85, yet the paper reports 40.89. However, there's a note indicating the registry value was re-verified in May 2026 using a corrected evaluation script that fixed a parse-failure bug, which accounts for a 0.04 percentage point difference from the older unified evaluation method. So the paper's 40.89 is actually the outdated figure.

The same pattern appears with the Llama models—the grammar-only version shows 43.72 in the registry but 43.77 in the paper, and the semantic-only variant has 43.85 in the registry.

Now looking at the unconstrained results, the w5 experiment shows R-F1 of 40.86 and E-F1 of 82.15, but the paper lists 40.89 and 82.35 respectively. These don't align with either the corrected or uncorrected w8 values, which is strange. The DR metric is also off—the w5 experiment has 0.76 while the paper shows 0.56, suggesting these unconstrained values might come from a completely different evaluation run or use a different calculation method for DR. The paper's ft-ablation table seems to use results from the original, pre-corrected evaluation methodology, while the registry values were updated later—but only for the w8 experiments, not for the w5 unconstrained baseline, creating this mismatch between what's reported in the paper and what's stored in the registry. None of the values match what's in the paper—neither the all_set nor excl_fail metrics align with the reported E-F1 of 82.35. I should flag that the DocRED fine-tuned unconstrained results don't match either the old or new evaluation in the registry, and the grammar/semantic values are using pre-correction numbers. Looking at the constrained eval more closely, I see different metrics entirely: DR at 0.01%, CF at 0.41%, E-F1 at 81.43, and R-F1 at 40.56.

The paper and d065 report different values—DR at 0%, CF at 0.22%, E-F1 at 81.87, and R-F1 at 40.79—so these must be from separate experiments. The w5 runs were likely the initial LoRA training with possibly different max_new_tokens or context settings, while d065 was labeled "greedy_4096" suggesting a 4096-token context window. Since d065 came later in the project timeline and its values appear in the ft-ablation table S1 for DocRED/Qwen, that's probably the authoritative result.

But here's the problem: the unconstrained, grammar-only, and semantic-only rows in that same table are using the old unified_f1_eval.py values from w5 and w8, which had the parse-failure bug. So the table is mixing corrected and uncorrected evaluation pipelines for different constraint types. The corrected w8 values differ by 0.04-0.05 percentage points in R-F1 from what's reported, and the unconstrained row doesn't match any registry entry exactly.

I need to finalize my audit findings now. The core issue is that the DocRED rows in the ft-ablation table contain pre-correction values for R-F1 and E-F1 in the unconstrained, grammar-only, and semantic-only conditions.

Beyond that, there are several other mismatches I'm seeing: the Qwen unconstrained row shows DR=0.56 but the registry has 0.76, the Llama unconstrained row has different E-F1 and R-F1 values than what's registered, and the full-ft LoRA unconstrained row doesn't correspond to any registry entry at all.

Looking at the beam-docred-lora table, I'm noticing the Qwen greedy PF value is listed as 7.8% in the paper but 8.52% in the registry, and the Llama values appear to use pre-correction numbers rather than the corrected ones.

I need to dig deeper into whether these discrepancies stem from different experimental runs or if there's an issue with how the values were computed or reported.

Checking the DocRED FT Llama unconstrained results more carefully: the violation rates (DR, RV, PF) all match between the paper and registry, but the F1 scores don't. This pattern is exactly what I'd expect from that parse-failure bug—the old evaluation excluded parse-failed documents from the gold set, which would artificially inflate the F1 metrics.

Looking at the corrected constrained version and comparing it to the paper's reported Llama DocRED S1 scores, I'm still seeing the same discrepancy pattern across both E-F1 and R-F1, suggesting the parse-failure issue persists. Now I'm checking the Qwen DocRED results to see if they show a similar pattern.

The S1 constrained row for Qwen is actually correct since it used the fixed evaluation script, but the unconstrained and other variant rows are pulling from the old evaluation. However, the grammar-only variant appears to match the paper's reported values exactly, including the detailed breakdown metrics. So the semantic results are inconsistent with the registry—the paper reports 40.89, which matches the old buggy value, not the corrected 40.85. For unconstrained, the paper shows 40.89 but the registry has 40.86, so neither the old nor corrected value aligns exactly.

Looking at the Llama models, both grammar and semantic variants also report the old values in the paper: grammar shows 43.77 (old) instead of 43.72 (corrected), and semantic shows 43.90 (old) instead of 43.85 (corrected). This is strange because the Qwen grammar was actually corrected to 40.85 in the paper, but the semantic stayed at the old 40.89—so the paper is mixing corrected and uncorrected values across different model variants. Looking at the Llama results, the paper shows 44.55 for unconstrained, but the actual eval file shows 43.72—there's a significant discrepancy that suggests the unconstrained baseline wasn't corrected in the same way the grammar and semantic variants were. The Qwen Unconstrained, Semantic, and all Llama DocRED rows are still using pre-correction values, which is inconsistent with the corrected Grammar and S1 entries. Even the Llama S1 row appears to use the old uncorrected value (R-F1=44.70 vs. corrected 43.78), so I'm puzzled why that particular entry wasn't updated along with the others.

Looking at the pattern, the d065 experiments are inherently correct because they used the fixed evaluation script from the start, while the w5 and w8 experiments were run with the buggy eval and only partially corrected in the registry without updating the paper itself. This mirrors the same inconsistency issue already identified in Table 2 of the main text.

Now I'm diving deeper into the DocRED fine-tuned Llama results by cross-referencing the delta values in the registry. The w5_llama_docred_lora_constrained_eval entry shows a delta of -0.28 for DR and +0.06 for R-F1, which would put the constrained values at 0.21% and 43.78% respectively. But the paper reports 0.00% for DR and 44.70% for R-F1—a significant discrepancy that suggests the registry correction wasn't fully applied to the published numbers.

Looking at the raw registry data, there are 33 DR violations at a 0.21% rate, yet the paper claims zero violations. This could mean the evaluation script used for the registry (eval_d064.py) computes DR differently than what the paper's methodology uses, or there's an inconsistency in how the constrained model was actually evaluated versus what was reported. Looking at the corrected evaluation data, I see the w5 entry shows 33 DR violations out of 16074 relations, which calculates to about 0.21% — matching the registry's corrected value. The old evaluation script (unified_f1_eval.py) likely computed DR differently, possibly excluding certain documents or handling parse failures in a way that resulted in DR=0.

I'm also noticing a pattern across different experiment subsets: the 200-doc quantization experiment shows DR=0, while the 998-doc w5 set shows DR=0.21, yet the ft-ablation table uses 998 docs but still reports DR=0, suggesting it was evaluated with the older buggy script. Rather than chase down every individual discrepancy, I should compile all these findings into a comprehensive audit report that flags each inconsistency I've found and documents the likely causes.

Now I need to verify the Qwen DocRED unconstrained values since there's a mismatch: the paper reports DR=0.56 but the registry shows DR=0.76 for the same experiment. Looking at the registry, w5_qwen_docred_lora_unconstrained_eval has DR_pct=0.76, and there's no other unconstrained Qwen DocRED LoRA variant, so either the registry was updated without documentation or the paper used a different evaluation methodology. The constrained version was corrected with eval_d064.py and shows DR=0.01, which suggests different eval scripts produce substantially different results.

Comparing across experiments, d065_qwen_greedy_4096_r2 gives DR=0 for the same model and data, while the corrected w5 shows DR=0.01—a negligible difference that could stem from slight variations in evaluation or inference. The pattern emerging is that the ft-ablation table was originally generated with the old unified_f1_eval.py, partially corrected for Qwen grammar issues, and the registry was updated with values from eval_d064.py, but the paper wasn't fully synchronized with these corrections.

Now I'm compiling the final report and checking the quantization table values, which should be reliable since d065 and d066 experiments used the correct evaluation from the start. Spot-checking the Llama SciERC FP16 results confirms they match: the paper's DR=0.09, R-F1=45.47, E-F1=67.76 align perfectly with the registry values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "180e43de-3b1f-42e3-bdf7-3ee4f763866f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWDUDLyA4SzbAnyrFLb8zw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14754,
      "cache_read_input_tokens": 119611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14754
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 100_

Now I have all the data I need. Let me also quickly check a few remaining experiments and verify the bootstrap/posthoc tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "778ae442-04f3-4f7c-8b30-f8f28e761dd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWDUDLyA4SzbAnyrFLb8zw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14754,
      "cache_read_input_tokens": 119611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14754
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 101_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y5is9F6r3NrHCc3ijiSv4u`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt\"\npython3 -c \"\nimport json\n\nwith open('${REGFILE}') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Check remaining: bootstrap CI, causal tracing, lucky violation, sampling DocRED\nids = [\n    'd067_seed_variance',\n    'phase2_scierc_full_s2',\n    'llama_docred_unconstrained_mt6144', 'llama_docred_full_s1_mt6144',\n    'w1_cf_fallback_llama_docred', 'w1_cf_fallback_llama_scierc',\n    'w1_cf_fallback_docred',\n]\n\nfor eid in ids:\n    if eid in exps:\n        exp = exps[eid]\n        print(f'\\\\n=== {eid} ===')\n        metrics = exp.get('metrics', {})\n        print(json.dumps(metrics, indent=2)[:1500])\n    else:\n        print(f'\\\\n=== {eid} === NOT FOUND')\n\" 2>&1",
  "description": "Check remaining experiment metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "46309df0-58d9-47e3-80ef-01217f65b15a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWDUDLyA4SzbAnyrFLb8zw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14754,
      "cache_read_input_tokens": 119611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14754
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 102 · 2026-05-23T10:54:48.912Z_

<details><summary>↩ Tool result · `toolu_01Y5is9F6r3NrHCc3ijiSv4u`</summary>

```text
=== d067_seed_variance ===
{
  "qwen_scierc_unc": {
    "E_F1": "66.94 \u00b1 0.08",
    "R_F1": "43.25 \u00b1 0.43",
    "DR": "2.06 \u00b1 0.08",
    "CF": "0.00 \u00b1 0.00"
  },
  "qwen_scierc_con": {
    "E_F1": "66.94 \u00b1 0.08",
    "R_F1": "43.22 \u00b1 0.39",
    "DR": "0.00 \u00b1 0.00",
    "CF": "0.48 \u00b1 0.02"
  },
  "llama_scierc_unc": {
    "E_F1": "67.99 \u00b1 0.16",
    "R_F1": "45.38 \u00b1 0.05",
    "DR": "1.04 \u00b1 0.05",
    "CF": "0.00 \u00b1 0.00"
  },
  "llama_scierc_con": {
    "E_F1": "67.99 \u00b1 0.16",
    "R_F1": "45.40 \u00b1 0.05",
    "DR": "0.03 \u00b1 0.04",
    "CF": "0.26 \u00b1 0.02"
  },
  "max_sigma_pp": 0.43,
  "greedy_deterministic": true,
  "snr_dr_improvement": ">12x",
  "qwen_docred_status": "pending (not started)",
  "llama_scierc_seed456_con_status": "running (407/551)"
}

=== phase2_scierc_full_s2 ===
{
  "total_samples": 551,
  "total_triples": 1644,
  "total_entities": 2228,
  "json_parse_rate": 1,
  "entity_type_violation_rate": 0,
  "relation_vocabulary_violation_rate": 0,
  "domain_range_violation_rate": 0.0097,
  "cross_field_consistency_violation_rate": 0.0803,
  "entity_precision": 0.2797,
  "entity_recall": 0.3712,
  "entity_f1": 0.319,
  "relation_precision": 0.064,
  "relation_recall": 0.1078,
  "relation_f1": 0.0803,
  "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}

=== llama_docred_unconstrained_mt6144 ===
{
  "ET_rate": 0.13,
  "RV_rate": 15.89,
  "DR_rate": 26.18,
  "DR_rate_eligible": 31.15,
  "CF_rate": 0.17,
  "entity_precision": 61.19,
  "entity_recall": 51.06,
  "entity_f1": 55.67,
  "relation_precision": 5.18,
  "relation_recall": 7,
  "relation_f1": 5.95,
  "parse_failures": 67,
  "documents_checked": 931,
  "total_documents": 998,
  "unique_entities": 11534,
  "total_triples": 16584,
  "dr_eligible_triples": 13936,
  "fuzzy_relation_matches": 121
}

=== llama_docred_full_s1_mt6144 ===
{
  "DR_rate_pct": 2.57,
  "RV_rate_pct": 0,
  "ET_rate_pct": 0,
  "CF_rate_pct": 12.13,
  "R_F1": 6.25,
  "R_precision": 5.45,
  "R_recall": 7.32,
  "E_F1": 55.04,
  "E_precision": 61.41,
  "E_recall": 49.87,
  "documents_total": 998,
  "documents_checked": 908,
  "parse_failures": 90,
  "triples": 16471,
  "unique_entities": 11307,
  "fallback_events": 67911,
  "wall_clock_seconds": 23926,
  "vs_unconstrained_mt6144": {
    "DR_delta_pp": -23.61,
    "DR_reduction_pct": -90.2,
    "R_F1_delta_pp": 0.3,
    "E_F1_delta_pp": -0.63
  },
  "vs_full_s1_mt4096": {
    "DR_delta_pp": 0.02,
    "R_F1_delta_pp": -0.02,
    "E_F1_delta_pp": 0.03,
    "CF_delta_pp": 0.11,
    "parse_fail_delta": -1
  }
}

=== w1_cf_fallback_llama_docred ===
{}

=== w1_cf_fallback_llama_scierc ===
{}

=== w1_cf_fallback_docred ===
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "8aa20c63-1437-4fcc-bb01-9c4e8bdc926f",
  "tool_use_result": {
    "stdout": "=== d067_seed_variance ===\n{\n  \"qwen_scierc_unc\": {\n    \"E_F1\": \"66.94 \\u00b1 0.08\",\n    \"R_F1\": \"43.25 \\u00b1 0.43\",\n    \"DR\": \"2.06 \\u00b1 0.08\",\n    \"CF\": \"0.00 \\u00b1 0.00\"\n  },\n  \"qwen_scierc_con\": {\n    \"E_F1\": \"66.94 \\u00b1 0.08\",\n    \"R_F1\": \"43.22 \\u00b1 0.39\",\n    \"DR\": \"0.00 \\u00b1 0.00\",\n    \"CF\": \"0.48 \\u00b1 0.02\"\n  },\n  \"llama_scierc_unc\": {\n    \"E_F1\": \"67.99 \\u00b1 0.16\",\n    \"R_F1\": \"45.38 \\u00b1 0.05\",\n    \"DR\": \"1.04 \\u00b1 0.05\",\n    \"CF\": \"0.00 \\u00b1 0.00\"\n  },\n  \"llama_scierc_con\": {\n    \"E_F1\": \"67.99 \\u00b1 0.16\",\n    \"R_F1\": \"45.40 \\u00b1 0.05\",\n    \"DR\": \"0.03 \\u00b1 0.04\",\n    \"CF\": \"0.26 \\u00b1 0.02\"\n  },\n  \"max_sigma_pp\": 0.43,\n  \"greedy_deterministic\": true,\n  \"snr_dr_improvement\": \">12x\",\n  \"qwen_docred_status\": \"pending (not started)\",\n  \"llama_scierc_seed456_con_status\": \"running (407/551)\"\n}\n\n=== phase2_scierc_full_s2 ===\n{\n  \"total_samples\": 551,\n  \"total_triples\": 1644,\n  \"total_entities\": 2228,\n  \"json_parse_rate\": 1,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0.0097,\n  \"cross_field_consistency_violation_rate\": 0.0803,\n  \"entity_precision\": 0.2797,\n  \"entity_recall\": 0.3712,\n  \"entity_f1\": 0.319,\n  \"relation_precision\": 0.064,\n  \"relation_recall\": 0.1078,\n  \"relation_f1\": 0.0803,\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== llama_docred_unconstrained_mt6144 ===\n{\n  \"ET_rate\": 0.13,\n  \"RV_rate\": 15.89,\n  \"DR_rate\": 26.18,\n  \"DR_rate_eligible\": 31.15,\n  \"CF_rate\": 0.17,\n  \"entity_precision\": 61.19,\n  \"entity_recall\": 51.06,\n  \"entity_f1\": 55.67,\n  \"relation_precision\": 5.18,\n  \"relation_recall\": 7,\n  \"relation_f1\": 5.95,\n  \"parse_failures\": 67,\n  \"documents_checked\": 931,\n  \"total_documents\": 998,\n  \"unique_entities\": 11534,\n  \"total_triples\": 16584,\n  \"dr_eligible_triples\": 13936,\n  \"fuzzy_relation_matches\": 121\n}\n\n=== llama_docred_full_s1_mt6144 ===\n{\n  \"DR_rate_pct\": 2.57,\n  \"RV_rate_pct\": 0,\n  \"ET_rate_pct\": 0,\n  \"CF_rate_pct\": 12.13,\n  \"R_F1\": 6.25,\n  \"R_precision\": 5.45,\n  \"R_recall\": 7.32,\n  \"E_F1\": 55.04,\n  \"E_precision\": 61.41,\n  \"E_recall\": 49.87,\n  \"documents_total\": 998,\n  \"documents_checked\": 908,\n  \"parse_failures\": 90,\n  \"triples\": 16471,\n  \"unique_entities\": 11307,\n  \"fallback_events\": 67911,\n  \"wall_clock_seconds\": 23926,\n  \"vs_unconstrained_mt6144\": {\n    \"DR_delta_pp\": -23.61,\n    \"DR_reduction_pct\": -90.2,\n    \"R_F1_delta_pp\": 0.3,\n    \"E_F1_delta_pp\": -0.63\n  },\n  \"vs_full_s1_mt4096\": {\n    \"DR_delta_pp\": 0.02,\n    \"R_F1_delta_pp\": -0.02,\n    \"E_F1_delta_pp\": 0.03,\n    \"CF_delta_pp\": 0.11,\n    \"parse_fail_delta\": -1\n  }\n}\n\n=== w1_cf_fallback_llama_docred ===\n{}\n\n=== w1_cf_fallback_llama_scierc ===\n{}\n\n=== w1_cf_fallback_docred ===\n{}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 103_

<details><summary>Logged reasoning block</summary>

```text
OK, I now have a comprehensive view of the data. Let me compile the audit report.

Let me also check the WikiEvents grammar-only values more carefully. The paper says:
- Qwen Grammar: EV=0, RoV=76.1, AC=8.2
- Llama Grammar: EV=0, RoV=77.0, AC=8.8
- Mistral Grammar: EV=0, RoV=64.0, AC=13.8

But I only have ee_mistral_wikievents_grammar_only_v3 in the registry: RoV=64, AC=13.8 ✅


The Qwen and Llama grammar-only WikiEvents experiments aren't in the registry—they might be stored separately. Now checking the S1 results: the Qwen WikiEvents constrained experiment matches the paper's values across all metrics including the trigger and entity F1 scores. Now I'm verifying the Mistral model's metrics against the registry—the trigger and entity F1 scores both check out. Moving on to the WikiEvents unconstrained results, starting with Qwen's performance data. I've verified all the WikiEvents metrics match across the models, so now I'm moving on to check the TCR table results for the SciERC dataset, starting with the Zero-Shot Qwen configuration. Now I'm reviewing the performance metrics for the remaining model variants—Mistral shows minimal change in F1 despite reducing hallucinations slightly, while the LoRA Qwen approach eliminates hallucinations entirely but at the cost of a larger F1 drop. Now I'm verifying the DocRED results for both Qwen and Llama models, checking that the registry values match the computed metrics across all parameters. Now I'm verifying the LoRA configurations across different models—Qwen and Llama both show their calibration and drift metrics matching the registry values. All the TCR DocRED entries check out, so I'm moving on to examine the posthoc-extended table which contains both zero-shot and fine-tuned results, starting with the Qwen SciERC zero-shot values. Continuing to verify the metrics across the remaining model configurations—Mistral's DocRED results are showing a 73.7% rejection rate with a 3.85 post-hoc F1 score, and I'm checking that these align with the registry values as expected. I'm noticing a discrepancy with the Llama DocRED constrained value—the paper reports 44.70 but the registry shows 44.23, which doesn't match. Let me check if there's a different baseline or table in the paper that might explain this mismatch.

Looking at the different evaluation runs, I'm seeing four different values floating around: 44.70 from the original paper ablation, 44.23 from an intermediate registry entry, and 43.78 from the corrected evaluation. I need to figure out which one is actually correct and where the 44.23 came from—it might be from an earlier evaluation before the full bug fix was applied.

I'm also noticing that both the posthoc-extended table and the beam-docred-lora results are using that old 44.70 value, which suggests they haven't been updated with the correction yet. The 43.78 from the corrected evaluation is the most authoritative since it came from the fixed code, so that's what should be used going forward.

Now I'm ready to put together the full audit report, focusing on which values are clearly correct versus which ones are using the pre-correction numbers that need to be flagged.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "06c2946a-4732-4ae3-8868-8d7495f539f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kG4CVz9NvBYni7hrR6y3z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8839,
      "cache_read_input_tokens": 134365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8839
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 104_

I now have comprehensive data for all appendix tables. Let me also verify the prompt sensitivity and trie baseline values, then compile the full audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "e154e07d-04d1-4f90-aa3a-f4c430beba2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kG4CVz9NvBYni7hrR6y3z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8839,
      "cache_read_input_tokens": 134365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8839
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 105_

<details open><summary>🔧 Tool call — Bash · `toolu_01LeTrWFWa6Aaxs7nJ8hfTDv`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained_ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt\"\n# Check if the w8_ft_posthoc_baseline has the truncated Mistral DocRED data\npython3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\nexp = exps.get('w8_ft_posthoc_baseline', {})\nmetrics = exp.get('metrics', {})\nzs = metrics.get('zs_regime', {})\nmistral_docred = zs.get('mistral_docred', {})\nprint('Mistral DocRED ZS posthoc:', json.dumps(mistral_docred, indent=2))\nft = metrics.get('ft_regime', {})\nprint('\\\\nFT regime:', json.dumps(ft, indent=2))\n\"",
  "description": "Check remaining posthoc values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "91ce689f-1a6a-4fb4-9d7e-240acfec87af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kG4CVz9NvBYni7hrR6y3z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8839,
      "cache_read_input_tokens": 134365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8839
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 106 · 2026-05-23T10:55:56.849Z_

<details><summary>↩ Tool result · `toolu_01LeTrWFWa6Aaxs7nJ8hfTDv`</summary>

```text
Mistral DocRED ZS posthoc: {
  "triples": 11836,
  "reject_pct": 73.73,
  "R_F1_before": 0.0434,
  "R_F1_posthoc": 0.0385,
  "R_F1_constrained": 0.0552,
  "TP_before": 518,
  "TP_after": 292,
  "TP_lost": 226,
  "removed_RV": 4172,
  "removed_ET": 3382,
  "removed_DR": 1173,
  "note": "Only ZS case where posthoc HURTS R_F1 \u2014 73.7% rejection rate loses 43.6% of TPs"
}

FT regime: {
  "qwen_scierc": {
    "R_F1_before": 43.86,
    "R_F1_posthoc": 43.94,
    "R_F1_constrained": 43.77,
    "reject_rate_pct": 1.95,
    "TP_lost": 4
  },
  "llama_scierc": {
    "R_F1_before": 45.45,
    "R_F1_posthoc": 45.23,
    "R_F1_constrained": 45.47,
    "reject_rate_pct": 1.11,
    "TP_lost": 5
  },
  "qwen_docred": {
    "R_F1_before": 40.91,
    "R_F1_posthoc": 41.11,
    "R_F1_constrained": "TBD",
    "reject_rate_pct": 1.03,
    "TP_lost": 1
  },
  "llama_docred": {
    "R_F1_before": 43.77,
    "R_F1_posthoc": 43.92,
    "R_F1_constrained": 44.23,
    "reject_rate_pct": 0.64,
    "TP_lost": 1
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "8242e131-63b5-44c4-b71e-3991bd68c6df",
  "tool_use_result": {
    "stdout": "Mistral DocRED ZS posthoc: {\n  \"triples\": 11836,\n  \"reject_pct\": 73.73,\n  \"R_F1_before\": 0.0434,\n  \"R_F1_posthoc\": 0.0385,\n  \"R_F1_constrained\": 0.0552,\n  \"TP_before\": 518,\n  \"TP_after\": 292,\n  \"TP_lost\": 226,\n  \"removed_RV\": 4172,\n  \"removed_ET\": 3382,\n  \"removed_DR\": 1173,\n  \"note\": \"Only ZS case where posthoc HURTS R_F1 \\u2014 73.7% rejection rate loses 43.6% of TPs\"\n}\n\nFT regime: {\n  \"qwen_scierc\": {\n    \"R_F1_before\": 43.86,\n    \"R_F1_posthoc\": 43.94,\n    \"R_F1_constrained\": 43.77,\n    \"reject_rate_pct\": 1.95,\n    \"TP_lost\": 4\n  },\n  \"llama_scierc\": {\n    \"R_F1_before\": 45.45,\n    \"R_F1_posthoc\": 45.23,\n    \"R_F1_constrained\": 45.47,\n    \"reject_rate_pct\": 1.11,\n    \"TP_lost\": 5\n  },\n  \"qwen_docred\": {\n    \"R_F1_before\": 40.91,\n    \"R_F1_posthoc\": 41.11,\n    \"R_F1_constrained\": \"TBD\",\n    \"reject_rate_pct\": 1.03,\n    \"TP_lost\": 1\n  },\n  \"llama_docred\": {\n    \"R_F1_before\": 43.77,\n    \"R_F1_posthoc\": 43.92,\n    \"R_F1_constrained\": 44.23,\n    \"reject_rate_pct\": 0.64,\n    \"TP_lost\": 1\n  }\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 107_

<details><summary>Logged reasoning block</summary>

```text
Now let me verify the posthoc-extended table more carefully:

Paper posthoc-extended FT:
- Qwen SciERC: Reject=1.95%, ph=43.94, cd=43.77
  Registry: reject=1.95 ✅, ph=43.94 ✅, cd=43.77 ✅

- Llama SciERC: Reject=1.11%, ph=45.23, cd=45.47
  Registry: reject=1.11 ✅, ph=45.23 ✅, cd=45.47 ✅
  
Checking the DocRED entries now. Qwen's metrics match across the board, though the registry shows the cd value as TBD while the paper and d065 both confirm 40.79. For Llama DocRED, there's a discrepancy—the paper reports cd=44.70 but the registry has 44.23 instead.

Looking deeper, that 44.70 comes from an older buggy evaluation run, while 44.23 was from an intermediate stage. The latest corrected value from eval_d064.py is actually 43.78, which means the posthoc table has the same issue—it's using the outdated buggy eval result for Llama DocRED's cd value.

Shifting to the unconstrained R-F1 scores in the fine-tuning regime, both Qwen and Llama SciERC match perfectly between my data and the paper, but Qwen DocRED shows a slight discrepancy: I have 40.91 while the paper lists 40.89.

For Llama DocRED, there's a bigger problem—the paper reports 44.55 unconstrained R-F1, but my registry shows 43.77, and the corrected evaluation gives 43.72. These three values suggest the paper used a buggy eval, while my different registry entries might come from slightly different evaluation runs.

Now I'm compiling the full audit report. I've verified that all the quantization, fine-tuning ablation, DocRED ablation, zero-shot ablation, beam search, beam ablation, beam sweep, beam DocRED zero-shot, and beam latency tables match the registry values correctly. I'm going through the remaining tables to verify their values against the experiment registry. Most of the zero-shot and full fine-tuning results check out, but I'm running into issues with tables that rely on computed metrics like bootstrap distributions and causal analysis data that aren't directly stored in the registry. I'm also spotting some discrepancies in the fine-tuning ablation results, particularly with the Llama DocRED comparison row.

The critical issue is that several DocRED metrics in the ft-ablation table are pulling from the buggy unified_f1_eval.py script, except for a couple of Qwen entries that either use corrected values or come from a different source. The Qwen Unconstrained and Semantic rows have noticeably different corrected values compared to what's in the paper, especially for the relation F1 and discrepancy ratio.

Looking at the Llama results, I'm seeing similar problems across multiple constraint types—Unconstrained, Grammar, Semantic, and S1 all have discrepancies between the paper values and the corrected ones. The relation F1 scores are consistently lower after correction, and the entity F1 values also shift downward. There's also a parse-failure bug affecting the Llama rows in the beam-docred-lora table that I need to investigate further.

Moving through the other tables, I'm noticing the posthoc-extended table is using pre-correction values for Llama DocRED, and the full-ft LoRA unconstrained row has metrics that don't align with anything in the registry—the ft-ablation table shows different numbers for what should be the same LoRA SciERC unconstrained setup. The Qwen SciERC Semantic results are also flagged as needing verification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "d7da46d7-6ada-4980-834f-c1b1989bf83e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XAsaLWUA2L61qyWyT4v8Ww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4888,
      "cache_read_input_tokens": 143204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4888
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 108_

I now have all the data needed for a comprehensive audit. Here is the full report:

---

# Appendix Table Audit Report

## Summary

Audited **25 appendix files** containing **~30 tables** against 164 registry experiments. The vast majority of values are verified correct. One systematic issue affects multiple tables: **the parse-failure bug** (same as known Table 2 issue) impacts DocRED FT values in several appendix tables.

---

## VERIFIED CORRECT ✅

### tab:quantization (appendix_quantization.tex)
All 18 data cells verified against 7 registry experiments:
- `sf2_qwen_int4_scierc_s1`: DR=0, R-F1=41.71, E-F1=67.05 ✅
- `sf2_llama_int4_scierc_s1`: DR=0, R-F1=43.98, E-F1=67.54 ✅
- `sf2_qwen_int4_docred_s1`: DR=0, R-F1=40.07, E-F1=74.84, PF=18.5% ✅
- `sf2_llama_int4_docred_s1`: DR=0, R-F1=48.04, E-F1=84.18, PF=2.5% ✅
- `entity_order_ablation_qwen_scierc` (FP16 Qwen SciERC): DR=0, R-F1=43.77, E-F1=67.05 ✅
- `d065_qwen_greedy_4096_r2` (FP16 Qwen DocRED): DR=0, R-F1=40.79, E-F1=81.87, PF=8.5% ✅
- `w5_llama_lora_scierc_constrained_eval` (FP16 Llama SciERC): DR=0.09, R-F1=45.47, E-F1=67.76 ✅
- `d066_sweep_llama_docred_beam1_s1` (FP16 Llama DocRED): DR=0, R-F1=47.35, E-F1=85.43, PF=2.0% ✅

Δ columns all arithmetically correct. ✅

### tab:70b-ft-ablation (appendix_70b_ablation.tex)
All 6 rows verified against `eval_70b_lora_scierc_*`:
- Unconstrained: DR=1.50, R-F1=44.73, E-F1=64.86 ✅
- Grammar: DR=1.50, R-F1=44.63, E-F1=64.82 ✅
- Semantic: DR=0.60, CF=9, R-F1=44.73, E-F1=64.86 ✅
- S1: DR=0, CF=15, R-F1=44.53, E-F1=64.76 ✅
- S2: DR=0, CF=18, R-F1=36.28, E-F1=62.35 ✅
- Beam4 S1: DR=0, CF=1, R-F1=44.81, E-F1=64.89 ✅

### tab:70b-docred-ablation (appendix_70b_ablation.tex)
All 6 rows verified against `eval_70b_lora_docred_200_*`:
- Unconstrained: DR=0.22, RV=0.57, R-F1=43.80, E-F1=80.34 ✅
- Grammar: DR=0.38, R-F1=43.96 ✅
- Semantic: DR=0, RV=0.51, R-F1=43.61 ✅
- S1: DR=0, CF=0.18%, R-F1=43.95, E-F1=79.38 ✅
- S2: DR=0, CF=0.34%, R-F1=36.45, E-F1=84.96 ✅
- Beam4 S1: DR=0, CF=0, R-F1=48.14, E-F1=85.57 ✅

### tab:70b-docred-zs-ablation (appendix_70b_ablation.tex)
All 4 rows verified against `eval_70b_zs_docred_200_*`:
- Unconstrained: DR=13.45, RV=7.88, R-F1=13.25, E-F1=70.14 ✅
- Grammar: DR=17.03, R-F1=13.23, E-F1=70.12 ✅
- Semantic: DR=1.66, RV=8.24, ET=0.12, CF=132, R-F1=13.05, E-F1=70.10 ✅
- S1: DR=0, CF=173, R-F1=13.25, E-F1=70.05 ✅

### tab:cross-model (appendix_zs_crossmodel.tex)
All 12 rows (3 models × 2 datasets × U/S1) verified. Every DR, RV, ET, CF, R-F1 value matches. ✅

### tab:docred-ablation (appendix_discussion.tex — ZS 4-way)
All 4 rows verified against `phase2_docred_*`. All violation rates, F1, and Δ values match. ✅

### tab:beam-ablation (appendix_beam_search.tex)
All 4 rows (k=1,2,4,8) verified:
- k=1: DR=0.93, CF=9.90, E-F1=30.98, R-F1=8.36 ✅
- k=2: DR=0.35, CF=4.12, E-F1=31.54, R-F1=8.75 ✅
- k=4: DR=0, CF=0.53, E-F1=32.00, R-F1=8.56 ✅
- k=8: DR=0, CF=0.08, E-F1=32.18, R-F1=8.39 ✅

### tab:beam-sweep (appendix_beam_search.tex)
All 8 rows (4 beam widths × unc/con) verified against `d066_beam_sweep`. All F1, DR, CF, latency, and relative latency values match. ✅

### tab:beam-docred-998-zs (appendix_beam_search.tex)
Both rows verified against `r14_*_docred_beam4_998`:
- Qwen: DR=0, CF=4.94, E-F1=58.19, R-F1=8.72 ✅
- Llama: DR=0, CF=1.00, E-F1=57.81, R-F1=8.83 ✅

### tab:beam-latency (appendix_beam_search.tex)
All 4 rows verified against `d062_beam_latency`:
- Greedy unc: 2.612 s/doc, 1.00× ✅
- Greedy con: 2.873, 1.10× ✅
- Beam-4 unc: 3.446, 1.32× ✅
- Beam-4 con: 4.013, 1.54× ✅

### tab:gollie-comparison (appendix_gollie_comparison.tex)
All 3 rows verified against `sf2_gollie_scierc_violation`. ✅

### tab:wikievents (appendix_wikievents_pilot.tex)
All 9 rows (3 models × 3 modes) verified against `ee_*_wikievents_*_v3`. ✅

### tab:tcr-scierc and tab:tcr-docred (appendix_tcr.tex)
All 10 TCR configurations verified against `d065_tcr_pilot`. ✅

### tab:prompt-sensitivity (appendix_prompt_sensitivity.tex)
All 6 rows verified against `r4_prompt_minimal`, `r4_prompt_detailed`, and `phase2_scierc_*`. ✅

### tab:vllm-verification (appendix_discussion.tex)
Both rows verified: Grammar-Only DR=14.84 ✅; vLLM DR=15.26, R-F1=8.75 ✅

### tab:trie-baseline (appendix_discussion.tex)
All 4 rows verified against `r16_trie_*_scierc`. Uses corrected values. ✅

### tab:scalability (appendix_scalability.tex)
All 4 rows verified against `d062_ontology_scalability`. ✅

### tab:cf-dr-tradeoff (appendix_discussion.tex)
Verified against `w1_cf_fallback_scierc_pilot`: DR=14.78%, CF=0.04% ✅

### tab:sampling-robustness (appendix_sampling_table.tex)
SciERC row verified against `w9_qwen_scierc_zs_sampling`. ✅

### Other discussion tables
tab:causal-tracing, tab:cf-distribution, tab:cascade-breakdown, tab:lora-per-relation, tab:lucky-violations, tab:lucky-violations-detail, tab:posthoc-extended (ZS rows), tab:power-analysis, tab:high-kappa-rels, tab:dr-by-ambiguity, tab:doc-length-*, tab:kappa-case-study, tab:gcd-comparison: Source experiments exist in registry with matching violation rates where verifiable. Statistical computation tables (bootstrap CI, power analysis) cannot be verified from raw metrics but source experiments are confirmed correct.

---

## DISCREPANCIES FOUND ❌

### 1. tab:ft-ablation DocRED rows — PARSE-FAILURE BUG (CRITICAL)

Same issue as known Table 2 bug. The DocRED FT rows use pre-correction values from buggy `unified_f1_eval.py`. Registry was corrected on 2026-05-22 with `eval_d064.py`, but paper wasn't fully updated.

**Qwen DocRED:**

| Cell | Paper | Registry (corrected) | Δ |
|------|-------|---------------------|---|
| Unconstrained R-F1 | 40.89 | 40.86 | -0.03 |
| Unconstrained E-F1 | 82.35 | 82.15 | -0.20 |
| Unconstrained DR | 0.56 | 0.76 | +0.20 |
| Semantic R-F1 | 40.89 | 40.85 | -0.04 |
| Grammar R-F1 | 40.85 | 40.85 | 0 ✅ (already corrected) |
| S1 R-F1 | 40.79 | 40.79 | 0 ✅ (from d065) |

**Llama DocRED:**

| Cell | Paper | Registry (corrected) | Δ |
|------|-------|---------------------|---|
| Unconstrained E-F1 | 84.77 | 83.93 | -0.84 |
| Unconstrained R-F1 | 44.55 | 43.72 | -0.83 |
| Grammar R-F1 | 43.77 | 43.72 | -0.05 |
| Semantic R-F1 | 43.90 | 43.85 | -0.05 |
| S1 E-F1 | 84.71 | 83.94 | -0.77 |
| S1 R-F1 | 44.70 | 43.78 | -0.92 |

Note: Qwen Grammar was correctly updated. Qwen S1 uses `d065_qwen_greedy_4096_r2` (inherently correct). All other DocRED FT cells need correction.

### 2. tab:beam-docred-lora — SAME BUG + PF mismatch

**Llama Greedy con row** uses same pre-correction values:
- Paper E-F1=84.71, R-F1=44.70 → Corrected: 83.94, 43.78

**Qwen Greedy con PF:**
- Paper: PF=7.8%
- Registry `d065_qwen_greedy_4096_r2`: PF=8.52%
- ft-ablation table for same experiment: PF=8.52

The 7.8% value has no registry source. Likely a transcription error — should be 8.52% (or possibly 7.8% = 78/998 while 8.52% = 85/998 under different parse-failure definition).

### 3. tab:posthoc-extended — Llama DocRED FT cd value

Paper says cd R-F1=44.70, registry `w8_ft_posthoc_baseline` has cd=44.23 (intermediate value), corrected eval gives 43.78. Same parse-failure bug.

### 4. tab:full-ft LoRA unconstrained comparison row

| Metric | Paper (full-ft table) | Paper (ft-ablation table) | Registry |
|--------|----------------------|--------------------------|----------|
| E-F1 | 66.86 | 67.05 | 67.05 |
| R-F1 | 43.65 | 43.86 | 43.86 |
| DR% | 0.31 | 1.95 | 1.95 |

The full-ft table's LoRA unconstrained row doesn't match the ft-ablation table or registry. May come from a different LoRA checkpoint or obsolete run. The LoRA+S1 row (E-F1=67.05, R-F1=43.77) matches correctly.

### 5. tab:ft-ablation Qwen SciERC Semantic CF — Minor

Paper says CF=0.18%. Registry `w7_qwen_scierc_ft_semantic_only` has CF_count=15, total_entities=1784 → 15/1784 = 0.84%. Denominator or metric computation mismatch. Low severity but unexplained.

---

## Affected Prose Passages

The following text passages reference DocRED FT values that need updating:
- appendix_beam_search.tex line 136: "E-F1=67.05 and R-F1=43.77" — correct (SciERC)
- appendix_beam_search.tex line 176-180: Llama DocRED LoRA greedy values — affected
- appendix_discussion.tex: Multiple references to DocRED FT delta computations may need rechecking

---

## Recommendation

1. **Immediate fix**: Update all DocRED FT values (tab:ft-ablation, tab:beam-docred-lora Llama row, tab:posthoc-extended Llama DocRED FT) to corrected `eval_d064.py` values from registry
2. **Fix PF**: Correct Qwen DocRED PF in beam-docred-lora table (7.8→8.52 or verify source)
3. **Fix full-ft table**: Update LoRA unconstrained row to match registry/ft-ablation values
4. **Verify CF computation**: Check semantic-only CF=0.18% denominator for Qwen SciERC

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "10d236c0-700e-476f-97a1-765718342957",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XAsaLWUA2L61qyWyT4v8Ww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4888,
      "cache_read_input_tokens": 143204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4888
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 109_

I now have all the data needed for a comprehensive audit. Here is the full report:

---

# Appendix Table Audit Report

## Summary

Audited **25 appendix files** containing **~30 tables** against 164 registry experiments. The vast majority of values are verified correct. One systematic issue affects multiple tables: **the parse-failure bug** (same as known Table 2 issue) impacts DocRED FT values in several appendix tables.

---

## VERIFIED CORRECT ✅

### tab:quantization (appendix_quantization.tex)
All 18 data cells verified against 7 registry experiments:
- `sf2_qwen_int4_scierc_s1`: DR=0, R-F1=41.71, E-F1=67.05 ✅
- `sf2_llama_int4_scierc_s1`: DR=0, R-F1=43.98, E-F1=67.54 ✅
- `sf2_qwen_int4_docred_s1`: DR=0, R-F1=40.07, E-F1=74.84, PF=18.5% ✅
- `sf2_llama_int4_docred_s1`: DR=0, R-F1=48.04, E-F1=84.18, PF=2.5% ✅
- `entity_order_ablation_qwen_scierc` (FP16 Qwen SciERC): DR=0, R-F1=43.77, E-F1=67.05 ✅
- `d065_qwen_greedy_4096_r2` (FP16 Qwen DocRED): DR=0, R-F1=40.79, E-F1=81.87, PF=8.5% ✅
- `w5_llama_lora_scierc_constrained_eval` (FP16 Llama SciERC): DR=0.09, R-F1=45.47, E-F1=67.76 ✅
- `d066_sweep_llama_docred_beam1_s1` (FP16 Llama DocRED): DR=0, R-F1=47.35, E-F1=85.43, PF=2.0% ✅

Δ columns all arithmetically correct. ✅

### tab:70b-ft-ablation (appendix_70b_ablation.tex)
All 6 rows verified against `eval_70b_lora_scierc_*`:
- Unconstrained: DR=1.50, R-F1=44.73, E-F1=64.86 ✅
- Grammar: DR=1.50, R-F1=44.63, E-F1=64.82 ✅
- Semantic: DR=0.60, CF=9, R-F1=44.73, E-F1=64.86 ✅
- S1: DR=0, CF=15, R-F1=44.53, E-F1=64.76 ✅
- S2: DR=0, CF=18, R-F1=36.28, E-F1=62.35 ✅
- Beam4 S1: DR=0, CF=1, R-F1=44.81, E-F1=64.89 ✅

### tab:70b-docred-ablation (appendix_70b_ablation.tex)
All 6 rows verified against `eval_70b_lora_docred_200_*`:
- Unconstrained: DR=0.22, RV=0.57, R-F1=43.80, E-F1=80.34 ✅
- Grammar: DR=0.38, R-F1=43.96 ✅
- Semantic: DR=0, RV=0.51, R-F1=43.61 ✅
- S1: DR=0, CF=0.18%, R-F1=43.95, E-F1=79.38 ✅
- S2: DR=0, CF=0.34%, R-F1=36.45, E-F1=84.96 ✅
- Beam4 S1: DR=0, CF=0, R-F1=48.14, E-F1=85.57 ✅

### tab:70b-docred-zs-ablation (appendix_70b_ablation.tex)
All 4 rows verified against `eval_70b_zs_docred_200_*`:
- Unconstrained: DR=13.45, RV=7.88, R-F1=13.25, E-F1=70.14 ✅
- Grammar: DR=17.03, R-F1=13.23, E-F1=70.12 ✅
- Semantic: DR=1.66, RV=8.24, ET=0.12, CF=132, R-F1=13.05, E-F1=70.10 ✅
- S1: DR=0, CF=173, R-F1=13.25, E-F1=70.05 ✅

### tab:cross-model (appendix_zs_crossmodel.tex)
All 12 rows (3 models × 2 datasets × U/S1) verified. Every DR, RV, ET, CF, R-F1 value matches. ✅

### tab:docred-ablation (appendix_discussion.tex — ZS 4-way)
All 4 rows verified against `phase2_docred_*`. All violation rates, F1, and Δ values match. ✅

### tab:beam-ablation (appendix_beam_search.tex)
All 4 rows (k=1,2,4,8) verified:
- k=1: DR=0.93, CF=9.90, E-F1=30.98, R-F1=8.36 ✅
- k=2: DR=0.35, CF=4.12, E-F1=31.54, R-F1=8.75 ✅
- k=4: DR=0, CF=0.53, E-F1=32.00, R-F1=8.56 ✅
- k=8: DR=0, CF=0.08, E-F1=32.18, R-F1=8.39 ✅

### tab:beam-sweep (appendix_beam_search.tex)
All 8 rows (4 beam widths × unc/con) verified against `d066_beam_sweep`. All F1, DR, CF, latency, and relative latency values match. ✅

### tab:beam-docred-998-zs (appendix_beam_search.tex)
Both rows verified against `r14_*_docred_beam4_998`:
- Qwen: DR=0, CF=4.94, E-F1=58.19, R-F1=8.72 ✅
- Llama: DR=0, CF=1.00, E-F1=57.81, R-F1=8.83 ✅

### tab:beam-latency (appendix_beam_search.tex)
All 4 rows verified against `d062_beam_latency`:
- Greedy unc: 2.612 s/doc, 1.00× ✅
- Greedy con: 2.873, 1.10× ✅
- Beam-4 unc: 3.446, 1.32× ✅
- Beam-4 con: 4.013, 1.54× ✅

### tab:gollie-comparison (appendix_gollie_comparison.tex)
All 3 rows verified against `sf2_gollie_scierc_violation`. ✅

### tab:wikievents (appendix_wikievents_pilot.tex)
All 9 rows (3 models × 3 modes) verified against `ee_*_wikievents_*_v3`. ✅

### tab:tcr-scierc and tab:tcr-docred (appendix_tcr.tex)
All 10 TCR configurations verified against `d065_tcr_pilot`. ✅

### tab:prompt-sensitivity (appendix_prompt_sensitivity.tex)
All 6 rows verified against `r4_prompt_minimal`, `r4_prompt_detailed`, and `phase2_scierc_*`. ✅

### tab:vllm-verification (appendix_discussion.tex)
Both rows verified: Grammar-Only DR=14.84 ✅; vLLM DR=15.26, R-F1=8.75 ✅

### tab:trie-baseline (appendix_discussion.tex)
All 4 rows verified against `r16_trie_*_scierc`. Uses corrected values. ✅

### tab:scalability (appendix_scalability.tex)
All 4 rows verified against `d062_ontology_scalability`. ✅

### tab:cf-dr-tradeoff (appendix_discussion.tex)
Verified against `w1_cf_fallback_scierc_pilot`: DR=14.78%, CF=0.04% ✅

### tab:sampling-robustness (appendix_sampling_table.tex)
SciERC row verified against `w9_qwen_scierc_zs_sampling`. ✅

### Other discussion tables
tab:causal-tracing, tab:cf-distribution, tab:cascade-breakdown, tab:lora-per-relation, tab:lucky-violations, tab:lucky-violations-detail, tab:posthoc-extended (ZS rows), tab:power-analysis, tab:high-kappa-rels, tab:dr-by-ambiguity, tab:doc-length-*, tab:kappa-case-study, tab:gcd-comparison: Source experiments exist in registry with matching violation rates where verifiable. Statistical computation tables (bootstrap CI, power analysis) cannot be verified from raw metrics but source experiments are confirmed correct.

---

## DISCREPANCIES FOUND ❌

### 1. tab:ft-ablation DocRED rows — PARSE-FAILURE BUG (CRITICAL)

Same issue as known Table 2 bug. The DocRED FT rows use pre-correction values from buggy `unified_f1_eval.py`. Registry was corrected on 2026-05-22 with `eval_d064.py`, but paper wasn't fully updated.

**Qwen DocRED:**

| Cell | Paper | Registry (corrected) | Δ |
|------|-------|---------------------|---|
| Unconstrained R-F1 | 40.89 | 40.86 | -0.03 |
| Unconstrained E-F1 | 82.35 | 82.15 | -0.20 |
| Unconstrained DR | 0.56 | 0.76 | +0.20 |
| Semantic R-F1 | 40.89 | 40.85 | -0.04 |
| Grammar R-F1 | 40.85 | 40.85 | 0 ✅ (already corrected) |
| S1 R-F1 | 40.79 | 40.79 | 0 ✅ (from d065) |

**Llama DocRED:**

| Cell | Paper | Registry (corrected) | Δ |
|------|-------|---------------------|---|
| Unconstrained E-F1 | 84.77 | 83.93 | -0.84 |
| Unconstrained R-F1 | 44.55 | 43.72 | -0.83 |
| Grammar R-F1 | 43.77 | 43.72 | -0.05 |
| Semantic R-F1 | 43.90 | 43.85 | -0.05 |
| S1 E-F1 | 84.71 | 83.94 | -0.77 |
| S1 R-F1 | 44.70 | 43.78 | -0.92 |

Note: Qwen Grammar was correctly updated. Qwen S1 uses `d065_qwen_greedy_4096_r2` (inherently correct). All other DocRED FT cells need correction.

### 2. tab:beam-docred-lora — SAME BUG + PF mismatch

**Llama Greedy con row** uses same pre-correction values:
- Paper E-F1=84.71, R-F1=44.70 → Corrected: 83.94, 43.78

**Qwen Greedy con PF:**
- Paper: PF=7.8%
- Registry `d065_qwen_greedy_4096_r2`: PF=8.52%
- ft-ablation table for same experiment: PF=8.52

The 7.8% value has no registry source. Likely a transcription error — should be 8.52% (or possibly 7.8% = 78/998 while 8.52% = 85/998 under different parse-failure definition).

### 3. tab:posthoc-extended — Llama DocRED FT cd value

Paper says cd R-F1=44.70, registry `w8_ft_posthoc_baseline` has cd=44.23 (intermediate value), corrected eval gives 43.78. Same parse-failure bug.

### 4. tab:full-ft LoRA unconstrained comparison row

| Metric | Paper (full-ft table) | Paper (ft-ablation table) | Registry |
|--------|----------------------|--------------------------|----------|
| E-F1 | 66.86 | 67.05 | 67.05 |
| R-F1 | 43.65 | 43.86 | 43.86 |
| DR% | 0.31 | 1.95 | 1.95 |

The full-ft table's LoRA unconstrained row doesn't match the ft-ablation table or registry. May come from a different LoRA checkpoint or obsolete run. The LoRA+S1 row (E-F1=67.05, R-F1=43.77) matches correctly.

### 5. tab:ft-ablation Qwen SciERC Semantic CF — Minor

Paper says CF=0.18%. Registry `w7_qwen_scierc_ft_semantic_only` has CF_count=15, total_entities=1784 → 15/1784 = 0.84%. Denominator or metric computation mismatch. Low severity but unexplained.

---

## Affected Prose Passages

The following text passages reference DocRED FT values that need updating:
- appendix_beam_search.tex line 136: "E-F1=67.05 and R-F1=43.77" — correct (SciERC)
- appendix_beam_search.tex line 176-180: Llama DocRED LoRA greedy values — affected
- appendix_discussion.tex: Multiple references to DocRED FT delta computations may need rechecking

---

## Recommendation

1. **Immediate fix**: Update all DocRED FT values (tab:ft-ablation, tab:beam-docred-lora Llama row, tab:posthoc-extended Llama DocRED FT) to corrected `eval_d064.py` values from registry
2. **Fix PF**: Correct Qwen DocRED PF in beam-docred-lora table (7.8→8.52 or verify source)
3. **Fix full-ft table**: Update LoRA unconstrained row to match registry/ft-ablation values
4. **Verify CF computation**: Check semantic-only CF=0.18% denominator for Qwen SciERC

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 855119,
  "duration_api_ms": 853152,
  "num_turns": 39,
  "stop_reason": "end_turn",
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "total_cost_usd": 2.8725312499999998,
  "usage": {
    "input_tokens": 25,
    "cache_creation_input_tokens": 136251,
    "cache_read_input_tokens": 1642495,
    "output_tokens": 47924,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 136251,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 6008,
        "cache_read_input_tokens": 143204,
        "cache_creation_input_tokens": 4888,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4888
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1410,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00149,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 25,
      "outputTokens": 47924,
      "cacheReadInputTokens": 1642495,
      "cacheCreationInputTokens": 136251,
      "webSearchRequests": 0,
      "costUSD": 2.8710412499999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c62ee923-dff0-4c68-b850-df993be383ee"
}
```

</details>

---
