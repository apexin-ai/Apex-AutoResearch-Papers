# analysis fk excess agreement

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_analysis_fk_excess_agreement_20260515T121311.jsonl`
- **Structured JSON:** [`ffbc070ae02ac198dd4c.json`](../../sessions/ff/ffbc070ae02ac198dd4c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-15T12:15:10.204736+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T12:15:10.205250+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T12:15:10.205526+00:00_

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
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
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

_source line 4 · 2026-05-15T12:15:10.205750+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fleiss|kappa",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fleiss|kappa",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T12:15:10.206038+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bootstrap_ci_nscaling\\nbootstrap_ci_summary.json\\nbootstrap_ci_tables.tex\\nconditional_filter_diagnosis.json\\nexp001_n16_seed123\\nexp001_n16_seed123_200only\\nexp001_n16_seed123_200only_backup\\nexp001_n16_seed123_full\\nexp001_n16_seed123_run.log\\nexp001_n16_seed42\\nexp001_n16_seed42_200only_backup\\nexp001_n16_seed42_run.log\\nexp001_n16_seed456\\nexp001_n16_seed456_200only\\nexp001_n16_seed456_run.log\\nexp001_seed123_t10_full\\nexp001_seed123_t10_full.log\\nexp001_seed456_t10_full\\nexp001_seed456_t10_full.log\\nexp002_conll2003\\nexp003_wnut17_dryrun\\nexp003_wnut17_eval\\nexp003_wnut17_eval.log\\nexp003_wnut17_pilot\\nexp003_wnut17_pilot.log\\nexp004_re_diagnostic\\nexp004v2_re_diagnostic\\nexp007_llama_dryrun\\nexp007_llama_inference\\nexp008_re_n16\\nexp008_re_n16_200only\\nexp008_re_n16_t10_full\\nexp008_re_n16_t10_full.log\\nexp009_stratification_results.json\\nexp010_selection_curves\\nexp016_signal_ensemble\\nexp018_3seed_5signal_results.json\\nexp_001_seed123_v2\\nexp_001_seed123_v2_r1024\\nexp_001_seed42_v2\\nexp_001_seed42_v2_r1024\\nexp_001_seed456_v2\\nexp_001_seed456_v2_ner\\nexp_001_seed456_v2_ner.log\\nexp_001_seed456_v2_ner_r1024\\nexp_002_conll_n16\\nexp_002_conll_n16.log\\nexp_002_conll_n16_r1024\\nexp_003_wnut17_v2_infer\\nexp_005_v2_temperature\\nexp_006_v2\\nexp_006_v2_run.log\\nexp_007_llama_n16\\nexp_007_llama_n16.log\\nexp_007_llama_n16_r1024\\nexp_007_llama_seed123\\nexp_007_llama_seed456\\nexp_008_re_n16_v2\\nexp_008_re_seed123\\nexp_009_v2\\nexp_009_v2_re_rerun\\nexp_009_v2_run.log\\nexp_011_ood_analysis\\nexp_011_ood_conll_to_scierc\\nexp_011_ood_scierc_to_conll\\nexp_011_ood_scierc_to_conll_run.log\\nexp_012_logprob\\nexp_012_rerun_1024\\nexp_015_unified\\nexp_015_v2\\nexp_016_rerun_1024\\nexp_016_v2\\nexp_017_llama_conll_infer\\nexp_017_llama_conll_infer.log\\nexp_017_llama_conll_n16\\nexp_017_llama_conll_n16_r1024\\nexp_017_llama_conll_n16_r1024_run.log\\nexp_017_llama
…[truncated 1099 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T12:15:10.206471+00:00_

Found 250 files limit: 250
logs/workers/worker_analysis_fk_excess_agreement_20260515T121311.log
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_paper_agent.jsonl
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer.jsonl
logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl
logs/chats/feishu_group_oc_3897c2857f11615119e277e820eae311_director.jsonl
docs/paper/main.aux
docs/paper/main.bbl
docs/paper/sections/appendix.tex
registry.yaml
artifacts/manifest.yaml
docs/paper/sections/introduction.tex
docs/paper/references.bib
docs/paper/sections/method.tex
decisions.yaml
logs/workers/worker_code_exp_011_ood_cross_dataset_20260515T113645.log
logs/workers/worker_ops_registry_metrics_update_20260515T113729.log
artifacts/analyze_ood_signals.py
logs/workers/worker_analysis_n16_3seed_scs_20260515T113242.log
logs/workers/worker_analysis_d072_paper_patch_inventory_20260515T113312.log
logs/workers/worker_analysis_ood_cross_dataset_feasibility_20260515T113259.log
logs/workers/worker_code_exp_017_llama_conll_submit_20260515T103759.log
logs/workers/worker_analysis_pending_exp_readiness_20260515T103205.log
logs/workers/worker_analysis_freeform_deep_analysis_20260515T102907.log
artifacts/dream_reports/dream_20260515T092545/meta.yaml
artifacts/dream_reports/dream_20260515T092545/logs/review_worst.log
artifacts/dream_reports/dream_20260515T092545/worst/review_report.md
artifacts/dream_reports/dream_20260515T092545/logs/review_median.log
artifacts/dream_reports/dream_20260515T092545/median/review_report.md
logs/chats/worker_code_exp_019_supervised_verifier_20260515T100946.jsonl
logs/workers/worker_code_exp_019_supervised_verifier_20260515T100946.log
logs/chats/archive/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer_20260515T102035_551765.jsonl
logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T102033_395761.jsonl
artifacts/evaluate_verifier.py
logs/chats/worker_analysis_n16_readiness_check_20260515T100959.j
…[truncated 14689 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T12:15:10.206927+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fleiss|kappa",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "-i": "True",
  "glob": "*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fleiss|kappa",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "-i": "True",
    "glob": "*.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T12:15:10.207192+00:00_

Found 56 files
artifacts/analyze_ood_signals.py
artifacts/evaluate_verifier.py
artifacts/re_conditional_analysis.py
artifacts/n8_bootstrap_ci.py
.venv/lib/python3.14/site-packages/matplotlib/tests/test_mathtext.py
.venv/lib/python3.14/site-packages/matplotlib/_mathtext_data.py
.venv/lib/python3.14/site-packages/scipy/stats/tests/test_sampling.py
.venv/lib/python3.14/site-packages/scipy/stats/tests/test_multivariate.py
.venv/lib/python3.14/site-packages/scipy/stats/tests/test_fit.py
.venv/lib/python3.14/site-packages/scipy/stats/tests/test_distributions.py
.venv/lib/python3.14/site-packages/scipy/stats/tests/test_continuous_basic.py
.venv/lib/python3.14/site-packages/scipy/stats/tests/test_continuous.py
.venv/lib/python3.14/site-packages/scipy/stats/_multivariate.py
.venv/lib/python3.14/site-packages/scipy/stats/_morestats.py
.venv/lib/python3.14/site-packages/scipy/stats/_distr_params.py
.venv/lib/python3.14/site-packages/scipy/stats/_distn_infrastructure.py
.venv/lib/python3.14/site-packages/scipy/stats/_continuous_distns.py
.venv/lib/python3.14/site-packages/scipy/stats/__init__.py
.venv/lib/python3.14/site-packages/scipy/spatial/transform/_rotation_xp.py
.venv/lib/python3.14/site-packages/scipy/signal/_filter_design.py
.venv/lib/python3.14/site-packages/scipy/optimize/_linprog_ip.py
.venv/lib/python3.14/site-packages/scipy/linalg/tests/test_matfuncs.py
.venv/lib/python3.14/site-packages/scipy/linalg/_expm_frechet.py
.venv/lib/python3.14/site-packages/scipy/integrate/tests/test_bvp.py
.venv/lib/python3.14/site-packages/scipy/integrate/_ivp/bdf.py
.venv/lib/python3.14/site-packages/fontTools/agl.py
.venv/lib/python3.14/site-packages/numpy/random/tests/test_randomstate.py
.venv/lib/python3.14/site-packages/numpy/random/tests/test_random.py
.venv/lib/python3.14/site-packages/numpy/random/tests/test_generator_mt19937.py
.venv/lib/python3.14/site-packages/pip/_vendor/pygments/filters/__init__.py
artifacts/figures/plot_all_figures.py
artifacts/exp_016_v2_ensemble.py
art
…[truncated 1147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T12:15:10.207457+00:00_

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
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
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

_source line 10 · 2026-05-15T12:15:10.207706+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"all_signals_5signal.json\\nauroc_5signal.json\\ncomparison.json\\nreliability_data_1024.json\\nreport.json\\nrun.log\\nsamples.jsonl\\nsamples_with_logprobs.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T12:15:10.208039+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T12:15:10.208314+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"report.json\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T12:15:10.208552+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T12:15:10.208792+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"report.json\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T12:15:10.209057+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16_r1024/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16_r1024/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T12:15:10.209315+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"report.json\\nrun.log\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T12:15:10.209747+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T12:15:10.209954+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"all_signals_report.json\\nreport.json\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T12:15:10.210190+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_r1024/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_r1024/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T12:15:10.210416+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"report.json\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T12:15:10.210672+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fleiss|kappa|def.*consistency",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py",
  "-i": "True",
  "output_mode": "content",
  "-n": "True",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fleiss|kappa|def.*consistency",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py",
    "-i": "True",
    "output_mode": "content",
    "-n": "True",
    "-C": "3"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T12:15:10.211093+00:00_

1-"""Consistency metrics for structured information extraction with self-consistency.
2-
3-Implements three complementary consistency measures over N sampled extractions:
4:1. Fleiss' Kappa (surface matching) — treats N samples as N raters on entity presence
5-2. Structural soft Jaccard — span-level soft overlap with Hungarian matching
6-3. Oracle best-of-N — upper-bound F1 by selecting the best sample per instance
7-
--
29-
30-
31-# ===================================================================
32:# 1. Fleiss' Kappa — surface‐level entity agreement
33-# ===================================================================
34-
35-def _extract_surface_keys(sample: Extraction, subtask: str) -> set[tuple]:
36:    """Extract surface-level keys from a sample for Fleiss' Kappa computation."""
37-    if subtask == "ner":
38-        return {(e["text"], e["type"]) for e in sample.get("entities", [])}
39-    elif subtask == "re":
--
49-        raise ValueError(f"Unknown subtask: {subtask}")
50-
51-
52:def fleiss_kappa_surface(samples: list[Extraction], subtask: str = "ner") -> float:
53:    """Compute Fleiss' kappa treating N LLM samples as N raters on item presence.
54-
55-    Items are subtask-dependent surface keys:
56-    - ner: (entity_text, entity_type)
--
62-        subtask: "ner", "re", or "eae".
63-
64-    Returns:
65:        Fleiss' kappa in [-1, 1].  Returns 1.0 for degenerate cases (≤1 unique
66-        item, perfect agreement, or undefined P_e).
67-    """
68-    n_raters = len(samples)
--
112-    if abs(1.0 - P_e) < 1e-12:
113-        return 1.0
114-
115:    kappa = (P_bar - P_e) / (1.0 - P_e)
116:    return float(kappa)
117-
118-
119-# ===================================================================
--
285-    return total_score / total_weight
286-
287-
288:def structural_consistency_soft_jaccard(
289-    samples: list[Extraction],
290-    subtask: str = "ner",
291-) -> float:
--
366-# Aggregate helper
367-# ===============================================
…[truncated 920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T12:15:10.211376+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples_with_logprobs.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples_with_logprobs.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T12:15:10.212018+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"X96-1059_sent000\\\", \\\"text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\", \\\"start\\\": 15, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 0, \\\"head_end\\\": 27, \\\"tail_start\\\": 103, \\\"tail_end\\\": 125}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 15, \\\"head_end\\\": 27, \\\"tail_start\\\": 31, \\\"tail_end\\\": 44}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"USED-FOR\\\", \\\"head_start\\\": 103, \\\"head_end\\\": 125, \\\"tail_start\\\": 129, \\\"tail_end\\\": 153}], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"
…[truncated 9068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T12:15:10.212350+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py",
  "offset": "52",
  "limit": "70"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py",
    "offset": "52",
    "limit": "70"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T12:15:10.212600+00:00_

52	def fleiss_kappa_surface(samples: list[Extraction], subtask: str = "ner") -> float:
53	    """Compute Fleiss' kappa treating N LLM samples as N raters on item presence.
54	
55	    Items are subtask-dependent surface keys:
56	    - ner: (entity_text, entity_type)
57	    - re: (head_text, tail_text, relation_type)
58	    - eae: (trigger_text, trigger_type, role, argument_text)
59	
60	    Args:
61	        samples: List of N extraction dicts.
62	        subtask: "ner", "re", or "eae".
63	
64	    Returns:
65	        Fleiss' kappa in [-1, 1].  Returns 1.0 for degenerate cases (≤1 unique
66	        item, perfect agreement, or undefined P_e).
67	    """
68	    n_raters = len(samples)
69	    if n_raters <= 1:
70	        return 1.0
71	
72	    # Collect unique keys and per-sample presence sets
73	    entity_sets: list[set[tuple]] = []
74	    all_keys: set[tuple] = set()
75	    for sample in samples:
76	        keys = _extract_surface_keys(sample, subtask)
77	        entity_sets.append(keys)
78	        all_keys |= keys
79	
80	    n_subjects = len(all_keys)
81	    if n_subjects <= 0:
82	        # All samples extracted nothing — perfect agreement on empty set
83	        return 1.0
84	
85	    key_list = sorted(all_keys)
86	
87	    # Build rating matrix: n_subjects × 2 (categories: absent=0, present=1)
88	    # n_ij = number of raters assigning subject i to category j
89	    rating = np.zeros((n_subjects, 2), dtype=np.int64)
90	    for es in entity_sets:
91	        for idx, key in enumerate(key_list):
92	            if key in es:
93	                rating[idx, 1] += 1
94	            else:
95	                rating[idx, 0] += 1
96	
97	    n = n_raters
98	    k = 2  # number of categories
99	
100	    # Check perfect agreement: every subject has all votes in one category
101	    if np.all(np.max(rating, axis=1) == n):
102	        return 1.0
103	
104	    # P_i for each subject
105	    P_i = (np.sum(rating ** 2, axis=1) - n) / (n * (n - 1))
106	    P_bar = np.mean(P_i)
107	
108	    #
…[truncated 465 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T12:15:10.212892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py",
  "offset": "35",
  "limit": "16"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py",
    "offset": "35",
    "limit": "16"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T12:15:10.213121+00:00_

35	def _extract_surface_keys(sample: Extraction, subtask: str) -> set[tuple]:
36	    """Extract surface-level keys from a sample for Fleiss' Kappa computation."""
37	    if subtask == "ner":
38	        return {(e["text"], e["type"]) for e in sample.get("entities", [])}
39	    elif subtask == "re":
40	        return {(r["head"], r["tail"], r["type"]) for r in sample.get("relations", [])}
41	    elif subtask == "eae":
42	        keys: set[tuple] = set()
43	        for ev in sample.get("events", []):
44	            t = ev.get("trigger", {})
45	            for arg in ev.get("arguments", []):
46	                keys.add((t.get("text", ""), t.get("type", ""), arg["role"], arg["text"]))
47	        return keys
48	    else:
49	        raise ValueError(f"Unknown subtask: {subtask}")
50	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T12:15:10.213408+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/autodl-tmp/struct_self_consist_ie/compute_fk_excess.py << 'PYEOF'\nimport json\nimport numpy as np\nimport sys\n\ndef extract_surface_keys(sample, subtask):\n    if subtask == \"ner\":\n        return {(e[\"text\"], e[\"type\"]) for e in sample.get(\"entities\", [])}\n    elif subtask == \"re\":\n        return {(r[\"head\"], r[\"tail\"], r[\"type\"]) for r in sample.get(\"relations\", [])}\n    else:\n        raise ValueError(f\"Unknown subtask: {subtask}\")\n\ndef fleiss_kappa_decomposed(samples, subtask=\"ner\"):\n    \"\"\"Returns (P_o, P_e, excess, kappa) for one instance.\"\"\"\n    n_raters = len(samples)\n    if n_raters <= 1:\n        return (1.0, 0.0, 1.0, 1.0)\n\n    entity_sets = []\n    all_keys = set()\n    for sample in samples:\n        keys = extract_surface_keys(sample, subtask)\n        entity_sets.append(keys)\n        all_keys |= keys\n\n    n_subjects = len(all_keys)\n    if n_subjects <= 0:\n        return (1.0, 0.0, 1.0, 1.0)\n\n    key_list = sorted(all_keys)\n    rating = np.zeros((n_subjects, 2), dtype=np.int64)\n    for es in entity_sets:\n        for idx, key in enumerate(key_list):\n            if key in es:\n                rating[idx, 1] += 1\n            else:\n                rating[idx, 0] += 1\n\n    n = n_raters\n    if np.all(np.max(rating, axis=1) == n):\n        return (1.0, 0.0, 1.0, 1.0)\n\n    P_i = (np.sum(rating ** 2, axis=1) - n) / (n * (n - 1))\n    P_bar = float(np.mean(P_i))  # P_o\n\n    p_j = np.sum(rating, axis=0) / (n_subjects * n)\n    P_e = float(np.sum(p_j ** 2))\n\n    excess = P_bar - P_e\n\n    if abs(1.0 - P_e) < 1e-12:\n        return (P_bar, P_e, excess, 1.0)\n\n    kappa = excess / (1.0 - P_e)\n    return (P_bar, P_e, excess, kappa)\n\nconfigs = [\n    {\n        \"name\": \"Qwen SciERC NER\",\n        \"path\": \"output/exp_012_rerun_1024/samples_with_logprobs.jsonl\",\n        \"subtask\": \"ner\",\n        \"n\": 8,\n    },\n    {\n        \"name\": \"Qwen SciERC RE\",\n        \"path\": \"output/exp_012_rerun_1024/samples_with_logprobs.jsonl\",\n        \"subtask\": \"re\",\n        \"n\": 8,\n    },\n    {\n        \"name\": \"Qwen CoNLL NER\",\n        \"path\": \"output/exp_002_conll_n16/samples.jsonl\",\n        \"subtask\": \"ner\",\n        \"n\": 8,\n        \"take_first_n\": 8,\n    },\n    {\n        \"name\": \"Qwen CoNLL NER N=16\",\n        \"path\": \"output/exp_002_conll_n16/samples.jsonl\",\n        \"subtask\": \"ner\",\n        \"n\": 16,\n    },\n    {\n        \"name\": \"LLaMA SciERC NER\",\n        \"path\": \"output/exp007_llama_inference/samples.jsonl\",\n        \"subtask\": \"ner\",\n        \"n\": 8,\n    },\n    {\n        \"name\": \"LLaMA SciERC RE\",\n        \"path\": \"output/exp007_llama_inference/samples.jsonl\",\n        \"subtask\": \"re\",\n        \"n\": 8,\n    },\n    {\n        \"name\": \"LLaMA CoNLL NER\",\n        \"path\": \"output/exp_017_llama_conll_infer/samples.jsonl\",\n        \"subtask\": \"ner\",\n        \"n\": 8,\n    },\n    {\n        \"name\": \"LLaMA CoNLL NER N=16\",\n        \"path\": \"output/exp_017_llama_conll_n16_r1024/samples.jsonl\",\n        \"subtask\": \"ner\",\n        \"n\": 16,\n    },\n]\n\nbase = \"/root/autodl-tmp/struct_self_consist_ie\"\nresults = []\n\nfor cfg in configs:\n    filepath = f\"{base}/{cfg['path']}\"\n    try:\n        with open(filepath) as f:\n            instances = [json.loads(line) for line in f if line.strip()]\n    except FileNotFoundError:\n        results.append({**cfg, \"status\": \"FILE_NOT_FOUND\"})\n        continue\n\n    po_list, pe_list, excess_list, fk_list = [], [], [], []\n    for inst in instances:\n        samples = inst[\"samples\"]\n        n_expected = cfg.get(\"take_first_n\", cfg[\"n\"])\n        if len(samples) < n_expected:\n            continue\n        samples = samples[:n_expected]\n\n        P_o, P_e, excess, kappa = fleiss_kappa_decomposed(samples, cfg[\"subtask\"])\n        po_list.append(P_o)\n        pe_list.append(P_e)\n        excess_list.append(excess)\n        fk_list.append(kappa)\n\n    if not fk_list:\n        results.append({**cfg, \"status\": \"NO_VALID_INSTANCES\"})\n        continue\n\n    fk_arr = np.array(fk_list)\n    results.append({\n        \"name\": cfg[\"name\"],\n        \"subtask\": cfg[\"subtask\"],\n        \"n\": cfg.get(\"take_first_n\", cfg[\"n\"]),\n        \"n_instances\": len(fk_list),\n        \"mean_po\": float(np.mean(po_list)),\n        \"mean_pe\": float(np.mean(pe_list)),\n        \"mean_excess\": float(np.mean(excess_list)),\n        \"mean_fk\": float(np.mean(fk_list)),\n        \"fk_p5\": float(np.percentile(fk_arr, 5)),\n        \"fk_p95\": float(np.percentile(fk_arr, 95)),\n        \"std_po\": float(np.std(po_list)),\n        \"std_pe\": float(np.std(pe_list)),\n        \"std_excess\": float(np.std(excess_list)),\n        \"std_fk\": float(np.std(fk_list)),\n        \"status\": \"OK\",\n    })\n\nprint(json.dumps(results, indent=2))\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python compute_fk_excess.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/autodl-tmp/struct_self_consist_ie/compute_fk_excess.py << 'PYEOF'\nimport json\nimport numpy as np\nimport sys\n\ndef extract_surface_keys(sample, subtask):\n    if subtask == \"ner\":\n        return {(e[\"text\"], e[\"type\"]) for e in sample.get(\"entities\", [])}\n    elif subtask == \"re\":\n        return {(r[\"head\"], r[\"tail\"], r[\"type\"]) for r in sample.get(\"relations\", [])}\n    else:\n        raise ValueError(f\"Unknown subtask: {subtask}\")\n\ndef fleiss_kappa_decomposed(samples, subtask=\"ner\"):\n    \"\"\"Returns (P_o, P_e, excess, kappa) for one instance.\"\"\"\n    n_raters = len(samples)\n    if n_raters <= 1:\n        return (1.0, 0.0, 1.0, 1.0)\n\n    entity_sets = []\n    all_keys = set()\n    for sample in samples:\n        keys = extract_surface_keys(sample, subtask)\n        entity_sets.append(keys)\n        all_keys |= keys\n\n    n_subjects = len(all_keys)\n    if n_subjects <= 0:\n        return (1.0, 0.0, 1.0, 1.0)\n\n    key_list = sorted(all_keys)\n    rating = np.zeros((n_subjects, 2), dtype=np.int64)\n    for es in entity_sets:\n        for idx, key in enumerate(key_list):\n            if key in es:\n                rating[idx, 1] += 1\n            else:\n                rating[idx, 0] += 1\n\n    n = n_raters\n    if np.all(np.max(rating, axis=1) == n):\n        return (1.0, 0.0, 1.0, 1.0)\n\n    P_i = (np.sum(rating ** 2, axis=1) - n) / (n * (n - 1))\n    P_bar = float(np.mean(P_i))  # P_o\n\n    p_j = np.sum(rating, axis=0) / (n_subjects * n)\n    P_e = float(np.sum(p_j ** 2))\n\n    excess = P_bar - P_e\n\n    if abs(1.0 - P_e) < 1e-12:\n        return (P_bar, P_e, excess, 1.0)\n\n    kappa = excess / (1.0 - P_e)\n    return (P_bar, P_e, excess, kappa)\n\nconfigs = [\n    {\n        \"name\": \"Qwen SciERC NER\",\n        \"path\": \"output/exp_012_rerun_1024/samples_with_logprobs.jsonl\",\n        \"subtask\": \"ner\",\n        \"n\": 8,\n    },\n    {\n        \"name\": \"Qwen SciERC RE\",\n        \"path\": \"output/exp_012_rerun_1024/samples_with_logprobs.jsonl\",\n        \"subtask\": \"re\",\n        \"n\": 8,\n    },\n    {\n        \"name\": \"Qwen CoNLL NER\",\n        \"path\": \"output/exp_002_conll_n16/samples.jsonl\",\n        \"subtask\": \"ner\",\n        \"n\": 8,\n        \"take_first_n\": 8,\n    },\n    {\n        \"name\": \"Qwen CoNLL NER N=16\",\n        \"path\": \"output/exp_002_conll_n16/samples.jsonl\",\n        \"subtask\": \"ner\",\n        \"n\": 16,\n    },\n    {\n        \"name\": \"LLaMA SciERC NER\",\n        \"path\": \"output/exp007_llama_inference/samples.jsonl\",\n        \"subtask\": \"ner\",\n        \"n\": 8,\n    },\n    {\n        \"name\": \"LLaMA SciERC RE\",\n        \"path\": \"output/exp007_llama_inference/samples.jsonl\",\n        \"subtask\": \"re\",\n        \"n\": 8,\n    },\n    {\n        \"name\": \"LLaMA CoNLL NER\",\n        \"path\": \"output/exp_017_llama_conll_infer/samples.jsonl\",\n        \"subtask\": \"ner\",\n        \"n\": 8,\n    },\n    {\n        \"name\": \"LLaMA CoNLL NER N=16\",\n        \"path\": \"output/exp_017_llama_conll_n16_r1024/samples.jsonl\",\n        \"subtask\": \"ner\",\n        \"n\": 16,\n    },\n]\n\nbase = \"/root/autodl-tmp/struct_self_consist_ie\"\nresults = []\n\nfor cfg in configs:\n    filepath = f\"{base}/{cfg['path']}\"\n    try:\n        with open(filepath) as f:\n            instances = [json.loads(line) for line in f if line.strip()]\n    except FileNotFoundError:\n        results.append({**cfg, \"status\": \"FILE_NOT_FOUND\"})\n        continue\n\n    po_list, pe_list, excess_list, fk_list = [], [], [], []\n    for inst in instances:\n        samples = inst[\"samples\"]\n        n_expected = cfg.get(\"take_first_n\", cfg[\"n\"])\n        if len(samples) < n_expected:\n            continue\n        samples = samples[:n_expected]\n\n        P_o, P_e, excess, kappa = fleiss_kappa_decomposed(samples, cfg[\"subtask\"])\n        po_list.append(P_o)\n        pe_list.append(P_e)\n        excess_list.append(excess)\n        fk_list.append(kappa)\n\n    if not fk_list:\n        results.append({**cfg, \"status\": \"NO_VALID_INSTANCES\"})\n        continue\n\n    fk_arr = np.array(fk_list)\n    results.append({\n        \"name\": cfg[\"name\"],\n        \"subtask\": cfg[\"subtask\"],\n        \"n\": cfg.get(\"take_first_n\", cfg[\"n\"]),\n        \"n_instances\": len(fk_list),\n        \"mean_po\": float(np.mean(po_list)),\n        \"mean_pe\": float(np.mean(pe_list)),\n        \"mean_excess\": float(np.mean(excess_list)),\n        \"mean_fk\": float(np.mean(fk_list)),\n        \"fk_p5\": float(np.percentile(fk_arr, 5)),\n        \"fk_p95\": float(np.percentile(fk_arr, 95)),\n        \"std_po\": float(np.std(po_list)),\n        \"std_pe\": float(np.std(pe_list)),\n        \"std_excess\": float(np.std(excess_list)),\n        \"std_fk\": float(np.std(fk_list)),\n        \"status\": \"OK\",\n    })\n\nprint(json.dumps(results, indent=2))\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python compute_fk_excess.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T12:15:10.213820+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"name\\\": \\\"Qwen SciERC NER\\\",\\n    \\\"subtask\\\": \\\"ner\\\",\\n    \\\"n\\\": 8,\\n    \\\"n_instances\\\": 551,\\n    \\\"mean_po\\\": 0.7472988758281732,\\n    \\\"mean_pe\\\": 0.5076475603232583,\\n    \\\"mean_excess\\\": 0.23965131550491497,\\n    \\\"mean_fk\\\": 0.3932668065534345,\\n    \\\"fk_p5\\\": -0.11355311355311361,\\n    \\\"fk_p95\\\": 1.0,\\n    \\\"std_po\\\": 0.13523910593212604,\\n    \\\"std_pe\\\": 0.20639527675051936,\\n    \\\"std_excess\\\": 0.29293307938889784,\\n    \\\"std_fk\\\": 0.30998344677591005,\\n    \\\"status\\\": \\\"OK\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"Qwen SciERC RE\\\",\\n    \\\"subtask\\\": \\\"re\\\",\\n    \\\"n\\\": 8,\\n    \\\"n_instances\\\": 551,\\n    \\\"mean_po\\\": 0.7255494741562376,\\n    \\\"mean_pe\\\": 0.48750281155326075,\\n    \\\"mean_excess\\\": 0.2380466626029769,\\n    \\\"mean_fk\\\": 0.29342166441787654,\\n    \\\"fk_p5\\\": -0.14285714285714285,\\n    \\\"fk_p95\\\": 1.0,\\n    \\\"std_po\\\": 0.15503110429600384,\\n    \\\"std_pe\\\": 0.24756178429463546,\\n    \\\"std_excess\\\": 0.3738954974210933,\\n    \\\"std_fk\\\": 0.39587715860302447,\\n    \\\"status\\\": \\\"OK\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"Qwen CoNLL NER\\\",\\n    \\\"subtask\\\": \\\"ner\\\",\\n    \\\"n\\\": 8,\\n    \\\"n_instances\\\": 3453,\\n    \\\"mean_po\\\": 0.8952663629123238,\\n    \\\"mean_pe\\\": 0.23819161608984724,\\n    \\\"mean_excess\\\": 0.6570747468224766,\\n    \\\"mean_fk\\\": 0.7212693184162104,\\n    \\\"fk_p5\\\": -0.14285714285714285,\\n    \\\"fk_p95\\\": 1.0,\\n    \\\"std_po\\\": 0.1466837432146799,\\n    \\\"std_pe\\\": 0.3022400657778882,\\n    \\\"std_excess\\\": 0.43038561604901276,\\n    \\\"std_fk\\\": 0.3924976993702876,\\n    \\\"status\\\": \\\"OK\\\"\\n  },\\n  {\\n    \\\"name\\\": \\\"Qwen CoNLL NER N=16\\\",\\n    \\\"subtask\\\": \\\"ner\\\",\\n    \\\"n\\\": 16,\\n    \\\"n_instances\\\": 34
…[truncated 2975 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T12:15:10.214115+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/fk_excess_agreement_all_configs.md",
  "content": "# FK Excess Agreement — All Configurations\n\nFleiss' Kappa decomposition: FK = (P_o - P_e) / (1 - P_e), where excess agreement = P_o - P_e.\n\n| Config | Subtask | N | n_instances | mean P_o | mean P_e | mean excess (P_o−P_e) | mean FK | FK range (5th–95th pctl) |\n|--------|---------|---|-------------|----------|----------|-----------------------|---------|--------------------------|\n| Qwen SciERC NER | NER | 8 | 551 | 0.747 | 0.508 | 0.240 | 0.393 | −0.114 – 1.000 |\n| Qwen SciERC RE | RE | 8 | 551 | 0.726 | 0.488 | 0.238 | 0.293 | −0.143 – 1.000 |\n| Qwen CoNLL NER | NER | 8 | 3453 | 0.895 | 0.238 | 0.657 | 0.721 | −0.143 – 1.000 |\n| Qwen CoNLL NER N=16 | NER | 16 | 3453 | 0.910 | 0.309 | 0.601 | 0.716 | −0.067 – 1.000 |\n| LLaMA SciERC NER | NER | 8 | 551 | 0.774 | 0.472 | 0.302 | 0.451 | −0.126 – 1.000 |\n| LLaMA SciERC RE | RE | 8 | 551 | 0.755 | 0.447 | 0.308 | 0.368 | −0.143 – 1.000 |\n| LLaMA CoNLL NER | NER | 8 | 3453 | 0.973 | 0.068 | 0.906 | 0.928 | 0.357 – 1.000 |\n| LLaMA CoNLL NER N=16 | NER | 16 | 3453 | 0.976 | 0.085 | 0.891 | 0.929 | 0.426 – 1.000 |\n\n## Key Findings\n\n**P_e (chance agreement) varies dramatically by dataset, not model.** SciERC configs have high P_e (0.45–0.51) reflecting few distinct items per instance and skewed category distributions. CoNLL P_e is much lower (0.07–0.31), meaning more diverse item spaces where chance agreement is rare.\n\n**Excess agreement (P_o − P_e) is the more informative metric.** LLaMA CoNLL shows the highest excess (~0.90), meaning nearly all observed agreement is genuine. SciERC configs have modest excess (0.24–0.31) despite reasonable P_o, because P_e inflates the baseline. This means a substantial fraction of SciERC's raw agreement is attributable to chance.\n\n**RE consistently has lower FK than NER on the same data**, despite similar P_o levels. Qwen SciERC RE (FK=0.293) vs NER (FK=0.393); LLaMA SciERC RE (FK=0.368) vs NER (FK=0.451). RE's slightly lower P_e doesn't compensate for its lower P_o, resulting in less excess agreement.\n\n**N=8 vs N=16 shows minimal FK change.** Qwen CoNLL: 0.721→0.716; LLaMA CoNLL: 0.928→0.929. However, P_e increases with N (0.238→0.309 for Qwen CoNLL) because more samples surface more unique items, slightly reducing excess despite higher P_o.\n\n**LLaMA vs Qwen:** LLaMA consistently achieves higher excess agreement across all configs, particularly on CoNLL (+0.25 excess over Qwen). On SciERC the gap is smaller (~0.06). This suggests LLaMA's outputs are more internally consistent.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/fk_excess_agreement_all_configs.md",
    "content": "# FK Excess Agreement — All Configurations\n\nFleiss' Kappa decomposition: FK = (P_o - P_e) / (1 - P_e), where excess agreement = P_o - P_e.\n\n| Config | Subtask | N | n_instances | mean P_o | mean P_e | mean excess (P_o−P_e) | mean FK | FK range (5th–95th pctl) |\n|--------|---------|---|-------------|----------|----------|-----------------------|---------|--------------------------|\n| Qwen SciERC NER | NER | 8 | 551 | 0.747 | 0.508 | 0.240 | 0.393 | −0.114 – 1.000 |\n| Qwen SciERC RE | RE | 8 | 551 | 0.726 | 0.488 | 0.238 | 0.293 | −0.143 – 1.000 |\n| Qwen CoNLL NER | NER | 8 | 3453 | 0.895 | 0.238 | 0.657 | 0.721 | −0.143 – 1.000 |\n| Qwen CoNLL NER N=16 | NER | 16 | 3453 | 0.910 | 0.309 | 0.601 | 0.716 | −0.067 – 1.000 |\n| LLaMA SciERC NER | NER | 8 | 551 | 0.774 | 0.472 | 0.302 | 0.451 | −0.126 – 1.000 |\n| LLaMA SciERC RE | RE | 8 | 551 | 0.755 | 0.447 | 0.308 | 0.368 | −0.143 – 1.000 |\n| LLaMA CoNLL NER | NER | 8 | 3453 | 0.973 | 0.068 | 0.906 | 0.928 | 0.357 – 1.000 |\n| LLaMA CoNLL NER N=16 | NER | 16 | 3453 | 0.976 | 0.085 | 0.891 | 0.929 | 0.426 – 1.000 |\n\n## Key Findings\n\n**P_e (chance agreement) varies dramatically by dataset, not model.** SciERC configs have high P_e (0.45–0.51) reflecting few distinct items per instance and skewed category distributions. CoNLL P_e is much lower (0.07–0.31), meaning more diverse item spaces where chance agreement is rare.\n\n**Excess agreement (P_o − P_e) is the more informative metric.** LLaMA CoNLL shows the highest excess (~0.90), meaning nearly all observed agreement is genuine. SciERC configs have modest excess (0.24–0.31) despite reasonable P_o, because P_e inflates the baseline. This means a substantial fraction of SciERC's raw agreement is attributable to chance.\n\n**RE consistently has lower FK than NER on the same data**, despite similar P_o levels. Qwen SciERC RE (FK=0.293) vs NER (FK=0.393); LLaMA SciERC RE (FK=0.368) vs NER (FK=0.451). RE's slightly lower P_e doesn't compensate for its lower P_o, resulting in less excess agreement.\n\n**N=8 vs N=16 shows minimal FK change.** Qwen CoNLL: 0.721→0.716; LLaMA CoNLL: 0.928→0.929. However, P_e increases with N (0.238→0.309 for Qwen CoNLL) because more samples surface more unique items, slightly reducing excess despite higher P_o.\n\n**LLaMA vs Qwen:** LLaMA consistently achieves higher excess agreement across all configs, particularly on CoNLL (+0.25 excess over Qwen). On SciERC the gap is smaller (~0.06). This suggests LLaMA's outputs are more internally consistent.\n"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T12:15:10.214415+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/fk_excess_agreement_all_configs.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T12:15:10.214627+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "fk_excess_agreement_all_configs",
  "type": "report",
  "description": "Fleiss Kappa excess agreement decomposition (P_o, P_e, excess, FK) for all 8 experiment configurations",
  "project": "struct_self_consist_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/fk_excess_agreement_all_configs.md",
  "tags": "['fleiss_kappa', 'excess_agreement', 'analysis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "fk_excess_agreement_all_configs",
    "type": "report",
    "description": "Fleiss Kappa excess agreement decomposition (P_o, P_e, excess, FK) for all 8 experiment configurations",
    "project": "struct_self_consist_ie",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/fk_excess_agreement_all_configs.md",
    "tags": "['fleiss_kappa', 'excess_agreement', 'analysis']"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T12:15:10.214861+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_8c9da1\", \"name\": \"fk_excess_agreement_all_configs\", \"type\": \"report\", \"description\": \"Fleiss Kappa excess agreement decomposition (P_o, P_e, excess, FK) for all 8 experiment configurations\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/fk_excess_agreement_all_configs.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T12:15:03.193487+00:00\", \"tags\": [\"fleiss_kappa\", \"excess_agreement\", \"analysis\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-15T12:15:10.215114+00:00_

报告已写入 `artifacts/fk_excess_agreement_all_configs.md` 并注册。

核心结论：
- **P_e 由数据集决定**：SciERC P_e 高（0.45–0.51），CoNLL P_e 低（0.07–0.31）
- **LLaMA CoNLL excess 最高**（~0.90），SciERC excess 最低（0.24–0.31）——SciERC 的大量观察一致性来自 chance
- RE 的 FK 系统性低于同数据集的 NER
- N=8→16 对 FK 几乎无影响，但 P_e 随 N 增大而上升

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_fk_excess_agreement_20260515T121311"
}
```

</details>

---
