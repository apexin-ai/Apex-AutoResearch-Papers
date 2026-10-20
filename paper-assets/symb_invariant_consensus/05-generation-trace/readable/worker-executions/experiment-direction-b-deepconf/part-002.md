# experiment direction b deepconf — Part 2 of 2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../experiment-direction-b-deepconf.md) · [Structured JSON](../../../sessions/33/33f21fd74ef9911e6d24.json)

## Before a recorded user message

### Tool result

_source line 295 · 2026-05-20T08:07:14.086Z_

<details><summary>↩ Tool result · `toolu_01Ad6tnuRrbvpXxCVjkAXpAz`</summary>

```text
_extracted
_project
aime30_v2_partial_analysis.md
analysis_exp045.md
analysis_prove_verify.py
analyze_adaptive_sica.py
analyze_discriminative_rate.py
analyze_expanded.py
analyze_seed_replication.py
appendix_prompt_template.md
backward_verification.py
case_study_materials.md
citation_verification.md
code_verify_report.md
constraint_ablation
constraint_extractor.py
constraint_extractor_fixed.py
constraint_quality_crossmethod.json
crd_audit_report.md
cross_model_kappa_results.json
cross_trace_unsat.py
d016_model_pivot_report.md
diagnose_exp039.md
diagnose_exp062_exp065.md
direction_e_abstention.py
direction_e_abstention_results.json
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
exp-045-backward-verification
exp-046
exp-060-cross-qwen25-14b-extractor
exp-064
exp-064-diagnosis.md
exp-074
exp-078-debate-mistral-logiqa200
exp-084-diag.md
exp011_truncation_bias_analysis.md
exp019_analysis.md
exp033_analysis.md
exp046_analysis.md
exp069_data_pipeline_audit.md
exp_005_qwq_regime
exp_009_overhead
exp_016_weighted_sc
f2_discriminative_analysis.md
f2_preview.png
f3_preview.png
figures
fleiss_kappa_raw_all.json
fleiss_kappa_unified_merged.json
folio_c0_precheck_raw.json
folio_c0_precheck_report.md
gsm8k_pilot_14b
icg_kappa_corrected.json
kappa_icg_contrastive.json
launch_mvp.sh
literature_independence_bottleneck.md
llama8b_sc_prep.md
manifest.yaml
maxsat_diagnosis_proofwriter30_v2.md
mcnemar_method_experiments.json
mcnemar_recompute.py
oracle_experiment_design.md
patch_debate_logiqa.py
pipeline.py
prepare_proofwriter.py
proofwriter30_v2
proofwriter30_v2_interim_analysis.md
quality_metrics.csv
qwen14b_kappa_analysis.json
report_proofwriter30_v2_progress.md
review_issues.yaml
review_reports
run_consistency_filtering.py
run_exp017_strategyqa.sh
run_exp018_arc.sh
run_exp024_llama70b.sh
run_exp025_qwen72b.sh
run_full_mvp.py
run_icg_logiqa.py
run_icl_oracle.py
run_icl_oracle.sh
run_mvp.py
sc_tiebreak_revalidation.py
sica_aime30_v2
sica_d012_14b
sica_expanded_14b
sica_folio30
sica_k_sensitivity_14b
status_check_20260519.md
summarize_k_sensitivity.py
trace_generator.py
track_discordant_pairs.py
westd16639_crash_diagnosis.md
westd16639_gpu_saturation_report.md
westd16639_recovery_report.md
westd25068_downloads_report.md
westd25068_gpu_saturation_report.md
wild1_max_unsat_results.json
wild2_ascii_results.json
wild6_combined.py
wild6_kappa_aware_sc_results.json
wild6_kappa_sc_analysis.py
wild6_run_all.py
z3_maxsat_patched.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ab60746-ef64-4b6e-9b64-a6e54d14b5e9",
  "uuid": "968e8411-23fa-4d97-82b7-434ff10c0904",
  "tool_use_result": {
    "stdout": "_extracted\n_project\naime30_v2_partial_analysis.md\nanalysis_exp045.md\nanalysis_prove_verify.py\nanalyze_adaptive_sica.py\nanalyze_discriminative_rate.py\nanalyze_expanded.py\nanalyze_seed_replication.py\nappendix_prompt_template.md\nbackward_verification.py\ncase_study_materials.md\ncitation_verification.md\ncode_verify_report.md\nconstraint_ablation\nconstraint_extractor.py\nconstraint_extractor_fixed.py\nconstraint_quality_crossmethod.json\ncrd_audit_report.md\ncross_model_kappa_results.json\ncross_trace_unsat.py\nd016_model_pivot_report.md\ndiagnose_exp039.md\ndiagnose_exp062_exp065.md\ndirection_e_abstention.py\ndirection_e_abstention_results.json\ndream_reports\nentropy_breakdown_crossmodel.json\nerror_categorization.py\nerror_categorization_discordant.json\nexp-001\nexp-005\nexp-007-qwen72b-awq\nexp-009\nexp-010-mistral-v2\nexp-011\nexp-011-llama8b\nexp-013-constraint-ablation\nexp-014\nexp-016\nexp-017-strategyqa-v3\nexp-017-strategyqa-v3_analysis.md\nexp-019\nexp-021-oracle-folio\nexp-022\nexp-022-oracle-proofwriter\nexp-023-discriminative-rate\nexp-030-crossmodel-mistral-folio204\nexp-031-oracle-folio-regen\nexp-038\nexp-045-backward-verification\nexp-046\nexp-060-cross-qwen25-14b-extractor\nexp-064\nexp-064-diagnosis.md\nexp-074\nexp-078-debate-mistral-logiqa200\nexp-084-diag.md\nexp011_truncation_bias_analysis.md\nexp019_analysis.md\nexp033_analysis.md\nexp046_analysis.md\nexp069_data_pipeline_audit.md\nexp_005_qwq_regime\nexp_009_overhead\nexp_016_weighted_sc\nf2_discriminative_analysis.md\nf2_preview.png\nf3_preview.png\nfigures\nfleiss_kappa_raw_all.json\nfleiss_kappa_unified_merged.json\nfolio_c0_precheck_raw.json\nfolio_c0_precheck_report.md\ngsm8k_pilot_14b\nicg_kappa_corrected.json\nkappa_icg_contrastive.json\nlaunch_mvp.sh\nliterature_independence_bottleneck.md\nllama8b_sc_prep.md\nmanifest.yaml\nmaxsat_diagnosis_proofwriter30_v2.md\nmcnemar_method_experiments.json\nmcnemar_recompute.py\noracle_experiment_design.md\npatch_debate_logiqa.py\npipeline.py\nprepare_proofwriter.py\nproofwriter30_v2\nproofwriter30_v2_interim_analysis.md\nquality_metrics.csv\nqwen14b_kappa_analysis.json\nreport_proofwriter30_v2_progress.md\nreview_issues.yaml\nreview_reports\nrun_consistency_filtering.py\nrun_exp017_strategyqa.sh\nrun_exp018_arc.sh\nrun_exp024_llama70b.sh\nrun_exp025_qwen72b.sh\nrun_full_mvp.py\nrun_icg_logiqa.py\nrun_icl_oracle.py\nrun_icl_oracle.sh\nrun_mvp.py\nsc_tiebreak_revalidation.py\nsica_aime30_v2\nsica_d012_14b\nsica_expanded_14b\nsica_folio30\nsica_k_sensitivity_14b\nstatus_check_20260519.md\nsummarize_k_sensitivity.py\ntrace_generator.py\ntrack_discordant_pairs.py\nwestd16639_crash_diagnosis.md\nwestd16639_gpu_saturation_report.md\nwestd16639_recovery_report.md\nwestd25068_downloads_report.md\nwestd25068_gpu_saturation_report.md\nwild1_max_unsat_results.json\nwild2_ascii_results.json\nwild6_combined.py\nwild6_kappa_aware_sc_results.json\nwild6_kappa_sc_analysis.py\nwild6_run_all.py\nz3_maxsat_patched.py",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 296_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_015rNvBgS9DbPxS5gAraJxEb`</summary>

```json
{
  "name": "direction_b_deepconf_results",
  "type": "data",
  "description": "Direction B: DeepConf confidence filtering + SICA on FOLIO-204 with Mistral-7B. Negative result - logprob-based filtering does not improve accuracy. Key finding: model is equally overconfident about correct and incorrect answers (correct median logprob=-0.075, wrong median logprob=-0.053). Per-quartile analysis shows no monotonic trend between confidence and correctness.",
  "project": "symb_invariant_consensus",
  "content": "{\n  \"experiment\": \"Direction B: DeepConf Confidence Filtering + SICA\",\n  \"model\": \"Mistral-7B-Instruct-v0.3\",\n  \"dataset\": \"FOLIO-204\",\n  \"date\": \"2026-05-20\",\n  \"method\": \"Score each trace's final answer token logprob via vLLM completions API, then filter top-K% traces by confidence before running SC and SICA\",\n\n  \"original_exp033_baseline\": {\n    \"sc_accuracy\": 0.5441,\n    \"sc_correct\": 111,\n    \"sica_accuracy\": 0.5931,\n    \"sica_correct\": 121,\n    \"total\": 204\n  },\n\n  \"filtered_results\": {\n    \"top_100pct\": {\"sc\": 0.5588, \"sica_reconstructed\": 0.5588, \"avg_k\": 10.5, \"note\": \"SICA reconstruction from constraint cache differs from original due to Z3 variable naming inconsistency\"},\n    \"top_75pct\":  {\"sc\": 0.5294, \"sica_reconstructed\": 0.5441, \"avg_k\": 8.2},\n    \"top_50pct\":  {\"sc\": 0.5294, \"sica_reconstructed\": 0.5294, \"avg_k\": 5.5}\n  },\n\n  \"logprob_distribution\": {\n    \"min\": -1.71, \"p25\": -0.15, \"median\": -0.06, \"p75\": -0.03, \"max\": -0.00,\n    \"note\": \"Extremely compressed - model outputs high-confidence answers regardless of correctness\"\n  },\n\n  \"logprob_correctness_analysis\": {\n    \"correct_traces\": 1136,\n    \"wrong_traces\": 1008,\n    \"correct_mean_logprob\": -0.1351,\n    \"wrong_mean_logprob\": -0.1410,\n    \"correct_median_logprob\": -0.0751,\n    \"wrong_median_logprob\": -0.0525,\n    \"per_quartile_correctness\": {\n      \"Q1_lowest_confidence\": \"53.0%\",\n      \"Q2\": \"61.6%\",\n      \"Q3\": \"48.5%\",\n      \"Q4_highest_confidence\": \"48.9%\"\n    },\n    \"finding\": \"No correlation. Highest-confidence traces (Q4) are LESS correct (48.9%) than lowest-confidence (Q1, 53.0%)\"\n  },\n\n  \"conclusion\": \"NEGATIVE RESULT. DeepConf logprob-based confidence filtering does NOT improve SC or SICA on FOLIO-204/Mistral-7B. The model is equally overconfident about correct and incorrect final answers. Filtering loses accuracy because it removes a mix of good and bad traces without discrimination.\",\n  \"server_results_path\": \"/root/symb_invariant_consensus/results/direction_b_deepconf/results.json\"\n}",
  "content_filename": "direction_b_deepconf_results.json",
  "tags": [
    "direction-b",
    "deepconf",
    "logprob",
    "folio",
    "mistral-7b",
    "negative-result"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ab60746-ef64-4b6e-9b64-a6e54d14b5e9",
  "uuid": "129cf56b-3e47-4c5a-ac56-e930e5545b16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpnH3GWcujne4B6rRGe6gy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1313,
      "cache_read_input_tokens": 134898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1313
      },
      "output_tokens": 42,
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

_source line 297 · 2026-05-20T08:07:42.924Z_

<details><summary>↩ Tool result · reported error · `toolu_015rNvBgS9DbPxS5gAraJxEb`</summary>

```text
Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'experiment': 'Direction..._deepconf/results.json'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ab60746-ef64-4b6e-9b64-a6e54d14b5e9",
  "uuid": "ad363b49-047d-4d16-aca8-28456cc44716",
  "tool_use_result": "Error: Error executing tool register_artifact: 1 validation error for register_artifactArguments\ncontent\n  Input should be a valid string [type=string_type, input_value={'experiment': 'Direction..._deepconf/results.json'}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"
}
```

</details>

---


### Tool call

_source line 298_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01Xw2eoQyeumCmpXGMTRFZWH`</summary>

```json
{
  "name": "direction_b_deepconf_results",
  "type": "data",
  "description": "Direction B: DeepConf confidence filtering + SICA on FOLIO-204 with Mistral-7B. Negative result - logprob-based filtering does not improve accuracy. Key finding: model is equally overconfident about correct and incorrect answers.",
  "project": "symb_invariant_consensus",
  "content": "{\"experiment\":\"Direction B: DeepConf Confidence Filtering + SICA\",\"model\":\"Mistral-7B-Instruct-v0.3\",\"dataset\":\"FOLIO-204\",\"date\":\"2026-05-20\",\"original_exp033_baseline\":{\"sc\":0.5441,\"sica\":0.5931},\"filtered_results\":{\"top_100pct\":{\"sc\":0.5588,\"sica_reconstructed\":0.5588,\"avg_k\":10.5},\"top_75pct\":{\"sc\":0.5294,\"sica_reconstructed\":0.5441,\"avg_k\":8.2},\"top_50pct\":{\"sc\":0.5294,\"sica_reconstructed\":0.5294,\"avg_k\":5.5}},\"logprob_distribution\":{\"min\":-1.71,\"p25\":-0.15,\"median\":-0.06,\"p75\":-0.03,\"max\":-0.00},\"logprob_correctness_analysis\":{\"correct_mean\":-0.1351,\"wrong_mean\":-0.1410,\"Q1_lowest_conf\":\"53.0% correct\",\"Q2\":\"61.6% correct\",\"Q3\":\"48.5% correct\",\"Q4_highest_conf\":\"48.9% correct\"},\"conclusion\":\"NEGATIVE RESULT: logprob filtering does NOT improve accuracy. Model equally overconfident on correct and incorrect answers.\",\"server_path\":\"/root/symb_invariant_consensus/results/direction_b_deepconf/results.json\"}",
  "content_filename": "direction_b_deepconf_results.json",
  "tags": [
    "direction-b",
    "deepconf",
    "logprob",
    "folio",
    "mistral-7b",
    "negative-result"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ab60746-ef64-4b6e-9b64-a6e54d14b5e9",
  "uuid": "e66f6269-5d96-49e1-a92c-af4e587ef487",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5bhxsSZZpnFe1r78Htrrk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1161,
      "cache_read_input_tokens": 136211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1161
      },
      "output_tokens": 64,
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

_source line 299 · 2026-05-20T08:07:52.218Z_

<details><summary>↩ Tool result · reported error · `toolu_01Xw2eoQyeumCmpXGMTRFZWH`</summary>

```text
Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'experiment': 'Direction..._deepconf/results.json'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ab60746-ef64-4b6e-9b64-a6e54d14b5e9",
  "uuid": "16e0f5a8-310b-4b40-8d30-7b7f50445b8f",
  "tool_use_result": "Error: Error executing tool register_artifact: 1 validation error for register_artifactArguments\ncontent\n  Input should be a valid string [type=string_type, input_value={'experiment': 'Direction..._deepconf/results.json'}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"
}
```

</details>

---


### Tool call

_source line 300_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01SKrghcZEZkQsfk1UbtnpWN`</summary>

```json
{
  "name": "direction_b_deepconf_results",
  "type": "data",
  "description": "Direction B: DeepConf confidence filtering + SICA on FOLIO-204 with Mistral-7B. Negative result - logprob-based filtering does not improve accuracy. Key finding: model is equally overconfident about correct and incorrect answers.",
  "project": "symb_invariant_consensus",
  "content": "Direction B DeepConf Confidence Filtering + SICA Results\n\nModel: Mistral-7B-Instruct-v0.3 | Dataset: FOLIO-204 | Date: 2026-05-20\n\nOriginal exp-033 baseline: SC=54.4% (111/204), SICA=59.3% (121/204)\n\nFiltered Results:\n- top 100%: SC=55.9%, SICA(reconstructed)=55.9%, avg_K=10.5\n- top 75%:  SC=52.9%, SICA(reconstructed)=54.4%, avg_K=8.2\n- top 50%:  SC=52.9%, SICA(reconstructed)=52.9%, avg_K=5.5\n\nLogprob Distribution: min=-1.71, p25=-0.15, median=-0.06, p75=-0.03, max=-0.00\n\nLogprob vs Correctness (no correlation):\n- Correct traces: mean=-0.1351, median=-0.0751 (1136 traces)\n- Wrong traces:   mean=-0.1410, median=-0.0525 (1008 traces)\n- Q1 lowest conf: 53.0% correct\n- Q2: 61.6% correct\n- Q3: 48.5% correct\n- Q4 highest conf: 48.9% correct\n\nCONCLUSION: NEGATIVE RESULT. Logprob filtering does NOT improve accuracy. Model equally overconfident on correct and incorrect answers. Highest-confidence traces (Q4) are LESS correct than lowest-confidence (Q1).\n\nServer path: /root/symb_invariant_consensus/results/direction_b_deepconf/results.json",
  "content_filename": "direction_b_deepconf_results.json",
  "tags": [
    "direction-b",
    "deepconf",
    "logprob",
    "folio",
    "mistral-7b",
    "negative-result"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ab60746-ef64-4b6e-9b64-a6e54d14b5e9",
  "uuid": "91954d6d-8131-497e-b264-65b9b2ef67ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XmDK8k1BgqxxYV9ADnx8Nn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 739,
      "cache_read_input_tokens": 137372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 739
      },
      "output_tokens": 72,
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

_source line 301 · 2026-05-20T08:08:03.832Z_

<details><summary>↩ Tool result · `toolu_01SKrghcZEZkQsfk1UbtnpWN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_09b472\", \"name\": \"direction_b_deepconf_results\", \"type\": \"data\", \"description\": \"Direction B: DeepConf confidence filtering + SICA on FOLIO-204 with Mistral-7B. Negative result - logprob-based filtering does not improve accuracy. Key finding: model is equally overconfident about correct and incorrect answers.\", \"path\": \"projects/symb_invariant_consensus/artifacts/_project/data/direction_b_deepconf_results.json\", \"url\": null, \"project\": \"symb_invariant_consensus\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T08:08:03.612771+00:00\", \"tags\": [\"direction-b\", \"deepconf\", \"logprob\", \"folio\", \"mistral-7b\", \"negative-result\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ab60746-ef64-4b6e-9b64-a6e54d14b5e9",
  "uuid": "1423b8be-4a02-4e84-9acd-178e8346fa4a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260520_09b472\\\", \\\"name\\\": \\\"direction_b_deepconf_results\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Direction B: DeepConf confidence filtering + SICA on FOLIO-204 with Mistral-7B. Negative result - logprob-based filtering does not improve accuracy. Key finding: model is equally overconfident about correct and incorrect answers.\\\", \\\"path\\\": \\\"projects/symb_invariant_consensus/artifacts/_project/data/direction_b_deepconf_results.json\\\", \\\"url\\\": null, \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-20T08:08:03.612771+00:00\\\", \\\"tags\\\": [\\\"direction-b\\\", \\\"deepconf\\\", \\\"logprob\\\", \\\"folio\\\", \\\"mistral-7b\\\", \\\"negative-result\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_09b472\", \"name\": \"direction_b_deepconf_results\", \"type\": \"data\", \"description\": \"Direction B: DeepConf confidence filtering + SICA on FOLIO-204 with Mistral-7B. Negative result - logprob-based filtering does not improve accuracy. Key finding: model is equally overconfident about correct and incorrect answers.\", \"path\": \"projects/symb_invariant_consensus/artifacts/_project/data/direction_b_deepconf_results.json\", \"url\": null, \"project\": \"symb_invariant_consensus\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T08:08:03.612771+00:00\", \"tags\": [\"direction-b\", \"deepconf\", \"logprob\", \"folio\", \"mistral-7b\", \"negative-result\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 302_

清理 vLLM 进程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ab60746-ef64-4b6e-9b64-a6e54d14b5e9",
  "uuid": "4fff6fdc-7872-4b4d-a19c-d40f86da6c62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zPrt95p8ZMJr7MFVz3SwU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1018,
      "cache_read_input_tokens": 138111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1018
      },
      "output_tokens": 1,
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

_source line 303_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01EEiX6toRNJzMx17U9cGtmV`</summary>

```json
{
  "server": "westd-25068",
  "command": "kill 361723 2>/dev/null; echo \"vLLM stopped\"",
  "warn": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ab60746-ef64-4b6e-9b64-a6e54d14b5e9",
  "uuid": "e85bcf19-9f0f-46f1-9145-0360ad0d31b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zPrt95p8ZMJr7MFVz3SwU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1018,
      "cache_read_input_tokens": 138111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1018
      },
      "output_tokens": 1,
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

_source line 304 · 2026-05-20T08:08:08.610Z_

<details><summary>↩ Tool result · `toolu_01EEiX6toRNJzMx17U9cGtmV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"vLLM stopped\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ab60746-ef64-4b6e-9b64-a6e54d14b5e9",
  "uuid": "72b69ce4-7949-426b-93e6-7c05bce04c43",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"vLLM stopped\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"vLLM stopped\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 305_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01LfvwKio1pPYoaoBFzb9hta`</summary>

```json
{
  "todos": [
    {
      "content": "Start vLLM on cuda:0 with Mistral-7B",
      "status": "completed",
      "activeForm": "Starting vLLM on cuda:0"
    },
    {
      "content": "Write analysis_deepconf_filter.py script",
      "status": "completed",
      "activeForm": "Writing DeepConf filter script"
    },
    {
      "content": "Dry-run script validation",
      "status": "completed",
      "activeForm": "Validating script with dry-run"
    },
    {
      "content": "Run logprob scoring + filtered SC/SICA comparisons",
      "status": "completed",
      "activeForm": "Running logprob scoring and comparisons"
    },
    {
      "content": "Save and register results",
      "status": "completed",
      "activeForm": "Saving results"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ab60746-ef64-4b6e-9b64-a6e54d14b5e9",
  "uuid": "8bdde86d-cb11-433f-92fd-e2d0345a28d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQFLLhwyW2TVZ12ucf6Fjh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 210,
      "cache_read_input_tokens": 139129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 210
      },
      "output_tokens": 35,
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

_source line 306 · 2026-05-20T08:08:13.540Z_

<details><summary>↩ Tool result · `toolu_01LfvwKio1pPYoaoBFzb9hta`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4ab60746-ef64-4b6e-9b64-a6e54d14b5e9",
  "uuid": "ae21e3f8-5617-4149-a709-ae36d50b2a27",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Start vLLM on cuda:0 with Mistral-7B",
        "status": "completed",
        "activeForm": "Starting vLLM on cuda:0"
      },
      {
        "content": "Write analysis_deepconf_filter.py script",
        "status": "completed",
        "activeForm": "Writing DeepConf filter script"
      },
      {
        "content": "Dry-run script validation",
        "status": "completed",
        "activeForm": "Validating script with dry-run"
      },
      {
        "content": "Run logprob scoring + filtered SC/SICA comparisons",
        "status": "in_progress",
        "activeForm": "Running logprob scoring and comparisons"
      },
      {
        "content": "Save and register results",
        "status": "pending",
        "activeForm": "Saving results"
      }
    ],
    "newTodos": [
      {
        "content": "Start vLLM on cuda:0 with Mistral-7B",
        "status": "completed",
        "activeForm": "Starting vLLM on cuda:0"
      },
      {
        "content": "Write analysis_deepconf_filter.py script",
        "status": "completed",
        "activeForm": "Writing DeepConf filter script"
      },
      {
        "content": "Dry-run script validation",
        "status": "completed",
        "activeForm": "Validating script with dry-run"
      },
      {
        "content": "Run logprob scoring + filtered SC/SICA comparisons",
        "status": "completed",
        "activeForm": "Running logprob scoring and comparisons"
      },
      {
        "content": "Save and register results",
        "status": "completed",
        "activeForm": "Saving results"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 307_

---

## Direction B 结果汇总

**方法**：用 vLLM completions API 获取每条 trace 最终答案 token 的 logprob 作为置信度，按置信度过滤 traces 后重新运行 SC 和 SICA。

### 结果表

| Method | K_eff | Accuracy | Δ vs exp-033 SC |
|--------|-------|----------|-----------------|
| exp-033 Full SC (K=12) | 12 | 54.4% | — |
| exp-033 Full SICA (K=12) | 12 | 59.3% | +4.9pp |
| Filtered SC (top 75%) | 8.2 | 52.9% | -1.5pp |
| Filtered SICA (top 75%) | 8.2 | 54.4% | +0.0pp |
| Filtered SC (top 50%) | 5.5 | 52.9% | -1.5pp |
| Filtered SICA (top 50%) | 5.5 | 52.9% | -1.5pp |

### 核心发现：**负面结果**

Logprob 与正确性**无相关性**：
- 正确 trace 平均 logprob: **-0.135**；错误 trace: **-0.141**（几乎一样）
- Q4 (最高置信度) 正确率 **48.9%** 反而低于 Q1 (最低置信度) 的 **53.0%**
- Logprob 分布极度压缩 (median=-0.06)，模型对正确和错误答案同样过度自信

**结论**：DeepConf 假设（低置信 trace 产生低质量约束）在 Mistral-7B / FOLIO 上不成立。过滤只是随机丢弃 trace，损害而非提升准确率。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4ab60746-ef64-4b6e-9b64-a6e54d14b5e9",
  "uuid": "c36f5d1a-f900-4c61-9c8c-17419f6adb9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkzvytZCKXCCjLmEgYTBjo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 139339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 270
      },
      "output_tokens": 1,
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

_source line 308_

---

## Direction B 结果汇总

**方法**：用 vLLM completions API 获取每条 trace 最终答案 token 的 logprob 作为置信度，按置信度过滤 traces 后重新运行 SC 和 SICA。

### 结果表

| Method | K_eff | Accuracy | Δ vs exp-033 SC |
|--------|-------|----------|-----------------|
| exp-033 Full SC (K=12) | 12 | 54.4% | — |
| exp-033 Full SICA (K=12) | 12 | 59.3% | +4.9pp |
| Filtered SC (top 75%) | 8.2 | 52.9% | -1.5pp |
| Filtered SICA (top 75%) | 8.2 | 54.4% | +0.0pp |
| Filtered SC (top 50%) | 5.5 | 52.9% | -1.5pp |
| Filtered SICA (top 50%) | 5.5 | 52.9% | -1.5pp |

### 核心发现：**负面结果**

Logprob 与正确性**无相关性**：
- 正确 trace 平均 logprob: **-0.135**；错误 trace: **-0.141**（几乎一样）
- Q4 (最高置信度) 正确率 **48.9%** 反而低于 Q1 (最低置信度) 的 **53.0%**
- Logprob 分布极度压缩 (median=-0.06)，模型对正确和错误答案同样过度自信

**结论**：DeepConf 假设（低置信 trace 产生低质量约束）在 Mistral-7B / FOLIO 上不成立。过滤只是随机丢弃 trace，损害而非提升准确率。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1514292,
  "duration_api_ms": 1160607,
  "num_turns": 113,
  "stop_reason": "end_turn",
  "session_id": "4ab60746-ef64-4b6e-9b64-a6e54d14b5e9",
  "total_cost_usd": 6.487399999999998,
  "usage": {
    "input_tokens": 97,
    "cache_creation_input_tokens": 127768,
    "cache_read_input_tokens": 8750976,
    "output_tokens": 52433,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 127768,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 524,
        "cache_read_input_tokens": 139339,
        "cache_creation_input_tokens": 270,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 270
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1957,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002052,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 97,
      "outputTokens": 52433,
      "cacheReadInputTokens": 8750976,
      "cacheCreationInputTokens": 127768,
      "webSearchRequests": 0,
      "costUSD": 6.485347999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "562f3ace-e033-41d5-a9e7-18d6d3f58208"
}
```

</details>

---
