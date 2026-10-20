# Research conversation: <project_context> # 项目: schema_semantic_constrained_ie ## 运行环境 - 服务器名: westd-16980 - SSH 连接命令: ssh connect.westd.seetacl — Part 2 of 2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-project-context-schema-semantic-constrained-ie-westd-16980-ssh-ssh-connect-wes-copy-35.md) · [Structured JSON](../../../sessions/06/06ef9009bb27e84b5e26.json)

## Round 1

### Tool result

_source line 160 · 2026-05-17T11:09:48.560Z_

<details><summary>↩ Tool result · `toolu_01PcmA46wY15y1vZwXzJsL3X`</summary>

```text
_project
analyze_ontology_docred.py
appendix_sampling_table.tex
beam_sampling_feasibility.md
cf_fallback_code_diff_analysis.md
compare_prompts.py
composability_update_checklist.md
composability_update_template.md
constrained_eval_readiness.md
cross_model_analysis_framework.md
d009_llama_prep.md
data_consistency_audit.md
docred_full_s1_dr_root_cause_analysis.md
docred_lora_eval_commands.md
docred_paper_update_checklist.md
docred_phase2_ablation_analysis.md
docred_progress_check.md
docred_unconstrained_baseline_verify.md
dream_reports
dual_factor_analysis
ft_ablation_analysis.md
fuzzy_matching_threshold_analysis.md
impact_analysis.py
latency_profiling_docred_qwen_ft.json
literature_docred_compare.md
literature_map.yaml
literature_survey_constrained_decoding_ie.md
literature_survey_ontology_constrained_ie.md
llama_docred_full_s1
llama_docred_full_s1_mt6144
llama_docred_maxtoken
llama_docred_per_relation_dr_analysis.md
llama_docred_unconstrained_mt6144
llama_submit_commands.md
manifest.yaml
method_invariant_notes.md
mistral_tightness_r2_analysis.md
oov_replacement_cases.md
pair_based_enforcement_plan.md
paper_number_consistency_check.md
paper_number_preaudit.md
paper_results_summary.md
paper_results_tables.md
paper_writing_readiness.md
parse_failure_denominator_analysis.md
phase2_docred_full_s1
phase2_docred_semantic_only
r4_m6q4_cfdr_transferability.md
r4_sf1_matched_greedy_results.md
r4_sf5_sf7_results.md
r4_sf8_reproducibility.md
rebuttal
rebuttal_draft_v1.md
rebuttal_draft_v2.md
reference_audit_relwork.md
reference_audit_results.md
related_work_survey.md
residual_dr_error_analysis.md
review_issues.yaml
review_reports
run_constrained_extraction.py
run_extraction_docred.py
runtime_benchmark.json
table2_main_results.md
table3_composability.md
table4_ft_ablation.md
table5_posthoc.md
table6_latency.md
tightness_ablation
unified_et_dr_recalc.md
violation_checker_docred.py
w1_cf_fallback
w1_cf_fallback_pilot_detailed_analysis.md
w1_cf_fallback_scierc_pilot
w4_table1_v2
w5_docred_sft_data_gen
w5_llama_docred_lora_constrained_eval.md
w5_llama_docred_lora_training
w5_llama_lora_scierc_constrained_eval
w5_lora_scierc_training
w6_mistral_docred_constrained
w7_qwen_grammar_only_failure_diagnosis.md
w8_ft_posthoc_baseline
w9_docred_sampling_subset_analysis.md
w9_qwen_scierc_zs_sampling
w9_scierc_sampling_analysis.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cedb965-c70f-44cd-98d4-dfd28de192fd",
  "isSidechain": false,
  "promptId": "cef9a42d-b888-429a-a83a-1ec5f041c71f",
  "type": "user",
  "uuid": "8ddbb427-4167-45a6-932c-eaa6b4759445",
  "toolUseResult": {
    "stdout": "_project\nanalyze_ontology_docred.py\nappendix_sampling_table.tex\nbeam_sampling_feasibility.md\ncf_fallback_code_diff_analysis.md\ncompare_prompts.py\ncomposability_update_checklist.md\ncomposability_update_template.md\nconstrained_eval_readiness.md\ncross_model_analysis_framework.md\nd009_llama_prep.md\ndata_consistency_audit.md\ndocred_full_s1_dr_root_cause_analysis.md\ndocred_lora_eval_commands.md\ndocred_paper_update_checklist.md\ndocred_phase2_ablation_analysis.md\ndocred_progress_check.md\ndocred_unconstrained_baseline_verify.md\ndream_reports\ndual_factor_analysis\nft_ablation_analysis.md\nfuzzy_matching_threshold_analysis.md\nimpact_analysis.py\nlatency_profiling_docred_qwen_ft.json\nliterature_docred_compare.md\nliterature_map.yaml\nliterature_survey_constrained_decoding_ie.md\nliterature_survey_ontology_constrained_ie.md\nllama_docred_full_s1\nllama_docred_full_s1_mt6144\nllama_docred_maxtoken\nllama_docred_per_relation_dr_analysis.md\nllama_docred_unconstrained_mt6144\nllama_submit_commands.md\nmanifest.yaml\nmethod_invariant_notes.md\nmistral_tightness_r2_analysis.md\noov_replacement_cases.md\npair_based_enforcement_plan.md\npaper_number_consistency_check.md\npaper_number_preaudit.md\npaper_results_summary.md\npaper_results_tables.md\npaper_writing_readiness.md\nparse_failure_denominator_analysis.md\nphase2_docred_full_s1\nphase2_docred_semantic_only\nr4_m6q4_cfdr_transferability.md\nr4_sf1_matched_greedy_results.md\nr4_sf5_sf7_results.md\nr4_sf8_reproducibility.md\nrebuttal\nrebuttal_draft_v1.md\nrebuttal_draft_v2.md\nreference_audit_relwork.md\nreference_audit_results.md\nrelated_work_survey.md\nresidual_dr_error_analysis.md\nreview_issues.yaml\nreview_reports\nrun_constrained_extraction.py\nrun_extraction_docred.py\nruntime_benchmark.json\ntable2_main_results.md\ntable3_composability.md\ntable4_ft_ablation.md\ntable5_posthoc.md\ntable6_latency.md\ntightness_ablation\nunified_et_dr_recalc.md\nviolation_checker_docred.py\nw1_cf_fallback\nw1_cf_fallback_pilot_detailed_analysis.md\nw1_cf_fallback_scierc_pilot\nw4_table1_v2\nw5_docred_sft_data_gen\nw5_llama_docred_lora_constrained_eval.md\nw5_llama_docred_lora_training\nw5_llama_lora_scierc_constrained_eval\nw5_lora_scierc_training\nw6_mistral_docred_constrained\nw7_qwen_grammar_only_failure_diagnosis.md\nw8_ft_posthoc_baseline\nw9_docred_sampling_subset_analysis.md\nw9_qwen_scierc_zs_sampling\nw9_scierc_sampling_analysis.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1cedb965-c70f-44cd-98d4-dfd28de192fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "3e9ce29d-87c3-49f7-ac0f-6c69e795da79",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 161 · 2026-05-17T11:10:30.270Z_

<details open><summary>🔧 Tool call — Write · `toolu_016A3cyouKM5f7rCFcSt785J`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/r4_m3q3_semantic_et_analysis.md",
  "content": "# M3+Q3: Why Semantic-only Increases DocRED ET by +70%\n\n## 1. The Numbers\n\n| Dataset | Mode | ET violations | Total entities | ET rate |\n|---------|------|--------------|----------------|---------|\n| DocRED | Unconstrained | 500 | 20,171 | 2.48% |\n| DocRED | Semantic-only | 851 | 20,185 | 4.22% |\n| SciERC | Unconstrained | 10 | 2,474 | 0.40% |\n| SciERC | Semantic-only | 10 | 2,474 | 0.40% |\n\nDocRED semantic-only: +351 extra ET violations (+70%). SciERC: unchanged.\n\n## 2. Where the Extra Violations Come From\n\nDecomposing DocRED ET violations by source:\n\n| Mode | Entity-list violations | Relation head/tail_type violations | Total |\n|------|----------------------|-----------------------------------|-------|\n| Unconstrained | 496 | 4 | 500 |\n| Semantic-only | 496 | 355 | 851 |\n\nThe entity list is **identical** between the two modes (same 496 OOV types: EVENT=261, WORK=121, ETHNIC_GROUP=64, etc.). All 355 extra violations come from relation `head_type`/`tail_type` fields.\n\nTop OOV types appearing only in semantic-only relation fields:\n- `ORGB` (57), `OR` (48): truncated/garbled versions of \"ORG\"\n- `EVENT` (55), `WORK` (55): model-invented types\n- `ENTITY_TYPE` (22): literal string, model confused about what to generate\n- `GENRE` (20), `JOB` (17), `MSC` (12): novel OOV types\n\n## 3. Root Cause: D/R Mask Without Grammar Creates OOV Escape Path\n\n### 3.1 How `_apply_type_mask` works (type_mask_processor.py:357-369)\n\n```python\ndef _apply_type_mask(self, logits, allowed_types):\n    disallowed_first_tokens = [\n        tid for etype, tid in self._type_first_token.items()\n        if etype not in allowed_types\n    ]\n    if disallowed_first_tokens:\n        logits[disallowed_first_tokens] = float(\"-inf\")\n    return logits\n```\n\nThis only masks the first tokens of **disallowed entity types** (6 tokens total for DocRED). The remaining ~150k vocabulary tokens are untouched. In `full_s1` mode, XGrammar's enum constraint guarantees the output is one of the 6 valid types. Without grammar (semantic-only), the model can escape to any of the ~150k unmasked tokens.\n\n### 3.2 The failure path in semantic-only mode\n\n1. Model generates a relation and reaches the `head_type` field\n2. `_mask_head_type` looks up D/R constraints for the current relation type\n3. D/R mask blocks certain entity type first tokens (e.g., blocks PER, TIME, NUM for relation P131)\n4. Without XGrammar, the model is free to pick any non-entity-type token\n5. Model generates OOV strings like \"ORGB\", \"GENRE\", \"JOB\" instead of a valid type\n\n### 3.3 Why the entity list is unaffected\n\nAt entity type position, `_mask_entity_type` allows **all** entity types:\n```python\ndef _mask_entity_type(self, logits):\n    return self._apply_type_mask(logits, set(self.spec.entity_types))\n```\nSince all types are allowed, no tokens are blocked, and the function is a no-op. Entity-list types are generated identically to unconstrained mode.\n\n## 4. Why SciERC is Unaffected: Zero Type-Level Blocking\n\n### 4.1 Constraint space geometry\n\n| Metric | SciERC | DocRED |\n|--------|--------|--------|\n| Entity types | 6 | 6 |\n| Relation types | 7 | 96 |\n| Avg valid pairs per relation | 24.0/36 (66.7%) | 5.7/36 (15.8%) |\n| **Max type-level head blocking** | **0%** | **92% (NUM)** |\n| **Max type-level tail blocking** | **0%** | **96% (NUM)** |\n\n### 4.2 Type-level blocking comparison\n\n**SciERC**: Every entity type appears as a valid head and valid tail for **every** relation (0% blocking for all 6 types across all 7 relations). The D/R mask at head_type/tail_type positions is always a no-op because `valid_head_types()` and `valid_tail_types()` always return all 6 types.\n\n**DocRED**: Entity types are frequently blocked:\n- NUM: blocked as head in 92/96 relations (92%), as tail in 96%\n- TIME: blocked as head in 88%, tail in 83%\n- PER: blocked as head in 27%, tail in 55%\n- ORG/LOC/MISC: blocked as head in 20-24%, tail in 31-42%\n\nWith 96 relations and high blocking rates, there are many opportunities for the model to be forced away from the correct entity type and escape to an OOV string.\n\n### 4.3 Summary\n\nSciERC's constraint structure is **pair-restrictive but type-permissive**: individual (head_type, tail_type) pairs are constrained (66.7% valid), but no entity type is ever completely excluded from any relation's head or tail position. The D/R mask operates at the **type level** (blocking first tokens), not the pair level, so it has nothing to block.\n\nDocRED's constraint structure is **type-restrictive**: many entity types are entirely excluded from many relations' head/tail positions. The D/R mask actively blocks entity type tokens, and without grammar to contain the output within the enum, the model escapes to OOV types.\n\n## 5. Suggested Paper Text\n\n> In semantic-only mode, the domain/range mask blocks specific entity-type tokens at head\\_type and tail\\_type positions but cannot prevent the model from generating out-of-vocabulary types, as no grammar layer constrains the output to the type enum. On DocRED, where 84% of (relation, entity-type) combinations are blocked by domain/range rules, this creates frequent \"escape paths\" to OOV types, accounting for the +70% ET increase. On SciERC, every entity type is a valid head and tail for every relation, so the mask is never triggered and ET remains unchanged.\n\n## 6. Verification Details\n\n### Data sources\n- DocRED unconstrained: `outputs/docred_unconstrained.jsonl`\n- DocRED semantic-only: `outputs/docred_semantic_only.jsonl`\n- Violation reports: `outputs/violation_report_docred_{unconstrained,semantic_only}_v2.json`\n- Constraint files: `data/docred/ontology_constraints_docred.json`, `ontology_constraints.json`\n\n### Code references\n- `_apply_type_mask`: `compiler/type_mask_processor.py:357-369`\n- `_mask_entity_type`: `compiler/type_mask_processor.py:288-296`\n- `_mask_head_type`: `compiler/type_mask_processor.py:298-319`\n- `PositionDetector.detect`: `compiler/type_mask_processor.py:120-173`\n- Semantic-only processor stack: `run_constrained_extraction.py:435-437`\n- ET violation counting (DocRED v2): `violation_checker_docred.py:109-154` (counts unique (text, type) from both entity list and relation head/tail fields)\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ddbb427-4167-45a6-932c-eaa6b4759445",
  "isSidechain": false,
  "requestId": "req_011Cb839An6VdGDBaof2CmKu",
  "type": "assistant",
  "uuid": "04be403f-3fb8-421d-8740-5357f51b4007",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "3e9ce29d-87c3-49f7-ac0f-6c69e795da79",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Epz6pJymrgMPrY6WLdxZtg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2467,
      "cache_read_input_tokens": 113117,
      "output_tokens": 2046,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2467,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2046,
          "cache_read_input_tokens": 113117,
          "cache_creation_input_tokens": 2467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2467
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 162 · 2026-05-17T11:10:30.305Z_

<details><summary>↩ Tool result · `toolu_016A3cyouKM5f7rCFcSt785J`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/r4_m3q3_semantic_et_analysis.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "04be403f-3fb8-421d-8740-5357f51b4007",
  "isSidechain": false,
  "promptId": "cef9a42d-b888-429a-a83a-1ec5f041c71f",
  "type": "user",
  "uuid": "72c62582-53f0-446a-bc16-1b192023346c",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/r4_m3q3_semantic_et_analysis.md",
    "content": "# M3+Q3: Why Semantic-only Increases DocRED ET by +70%\n\n## 1. The Numbers\n\n| Dataset | Mode | ET violations | Total entities | ET rate |\n|---------|------|--------------|----------------|---------|\n| DocRED | Unconstrained | 500 | 20,171 | 2.48% |\n| DocRED | Semantic-only | 851 | 20,185 | 4.22% |\n| SciERC | Unconstrained | 10 | 2,474 | 0.40% |\n| SciERC | Semantic-only | 10 | 2,474 | 0.40% |\n\nDocRED semantic-only: +351 extra ET violations (+70%). SciERC: unchanged.\n\n## 2. Where the Extra Violations Come From\n\nDecomposing DocRED ET violations by source:\n\n| Mode | Entity-list violations | Relation head/tail_type violations | Total |\n|------|----------------------|-----------------------------------|-------|\n| Unconstrained | 496 | 4 | 500 |\n| Semantic-only | 496 | 355 | 851 |\n\nThe entity list is **identical** between the two modes (same 496 OOV types: EVENT=261, WORK=121, ETHNIC_GROUP=64, etc.). All 355 extra violations come from relation `head_type`/`tail_type` fields.\n\nTop OOV types appearing only in semantic-only relation fields:\n- `ORGB` (57), `OR` (48): truncated/garbled versions of \"ORG\"\n- `EVENT` (55), `WORK` (55): model-invented types\n- `ENTITY_TYPE` (22): literal string, model confused about what to generate\n- `GENRE` (20), `JOB` (17), `MSC` (12): novel OOV types\n\n## 3. Root Cause: D/R Mask Without Grammar Creates OOV Escape Path\n\n### 3.1 How `_apply_type_mask` works (type_mask_processor.py:357-369)\n\n```python\ndef _apply_type_mask(self, logits, allowed_types):\n    disallowed_first_tokens = [\n        tid for etype, tid in self._type_first_token.items()\n        if etype not in allowed_types\n    ]\n    if disallowed_first_tokens:\n        logits[disallowed_first_tokens] = float(\"-inf\")\n    return logits\n```\n\nThis only masks the first tokens of **disallowed entity types** (6 tokens total for DocRED). The remaining ~150k vocabulary tokens are untouched. In `full_s1` mode, XGrammar's enum constraint guarantees the output is one of the 6 valid types. Without grammar (semantic-only), the model can escape to any of the ~150k unmasked tokens.\n\n### 3.2 The failure path in semantic-only mode\n\n1. Model generates a relation and reaches the `head_type` field\n2. `_mask_head_type` looks up D/R constraints for the current relation type\n3. D/R mask blocks certain entity type first tokens (e.g., blocks PER, TIME, NUM for relation P131)\n4. Without XGrammar, the model is free to pick any non-entity-type token\n5. Model generates OOV strings like \"ORGB\", \"GENRE\", \"JOB\" instead of a valid type\n\n### 3.3 Why the entity list is unaffected\n\nAt entity type position, `_mask_entity_type` allows **all** entity types:\n```python\ndef _mask_entity_type(self, logits):\n    return self._apply_type_mask(logits, set(self.spec.entity_types))\n```\nSince all types are allowed, no tokens are blocked, and the function is a no-op. Entity-list types are generated identically to unconstrained mode.\n\n## 4. Why SciERC is Unaffected: Zero Type-Level Blocking\n\n### 4.1 Constraint space geometry\n\n| Metric | SciERC | DocRED |\n|--------|--------|--------|\n| Entity types | 6 | 6 |\n| Relation types | 7 | 96 |\n| Avg valid pairs per relation | 24.0/36 (66.7%) | 5.7/36 (15.8%) |\n| **Max type-level head blocking** | **0%** | **92% (NUM)** |\n| **Max type-level tail blocking** | **0%** | **96% (NUM)** |\n\n### 4.2 Type-level blocking comparison\n\n**SciERC**: Every entity type appears as a valid head and valid tail for **every** relation (0% blocking for all 6 types across all 7 relations). The D/R mask at head_type/tail_type positions is always a no-op because `valid_head_types()` and `valid_tail_types()` always return all 6 types.\n\n**DocRED**: Entity types are frequently blocked:\n- NUM: blocked as head in 92/96 relations (92%), as tail in 96%\n- TIME: blocked as head in 88%, tail in 83%\n- PER: blocked as head in 27%, tail in 55%\n- ORG/LOC/MISC: blocked as head in 20-24%, tail in 31-42%\n\nWith 96 relations and high blocking rates, there are many opportunities for the model to be forced away from the correct entity type and escape to an OOV string.\n\n### 4.3 Summary\n\nSciERC's constraint structure is **pair-restrictive but type-permissive**: individual (head_type, tail_type) pairs are constrained (66.7% valid), but no entity type is ever completely excluded from any relation's head or tail position. The D/R mask operates at the **type level** (blocking first tokens), not the pair level, so it has nothing to block.\n\nDocRED's constraint structure is **type-restrictive**: many entity types are entirely excluded from many relations' head/tail positions. The D/R mask actively blocks entity type tokens, and without grammar to contain the output within the enum, the model escapes to OOV types.\n\n## 5. Suggested Paper Text\n\n> In semantic-only mode, the domain/range mask blocks specific entity-type tokens at head\\_type and tail\\_type positions but cannot prevent the model from generating out-of-vocabulary types, as no grammar layer constrains the output to the type enum. On DocRED, where 84% of (relation, entity-type) combinations are blocked by domain/range rules, this creates frequent \"escape paths\" to OOV types, accounting for the +70% ET increase. On SciERC, every entity type is a valid head and tail for every relation, so the mask is never triggered and ET remains unchanged.\n\n## 6. Verification Details\n\n### Data sources\n- DocRED unconstrained: `outputs/docred_unconstrained.jsonl`\n- DocRED semantic-only: `outputs/docred_semantic_only.jsonl`\n- Violation reports: `outputs/violation_report_docred_{unconstrained,semantic_only}_v2.json`\n- Constraint files: `data/docred/ontology_constraints_docred.json`, `ontology_constraints.json`\n\n### Code references\n- `_apply_type_mask`: `compiler/type_mask_processor.py:357-369`\n- `_mask_entity_type`: `compiler/type_mask_processor.py:288-296`\n- `_mask_head_type`: `compiler/type_mask_processor.py:298-319`\n- `PositionDetector.detect`: `compiler/type_mask_processor.py:120-173`\n- Semantic-only processor stack: `run_constrained_extraction.py:435-437`\n- ET violation counting (DocRED v2): `violation_checker_docred.py:109-154` (counts unique (text, type) from both entity list and relation head/tail fields)\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "04be403f-3fb8-421d-8740-5357f51b4007",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "3e9ce29d-87c3-49f7-ac0f-6c69e795da79",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---


### Runtime record

_source line 163_

```json
{
  "type": "last-prompt",
  "leafUuid": "72c62582-53f0-446a-bc16-1b192023346c",
  "sessionId": "3e9ce29d-87c3-49f7-ac0f-6c69e795da79"
}
```

---


### Runtime record

_source line 164_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze semantic-only DocRED ET increase mechanism",
  "sessionId": "3e9ce29d-87c3-49f7-ac0f-6c69e795da79"
}
```

---


### Assistant

_source line 165 · 2026-05-17T11:10:39.282Z_

分析完成。写入 `artifacts/r4_m3q3_semantic_et_analysis.md`。

核心发现：

1. **851 中的 355 个额外 ET 违规全部来自 relation 的 head_type/tail_type 字段**，entity list 的违规数量（496）与 unconstrained 完全一致。

2. **机制**：`_apply_type_mask` 只屏蔽 6 个 entity type 的 first token，剩余 ~150k vocab token 不受影响。在 full_s1 中 XGrammar 的 enum 约束保证输出只能是合法类型；semantic-only 没有 grammar 层，模型在被 D/R mask 屏蔽掉正确 type token 后会逃逸到 OOV 类型（如 "ORGB"=57, "OR"=48, "EVENT"=55）。

3. **SciERC 不受影响的原因**：SciERC 每个 entity type 在所有 7 个 relation 中都是合法的 head 和 tail（type-level blocking = 0%），D/R mask 从未真正屏蔽任何 token。DocRED 则相反：NUM 在 92% 的 relation 中被屏蔽，TIME 在 88% 中被屏蔽——高屏蔽率 + 无 grammar = 频繁 OOV 逃逸。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72c62582-53f0-446a-bc16-1b192023346c",
  "isSidechain": false,
  "requestId": "req_011Cb83CEgKzY4TxywFYrNF4",
  "type": "assistant",
  "uuid": "f360e3d3-e5ec-4ee5-b171-c39213fb0f04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "3e9ce29d-87c3-49f7-ac0f-6c69e795da79",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8Taqk9rDLsn7R1Xy4nMAS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2111,
      "cache_read_input_tokens": 115584,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2111,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 404,
          "cache_read_input_tokens": 115584,
          "cache_creation_input_tokens": 2111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2111
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 166_

```json
{
  "type": "last-prompt",
  "leafUuid": "f360e3d3-e5ec-4ee5-b171-c39213fb0f04",
  "sessionId": "3e9ce29d-87c3-49f7-ac0f-6c69e795da79"
}
```

---


### Runtime record

_source line 167_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze semantic-only DocRED ET increase mechanism",
  "sessionId": "3e9ce29d-87c3-49f7-ac0f-6c69e795da79"
}
```

---
