# experiment dir c counterfactual

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_experiment_dir-c-counterfactual_20260520T152704.jsonl`
- **Structured JSON:** [`44d055bc7f0edc4c8b4d.json`](../../sessions/44/44d055bc7f0edc4c8b4d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-20T15:32:04.506261+00:00_

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
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
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

_source line 2 · 2026-05-20T15:32:04.506839+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T15:32:04.507133+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T15:32:04.507360+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/data/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/data/ 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T15:32:04.507656+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nanalysis\\nanalysis_confirmation_bias.py\\nanalysis_confirmation_bias_crossmodel.py\\nanalysis_constraint_ablation_folio204.py\\nanalysis_constraint_precision.py\\nanalysis_deepconf_filter.py\\nanalysis_k_ablation_folio204.py\\nanalysis_max_unsat.py\\nanalysis_problem_perturbation.py\\nanalysis_process_kappa.py\\nanalysis_prove_verify.py\\nartifacts\\nauto_run_analysis.sh\\nbackward_verification.py\\nbaselines\\ncompute_fleiss_kappa.py\\ncompute_process_kappa_multi.py\\nconstraint_ablation.py\\ncross_trace_unsat.py\\ndata\\ndiff_scorers.py\\ndirection_f_blind_fol.py\\ndirection_g_decoupling.py\\ndirection_g_fast.py\\ndirection_g_fast2.py\\ndirection_i_z3_filter.py\\ndirection_k_minority_report.py\\ndirection_r_deberta.py\\ndirection_r_deberta_proofwriter.py\\ndirection_r_nli_verifier.py\\ndirection_rg_combo.py\\nerror_categorization.py\\nexperiments\\nextract_constraints.py\\nextract_constraints_parallel.py\\nextract_fast.py\\nfigures\\nlogs\\nmcnemar_recompute.py\\npremise_formalization.py\\nprepare_data.py\\nprepare_proofwriter.py\\nreextract_failed.py\\nreextract_v2.py\\nreextract_v3.py\\nresults\\nrun_ablation_analysis.py\\nrun_after_extraction.sh\\nrun_case_study.py\\nrun_consistency_filtering.py\\nrun_contrastive.py\\nrun_contrastive.py.bak_pre080\\nrun_contrastive_folio.py\\nrun_cross_model.py\\nrun_debate.py\\nrun_debate.py.bak_pre_logiqa\\nrun_exp028b.sh\\nrun_full_mvp.py\\nrun_full_mvp.py.bak\\nrun_full_mvp.py.bak2\\nrun_icg.py\\nrun_icg.py.bak\\nrun_icl_oracle.py\\nrun_kappa_generalization.py\\nrun_logiqa.py\\nrun_multi_temp.py\\nrun_mvp.py\\nrun_z3_feedback_folio.py\\nsc_tiebreak_revalidation.py\\nscripts\\nsica\\nutils\\nwild6_combined.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T15:32:04.507917+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T15:32:04.508126+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/data/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/data/"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T15:32:04.508342+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/experiments/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/experiments/"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T15:32:04.508651+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"case_study_3problems.json\\nempty.json\\nexplore_proofwriter.py\\nexplore_pw.py\\nexplore_pw2.py\\nexplore_pw3.py\\nfolio_3_dryrun.json\\nfolio_d012.json\\nfolio_dryrun3.json\\nfolio_dryrun_3.json\\nfolio_full.json\\nlogiqa_200.json\\nprepare_folio.py\\nprepare_logiqa.py\\nprepare_proofwriter.py\\nproofwriter-OWA-D5-validation.jsonl\\nproofwriter_d012.json\\nproofwriter_full.json\\npw_explore.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T15:32:04.508918+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"exp-061-qwen7b-folio204\\nexp-062-gemma27b-folio204\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T15:32:04.509138+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus/results/ -maxdepth 2 -type d -name \"exp-033*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus/results/ -maxdepth 2 -type d -name \"exp-033*\""
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T15:32:04.509329+00:00_

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
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
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

_source line 13 · 2026-05-20T15:32:04.509514+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T15:32:04.509759+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"adaptive_sica_validation.json\\ncase_study_constraints.json\\ncase_study_normalized.json\\ncondorcet_independence_analysis.json\\nconfirmation_bias\\ncross_model_experiment\\ncross_model_kappa\\ncross_model_mistral_folio\\ndirection_a_prove\\ndirection_b_deepconf\\ndirection_e_abstention\\ndirection_f_blind_fol\\ndirection_g_decoupling\\ndirection_g_dryrun.log\\ndirection_g_vllm.log\\ndirection_i_z3_filter\\ndirection_r_deberta\\ndirection_r_nli_large\\ndirection_r_nli_pw600\\ndirection_r_nli_small\\ndirection_rg_combo\\ndisc_filter_full.log\\ndisc_filter_test.log\\ndiscriminative_filter_exp033.json\\ndiscriminative_filter_exp033_test.json\\ndiscriminative_filter_exp044b.json\\ndiscriminative_filter_exp046.json\\ndiscriminative_filter_exp054.json\\nexp-007-qwen72b-awq\\nexp-029-contrastive-folio204\\nexp004_qwen7b_rerun\\nexp013_constraint_ablation\\nexp027_qwen3_14b_nonthinking\\nexp028_qwen3_14b_thinking\\nexp028b_discordant_tracking.json\\nexp028b_qwen3_thinking_folio204\\nexp033_mistral_7b_folio204\\nexp033_per_problem_analysis.json\\nexp033_per_problem_analysis_v2.json\\nexp034_llama31_8b_folio204\\nexp034_qwen25_14b_proofwriter\\nexp035_qwen25_7b_folio204\\nexp036_z3_feedback\\nexp036b_cross_trace_unsat.json\\nexp044b_icl_oracle_qwen14b\\nexp045b_backward_qwen14b\\nexp046_mistral_7b_pw600\\nexp047_qwen3_thinking_folio204\\nexp051_mistral_k_sensitivity\\nexp054_mistral_folio204_t10\\nexp057_mistral_folio204_t03\\nexp058_mistral_folio204_t05\\nexp059_cross_qwen3_extractor\\nexp05_backward_verification\\nexp060_cross_qwen25_14b_extractor\\nexp061_qwen25_7b_folio204\\nexp062_gemma27b_folio204\\nexp065_qwen7b_pw600\\nexp066_qwen14b_folio_seed123\\nexp066_vllm.log\\nexp067_mistral_folio_seed789\\nexp069_mistral_logiqa200\\nexp070_qwen7b_logiqa200\\nexp071_qwen7b_logiqa200_seed123\\nexp073_qwen7b_logiqa200_seed456\\nexp073b_qwen7b_logiqa200_seed456\\nexp074_icg_dryrun\\nexp074_icg_mistral_folio\\nexp074_icg_v2_d
…[truncated 973 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T15:32:04.511163+00:00_

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
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T15:32:04.511390+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -100 /root/symb_invariant_consensus/data/folio_full.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -100 /root/symb_invariant_consensus/data/folio_full.json"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T15:32:04.511588+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"constraint_cache\\nexp033.log\\nexp033_results.json\\nintermediates\\nsc_answer_matrix.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T15:32:04.511994+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"id\\\": \\\"folio_0\\\",\\n    \\\"problem\\\": \\\"Given the following premises:\\\\nIf people perform in school talent shows often, then they attend and are very engaged with school events. People either perform in school talent shows often or are inactive and disinterested members of their community. If people chaperone high school dances, then they are not students who attend the school. All people who are inactive and disinterested members of their community chaperone high school dances. All young children and teenagers who wish to further their academic careers and educational opportunities are students who attend the school. Bonnie either both attends and is very engaged with school events and is a student who attends the school, or she neither attends and is very engaged with school events nor is a student who attends the school.\\\\n\\\\nDetermine whether the following conclusion is true, false, or uncertain:\\\\nBonnie performs in school talent shows often.\\\",\\n    \\\"solution\\\": \\\"\\\",\\n    \\\"answer\\\": \\\"Unknown\\\",\\n    \\\"level\\\": \\\"validation\\\",\\n    \\\"premises_fol\\\": [\\n      \\\"\\\\u2200x (TalentShows(x) \\\\u2192 Engaged(x))\\\",\\n      \\\"\\\\u2200x (TalentShows(x) \\\\u2228 Inactive(x))\\\",\\n      \\\"\\\\u2200x (Chaperone(x) \\\\u2192 \\\\u00acStudents(x))\\\",\\n      \\\"\\\\u2200x (Inactive(x) \\\\u2192 Chaperone(x))\\\",\\n      \\\"\\\\u2200x (AcademicCareer(x) \\\\u2192 Students(x))\\\",\\n      \\\"(Engaged(bonnie) \\\\u2227 Students(bonnie)) \\\\u2295 (\\\\u00acEngaged(bonnie) \\\\u2227 \\\\u00acStudents(bonnie))\\\"\\n    ],\\n    \\\"conclusion_fol\\\": \\\"Engaged(bonnie)\\\"\\n  },\\n  {\\n    \\\"id\\\": \\\"folio_1\\\",\\n    \\\"problem\\\": \\\"Given the following premises:\\\\nIf people perform in school talent shows often, then they attend and are very engaged with school events. People either perform in school talent sh
…[truncated 7260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T15:32:04.512256+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T15:32:04.512533+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"folio_0.json\\nfolio_1.json\\nfolio_10.json\\nfolio_100.json\\nfolio_101.json\\nfolio_102.json\\nfolio_103.json\\nfolio_104.json\\nfolio_105.json\\nfolio_106.json\\nfolio_107.json\\nfolio_108.json\\nfolio_109.json\\nfolio_11.json\\nfolio_110.json\\nfolio_111.json\\nfolio_112.json\\nfolio_113.json\\nfolio_114.json\\nfolio_115.json\\nfolio_116.json\\nfolio_117.json\\nfolio_118.json\\nfolio_119.json\\nfolio_12.json\\nfolio_120.json\\nfolio_121.json\\nfolio_122.json\\nfolio_123.json\\nfolio_124.json\\nfolio_125.json\\nfolio_126.json\\nfolio_127.json\\nfolio_128.json\\nfolio_129.json\\nfolio_13.json\\nfolio_130.json\\nfolio_131.json\\nfolio_132.json\\nfolio_133.json\\nfolio_134.json\\nfolio_135.json\\nfolio_136.json\\nfolio_137.json\\nfolio_138.json\\nfolio_139.json\\nfolio_14.json\\nfolio_140.json\\nfolio_141.json\\nfolio_142.json\\nfolio_143.json\\nfolio_144.json\\nfolio_145.json\\nfolio_146.json\\nfolio_147.json\\nfolio_148.json\\nfolio_149.json\\nfolio_15.json\\nfolio_150.json\\nfolio_151.json\\nfolio_152.json\\nfolio_153.json\\nfolio_154.json\\nfolio_155.json\\nfolio_156.json\\nfolio_157.json\\nfolio_158.json\\nfolio_159.json\\nfolio_16.json\\nfolio_160.json\\nfolio_161.json\\nfolio_162.json\\nfolio_163.json\\nfolio_164.json\\nfolio_165.json\\nfolio_166.json\\nfolio_167.json\\nfolio_168.json\\nfolio_169.json\\nfolio_17.json\\nfolio_170.json\\nfolio_171.json\\nfolio_172.json\\nfolio_173.json\\nfolio_174.json\\nfolio_175.json\\nfolio_176.json\\nfolio_177.json\\nfolio_178.json\\nfolio_179.json\\nfolio_18.json\\nfolio_180.json\\nfolio_181.json\\nfolio_182.json\\nfolio_183.json\\nfolio_184.json\\nfolio_185.json\\nfolio_186.json\\nfolio_187.json\\nfolio_188.json\\nfolio_189.json\\nfolio_19.json\\nfolio_190.json\\nfolio_191.json\\nfolio_192.json\\nfolio_193.json\\nfolio_194.json\\nfolio_195.json\\nfolio_196.json\\nfolio_197.json\\nfolio_198.json\\nfolio_199.json\\nfolio_2.json\\nfolio_20.json\\nfolio_200.json\\nfolio_
…[truncated 1518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T15:32:04.512752+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_0.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_0.json"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T15:32:04.513064+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"problem\\\": {\\n    \\\"id\\\": \\\"folio_0\\\",\\n    \\\"problem\\\": \\\"Given the following premises:\\\\nIf people perform in school talent shows often, then they attend and are very engaged with school events. People either perform in school talent shows often or are inactive and disinterested members of their community. If people chaperone high school dances, then they are not students who attend the school. All people who are inactive and disinterested members of their community chaperone high school dances. All young children and teenagers who wish to further their academic careers and educational opportunities are students who attend the school. Bonnie either both attends and is very engaged with school events and is a student who attends the school, or she neither attends and is very engaged with school events nor is a student who attends the school.\\\\n\\\\nDetermine whether the following conclusion is true, false, or uncertain:\\\\nBonnie performs in school talent shows often.\\\",\\n    \\\"solution\\\": \\\"\\\",\\n    \\\"answer\\\": \\\"Unknown\\\",\\n    \\\"level\\\": \\\"validation\\\",\\n    \\\"premises_fol\\\": [\\n      \\\"\\\\u2200x (TalentShows(x) \\\\u2192 Engaged(x))\\\",\\n      \\\"\\\\u2200x (TalentShows(x) \\\\u2228 Inactive(x))\\\",\\n      \\\"\\\\u2200x (Chaperone(x) \\\\u2192 \\\\u00acStudents(x))\\\",\\n      \\\"\\\\u2200x (Inactive(x) \\\\u2192 Chaperone(x))\\\",\\n      \\\"\\\\u2200x (AcademicCareer(x) \\\\u2192 Students(x))\\\",\\n      \\\"(Engaged(bonnie) \\\\u2227 Students(bonnie)) \\\\u2295 (\\\\u00acEngaged(bonnie) \\\\u2227 \\\\u00acStudents(bonnie))\\\"\\n    ],\\n    \\\"conclusion_fol\\\": \\\"Engaged(bonnie)\\\",\\n    \\\"dataset\\\": \\\"folio\\\"\\n  },\\n  \\\"sica_result\\\": {\\n    \\\"answer\\\": \\\"Unknown\\\",\\n    \\\"scores\\\": {\\n      \\\"False\\\": 3.5,\\n      \\\"Unknown\\\": 58.0\\n    },\\n    \\\"answer_counts\\\": {\\n    
…[truncated 6881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T15:32:04.513288+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache/"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T15:32:04.513474+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"folio_0.json\\nfolio_1.json\\nfolio_10.json\\nfolio_100.json\\nfolio_101.json\\nfolio_102.json\\nfolio_103.json\\nfolio_104.json\\nfolio_105.json\\nfolio_106.json\\nfolio_107.json\\nfolio_108.json\\nfolio_109.json\\nfolio_11.json\\nfolio_110.json\\nfolio_111.json\\nfolio_112.json\\nfolio_113.json\\nfolio_114.json\\nfolio_115.json\\nfolio_116.json\\nfolio_117.json\\nfolio_118.json\\nfolio_119.json\\nfolio_12.json\\nfolio_120.json\\nfolio_121.json\\nfolio_122.json\\nfolio_123.json\\nfolio_124.json\\nfolio_125.json\\nfolio_126.json\\nfolio_127.json\\nfolio_128.json\\nfolio_129.json\\nfolio_13.json\\nfolio_130.json\\nfolio_131.json\\nfolio_132.json\\nfolio_133.json\\nfolio_134.json\\nfolio_135.json\\nfolio_136.json\\nfolio_137.json\\nfolio_138.json\\nfolio_139.json\\nfolio_14.json\\nfolio_140.json\\nfolio_141.json\\nfolio_142.json\\nfolio_143.json\\nfolio_144.json\\nfolio_145.json\\nfolio_146.json\\nfolio_147.json\\nfolio_148.json\\nfolio_149.json\\nfolio_15.json\\nfolio_150.json\\nfolio_151.json\\nfolio_152.json\\nfolio_153.json\\nfolio_154.json\\nfolio_155.json\\nfolio_156.json\\nfolio_157.json\\nfolio_158.json\\nfolio_159.json\\nfolio_16.json\\nfolio_160.json\\nfolio_161.json\\nfolio_162.json\\nfolio_163.json\\nfolio_164.json\\nfolio_165.json\\nfolio_166.json\\nfolio_167.json\\nfolio_168.json\\nfolio_169.json\\nfolio_17.json\\nfolio_170.json\\nfolio_171.json\\nfolio_172.json\\nfolio_173.json\\nfolio_174.json\\nfolio_175.json\\nfolio_176.json\\nfolio_177.json\\nfolio_178.json\\nfolio_179.json\\nfolio_18.json\\nfolio_180.json\\nfolio_181.json\\nfolio_182.json\\nfolio_183.json\\nfolio_184.json\\nfolio_185.json\\nfolio_186.json\\nfolio_187.json\\nfolio_188.json\\nfolio_189.json\\nfolio_19.json\\nfolio_190.json\\nfolio_191.json\\nfolio_192.json\\nfolio_193.json\\nfolio_194.json\\nfolio_195.json\\nfolio_196.json\\nfolio_197.json\\nfolio_198.json\\nfolio_199.json\\nfolio_2.json\\nfolio_20.json\\nfolio_200.json\\nfolio_
…[truncated 1518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T15:32:04.513632+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -100 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache/folio_0.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -100 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache/folio_0.json"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T15:32:04.513844+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"pid\\\": \\\"folio_0\\\",\\n  \\\"gt\\\": \\\"Unknown\\\",\\n  \\\"per_trace\\\": [\\n    {\\n      \\\"trace_idx\\\": 0,\\n      \\\"answer\\\": \\\"Unknown\\\",\\n      \\\"constraints\\\": [\\n        {\\n          \\\"type\\\": \\\"rule\\\",\\n          \\\"expression\\\": \\\"performs_in_school_talent_shows_often(X) -> attends_and_engaged_with_school_events(X) & student(X)\\\",\\n          \\\"z3_formula\\\": \\\"Implies(performs_in_school_talent_shows_often_X, And(attends_and_engaged_with_school_events_X, student_X))\\\",\\n          \\\"source_step\\\": 1\\n        },\\n        {\\n          \\\"type\\\": \\\"rule\\\",\\n          \\\"expression\\\": \\\"performs_in_school_talent_shows_often(X) | inactive_and_disinterested_member(X)\\\",\\n          \\\"z3_formula\\\": \\\"Or(performs_in_school_talent_shows_often_X, inactive_and_disinterested_member_X)\\\",\\n          \\\"source_step\\\": 4\\n        },\\n        {\\n          \\\"type\\\": \\\"rule\\\",\\n          \\\"expression\\\": \\\"chaperones_high_school_dances(X) -> !student(X)\\\",\\n          \\\"z3_formula\\\": \\\"Implies(chaperones_high_school_dances_X, Not(student_X))\\\",\\n          \\\"source_step\\\": 2\\n        },\\n        {\\n          \\\"type\\\": \\\"rule\\\",\\n          \\\"expression\\\": \\\"inactive_and_disinterested_member(X) -> chaperones_high_school_dances(X)\\\",\\n          \\\"z3_formula\\\": \\\"Implies(inactive_and_disinterested_member_X, chaperones_high_school_dances_X)\\\",\\n          \\\"source_step\\\": 2\\n        },\\n        {\\n          \\\"type\\\": \\\"rule\\\",\\n          \\\"expression\\\": \\\"young_child_or_teenager(X) & wishes_to_further_academic_career(X) -> student(X)\\\",\\n          \\\"z3_formula\\\": \\\"Implies(And(young_child_or_teenager_X, wishes_to_further_academic_career_X), student_X)\\\",\\n          \\\"source_step\\\": 3\\n        },\\n        {\\n          \\\"type\\\": \
…[truncated 3312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T15:32:04.514081+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/sica/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/sica/"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T15:32:04.514225+00:00_

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
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
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

_source line 29 · 2026-05-20T15:32:04.514455+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__init__.py\\n__pycache__\\nconstraint_extractor.py\\npipeline.py\\nscorer.py\\ntrace_generator.py\\nz3_feedback.py\\nz3_maxsat.py\\nz3_maxsat.py.bak\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.73}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T15:32:04.514675+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 204,\\n    \\\"sica_accuracy\\\": 0.5931372549019608,\\n    \\\"sc_accuracy\\\": 0.5441176470588235,\\n    \\\"sica_correct\\\": 121,\\n    \\\"sc_correct\\\": 111,\\n    \\\"extraction_rate\\\": 0.9714052287581699,\\n    \\\"total_constraints_extracted\\\": 14042,\\n    \\\"total_unique_constraints\\\": 8021,\\n    \\\"contradiction_rate\\\": 0.03503303827452936,\\n    \\\"problems_with_contradictions\\\": 128,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"validation\\\": {\\n        \\\"sica\\\": 0.5931372549019608,\\n        \\\"sc\\\": 0.5441176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.5931372549019608,\\n        \\\"sc\\\": 0.5441176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 4881.8\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"folio_0\\\",\\n      \\\"problem\\\": \\\"Given the following premises:\\\\nIf people perform in school talent shows often, then they attend and are very engaged with school events. People either perform in school talent shows often or are inactive and disinterested members of their community. If people chaperone high school dances, then they are not students who attend the school. All people who are inactive and disinterested members of their community chaperone high school dances. All young children and teenagers who wish to further their academic careers and educational opportunities are students who attend the school. Bonnie either both attends and is very engaged with school events and is a student who attends the school, or she neither attends and is very engaged with school events nor is a student who attends the school.\\\\n\\\\nDetermine whether the following conclusion
…[truncated 2950 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T15:32:04.514838+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/sica/z3_maxsat.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/sica/z3_maxsat.py"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T15:32:04.515122+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nZ3-based weighted partial MAX-SAT solver for constraint consensus.\\nInput: multi-trace constraint lists (list of list of dicts)\\nOutput: optimal satisfiable constraint subset, excluded contradictions, per-answer scores\\nDependencies: z3-solver\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport logging\\nimport re\\nimport time\\nfrom dataclasses import dataclass, field\\n\\nimport z3\\n\\nz3.set_param('smt.random_seed', 42)\\nz3.set_param('sat.random_seed', 42)\\n\\nlogger = logging.getLogger(__name__)\\n\\n_BOOL_INDICATORS = re.compile(r'\\\\bImplies\\\\s*\\\\(|==\\\\s*True|==\\\\s*False|\\\\bNot\\\\s*\\\\(|\\\\bAnd\\\\s*\\\\(|\\\\bOr\\\\s*\\\\(')\\n\\n\\ndef _is_boolean_formula(formula_str: str) -> bool:\\n    \\\"\\\"\\\"Detect whether a formula uses boolean logic (vs arithmetic).\\\"\\\"\\\"\\n    return bool(_BOOL_INDICATORS.search(formula_str))\\n\\n\\ndef _preprocess_formula(formula_str: str) -> str:\\n    \\\"\\\"\\\"Normalize common LLM output patterns before z3 eval.\\\"\\\"\\\"\\n    s = formula_str.strip()\\n    # Unicode logical operators (common in 7B model outputs)\\n    s = s.replace('¬', 'Not ')\\n    s = re.sub(r'[∀∃]\\\\s*\\\\w+\\\\s*[:.]\\\\s*', '', s)\\n    s = re.sub(r'~(\\\\w+)', r'Not(\\\\1)', s)\\n    # Sum -> sum\\n    s = re.sub(r'\\\\bSum\\\\b', 'sum', s)\\n    # sum([x1, x2, ...]) -> sum(x1, x2, ...)\\n    s = re.sub(r'\\\\bsum\\\\(\\\\[([^\\\\[\\\\]]*)\\\\]\\\\)', r'sum(\\\\1)', s)\\n    # pow(a, b) -> (a)**(b)\\n    s = re.sub(r'\\\\bpow\\\\(([^,]+),\\\\s*([^)]+)\\\\)', r'(\\\\1)**(\\\\2)', s)\\n    # Abs -> abs\\n    s = re.sub(r'\\\\bAbs\\\\b', 'abs', s)\\n    return s\\n\\n\\ndef parse_z3_formula(formula_str: str, var_type: str = \\\"auto\\\") -> z3.ExprRef | None:\\n    \\\"\\\"\\\"Safely parse a string into a z3 expression.\\n\\n    Supports:\\n      - Arithmetic: +, -, *, /, **, ==, !=, <, >, <=, >= (Real variables)\\n      - Boolean: Implies, 
…[truncated 7010 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T15:32:04.515303+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/sica/scorer.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/sica/scorer.py"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T15:32:04.515534+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nInvariant consensus scorer with A+C improvement:\\n  A (normal mode): score = positive_weight - alpha * negative_weight\\n  C (fallback mode): when satisfied_ratio < threshold, score = -excluded_exposure\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport logging\\nfrom collections import Counter\\n\\nfrom .z3_maxsat import MaxSATResult\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\nclass InvariantScorer:\\n\\n    def __init__(self, alpha: float = 0.5, fallback_threshold: float = 0.2):\\n        self.alpha = alpha\\n        self.fallback_threshold = fallback_threshold\\n\\n    def score(\\n        self,\\n        maxsat_result: MaxSATResult,\\n        traces: list[dict],\\n        candidates: list[str],\\n    ) -> dict[str, float]:\\n        \\\"\\\"\\\"Score each candidate answer using A+C strategy.\\n\\n        Normal mode (A): score = Σw(satisfied ∩ traces) - α·Σw(excluded ∩ traces)\\n        Fallback mode (C): score = -Σw(excluded ∩ traces)\\n        Switches to fallback when satisfied_ratio < fallback_threshold.\\n        \\\"\\\"\\\"\\n        answer_traces: dict[str, set[int]] = {}\\n        for t in traces:\\n            ans = str(t.get(\\\"answer\\\", \\\"\\\")).strip()\\n            idx = t.get(\\\"trace_idx\\\", 0)\\n            answer_traces.setdefault(ans, set()).add(idx)\\n\\n        n_satisfied = len(maxsat_result.satisfied)\\n        n_excluded = len(maxsat_result.excluded)\\n        n_total = n_satisfied + n_excluded\\n\\n        if n_total == 0:\\n            return {str(c).strip(): 0.0 for c in candidates}\\n\\n        satisfied_ratio = n_satisfied / n_total\\n        fallback = satisfied_ratio < self.fallback_threshold\\n\\n        logger.info(\\n            \\\"Scorer mode=%s  satisfied_ratio=%.3f (%d/%d)  alpha=%.2f  threshold=%.2f\\\",\\n            \\\"FALLBACK\\\" if fallback else \\\"NORMAL\\\",\\n            satisfied_ratio, n_satisfied, n_total,\\n      
…[truncated 1826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T15:32:04.515854+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/sica/pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/sica/pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T15:32:04.516222+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nSICA end-to-end pipeline: trace generation -> constraint extraction -> Z3 dedup -> MAX-SAT -> scoring -> answer selection.\\nInput: problem dict with \\\"problem\\\" and \\\"answer\\\" fields\\nOutput: result dict with answer, score, constraint stats, maxsat stats\\nDependencies: trace_generator, constraint_extractor, z3_maxsat, scorer\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport logging\\nimport time\\nfrom collections import Counter\\n\\nfrom .trace_generator import TraceGenerator\\nfrom .constraint_extractor import ConstraintExtractor\\nfrom .z3_maxsat import ConstraintDeduplicator, MaxSATSolver\\nfrom .scorer import InvariantScorer\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\nclass SICAPipeline:\\n    def __init__(\\n        self,\\n        trace_generator: TraceGenerator,\\n        constraint_extractor: ConstraintExtractor,\\n        k: int = 12,\\n        maxsat_timeout_ms: int = 10000,\\n    ):\\n        self.trace_generator = trace_generator\\n        self.constraint_extractor = constraint_extractor\\n        self.k = k\\n        self.deduplicator = ConstraintDeduplicator()\\n        self.solver = MaxSATSolver()\\n        self.scorer = InvariantScorer()\\n        self.maxsat_timeout_ms = maxsat_timeout_ms\\n\\n    def run_single(self, problem: dict) -> dict:\\n        \\\"\\\"\\\"Run full SICA pipeline on a single problem.\\\"\\\"\\\"\\n        t_start = time.perf_counter()\\n\\n        # 1. Generate K traces\\n        t0 = time.perf_counter()\\n        traces = self.trace_generator.generate(problem[\\\"problem\\\"], k=self.k)\\n        trace_time = time.perf_counter() - t0\\n\\n        # 2. Extract constraints from each trace (batch for concurrency)\\n        t0 = time.perf_counter()\\n        all_constraints = self.constraint_extractor.extract_batch(\\n            [t[\\\"trace\\\"] for t in traces]\\n        )\\n        extract_time = time.perf_counter() - t0\\n\
…[truncated 7011 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T15:32:04.516431+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/data/folio_full.json')); [print(p['id'], '|', p['answer'], '|', p['conclusion_fol']) for p in d[:20]]\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/data/folio_full.json')); [print(p['id'], '|', p['answer'], '|', p['conclusion_fol']) for p in d[:20]]\""
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T15:32:04.516612+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T15:32:04.516760+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep -o '\"id\":[^,]*\\|\"answer\":[^,]*\\|\"conclusion_fol\":[^,]*' /root/symb_invariant_consensus/data/folio_full.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep -o '\"id\":[^,]*\\|\"answer\":[^,]*\\|\"conclusion_fol\":[^,]*' /root/symb_invariant_consensus/data/folio_full.json"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T15:32:04.516916+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T15:32:04.517062+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep \"conclusion_fol\" /root/symb_invariant_consensus/data/folio_full.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep \"conclusion_fol\" /root/symb_invariant_consensus/data/folio_full.json"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T15:32:04.517387+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    \\\"conclusion_fol\\\": \\\"Engaged(bonnie)\\\"\\n    \\\"conclusion_fol\\\": \\\"AcademicCareer(bonnie) \\\\u2295 Chaperone(bonnie) \\\\u2192 AcademicCareer(bonnie) \\\\u2295 Inactive(bonnie)\\\"\\n    \\\"conclusion_fol\\\": \\\"Chaperone(bonnie) \\\\u2295 TalentShows(bonnie) \\\\u2192 AcademicCareer(bonnie) \\\\u2227 Inactive(bonnie))\\\"\\n    \\\"conclusion_fol\\\": \\\"LunchInCompany(james)\\\"\\n    \\\"conclusion_fol\\\": \\\"\\\\u00acLunchInCompany(james)\\\"\\n    \\\"conclusion_fol\\\": \\\"(Manager(james) \\\\u2295 InOtherCountries(james)) \\\\u2192 (LunchAtHome(james) \\\\u2295 WorkRemotelyFromHome(james))\\\"\\n    \\\"conclusion_fol\\\": \\\"\\\\u2203x (Animal(x))\\\"\\n    \\\"conclusion_fol\\\": \\\"\\\\u2200x (Human(x) \\\\u2192 \\\\u00acFlu(x))\\\"\\n    \\\"conclusion_fol\\\": \\\"\\\\u2203x (GetMonkeypox(x) \\\\u2227 Coughing(x))\\\"\\n    \\\"conclusion_fol\\\": \\\"Ocellated(tom)\\\"\\n    \\\"conclusion_fol\\\": \\\"Eastern(tom)\\\"\\n    \\\"conclusion_fol\\\": \\\"WildTurkey(joey)\\\"\\n    \\\"conclusion_fol\\\": \\\"Top10(thelegendofzelda)\\\"\\n    \\\"conclusion_fol\\\": \\\"\\\\u2200x (Created(fifa22, x) \\\\u2192 Japanese(x) \\\\u2227 VideoGameCompany(x))\\\"\\n    \\\"conclusion_fol\\\": \\\"\\\\u00acTop10(thelegendofzelda)\\\"\\n    \\\"conclusion_fol\\\": \\\"\\\\u2200x (Square(x) \\\\u2192 IsShape(x))\\\"\\n    \\\"conclusion_fol\\\": \\\"Turtle(rock)\\\"\\n    \\\"conclusion_fol\\\": \\\"\\\\u00acTurtle(rock)\\\"\\n    \\\"conclusion_fol\\\": \\\"Turtle(rock) \\\\u2228 Cute(rock)\\\"\\n    \\\"conclusion_fol\\\": \\\"\\\\u00ac(Turtle(rock) \\\\u2227 Squirrel(rock)) \\\\u2192 Cute(rock) \\\\u2295 Skittish(rock)\\\"\\n    \\\"conclusion_fol\\\": \\\"Cute(rock) \\\\u2227 Still(rock) \\\\u2192 Turtle(rock) \\\\u2227 Skittish(rock)\\\"\\n    \\\"conclusion_fol\\\": \\\"Share(strangerThings, lisa)\\\"\\n    \\\"conclusion_fol\\\": \\\"Popular(blackMirror)\\\"\\n    \\\"conclus
…[truncated 8307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T15:32:04.517604+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "python3 -c \"import json; r=json.load(open('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json')); [print(x['problem_id'], x['ground_truth'], x['sica_correct'], x['sc_correct']) for x in r['results'][:20]]\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "python3 -c \"import json; r=json.load(open('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json')); [print(x['problem_id'], x['ground_truth'], x['sica_correct'], x['sc_correct']) for x in r['results'][:20]]\""
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T15:32:04.517746+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T15:32:04.517894+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep -E \"problem_id|sica_correct|sc_correct|ground_truth\" /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep -E \"problem_id|sica_correct|sc_correct|ground_truth\" /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T15:32:04.518044+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T15:32:04.518171+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep \"sica_correct\" /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep \"sica_correct\" /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T15:32:04.518444+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    \\\"sica_correct\\\": 121,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": false,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_correct\\\": true,\\n      \\\"sica_co
…[truncated 5620 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T15:32:04.518697+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/direction_c_counterfactual.py",
  "content": "\"\"\"\nDirection C: Counterfactual Constraint Subtraction — Pilot 20 problems\n\nIdea: Filter out \"direction-agnostic\" constraints (bias) that would appear\nregardless of the hypothesis direction. Keep only \"signal\" constraints that\nare specific to the current conclusion.\n\nStrategies tested:\n  1. full       — all constraints (SICA baseline)\n  2. signal     — only constraints referencing conclusion predicates\n  3. premise    — only constraints NOT referencing conclusion predicates\n  4. rules_only — only \"rule\" type, drop \"fact\" type constraints\n\"\"\"\nimport json\nimport os\nimport re\nimport sys\nimport time\nfrom collections import Counter\nfrom pathlib import Path\n\nsys.path.insert(0, \"/root/symb_invariant_consensus\")\nfrom sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver, UniqueConstraint\nfrom sica.scorer import InvariantScorer\n\nEXP_DIR = Path(\"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204\")\nDATA_PATH = Path(\"/root/symb_invariant_consensus/data/folio_full.json\")\nN_PILOT = 20\n\n\ndef load_folio_data():\n    with open(DATA_PATH) as f:\n        return {p[\"id\"]: p for p in json.load(f)}\n\n\ndef load_constraint_cache(pid):\n    path = EXP_DIR / \"constraint_cache\" / f\"{pid}.json\"\n    with open(path) as f:\n        return json.load(f)\n\n\ndef load_intermediate(pid):\n    path = EXP_DIR / \"intermediates\" / f\"{pid}.json\"\n    with open(path) as f:\n        return json.load(f)\n\n\ndef extract_conclusion_keywords(conclusion_fol):\n    \"\"\"Extract predicate and entity names from conclusion FOL.\"\"\"\n    clean = conclusion_fol.replace(\"\\\\u2200\", \"\").replace(\"\\\\u2203\", \"\")\n    clean = conclusion_fol\n    # Remove unicode logical operators\n    for ch in [\"∀\", \"∃\", \"¬\", \"→\", \"∧\", \"∨\", \"⊕\"]:\n        clean = clean.replace(ch, \" \")\n    # Extract all identifiers (predicate and entity names)\n    tokens = re.findall(r'[A-Za-z_][A-Za-z0-9_]*', clean)\n    # Filter out single-char variables like x, y\n    tokens = [t for t in tokens if len(t) > 1]\n    return set(t.lower() for t in tokens)\n\n\ndef constraint_references_conclusion(constraint, conclusion_keywords):\n    \"\"\"Check if a constraint's expression or z3_formula mentions conclusion keywords.\"\"\"\n    expr = constraint.get(\"expression\", \"\").lower()\n    z3f = constraint.get(\"z3_formula\", \"\").lower()\n    text = expr + \" \" + z3f\n\n    # Extract tokens from constraint text\n    constraint_tokens = set(re.findall(r'[a-z_][a-z0-9_]*', text))\n\n    # Check for overlap with conclusion keywords\n    # Use fuzzy matching: keyword must appear as substring of some token\n    for kw in conclusion_keywords:\n        if len(kw) < 3:\n            continue\n        for ct in constraint_tokens:\n            if kw in ct or ct in kw:\n                return True\n    return False\n\n\ndef filter_constraints_by_strategy(per_trace_constraints, strategy, conclusion_keywords):\n    \"\"\"Return filtered per-trace constraint lists based on strategy.\"\"\"\n    filtered = []\n    for trace_constraints in per_trace_constraints:\n        if strategy == \"full\":\n            filtered.append(trace_constraints)\n        elif strategy == \"signal\":\n            filtered.append([\n                c for c in trace_constraints\n                if constraint_references_conclusion(c, conclusion_keywords)\n            ])\n        elif strategy == \"premise\":\n            filtered.append([\n                c for c in trace_constraints\n                if not constraint_references_conclusion(c, conclusion_keywords)\n            ])\n        elif strategy == \"rules_only\":\n            filtered.append([\n                c for c in trace_constraints\n                if c.get(\"type\") == \"rule\"\n            ])\n        else:\n            filtered.append(trace_constraints)\n    return filtered\n\n\ndef run_maxsat_scoring(per_trace_constraints, traces, candidates, answer_counts):\n    \"\"\"Run dedup -> MAX-SAT -> scoring pipeline on constraint lists.\"\"\"\n    deduplicator = ConstraintDeduplicator()\n    solver = MaxSATSolver()\n    scorer = InvariantScorer()\n\n    unique = deduplicator.deduplicate(per_trace_constraints)\n    if not unique:\n        return None, None, {\"unique\": 0, \"satisfied\": 0, \"excluded\": 0}\n\n    result = solver.solve(unique, timeout_ms=10000)\n    scores = scorer.score(result, traces, candidates)\n    answer = scorer.select_answer(scores, answer_counts)\n\n    stats = {\n        \"unique\": len(unique),\n        \"satisfied\": len(result.satisfied),\n        \"excluded\": len(result.excluded),\n        \"total_weight\": result.total_weight,\n    }\n    return answer, scores, stats\n\n\ndef normalize_logic_answer(ans):\n    ans = str(ans).strip().lower()\n    if ans in (\"true\", \"yes\", \"correct\", \"entailment\"):\n        return \"True\"\n    if ans in (\"false\", \"no\", \"incorrect\", \"contradiction\"):\n        return \"False\"\n    if ans in (\"unknown\", \"uncertain\", \"undetermined\", \"neutral\"):\n        return \"Unknown\"\n    return ans.capitalize()\n\n\ndef main():\n    folio_data = load_folio_data()\n\n    # Load exp033 results for baseline comparison\n    with open(EXP_DIR / \"exp033_results.json\") as f:\n        exp033 = json.load(f)\n\n    # Get first N problem IDs\n    pilot_results = exp033[\"results\"][:N_PILOT]\n    pids = [r[\"problem_id\"] for r in pilot_results]\n\n    strategies = [\"full\", \"signal\", \"premise\", \"rules_only\"]\n    results = {s: [] for s in strategies}\n    detail_rows = []\n\n    for i, pid in enumerate(pids):\n        prob = folio_data[pid]\n        gt = prob[\"answer\"]\n        conclusion_fol = prob.get(\"conclusion_fol\", \"\")\n        conclusion_kws = extract_conclusion_keywords(conclusion_fol)\n\n        # Load constraint cache (per-trace constraints)\n        cache = load_constraint_cache(pid)\n        per_trace = [t[\"constraints\"] for t in cache[\"per_trace\"]]\n\n        # Load intermediate for traces\n        inter = load_intermediate(pid)\n        traces = inter[\"sica_result\"][\"traces\"]\n        for t in traces:\n            if t.get(\"answer\"):\n                t[\"answer\"] = normalize_logic_answer(t[\"answer\"])\n\n        candidates = sorted(set(t[\"answer\"] for t in traces if t[\"answer\"]))\n        answer_counts = Counter(t[\"answer\"] for t in traces if t[\"answer\"])\n\n        # SC answer\n        sc_answer = answer_counts.most_common(1)[0][0] if answer_counts else \"\"\n\n        row = {\n            \"pid\": pid,\n            \"gt\": gt,\n            \"sc_answer\": sc_answer,\n            \"sc_correct\": sc_answer == gt,\n            \"conclusion_fol\": conclusion_fol,\n            \"conclusion_keywords\": sorted(conclusion_kws),\n        }\n\n        for strategy in strategies:\n            filtered = filter_constraints_by_strategy(per_trace, strategy, conclusion_kws)\n            n_constraints = sum(len(c) for c in filtered)\n\n            answer, scores, stats = run_maxsat_scoring(\n                filtered, traces, candidates, answer_counts\n            )\n            if answer is None:\n                answer = sc_answer  # fallback to SC\n\n            correct = answer == gt\n            results[strategy].append(correct)\n\n            row[f\"{strategy}_answer\"] = answer\n            row[f\"{strategy}_correct\"] = correct\n            row[f\"{strategy}_n_constraints\"] = n_constraints\n            row[f\"{strategy}_stats\"] = stats\n\n        detail_rows.append(row)\n        print(f\"  [{i+1:2d}/{N_PILOT}] {pid}: gt={gt}  sc={sc_answer}({'O' if row['sc_correct'] else 'X'})  \"\n              f\"full={row['full_answer']}({'O' if row['full_correct'] else 'X'})  \"\n              f\"signal={row['signal_answer']}({'O' if row['signal_correct'] else 'X'})  \"\n              f\"premise={row['premise_answer']}({'O' if row['premise_correct'] else 'X'})  \"\n              f\"rules={row['rules_only_answer']}({'O' if row['rules_only_correct'] else 'X'})\")\n\n    # Summary\n    print(\"\\n\" + \"=\" * 60)\n    print(f\"Direction C Pilot Results — {N_PILOT} problems (exp033 Mistral-7B)\")\n    print(\"=\" * 60)\n\n    for strategy in strategies:\n        correct = sum(results[strategy])\n        total = len(results[strategy])\n        acc = correct / total if total else 0\n        print(f\"  {strategy:12s}: {correct}/{total} = {acc:.1%}\")\n\n    sc_correct = sum(r[\"sc_correct\"] for r in detail_rows)\n    print(f\"  {'SC':12s}: {sc_correct}/{N_PILOT} = {sc_correct/N_PILOT:.1%}\")\n\n    # Constraint retention ratio\n    print(\"\\nConstraint retention (avg |filtered| / |full|):\")\n    for strategy in strategies:\n        if strategy == \"full\":\n            continue\n        ratios = []\n        for row in detail_rows:\n            full_n = row[\"full_n_constraints\"]\n            filt_n = row[f\"{strategy}_n_constraints\"]\n            if full_n > 0:\n                ratios.append(filt_n / full_n)\n        avg_ratio = sum(ratios) / len(ratios) if ratios else 0\n        print(f\"  {strategy:12s}: {avg_ratio:.1%}\")\n\n    # Disagreement analysis: where strategies differ from full\n    print(\"\\nDisagreements with full SICA:\")\n    for strategy in [\"signal\", \"premise\", \"rules_only\"]:\n        diffs = []\n        for row in detail_rows:\n            if row[f\"{strategy}_answer\"] != row[\"full_answer\"]:\n                diffs.append(row[\"pid\"])\n        print(f\"  {strategy:12s}: {len(diffs)} disagreements — {diffs}\")\n\n    # Flip analysis: cases where filtered gets right but full gets wrong (or vice versa)\n    print(\"\\nFlip analysis (vs full baseline):\")\n    for strategy in [\"signal\", \"premise\", \"rules_only\"]:\n        gained = []\n        lost = []\n        for row in detail_rows:\n            fc = row[\"full_correct\"]\n            sc = row[f\"{strategy}_correct\"]\n            if not fc and sc:\n                gained.append(row[\"pid\"])\n            elif fc and not sc:\n                lost.append(row[\"pid\"])\n        print(f\"  {strategy:12s}: gained={gained}  lost={lost}  net={len(gained)-len(lost):+d}\")\n\n    # Save results\n    output = {\n        \"summary\": {\n            \"n_problems\": N_PILOT,\n            \"strategies\": {\n                s: {\n                    \"accuracy\": sum(results[s]) / len(results[s]),\n                    \"correct\": sum(results[s]),\n                }\n                for s in strategies\n            },\n            \"sc_accuracy\": sc_correct / N_PILOT,\n        },\n        \"details\": detail_rows,\n    }\n\n    out_path = \"/root/symb_invariant_consensus/results/direction_c_counterfactual_pilot.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/direction_c_counterfactual.py",
    "content": "\"\"\"\nDirection C: Counterfactual Constraint Subtraction — Pilot 20 problems\n\nIdea: Filter out \"direction-agnostic\" constraints (bias) that would appear\nregardless of the hypothesis direction. Keep only \"signal\" constraints that\nare specific to the current conclusion.\n\nStrategies tested:\n  1. full       — all constraints (SICA baseline)\n  2. signal     — only constraints referencing conclusion predicates\n  3. premise    — only constraints NOT referencing conclusion predicates\n  4. rules_only — only \"rule\" type, drop \"fact\" type constraints\n\"\"\"\nimport json\nimport os\nimport re\nimport sys\nimport time\nfrom collections import Counter\nfrom pathlib import Path\n\nsys.path.insert(0, \"/root/symb_invariant_consensus\")\nfrom sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver, UniqueConstraint\nfrom sica.scorer import InvariantScorer\n\nEXP_DIR = Path(\"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204\")\nDATA_PATH = Path(\"/root/symb_invariant_consensus/data/folio_full.json\")\nN_PILOT = 20\n\n\ndef load_folio_data():\n    with open(DATA_PATH) as f:\n        return {p[\"id\"]: p for p in json.load(f)}\n\n\ndef load_constraint_cache(pid):\n    path = EXP_DIR / \"constraint_cache\" / f\"{pid}.json\"\n    with open(path) as f:\n        return json.load(f)\n\n\ndef load_intermediate(pid):\n    path = EXP_DIR / \"intermediates\" / f\"{pid}.json\"\n    with open(path) as f:\n        return json.load(f)\n\n\ndef extract_conclusion_keywords(conclusion_fol):\n    \"\"\"Extract predicate and entity names from conclusion FOL.\"\"\"\n    clean = conclusion_fol.replace(\"\\\\u2200\", \"\").replace(\"\\\\u2203\", \"\")\n    clean = conclusion_fol\n    # Remove unicode logical operators\n    for ch in [\"∀\", \"∃\", \"¬\", \"→\", \"∧\", \"∨\", \"⊕\"]:\n        clean = clean.replace(ch, \" \")\n    # Extract all identifiers (predicate and entity names)\n    tokens = re.findall(r'[A-Za-z_][A-Za-z0-9_]*', clean)\n    # Filter out single-char variables like x, y\n    tokens = [t for t in tokens if len(t) > 1]\n    return set(t.lower() for t in tokens)\n\n\ndef constraint_references_conclusion(constraint, conclusion_keywords):\n    \"\"\"Check if a constraint's expression or z3_formula mentions conclusion keywords.\"\"\"\n    expr = constraint.get(\"expression\", \"\").lower()\n    z3f = constraint.get(\"z3_formula\", \"\").lower()\n    text = expr + \" \" + z3f\n\n    # Extract tokens from constraint text\n    constraint_tokens = set(re.findall(r'[a-z_][a-z0-9_]*', text))\n\n    # Check for overlap with conclusion keywords\n    # Use fuzzy matching: keyword must appear as substring of some token\n    for kw in conclusion_keywords:\n        if len(kw) < 3:\n            continue\n        for ct in constraint_tokens:\n            if kw in ct or ct in kw:\n                return True\n    return False\n\n\ndef filter_constraints_by_strategy(per_trace_constraints, strategy, conclusion_keywords):\n    \"\"\"Return filtered per-trace constraint lists based on strategy.\"\"\"\n    filtered = []\n    for trace_constraints in per_trace_constraints:\n        if strategy == \"full\":\n            filtered.append(trace_constraints)\n        elif strategy == \"signal\":\n            filtered.append([\n                c for c in trace_constraints\n                if constraint_references_conclusion(c, conclusion_keywords)\n            ])\n        elif strategy == \"premise\":\n            filtered.append([\n                c for c in trace_constraints\n                if not constraint_references_conclusion(c, conclusion_keywords)\n            ])\n        elif strategy == \"rules_only\":\n            filtered.append([\n                c for c in trace_constraints\n                if c.get(\"type\") == \"rule\"\n            ])\n        else:\n            filtered.append(trace_constraints)\n    return filtered\n\n\ndef run_maxsat_scoring(per_trace_constraints, traces, candidates, answer_counts):\n    \"\"\"Run dedup -> MAX-SAT -> scoring pipeline on constraint lists.\"\"\"\n    deduplicator = ConstraintDeduplicator()\n    solver = MaxSATSolver()\n    scorer = InvariantScorer()\n\n    unique = deduplicator.deduplicate(per_trace_constraints)\n    if not unique:\n        return None, None, {\"unique\": 0, \"satisfied\": 0, \"excluded\": 0}\n\n    result = solver.solve(unique, timeout_ms=10000)\n    scores = scorer.score(result, traces, candidates)\n    answer = scorer.select_answer(scores, answer_counts)\n\n    stats = {\n        \"unique\": len(unique),\n        \"satisfied\": len(result.satisfied),\n        \"excluded\": len(result.excluded),\n        \"total_weight\": result.total_weight,\n    }\n    return answer, scores, stats\n\n\ndef normalize_logic_answer(ans):\n    ans = str(ans).strip().lower()\n    if ans in (\"true\", \"yes\", \"correct\", \"entailment\"):\n        return \"True\"\n    if ans in (\"false\", \"no\", \"incorrect\", \"contradiction\"):\n        return \"False\"\n    if ans in (\"unknown\", \"uncertain\", \"undetermined\", \"neutral\"):\n        return \"Unknown\"\n    return ans.capitalize()\n\n\ndef main():\n    folio_data = load_folio_data()\n\n    # Load exp033 results for baseline comparison\n    with open(EXP_DIR / \"exp033_results.json\") as f:\n        exp033 = json.load(f)\n\n    # Get first N problem IDs\n    pilot_results = exp033[\"results\"][:N_PILOT]\n    pids = [r[\"problem_id\"] for r in pilot_results]\n\n    strategies = [\"full\", \"signal\", \"premise\", \"rules_only\"]\n    results = {s: [] for s in strategies}\n    detail_rows = []\n\n    for i, pid in enumerate(pids):\n        prob = folio_data[pid]\n        gt = prob[\"answer\"]\n        conclusion_fol = prob.get(\"conclusion_fol\", \"\")\n        conclusion_kws = extract_conclusion_keywords(conclusion_fol)\n\n        # Load constraint cache (per-trace constraints)\n        cache = load_constraint_cache(pid)\n        per_trace = [t[\"constraints\"] for t in cache[\"per_trace\"]]\n\n        # Load intermediate for traces\n        inter = load_intermediate(pid)\n        traces = inter[\"sica_result\"][\"traces\"]\n        for t in traces:\n            if t.get(\"answer\"):\n                t[\"answer\"] = normalize_logic_answer(t[\"answer\"])\n\n        candidates = sorted(set(t[\"answer\"] for t in traces if t[\"answer\"]))\n        answer_counts = Counter(t[\"answer\"] for t in traces if t[\"answer\"])\n\n        # SC answer\n        sc_answer = answer_counts.most_common(1)[0][0] if answer_counts else \"\"\n\n        row = {\n            \"pid\": pid,\n            \"gt\": gt,\n            \"sc_answer\": sc_answer,\n            \"sc_correct\": sc_answer == gt,\n            \"conclusion_fol\": conclusion_fol,\n            \"conclusion_keywords\": sorted(conclusion_kws),\n        }\n\n        for strategy in strategies:\n            filtered = filter_constraints_by_strategy(per_trace, strategy, conclusion_kws)\n            n_constraints = sum(len(c) for c in filtered)\n\n            answer, scores, stats = run_maxsat_scoring(\n                filtered, traces, candidates, answer_counts\n            )\n            if answer is None:\n                answer = sc_answer  # fallback to SC\n\n            correct = answer == gt\n            results[strategy].append(correct)\n\n            row[f\"{strategy}_answer\"] = answer\n            row[f\"{strategy}_correct\"] = correct\n            row[f\"{strategy}_n_constraints\"] = n_constraints\n            row[f\"{strategy}_stats\"] = stats\n\n        detail_rows.append(row)\n        print(f\"  [{i+1:2d}/{N_PILOT}] {pid}: gt={gt}  sc={sc_answer}({'O' if row['sc_correct'] else 'X'})  \"\n              f\"full={row['full_answer']}({'O' if row['full_correct'] else 'X'})  \"\n              f\"signal={row['signal_answer']}({'O' if row['signal_correct'] else 'X'})  \"\n              f\"premise={row['premise_answer']}({'O' if row['premise_correct'] else 'X'})  \"\n              f\"rules={row['rules_only_answer']}({'O' if row['rules_only_correct'] else 'X'})\")\n\n    # Summary\n    print(\"\\n\" + \"=\" * 60)\n    print(f\"Direction C Pilot Results — {N_PILOT} problems (exp033 Mistral-7B)\")\n    print(\"=\" * 60)\n\n    for strategy in strategies:\n        correct = sum(results[strategy])\n        total = len(results[strategy])\n        acc = correct / total if total else 0\n        print(f\"  {strategy:12s}: {correct}/{total} = {acc:.1%}\")\n\n    sc_correct = sum(r[\"sc_correct\"] for r in detail_rows)\n    print(f\"  {'SC':12s}: {sc_correct}/{N_PILOT} = {sc_correct/N_PILOT:.1%}\")\n\n    # Constraint retention ratio\n    print(\"\\nConstraint retention (avg |filtered| / |full|):\")\n    for strategy in strategies:\n        if strategy == \"full\":\n            continue\n        ratios = []\n        for row in detail_rows:\n            full_n = row[\"full_n_constraints\"]\n            filt_n = row[f\"{strategy}_n_constraints\"]\n            if full_n > 0:\n                ratios.append(filt_n / full_n)\n        avg_ratio = sum(ratios) / len(ratios) if ratios else 0\n        print(f\"  {strategy:12s}: {avg_ratio:.1%}\")\n\n    # Disagreement analysis: where strategies differ from full\n    print(\"\\nDisagreements with full SICA:\")\n    for strategy in [\"signal\", \"premise\", \"rules_only\"]:\n        diffs = []\n        for row in detail_rows:\n            if row[f\"{strategy}_answer\"] != row[\"full_answer\"]:\n                diffs.append(row[\"pid\"])\n        print(f\"  {strategy:12s}: {len(diffs)} disagreements — {diffs}\")\n\n    # Flip analysis: cases where filtered gets right but full gets wrong (or vice versa)\n    print(\"\\nFlip analysis (vs full baseline):\")\n    for strategy in [\"signal\", \"premise\", \"rules_only\"]:\n        gained = []\n        lost = []\n        for row in detail_rows:\n            fc = row[\"full_correct\"]\n            sc = row[f\"{strategy}_correct\"]\n            if not fc and sc:\n                gained.append(row[\"pid\"])\n            elif fc and not sc:\n                lost.append(row[\"pid\"])\n        print(f\"  {strategy:12s}: gained={gained}  lost={lost}  net={len(gained)-len(lost):+d}\")\n\n    # Save results\n    output = {\n        \"summary\": {\n            \"n_problems\": N_PILOT,\n            \"strategies\": {\n                s: {\n                    \"accuracy\": sum(results[s]) / len(results[s]),\n                    \"correct\": sum(results[s]),\n                }\n                for s in strategies\n            },\n            \"sc_accuracy\": sc_correct / N_PILOT,\n        },\n        \"details\": detail_rows,\n    }\n\n    out_path = \"/root/symb_invariant_consensus/results/direction_c_counterfactual_pilot.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T15:32:04.519028+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/direction_c_counterfactual.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T15:32:04.519233+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "cat > /root/symb_invariant_consensus/direction_c_counterfactual.py << 'SCRIPT_EOF'\n\"\"\"\nDirection C: Counterfactual Constraint Subtraction — Pilot 20 problems\n\nIdea: Filter out \"direction-agnostic\" constraints (bias) that would appear\nregardless of the hypothesis direction. Keep only \"signal\" constraints that\nare specific to the current conclusion.\n\nStrategies tested:\n  1. full       — all constraints (SICA baseline)\n  2. signal     — only constraints referencing conclusion predicates\n  3. premise    — only constraints NOT referencing conclusion predicates\n  4. rules_only — only \"rule\" type, drop \"fact\" type constraints\n\"\"\"\nimport json\nimport os\nimport re\nimport sys\nimport time\nfrom collections import Counter\nfrom pathlib import Path\n\nsys.path.insert(0, \"/root/symb_invariant_consensus\")\nfrom sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver, UniqueConstraint\nfrom sica.scorer import InvariantScorer\n\nEXP_DIR = Path(\"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204\")\nDATA_PATH = Path(\"/root/symb_invariant_consensus/data/folio_full.json\")\nN_PILOT = 20\n\n\ndef load_folio_data():\n    with open(DATA_PATH) as f:\n        return {p[\"id\"]: p for p in json.load(f)}\n\n\ndef load_constraint_cache(pid):\n    path = EXP_DIR / \"constraint_cache\" / f\"{pid}.json\"\n    with open(path) as f:\n        return json.load(f)\n\n\ndef load_intermediate(pid):\n    path = EXP_DIR / \"intermediates\" / f\"{pid}.json\"\n    with open(path) as f:\n        return json.load(f)\n\n\ndef extract_conclusion_keywords(conclusion_fol):\n    \"\"\"Extract predicate and entity names from conclusion FOL.\"\"\"\n    clean = conclusion_fol\n    for ch in [\"∀\", \"∃\", \"¬\", \"→\", \"∧\", \"∨\", \"⊕\"]:\n        clean = clean.replace(ch, \" \")\n    tokens = re.findall(r'[A-Za-z_][A-Za-z0-9_]*', clean)\n    tokens = [t for t in tokens if len(t) > 1]\n    return set(t.lower() for t in tokens)\n\n\ndef constraint_references_conclusion(constraint, conclusion_keywords):\n    \"\"\"Check if a constraint's expression or z3_formula mentions conclusion keywords.\"\"\"\n    expr = constraint.get(\"expression\", \"\").lower()\n    z3f = constraint.get(\"z3_formula\", \"\").lower()\n    text = expr + \" \" + z3f\n    constraint_tokens = set(re.findall(r'[a-z_][a-z0-9_]*', text))\n\n    for kw in conclusion_keywords:\n        if len(kw) < 3:\n            continue\n        for ct in constraint_tokens:\n            if kw in ct or ct in kw:\n                return True\n    return False\n\n\ndef filter_constraints_by_strategy(per_trace_constraints, strategy, conclusion_keywords):\n    \"\"\"Return filtered per-trace constraint lists based on strategy.\"\"\"\n    filtered = []\n    for trace_constraints in per_trace_constraints:\n        if strategy == \"full\":\n            filtered.append(trace_constraints)\n        elif strategy == \"signal\":\n            filtered.append([\n                c for c in trace_constraints\n                if constraint_references_conclusion(c, conclusion_keywords)\n            ])\n        elif strategy == \"premise\":\n            filtered.append([\n                c for c in trace_constraints\n                if not constraint_references_conclusion(c, conclusion_keywords)\n            ])\n        elif strategy == \"rules_only\":\n            filtered.append([\n                c for c in trace_constraints\n                if c.get(\"type\") == \"rule\"\n            ])\n        else:\n            filtered.append(trace_constraints)\n    return filtered\n\n\ndef run_maxsat_scoring(per_trace_constraints, traces, candidates, answer_counts):\n    \"\"\"Run dedup -> MAX-SAT -> scoring pipeline on constraint lists.\"\"\"\n    deduplicator = ConstraintDeduplicator()\n    solver = MaxSATSolver()\n    scorer = InvariantScorer()\n\n    unique = deduplicator.deduplicate(per_trace_constraints)\n    if not unique:\n        return None, None, {\"unique\": 0, \"satisfied\": 0, \"excluded\": 0}\n\n    result = solver.solve(unique, timeout_ms=10000)\n    scores = scorer.score(result, traces, candidates)\n    answer = scorer.select_answer(scores, answer_counts)\n\n    stats = {\n        \"unique\": len(unique),\n        \"satisfied\": len(result.satisfied),\n        \"excluded\": len(result.excluded),\n        \"total_weight\": result.total_weight,\n    }\n    return answer, scores, stats\n\n\ndef normalize_logic_answer(ans):\n    ans = str(ans).strip().lower()\n    if ans in (\"true\", \"yes\", \"correct\", \"entailment\"):\n        return \"True\"\n    if ans in (\"false\", \"no\", \"incorrect\", \"contradiction\"):\n        return \"False\"\n    if ans in (\"unknown\", \"uncertain\", \"undetermined\", \"neutral\"):\n        return \"Unknown\"\n    return ans.capitalize()\n\n\ndef main():\n    folio_data = load_folio_data()\n\n    with open(EXP_DIR / \"exp033_results.json\") as f:\n        exp033 = json.load(f)\n\n    pilot_results = exp033[\"results\"][:N_PILOT]\n    pids = [r[\"problem_id\"] for r in pilot_results]\n\n    strategies = [\"full\", \"signal\", \"premise\", \"rules_only\"]\n    results = {s: [] for s in strategies}\n    detail_rows = []\n\n    for i, pid in enumerate(pids):\n        prob = folio_data[pid]\n        gt = prob[\"answer\"]\n        conclusion_fol = prob.get(\"conclusion_fol\", \"\")\n        conclusion_kws = extract_conclusion_keywords(conclusion_fol)\n\n        cache = load_constraint_cache(pid)\n        per_trace = [t[\"constraints\"] for t in cache[\"per_trace\"]]\n\n        inter = load_intermediate(pid)\n        traces = inter[\"sica_result\"][\"traces\"]\n        for t in traces:\n            if t.get(\"answer\"):\n                t[\"answer\"] = normalize_logic_answer(t[\"answer\"])\n\n        candidates = sorted(set(t[\"answer\"] for t in traces if t[\"answer\"]))\n        answer_counts = Counter(t[\"answer\"] for t in traces if t[\"answer\"])\n\n        sc_answer = answer_counts.most_common(1)[0][0] if answer_counts else \"\"\n\n        row = {\n            \"pid\": pid,\n            \"gt\": gt,\n            \"sc_answer\": sc_answer,\n            \"sc_correct\": sc_answer == gt,\n            \"conclusion_fol\": conclusion_fol,\n            \"conclusion_keywords\": sorted(conclusion_kws),\n        }\n\n        for strategy in strategies:\n            filtered = filter_constraints_by_strategy(per_trace, strategy, conclusion_kws)\n            n_constraints = sum(len(c) for c in filtered)\n\n            answer, scores, stats = run_maxsat_scoring(\n                filtered, traces, candidates, answer_counts\n            )\n            if answer is None:\n                answer = sc_answer\n\n            correct = answer == gt\n            results[strategy].append(correct)\n\n            row[f\"{strategy}_answer\"] = answer\n            row[f\"{strategy}_correct\"] = correct\n            row[f\"{strategy}_n_constraints\"] = n_constraints\n            row[f\"{strategy}_stats\"] = stats\n\n        detail_rows.append(row)\n        print(f\"  [{i+1:2d}/{N_PILOT}] {pid}: gt={gt}  sc={sc_answer}({'O' if row['sc_correct'] else 'X'})  \"\n              f\"full={row['full_answer']}({'O' if row['full_correct'] else 'X'})  \"\n              f\"signal={row['signal_answer']}({'O' if row['signal_correct'] else 'X'})  \"\n              f\"premise={row['premise_answer']}({'O' if row['premise_correct'] else 'X'})  \"\n              f\"rules={row['rules_only_answer']}({'O' if row['rules_only_correct'] else 'X'})\")\n\n    print(\"\\n\" + \"=\" * 60)\n    print(f\"Direction C Pilot Results -- {N_PILOT} problems (exp033 Mistral-7B)\")\n    print(\"=\" * 60)\n\n    for strategy in strategies:\n        correct = sum(results[strategy])\n        total = len(results[strategy])\n        acc = correct / total if total else 0\n        print(f\"  {strategy:12s}: {correct}/{total} = {acc:.1%}\")\n\n    sc_correct = sum(r[\"sc_correct\"] for r in detail_rows)\n    print(f\"  {'SC':12s}: {sc_correct}/{N_PILOT} = {sc_correct/N_PILOT:.1%}\")\n\n    print(\"\\nConstraint retention (avg |filtered| / |full|):\")\n    for strategy in strategies:\n        if strategy == \"full\":\n            continue\n        ratios = []\n        for row in detail_rows:\n            full_n = row[\"full_n_constraints\"]\n            filt_n = row[f\"{strategy}_n_constraints\"]\n            if full_n > 0:\n                ratios.append(filt_n / full_n)\n        avg_ratio = sum(ratios) / len(ratios) if ratios else 0\n        print(f\"  {strategy:12s}: {avg_ratio:.1%}\")\n\n    print(\"\\nDisagreements with full SICA:\")\n    for strategy in [\"signal\", \"premise\", \"rules_only\"]:\n        diffs = []\n        for row in detail_rows:\n            if row[f\"{strategy}_answer\"] != row[\"full_answer\"]:\n                diffs.append(row[\"pid\"])\n        print(f\"  {strategy:12s}: {len(diffs)} disagreements -- {diffs}\")\n\n    print(\"\\nFlip analysis (vs full baseline):\")\n    for strategy in [\"signal\", \"premise\", \"rules_only\"]:\n        gained = []\n        lost = []\n        for row in detail_rows:\n            fc = row[\"full_correct\"]\n            sc = row[f\"{strategy}_correct\"]\n            if not fc and sc:\n                gained.append(row[\"pid\"])\n            elif fc and not sc:\n                lost.append(row[\"pid\"])\n        print(f\"  {strategy:12s}: gained={gained}  lost={lost}  net={len(gained)-len(lost):+d}\")\n\n    output = {\n        \"summary\": {\n            \"n_problems\": N_PILOT,\n            \"strategies\": {\n                s: {\n                    \"accuracy\": sum(results[s]) / len(results[s]),\n                    \"correct\": sum(results[s]),\n                }\n                for s in strategies\n            },\n            \"sc_accuracy\": sc_correct / N_PILOT,\n        },\n        \"details\": detail_rows,\n    }\n\n    out_path = \"/root/symb_invariant_consensus/results/direction_c_counterfactual_pilot.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"Script written OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat > /root/symb_invariant_consensus/direction_c_counterfactual.py << 'SCRIPT_EOF'\n\"\"\"\nDirection C: Counterfactual Constraint Subtraction — Pilot 20 problems\n\nIdea: Filter out \"direction-agnostic\" constraints (bias) that would appear\nregardless of the hypothesis direction. Keep only \"signal\" constraints that\nare specific to the current conclusion.\n\nStrategies tested:\n  1. full       — all constraints (SICA baseline)\n  2. signal     — only constraints referencing conclusion predicates\n  3. premise    — only constraints NOT referencing conclusion predicates\n  4. rules_only — only \"rule\" type, drop \"fact\" type constraints\n\"\"\"\nimport json\nimport os\nimport re\nimport sys\nimport time\nfrom collections import Counter\nfrom pathlib import Path\n\nsys.path.insert(0, \"/root/symb_invariant_consensus\")\nfrom sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver, UniqueConstraint\nfrom sica.scorer import InvariantScorer\n\nEXP_DIR = Path(\"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204\")\nDATA_PATH = Path(\"/root/symb_invariant_consensus/data/folio_full.json\")\nN_PILOT = 20\n\n\ndef load_folio_data():\n    with open(DATA_PATH) as f:\n        return {p[\"id\"]: p for p in json.load(f)}\n\n\ndef load_constraint_cache(pid):\n    path = EXP_DIR / \"constraint_cache\" / f\"{pid}.json\"\n    with open(path) as f:\n        return json.load(f)\n\n\ndef load_intermediate(pid):\n    path = EXP_DIR / \"intermediates\" / f\"{pid}.json\"\n    with open(path) as f:\n        return json.load(f)\n\n\ndef extract_conclusion_keywords(conclusion_fol):\n    \"\"\"Extract predicate and entity names from conclusion FOL.\"\"\"\n    clean = conclusion_fol\n    for ch in [\"∀\", \"∃\", \"¬\", \"→\", \"∧\", \"∨\", \"⊕\"]:\n        clean = clean.replace(ch, \" \")\n    tokens = re.findall(r'[A-Za-z_][A-Za-z0-9_]*', clean)\n    tokens = [t for t in tokens if len(t) > 1]\n    return set(t.lower() for t in tokens)\n\n\ndef constraint_references_conclusion(constraint, conclusion_keywords):\n    \"\"\"Check if a constraint's expression or z3_formula mentions conclusion keywords.\"\"\"\n    expr = constraint.get(\"expression\", \"\").lower()\n    z3f = constraint.get(\"z3_formula\", \"\").lower()\n    text = expr + \" \" + z3f\n    constraint_tokens = set(re.findall(r'[a-z_][a-z0-9_]*', text))\n\n    for kw in conclusion_keywords:\n        if len(kw) < 3:\n            continue\n        for ct in constraint_tokens:\n            if kw in ct or ct in kw:\n                return True\n    return False\n\n\ndef filter_constraints_by_strategy(per_trace_constraints, strategy, conclusion_keywords):\n    \"\"\"Return filtered per-trace constraint lists based on strategy.\"\"\"\n    filtered = []\n    for trace_constraints in per_trace_constraints:\n        if strategy == \"full\":\n            filtered.append(trace_constraints)\n        elif strategy == \"signal\":\n            filtered.append([\n                c for c in trace_constraints\n                if constraint_references_conclusion(c, conclusion_keywords)\n            ])\n        elif strategy == \"premise\":\n            filtered.append([\n                c for c in trace_constraints\n                if not constraint_references_conclusion(c, conclusion_keywords)\n            ])\n        elif strategy == \"rules_only\":\n            filtered.append([\n                c for c in trace_constraints\n                if c.get(\"type\") == \"rule\"\n            ])\n        else:\n            filtered.append(trace_constraints)\n    return filtered\n\n\ndef run_maxsat_scoring(per_trace_constraints, traces, candidates, answer_counts):\n    \"\"\"Run dedup -> MAX-SAT -> scoring pipeline on constraint lists.\"\"\"\n    deduplicator = ConstraintDeduplicator()\n    solver = MaxSATSolver()\n    scorer = InvariantScorer()\n\n    unique = deduplicator.deduplicate(per_trace_constraints)\n    if not unique:\n        return None, None, {\"unique\": 0, \"satisfied\": 0, \"excluded\": 0}\n\n    result = solver.solve(unique, timeout_ms=10000)\n    scores = scorer.score(result, traces, candidates)\n    answer = scorer.select_answer(scores, answer_counts)\n\n    stats = {\n        \"unique\": len(unique),\n        \"satisfied\": len(result.satisfied),\n        \"excluded\": len(result.excluded),\n        \"total_weight\": result.total_weight,\n    }\n    return answer, scores, stats\n\n\ndef normalize_logic_answer(ans):\n    ans = str(ans).strip().lower()\n    if ans in (\"true\", \"yes\", \"correct\", \"entailment\"):\n        return \"True\"\n    if ans in (\"false\", \"no\", \"incorrect\", \"contradiction\"):\n        return \"False\"\n    if ans in (\"unknown\", \"uncertain\", \"undetermined\", \"neutral\"):\n        return \"Unknown\"\n    return ans.capitalize()\n\n\ndef main():\n    folio_data = load_folio_data()\n\n    with open(EXP_DIR / \"exp033_results.json\") as f:\n        exp033 = json.load(f)\n\n    pilot_results = exp033[\"results\"][:N_PILOT]\n    pids = [r[\"problem_id\"] for r in pilot_results]\n\n    strategies = [\"full\", \"signal\", \"premise\", \"rules_only\"]\n    results = {s: [] for s in strategies}\n    detail_rows = []\n\n    for i, pid in enumerate(pids):\n        prob = folio_data[pid]\n        gt = prob[\"answer\"]\n        conclusion_fol = prob.get(\"conclusion_fol\", \"\")\n        conclusion_kws = extract_conclusion_keywords(conclusion_fol)\n\n        cache = load_constraint_cache(pid)\n        per_trace = [t[\"constraints\"] for t in cache[\"per_trace\"]]\n\n        inter = load_intermediate(pid)\n        traces = inter[\"sica_result\"][\"traces\"]\n        for t in traces:\n            if t.get(\"answer\"):\n                t[\"answer\"] = normalize_logic_answer(t[\"answer\"])\n\n        candidates = sorted(set(t[\"answer\"] for t in traces if t[\"answer\"]))\n        answer_counts = Counter(t[\"answer\"] for t in traces if t[\"answer\"])\n\n        sc_answer = answer_counts.most_common(1)[0][0] if answer_counts else \"\"\n\n        row = {\n            \"pid\": pid,\n            \"gt\": gt,\n            \"sc_answer\": sc_answer,\n            \"sc_correct\": sc_answer == gt,\n            \"conclusion_fol\": conclusion_fol,\n            \"conclusion_keywords\": sorted(conclusion_kws),\n        }\n\n        for strategy in strategies:\n            filtered = filter_constraints_by_strategy(per_trace, strategy, conclusion_kws)\n            n_constraints = sum(len(c) for c in filtered)\n\n            answer, scores, stats = run_maxsat_scoring(\n                filtered, traces, candidates, answer_counts\n            )\n            if answer is None:\n                answer = sc_answer\n\n            correct = answer == gt\n            results[strategy].append(correct)\n\n            row[f\"{strategy}_answer\"] = answer\n            row[f\"{strategy}_correct\"] = correct\n            row[f\"{strategy}_n_constraints\"] = n_constraints\n            row[f\"{strategy}_stats\"] = stats\n\n        detail_rows.append(row)\n        print(f\"  [{i+1:2d}/{N_PILOT}] {pid}: gt={gt}  sc={sc_answer}({'O' if row['sc_correct'] else 'X'})  \"\n              f\"full={row['full_answer']}({'O' if row['full_correct'] else 'X'})  \"\n              f\"signal={row['signal_answer']}({'O' if row['signal_correct'] else 'X'})  \"\n              f\"premise={row['premise_answer']}({'O' if row['premise_correct'] else 'X'})  \"\n              f\"rules={row['rules_only_answer']}({'O' if row['rules_only_correct'] else 'X'})\")\n\n    print(\"\\n\" + \"=\" * 60)\n    print(f\"Direction C Pilot Results -- {N_PILOT} problems (exp033 Mistral-7B)\")\n    print(\"=\" * 60)\n\n    for strategy in strategies:\n        correct = sum(results[strategy])\n        total = len(results[strategy])\n        acc = correct / total if total else 0\n        print(f\"  {strategy:12s}: {correct}/{total} = {acc:.1%}\")\n\n    sc_correct = sum(r[\"sc_correct\"] for r in detail_rows)\n    print(f\"  {'SC':12s}: {sc_correct}/{N_PILOT} = {sc_correct/N_PILOT:.1%}\")\n\n    print(\"\\nConstraint retention (avg |filtered| / |full|):\")\n    for strategy in strategies:\n        if strategy == \"full\":\n            continue\n        ratios = []\n        for row in detail_rows:\n            full_n = row[\"full_n_constraints\"]\n            filt_n = row[f\"{strategy}_n_constraints\"]\n            if full_n > 0:\n                ratios.append(filt_n / full_n)\n        avg_ratio = sum(ratios) / len(ratios) if ratios else 0\n        print(f\"  {strategy:12s}: {avg_ratio:.1%}\")\n\n    print(\"\\nDisagreements with full SICA:\")\n    for strategy in [\"signal\", \"premise\", \"rules_only\"]:\n        diffs = []\n        for row in detail_rows:\n            if row[f\"{strategy}_answer\"] != row[\"full_answer\"]:\n                diffs.append(row[\"pid\"])\n        print(f\"  {strategy:12s}: {len(diffs)} disagreements -- {diffs}\")\n\n    print(\"\\nFlip analysis (vs full baseline):\")\n    for strategy in [\"signal\", \"premise\", \"rules_only\"]:\n        gained = []\n        lost = []\n        for row in detail_rows:\n            fc = row[\"full_correct\"]\n            sc = row[f\"{strategy}_correct\"]\n            if not fc and sc:\n                gained.append(row[\"pid\"])\n            elif fc and not sc:\n                lost.append(row[\"pid\"])\n        print(f\"  {strategy:12s}: gained={gained}  lost={lost}  net={len(gained)-len(lost):+d}\")\n\n    output = {\n        \"summary\": {\n            \"n_problems\": N_PILOT,\n            \"strategies\": {\n                s: {\n                    \"accuracy\": sum(results[s]) / len(results[s]),\n                    \"correct\": sum(results[s]),\n                }\n                for s in strategies\n            },\n            \"sc_accuracy\": sc_correct / N_PILOT,\n        },\n        \"details\": detail_rows,\n    }\n\n    out_path = \"/root/symb_invariant_consensus/results/direction_c_counterfactual_pilot.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"Script written OK\""
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T15:32:04.519483+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T15:32:04.519642+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, sys\nsys.path.insert(0, '.')\nfrom sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver\nfrom sica.scorer import InvariantScorer\nprint('Imports OK')\n\n# Check data\ndata = json.load(open('data/folio_full.json'))\nprint(f'FOLIO: {len(data)} problems')\n\ncache = json.load(open('results/exp033_mistral_7b_folio204/constraint_cache/folio_0.json'))\nprint(f'Cache traces: {len(cache[\\\"per_trace\\\"])}')\nprint(f'First trace constraints: {len(cache[\\\"per_trace\\\"][0][\\\"constraints\\\"])}')\n\nexp = json.load(open('results/exp033_mistral_7b_folio204/exp033_results.json'))\nprint(f'Exp033: {len(exp[\\\"results\\\"])} results')\nprint(f'First 20 IDs: {[r[\\\"problem_id\\\"] for r in exp[\\\"results\\\"][:20]]}')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, sys\nsys.path.insert(0, '.')\nfrom sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver\nfrom sica.scorer import InvariantScorer\nprint('Imports OK')\n\n# Check data\ndata = json.load(open('data/folio_full.json'))\nprint(f'FOLIO: {len(data)} problems')\n\ncache = json.load(open('results/exp033_mistral_7b_folio204/constraint_cache/folio_0.json'))\nprint(f'Cache traces: {len(cache[\\\"per_trace\\\"])}')\nprint(f'First trace constraints: {len(cache[\\\"per_trace\\\"][0][\\\"constraints\\\"])}')\n\nexp = json.load(open('results/exp033_mistral_7b_folio204/exp033_results.json'))\nprint(f'Exp033: {len(exp[\\\"results\\\"])} results')\nprint(f'First 20 IDs: {[r[\\\"problem_id\\\"] for r in exp[\\\"results\\\"][:20]]}')\n\""
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T15:32:04.519791+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Imports OK\\nFOLIO: 204 problems\\nCache traces: 12\\nFirst trace constraints: 6\\nExp033: 204 results\\nFirst 20 IDs: ['folio_0', 'folio_1', 'folio_2', 'folio_3', 'folio_4', 'folio_5', 'folio_6', 'folio_7', 'folio_8', 'folio_9', 'folio_10', 'folio_11', 'folio_12', 'folio_13', 'folio_14', 'folio_15', 'folio_16', 'folio_17', 'folio_18', 'folio_19']\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.72}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T15:32:04.519963+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 direction_c_counterfactual.py 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 direction_c_counterfactual.py 2>&1"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T15:32:04.520136+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  [ 1/20] folio_0: gt=Unknown  sc=Unknown(O)  full=Unknown(O)  signal=Unknown(O)  premise=Unknown(O)  rules=Unknown(O)\\n  [ 2/20] folio_1: gt=True  sc=True(O)  full=True(O)  signal=True(O)  premise=True(O)  rules=True(O)\\n  [ 3/20] folio_2: gt=False  sc=Unknown(X)  full=Unknown(X)  signal=Unknown(X)  premise=Unknown(X)  rules=Unknown(X)\\n  [ 4/20] folio_3: gt=Unknown  sc=Unknown(O)  full=Unknown(O)  signal=Unknown(O)  premise=Unknown(O)  rules=Unknown(O)\\n  [ 5/20] folio_4: gt=Unknown  sc=Unknown(O)  full=Unknown(O)  signal=Unknown(O)  premise=Unknown(O)  rules=Unknown(O)\\n  [ 6/20] folio_5: gt=True  sc=Unknown(X)  full=Unknown(X)  signal=Unknown(X)  premise=Unknown(X)  rules=Unknown(X)\\n  [ 7/20] folio_6: gt=True  sc=Unknown(X)  full=Unknown(X)  signal=Unknown(X)  premise=Unknown(X)  rules=Unknown(X)\\n  [ 8/20] folio_7: gt=Unknown  sc=Unknown(O)  full=Unknown(O)  signal=Unknown(O)  premise=Unknown(O)  rules=Unknown(O)\\n  [ 9/20] folio_8: gt=Unknown  sc=Unknown(O)  full=False(X)  signal=False(X)  premise=Unknown(O)  rules=Unknown(O)\\n  [10/20] folio_9: gt=True  sc=True(O)  full=True(O)  signal=True(O)  premise=True(O)  rules=True(O)\\n  [11/20] folio_10: gt=False  sc=Unknown(X)  full=False(O)  signal=False(O)  premise=False(O)  rules=Unknown(X)\\n  [12/20] folio_11: gt=Unknown  sc=Unknown(O)  full=Unknown(O)  signal=Unknown(O)  premise=Unknown(O)  rules=Unknown(O)\\n  [13/20] folio_12: gt=True  sc=True(O)  full=True(O)  signal=True(O)  premise=True(O)  rules=True(O)\\n  [14/20] folio_13: gt=Unknown  sc=Unknown(O)  full=Unknown(O)  signal=Unknown(O)  premise=Unknown(O)  rules=Unknown(O)\\n  [15/20] folio_14: gt=False  sc=Unknown(X)  full=Unknown(X)  signal=False(O)  premise=Unknown(X)  rules=Unknown(X)\\n  [16/20] folio_15: gt=True  sc=True(O)  full=True(O)  signal=True(O)  premise=True(O)  rules=True(O)\\n  [17/20] folio_16: gt=Unknown  sc=Unknown(O)  full=Unknown(O)  signal=Unknown(O)  premise=Unknown
…[truncated 1648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-20T15:32:04.520336+00:00_

结果出来了。

**Direction C Pilot — 20 题 (exp033 Mistral-7B)**

| 策略 | Accuracy | vs Full |
|------|----------|---------|
| **full** (SICA baseline) | 13/20 = 65.0% | — |
| **signal** (仅 conclusion-referencing) | 13/20 = 65.0% | net 0 |
| **premise** (去掉 conclusion-referencing) | **14/20 = 70.0%** | **net +1** |
| **rules_only** (去掉 fact 类型) | 12/20 = 60.0% | net -1 |
| SC | 13/20 = 65.0% | — |

**关键发现：**

1. **premise 策略是唯一有正向信号的**：保留 40.2% 的 constraints（去掉了引用 conclusion 的），accuracy +5pp (65%→70%)。在 folio_8 上修正了 full SICA 的错误，没有引入新错误。

2. **signal 策略（纯 counterfactual）中性**：保留 59.8% 的 constraints，精度持平。在 folio_14 上翻对了一题，但 folio_17 翻错了一题，net=0。

3. **rules_only 策略负面**：过于激进（只保留 35.6%），丢掉了 folio_10 和 folio_17。

4. **folio_8 是 premise 策略的一个干净 gain**：去掉 conclusion-referencing constraints 后，SICA 从 False→Unknown（正确答案），说明那些引用 conclusion 的 constraints 确实引入了偏差。

20 题样本偏小，但 **premise-only 方向有微弱正信号**，值得扩到全 204 题验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_experiment_dir-c-counterfactual_20260520T152704"
}
```

</details>

---
