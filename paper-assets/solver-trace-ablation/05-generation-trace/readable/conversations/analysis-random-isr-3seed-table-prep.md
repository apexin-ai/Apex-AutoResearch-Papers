# analysis random isr 3seed table prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_analysis_random-isr-3seed-table-prep_20260515T180802.jsonl`
- **Structured JSON:** [`8edabb09ac44b8486747.json`](../../sessions/8e/8edabb09ac44b8486747.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-15T18:11:11.786599+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T18:11:11.787117+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T18:11:11.787610+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": "{'exp_id': 'plan018-additive-random-b01-s42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "filters": "{'exp_id': 'plan018-additive-random-b01-s42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T18:11:11.787909+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3533}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T18:11:11.788146+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": "{'exp_id': 'plan018-additive-random-b01-s43-r3'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "filters": "{'exp_id': 'plan018-additive-random-b01-s43-r3'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T18:11:11.788382+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3117}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T18:11:11.788601+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": "{'exp_id': 'plan002-additive-b01-s42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "filters": "{'exp_id': 'plan002-additive-b01-s42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T18:11:11.788851+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3056}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T18:11:11.789075+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": "{'exp_id': 'plan002-additive-b01-s43-r2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "filters": "{'exp_id': 'plan002-additive-b01-s43-r2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T18:11:11.789298+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": "{'exp_id': 'plan002-additive-b01-s44'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "filters": "{'exp_id': 'plan002-additive-b01-s44'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T18:11:11.789518+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6473}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T18:11:11.789756+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4554}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T18:11:11.789999+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": "{'exp_id': 'plan018-additive-random-b01-s44-r2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "filters": "{'exp_id': 'plan018-additive-random-b01-s44-r2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T18:11:11.790229+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3225}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T18:11:11.790483+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "limit": "0",
  "fields": "['exp_id', 'status', 'conclusion', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "limit": "0",
    "fields": "['exp_id', 'status', 'conclusion', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T18:11:11.792057+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan018-additive-random-b01-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.79, \"eval_mean_isr\": 0.1038, \"eval_isr_std\": 0.1369, \"eval_median_isr\": 0.0357, \"eval_proved_only_isr\": 0.1314, \"eval_n_proved\": 79, \"eval_n_problems\": 100, \"tautological_collapse\": false, \"h7_count\": 0, \"h7_rate\": 0, \"h7a_count\": 0, \"h7b_count\": 0, \"h1_count\": 58, \"h1_rate\": 0.7342, \"h8_count\": 4, \"h8_rate\": 0.0506, \"genuine_count\": 18, \"genuine_rate\": 0.2278, \"taxonomy_tool\": \"classify_h7.py standard (2026-05-15)\", \"taxonomy_note\": \"Re-classified with current classify_h7.py. Old values: genuine_strict=12 (H1_exact=56, H1_near=8, H8=3). New standard: H1=58 (2 former H1-near now H1), H8=4, genuine=18. Standard definition: proved - H7 - H1 - H8.\"}}, \"plan018-additive-random-b01-s43-r3\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.94, \"n_proved\": 94, \"n_problems\": 100, \"mean_isr\": 0.1406, \"isr_std\": null, \"proved_only_isr\": 0.1495, \"h7_count\": 36, \"h7_rate\": 0.383, \"h7a_count\": 36, \"h7b_count\": 0, \"h1_count\": 56, \"h1_rate\": 0.596, \"h8_count\": 1, \"h8_rate\": 0.011, \"genuine_count\": 1, \"genuine_rate\": 0.0106, \"train_prove_rate\": 0.5825, \"train_mean_isr\": 0.1266}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s44-r2\": {\"status\": \"RUNNING\"}, \"plan002-additive-b01-s43-r2\": {\"status\": \"DONE\", \"metrics\": {\"eval_n_problems\": 100, \"eval_n_proved\": 61, \"eval_prove_rate\": 0.61, \"eval_mean_isr\": 0.5063, \"eval_isr_std\": 0.4518, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.8301, \"h7a_count\": 59, \"h7b_count\": 2, \"h7_count\": 61, \"h7_rate\": 1, \"h1_count\": 0, \"h1_rate\": 0, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"proved_single_premise_ratio\": 1, \"content_independent_predicates\"
…[truncated 38648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T18:11:11.792495+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T18:11:11.792791+00:00_

_deprecated
_project
analysis_random_vs_isr_b01_interim.md
bootstrap_ci_results.json
claim_coverage_audit.md
component_count_analysis.md
data_consistency_report.md
diagnose_phase1_r3.md
dream_reports
evidence_chain_status.md
evidence_tables_d051.md
figure_quality_report.md
genuine_isr_crosscheck.md
grpo_exec_only.yaml
grpo_exec_sta.yaml
hacking_characterization_report.md
hacking_taxonomy.md
hacking_taxonomy_comparison.md
inc05_literature_linkage.md
launch_phase1.sh
literature_goodhart.md
literature_map.yaml
manifest.yaml
paper-audit
paper_compile_audit.md
paper_consistency_audit.md
paper_figures
paper_number_audit.md
paper_number_audit_2026-05-15.json
paper_review_r1.md
paper_table1_evidence.md
paper_tables
paper_tables_draft.md
phase1_r2_diagnosis.md
plan001-exec-only-s43-1000-r2
plan001-exec-only-s43-r4
plan001-exec-only-s44
plan002-additive-b01-s42
plan002-additive-b01-s42-1000
plan002-additive-b01-s43
plan002-additive-b01-s43-r2
plan005_negative_literature.md
plan006
plan006_eval_compatibility.md
plan006_readiness.md
plan006_readiness_report.md
plan012
plan013-random-reward-s42-r4
plan013_analysis.md
plan014_design.md
plan016-extended-1000-s42
plan017-additive-random-s42
plan018
plan018-additive-random-b01-s42
plan018-additive-random-b01-s42-1000-r3
plan018-additive-random-b01-s42-1000-r3_analysis.json
preflight_prolog_sta_eval.md
prolog_sta_literature_linkage.md
prolog_sta_premise_count_analysis.md
reference_audit_report.md
reference_final_audit.md
registry_extract.json
review_issues.yaml
review_reports
s43_1000_n_components_investigation.md
section_4_3_1000step_draft.md
seed44_readiness.md
sft_3seed_pooled_ci.json
sta-phase0-baseline
stats_recalc_checklist.md
table1_comparison.md
table1_data.json
table1_draft.md
table2_draft.md
table2_hacking_taxonomy.csv
table2_hacking_taxonomy.tex
table_data.json
table_data_compilation.md
table_drafts_v2.md
tables_draft_v1.md
tex_number_audit_20260515.md
train_grpo.py
training_progress_check.md
wilson_ci.py
wilson_ci_complet
…[truncated 96 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T18:11:11.793147+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/3seed_comparison_table.md",
  "content": "# Random β=0.1 vs ISR β=0.1: Cross-Seed Comparison Table\n\nGenerated: 2026-05-15 | Source: project registry (solver-trace-ablation)\n\n## Data Quality Note\n\n**plan018-additive-random-b01-s42** was reclassified on 2026-05-15 with updated classify_h7.py.\n- Old values: H7=0, H1_exact=56, H1_near=8, H8=3, genuine_strict=12\n- New values: H7=0, H1=58, H8=4, genuine=18\n- **Consistency issue**: H7+H1+H8+genuine = 0+58+4+18 = 80 ≠ n_proved=79. One sample double-counted. Needs investigation.\n\nAll other experiments sum correctly (H7+H1+H8+genuine = n_proved).\n\n---\n\n## ISR β=0.1 — Per-Seed Results (3 seeds)\n\n| Metric | s42 | s43-r2 | s44 |\n|--------|-----|--------|-----|\n| exp_id | plan002-additive-b01-s42 | plan002-additive-b01-s43-r2 | plan002-additive-b01-s44 |\n| Prove Rate | 0.81 | 0.61 | 0.89 |\n| n_proved | 81 | 61 | 89 |\n| H7 | 13 (16.0%) | 61 (100%) | 89 (100%) |\n| H1 | 42 (51.9%) | 0 (0%) | 0 (0%) |\n| H8 | 12 (14.8%) | 0 (0%) | 0 (0%) |\n| genuine | 14 (17.3%) | 0 (0%) | 0 (0%) |\n| mean ISR | 0.3365 | 0.5063 | 0.803 |\n\n### ISR β=0.1 — Pooled Statistics\n\n| Metric | Value |\n|--------|-------|\n| total n_proved | 231 |\n| mean PR ± std | 0.770 ± 0.144 |\n| pooled genuine | 14/231 = 6.06% |\n| pooled H7 | 163/231 = 70.56% |\n| pooled H1 | 42/231 = 18.18% |\n| pooled H8 | 12/231 = 5.19% |\n| mean genuine_rate ± std | 5.77% ± 9.99% |\n\nPer-seed genuine rates: 17.3%, 0%, 0% — high variance driven by s42.\n\n**Key pattern**: 2/3 seeds (s43, s44) collapsed to 100% H7 tautology. Only s42 retained genuine proofs.\n\n---\n\n## Random β=0.1 — Per-Seed Results (2 seeds; s44-r2 RUNNING)\n\n| Metric | s42 | s43-r3 |\n|--------|-----|--------|\n| exp_id | plan018-additive-random-b01-s42 | plan018-additive-random-b01-s43-r3 |\n| Prove Rate | 0.79 | 0.94 |\n| n_proved | 79 | 94 |\n| H7 | 0 (0%) | 36 (38.3%) |\n| H1 | 58 (73.4%) | 56 (59.6%) |\n| H8 | 4 (5.1%) | 1 (1.1%) |\n| genuine | 18 (22.8%)* | 1 (1.1%) |\n| mean ISR | 0.1038 | 0.1406 |\n\n*See data quality note above. Old genuine_strict=12 (15.19%) before reclassification.\n\n### Random β=0.1 — Pooled Statistics (2-seed, provisional)\n\n| Metric | Value |\n|--------|-------|\n| total n_proved | 173 |\n| mean PR | 0.865 (range: 0.79–0.94) |\n| pooled genuine | 19/173 = 10.98% |\n| pooled H7 | 36/173 = 20.81% |\n| pooled H1 | 114/173 = 65.90% |\n| pooled H8 | 5/173 = 2.89% |\n| per-seed genuine rates | 22.8%, 1.1% |\n\n**Key pattern**: Both seeds dominated by H1 (conclusion-in-premise). s42 has 0% H7 while s43-r3 has 38.3% H7. High inter-seed variance.\n\n---\n\n## Side-by-Side Comparison\n\n| Metric | ISR β=0.1 (3-seed) | Random β=0.1 (2-seed) |\n|--------|--------------------|-----------------------|\n| mean PR | 0.770 ± 0.144 | 0.865 |\n| pooled genuine rate | 6.06% (14/231) | 10.98% (19/173) |\n| pooled H7 rate | 70.56% (163/231) | 20.81% (36/173) |\n| pooled H1 rate | 18.18% (42/231) | 65.90% (114/173) |\n| pooled H8 rate | 5.19% (12/231) | 2.89% (5/173) |\n| dominant failure mode | H7 tautology | H1 conclusion embedding |\n| seeds with genuine=0 | 2/3 | 0/2 |\n\n### Interpretation\n\n1. **ISR reward amplifies H7 tautology**: 70.6% pooled H7 vs 20.8% for Random. ISR incentivizes maximizing indispensability → model discovers tautological shortcut (single-premise = conclusion).\n2. **Random reward amplifies H1 embedding**: 65.9% pooled H1 vs 18.2% for ISR. Without ISR pressure, model defaults to embedding conclusion in premises.\n3. **Neither method produces reliable genuine proofs**: ISR pooled genuine 6.1%, Random pooled genuine 11.0%. Both far below SFT baseline (~93% genuine).\n4. **Both show extreme inter-seed variance**: ISR ranges 0%–17.3% genuine; Random ranges 1.1%–22.8%. Single-seed results unreliable.\n\n---\n\n## Pending\n\n- [ ] Random s44-r2 (plan018-additive-random-b01-s44-r2): RUNNING. Add to table when complete.\n- [ ] Investigate s42 reclassification sum mismatch (80 vs 79).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/3seed_comparison_table.md",
    "content": "# Random β=0.1 vs ISR β=0.1: Cross-Seed Comparison Table\n\nGenerated: 2026-05-15 | Source: project registry (solver-trace-ablation)\n\n## Data Quality Note\n\n**plan018-additive-random-b01-s42** was reclassified on 2026-05-15 with updated classify_h7.py.\n- Old values: H7=0, H1_exact=56, H1_near=8, H8=3, genuine_strict=12\n- New values: H7=0, H1=58, H8=4, genuine=18\n- **Consistency issue**: H7+H1+H8+genuine = 0+58+4+18 = 80 ≠ n_proved=79. One sample double-counted. Needs investigation.\n\nAll other experiments sum correctly (H7+H1+H8+genuine = n_proved).\n\n---\n\n## ISR β=0.1 — Per-Seed Results (3 seeds)\n\n| Metric | s42 | s43-r2 | s44 |\n|--------|-----|--------|-----|\n| exp_id | plan002-additive-b01-s42 | plan002-additive-b01-s43-r2 | plan002-additive-b01-s44 |\n| Prove Rate | 0.81 | 0.61 | 0.89 |\n| n_proved | 81 | 61 | 89 |\n| H7 | 13 (16.0%) | 61 (100%) | 89 (100%) |\n| H1 | 42 (51.9%) | 0 (0%) | 0 (0%) |\n| H8 | 12 (14.8%) | 0 (0%) | 0 (0%) |\n| genuine | 14 (17.3%) | 0 (0%) | 0 (0%) |\n| mean ISR | 0.3365 | 0.5063 | 0.803 |\n\n### ISR β=0.1 — Pooled Statistics\n\n| Metric | Value |\n|--------|-------|\n| total n_proved | 231 |\n| mean PR ± std | 0.770 ± 0.144 |\n| pooled genuine | 14/231 = 6.06% |\n| pooled H7 | 163/231 = 70.56% |\n| pooled H1 | 42/231 = 18.18% |\n| pooled H8 | 12/231 = 5.19% |\n| mean genuine_rate ± std | 5.77% ± 9.99% |\n\nPer-seed genuine rates: 17.3%, 0%, 0% — high variance driven by s42.\n\n**Key pattern**: 2/3 seeds (s43, s44) collapsed to 100% H7 tautology. Only s42 retained genuine proofs.\n\n---\n\n## Random β=0.1 — Per-Seed Results (2 seeds; s44-r2 RUNNING)\n\n| Metric | s42 | s43-r3 |\n|--------|-----|--------|\n| exp_id | plan018-additive-random-b01-s42 | plan018-additive-random-b01-s43-r3 |\n| Prove Rate | 0.79 | 0.94 |\n| n_proved | 79 | 94 |\n| H7 | 0 (0%) | 36 (38.3%) |\n| H1 | 58 (73.4%) | 56 (59.6%) |\n| H8 | 4 (5.1%) | 1 (1.1%) |\n| genuine | 18 (22.8%)* | 1 (1.1%) |\n| mean ISR | 0.1038 | 0.1406 |\n\n*See data quality note above. Old genuine_strict=12 (15.19%) before reclassification.\n\n### Random β=0.1 — Pooled Statistics (2-seed, provisional)\n\n| Metric | Value |\n|--------|-------|\n| total n_proved | 173 |\n| mean PR | 0.865 (range: 0.79–0.94) |\n| pooled genuine | 19/173 = 10.98% |\n| pooled H7 | 36/173 = 20.81% |\n| pooled H1 | 114/173 = 65.90% |\n| pooled H8 | 5/173 = 2.89% |\n| per-seed genuine rates | 22.8%, 1.1% |\n\n**Key pattern**: Both seeds dominated by H1 (conclusion-in-premise). s42 has 0% H7 while s43-r3 has 38.3% H7. High inter-seed variance.\n\n---\n\n## Side-by-Side Comparison\n\n| Metric | ISR β=0.1 (3-seed) | Random β=0.1 (2-seed) |\n|--------|--------------------|-----------------------|\n| mean PR | 0.770 ± 0.144 | 0.865 |\n| pooled genuine rate | 6.06% (14/231) | 10.98% (19/173) |\n| pooled H7 rate | 70.56% (163/231) | 20.81% (36/173) |\n| pooled H1 rate | 18.18% (42/231) | 65.90% (114/173) |\n| pooled H8 rate | 5.19% (12/231) | 2.89% (5/173) |\n| dominant failure mode | H7 tautology | H1 conclusion embedding |\n| seeds with genuine=0 | 2/3 | 0/2 |\n\n### Interpretation\n\n1. **ISR reward amplifies H7 tautology**: 70.6% pooled H7 vs 20.8% for Random. ISR incentivizes maximizing indispensability → model discovers tautological shortcut (single-premise = conclusion).\n2. **Random reward amplifies H1 embedding**: 65.9% pooled H1 vs 18.2% for ISR. Without ISR pressure, model defaults to embedding conclusion in premises.\n3. **Neither method produces reliable genuine proofs**: ISR pooled genuine 6.1%, Random pooled genuine 11.0%. Both far below SFT baseline (~93% genuine).\n4. **Both show extreme inter-seed variance**: ISR ranges 0%–17.3% genuine; Random ranges 1.1%–22.8%. Single-seed results unreliable.\n\n---\n\n## Pending\n\n- [ ] Random s44-r2 (plan018-additive-random-b01-s44-r2): RUNNING. Add to table when complete.\n- [ ] Investigate s42 reclassification sum mismatch (80 vs 79).\n"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T18:11:11.793478+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/3seed_comparison_table.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T18:11:11.793728+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "3seed_comparison_table",
  "type": "report",
  "description": "Random β=0.1 vs ISR β=0.1 cross-seed comparison table with pooled statistics. ISR 3-seed complete, Random 2-seed provisional (s44-r2 running).",
  "project": "solver-trace-ablation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/3seed_comparison_table.md",
  "tags": "['cross-seed', 'comparison', 'random-vs-isr', 'beta-0.1', 'taxonomy']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "3seed_comparison_table",
    "type": "report",
    "description": "Random β=0.1 vs ISR β=0.1 cross-seed comparison table with pooled statistics. ISR 3-seed complete, Random 2-seed provisional (s44-r2 running).",
    "project": "solver-trace-ablation",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/3seed_comparison_table.md",
    "tags": "['cross-seed', 'comparison', 'random-vs-isr', 'beta-0.1', 'taxonomy']"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T18:11:11.794005+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_c00dd1\", \"name\": \"3seed_comparison_table\", \"type\": \"report\", \"description\": \"Random β=0.1 vs ISR β=0.1 cross-seed comparison table with pooled statistics. ISR 3-seed complete, Random 2-seed provisional (s44-r2 running).\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/report/3seed_comparison_table.md\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T18:11:04.822618+00:00\", \"tags\": [\"cross-seed\", \"comparison\", \"random-vs-isr\", \"beta-0.1\", \"taxonomy\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-15T18:11:11.794309+00:00_

产出已写入并注册。

**发现一个数据问题**：plan018-additive-random-b01-s42 在 2026-05-15 被重新分类，registry 当前值 (H1=58, H8=4, genuine=18) 与你提供的旧值 (H1=56, H8=3, genuine_strict=12) 不一致。且新值存在内部矛盾：H7+H1+H8+genuine = 80 ≠ n_proved=79，有一个 sample 被重复计数。需要排查。

**核心结论**：
- ISR pooled genuine 6.06% (14/231), dominant failure = H7 tautology (70.6%)
- Random pooled genuine 10.98% (19/173, 2-seed provisional), dominant failure = H1 embedding (65.9%)
- 两种方法的 genuine rate 都远低于 SFT baseline (~93%)，且 inter-seed variance 极大

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_random-isr-3seed-table-prep_20260515T180802"
}
```

</details>

---
