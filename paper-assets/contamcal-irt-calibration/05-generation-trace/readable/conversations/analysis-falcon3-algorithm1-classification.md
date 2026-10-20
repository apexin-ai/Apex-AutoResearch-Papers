# analysis falcon3 algorithm1 classification

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_analysis_falcon3-algorithm1-classification_20260522T131404.jsonl`
- **Structured JSON:** [`bb8ed16c5cc065f30d6a.json`](../../sessions/bb/bb8ed16c5cc065f30d6a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-22T13:15:41.323013+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "algorithm_1|classify_pattern|dose_response.*class|taxonomy|pattern_class",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "type": "py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Grep",
  "tool_args": {
    "pattern": "algorithm_1|classify_pattern|dose_response.*class|taxonomy|pattern_class",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
    "type": "py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T13:15:41.323405+00:00_

Found 2 files
artifacts/qwen14b_n3_bootstrap/compute_qwen14b_n3_ci.py
analysis/bootstrap_triple_seed.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T13:15:41.323581+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/classification*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/classification*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T13:15:41.323710+00:00_

artifacts/classification_sensitivity_sweep.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T13:15:41.323844+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/algorithm*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/algorithm*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T13:15:41.323979+00:00_

.venv/lib/python3.14/site-packages/pandas/core/algorithms.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pandas/core/algorithms.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T13:15:41.324095+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/classification_sensitivity_sweep.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/classification_sensitivity_sweep.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T13:15:41.324375+00:00_

1	#!/usr/bin/env python3
2	"""Classification sensitivity sweep with mid-trajectory volatility check.
3	
4	Sweeps over τ (noise threshold) and σ (collapse threshold) to evaluate
5	classification robustness across 30 parameter combinations.
6	
7	v2: Adds volatility check within the Immune branch — if intermediate
8	dosages deviate beyond τ from baseline, reclassify as V-recovery.
9	"""
10	
11	import json
12	import os
13	from itertools import product
14	
15	import numpy as np
16	
17	# ── Parameters ──────────────────────────────────────────────────────
18	
19	TAU_VALUES = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]
20	SIGMA_VALUES = [3.0, 4.0, 5.0, 6.0, 7.0]
21	
22	# ── Classifier v2 (with volatility check) ──────────────────────────
23	
24	def classify_profile(accs, tau=1.0, sigma=5.0):
25	    """Classify a single dose-response profile.
26	
27	    Args:
28	        accs: dict d000..d100 -> float accuracy (percentage points)
29	        tau: noise threshold (pp) for Immune boundary
30	        sigma: collapse threshold (pp) for severe U-collapse
31	    Returns:
32	        str: Immune | U-collapse | V-recovery | Benefit | Benefit-sat
33	    """
34	    acc_d000 = accs['d000']
35	    acc_d100 = accs['d100']
36	    delta = acc_d100 - acc_d000
37	
38	    intermediate_accs = [accs['d005'], accs['d025'], accs['d050']]
39	
40	    if abs(delta) <= tau:
41	        # v2: mid-trajectory volatility check
42	        max_deviation = max(abs(a - acc_d000) for a in intermediate_accs)
43	        if max_deviation <= tau:
44	            return 'Immune'
45	        else:
46	            min_intermediate = min(intermediate_accs)
47	            if min_intermediate < acc_d000 - tau:
48	                return 'V-recovery'
49	            else:
50	                return 'Immune'
51	
52	    if delta <= -sigma:
53	        return 'U-collapse'
54	
55	    if delta < -tau:
56	        mid_min = min(intermediate_accs)
57	        if mid_min < acc_d100 and mid_min < acc_d000:
58	            return 'V-recovery'
59	       
…[truncated 15622 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T13:15:41.324567+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "classify|Immune|Benefit|Collapse|V-recovery|Saturat",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "type": "py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Grep",
  "tool_args": {
    "pattern": "classify|Immune|Benefit|Collapse|V-recovery|Saturat",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
    "type": "py"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T13:15:41.324709+00:00_

Found 31 files
artifacts/qwen14b_n3_bootstrap/compute_qwen14b_n3_ci.py
analysis/bootstrap_triple_seed.py
artifacts/classification_sensitivity_sweep.py
artifacts/profile_classifier.py
analysis/treated_untreated_analysis.py
artifacts/_project/data/profile_classifier_03f975.py
artifacts/_project/data/profile_classifier_12dd52.py
artifacts/_project/data/profile_classifier.py
artifacts/_project/data/bootstrap_profile_stability_a62645.py
artifacts/_project/data/bootstrap_profile_stability.py
artifacts/bootstrap_profile_stability.py
.venv/lib/python3.14/site-packages/fontTools/varLib/merger.py
.venv/lib/python3.14/site-packages/fontTools/varLib/cff.py
.venv/lib/python3.14/site-packages/fontTools/subset/__init__.py
.venv/lib/python3.14/site-packages/fontTools/misc/classifyTools.py
.venv/lib/python3.14/site-packages/fontTools/merge/layout.py
.venv/lib/python3.14/site-packages/PIL/TiffTags.py
.venv/lib/python3.14/site-packages/PIL/ExifTags.py
.venv/lib/python3.14/site-packages/pyparsing/core.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/scipy/stats/tests/test_continuous.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/scipy/stats/_morestats.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/scipy/optimize/_nonlin.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/scipy/cluster/vq.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/numpy/testing/print_coercion_tables.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py
.venv/lib/python3.14/site-packages/scipy/stats/tests/test_continuous.py
.venv/lib/python3.14/site-packages/scipy/stats/_morestats.py
.venv/lib/python3.14/site-packages/scipy/optimize/_nonlin.py
.venv/lib/python3.14/site-packages/scipy/cluster/vq.py
.venv/lib/python3.14/site-packages/numpy/testing/print_coercion_tables.py
.venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T13:15:41.324860+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/profile_classifier.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/profile_classifier.py"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T13:15:41.325066+00:00_

1	"""Dose-response profile classifier for contamination calibration.
2	
3	Classifies a model's accuracy trajectory across contamination dosages
4	into one of five canonical patterns: Immune, U-collapse, V-recovery,
5	Benefit, or Benefit-saturation.
6	"""
7	
8	from __future__ import annotations
9	
10	DOSAGES = ("d000", "d005", "d025", "d050", "d100")
11	PATTERNS = ("Immune", "U-collapse", "V-recovery", "V-recovery-full", "Benefit", "Benefit-sat")
12	
13	
14	def classify_profile(
15	    accuracies: dict[str, float],
16	    *,
17	    noise_threshold: float = 1.0,
18	    severe_threshold: float = 5.0,
19	    saturation_ratio: float = 0.3,
20	    late_gain_floor: float = 0.5,
21	) -> dict:
22	    """Classify a dose-response accuracy profile into a canonical pattern.
23	
24	    Args:
25	        accuracies: Mapping from dosage key to accuracy (percentage points),
26	            e.g. {"d000": 76.44, "d005": 76.56, "d025": 76.50,
27	                   "d050": 76.02, "d100": 76.27}.
28	        noise_threshold: Maximum |delta| (pp) to be considered noise (Immune).
29	        severe_threshold: Minimum |delta| (pp) for severe degradation (U-collapse).
30	        saturation_ratio: If second-half gain < first-half gain * ratio,
31	            the benefit is saturating.
32	        late_gain_floor: If d100 - d050 < this value, late gain has stalled.
33	
34	    Returns:
35	        {"pattern": str, "confidence": float, "delta": float, "reasoning": str}
36	    """
37	    for d in DOSAGES:
38	        if d not in accuracies:
39	            raise ValueError(f"Missing dosage key: {d}")
40	
41	    a = {d: float(accuracies[d]) for d in DOSAGES}
42	    delta = a["d100"] - a["d000"]
43	    mid_vals = [a["d005"], a["d025"], a["d050"]]
44	    mid_min = min(mid_vals)
45	
46	    # ── Decision tree ────────────────────────────────────────────────
47	
48	    if abs(delta) <= noise_threshold:
49	        max_deviation = max(abs(v - a["d000"]) for v in mid_vals)
50	        if max_deviation <= noise_thr
…[truncated 6139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T13:15:41.325226+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Falcon|falcon",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Falcon|falcon",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
    "type": "py",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T13:15:41.325393+00:00_

Found 24 files
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pandas/tests/window/test_groupby.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pandas/tests/groupby/methods/test_value_counts.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pandas/tests/groupby/test_groupby_dropna.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pandas/tests/frame/methods/test_value_counts.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pandas/tests/frame/test_subclass.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pandas/io/stata.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pandas/core/groupby/grouper.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pandas/core/groupby/groupby.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pandas/core/groupby/generic.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pandas/core/series.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pandas/core/generic.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pandas/core/frame.py
.venv/lib/python3.14/site-packages/pandas/tests/window/test_groupby.py
.venv/lib/python3.14/site-packages/pandas/tests/groupby/methods/test_value_counts.py
.venv/lib/python3.14/site-packages/pandas/tests/groupby/test_groupby_dropna.py
.venv/lib/python3.14/site-packages/pandas/tests/frame/methods/test_value_counts.py
.venv/lib/python3.14/site-packages/pandas/tests/frame/test_subclass.py
.venv/lib/python3.14/site-packages/pandas/io/stata.py
.venv/lib/python3.14/site-packages/pandas/core/groupby/grouper.py
.venv/lib/python3.14/site-packages/pandas/core/groupby/groupby.py
.venv/lib/python3.14/site-packages/pandas/core/groupby/generic.py
.venv/lib/python3.14/site-packages/pandas/core/series.py
.venv/lib/python3.14/site-packages/pandas/core/generic.py
.venv/lib/python3.14/site-packages/pandas/core/frame.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T13:15:41.325549+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Phi-4|Qwen-14B|Qwen-7B|Gemma-2|OLMo-2|Llama-3",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts",
  "glob": "*.md",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Phi-4|Qwen-14B|Qwen-7B|Gemma-2|OLMo-2|Llama-3",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts",
    "glob": "*.md",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T13:15:41.325696+00:00_

Found 81 files
artifacts/_project/report/sft_tax_analysis.md
artifacts/sft_tax_analysis.md
artifacts/_project/report/cross_benchmark_consistency.md
artifacts/cross_benchmark_consistency.md
artifacts/_project/report/data_audit_tables2_3_fig1.md
artifacts/data_audit_tables2_3_fig1.md
artifacts/_project/report/data_audit_table1.md
artifacts/data_audit_table1.md
artifacts/_project/report/data_audit_table4_10_xref.md
artifacts/data_audit_table4_10_xref.md
artifacts/review_reports/round_8.md
artifacts/review_reports/round_7.md
artifacts/_project/report/eval_olmo2_s42_rerun_analysis.md
artifacts/sft_llama3_8b_s0_validation/intermediate/sft_llama3_8b_launch_status.md
artifacts/review_reports/round_6.md
artifacts/retrain_gemma2_d100_s0/diagnosis.md
artifacts/retrain_gemma2_d100_s0/report/diagnosis.md
artifacts/eval_qwen7b_mmlu_arc_s0/eval_results_summary.md
artifacts/gemma2_s0_sweep_analysis.md
artifacts/sft_gemma2_s0_sweep/report/gemma2_s0_sweep_analysis.md
artifacts/_project/report/bootstrap_n3_phi4_d188.md
artifacts/_project/report/bootstrap_full_5family_s42_s123.md
artifacts/_project/report/gsm8k_dosage_analysis.md
artifacts/gsm8k_dosage_analysis.md
artifacts/exp001/report/sft_qwen7b_olmo2_s123_sweep_report.md
artifacts/sft_qwen7b_olmo2_s123_sweep_report.md
artifacts/_project/report/lit_cross_benchmark_transfer.md
artifacts/lit_cross_benchmark_transfer.md
artifacts/_project/report/paper_consistency_audit.md
artifacts/paper_consistency_audit.md
artifacts/_project/report/paper_update_checklist.md
artifacts/paper_update_checklist.md
artifacts/_project/paper/appendix_domain_decomposition.md
artifacts/appendix_domain_decomposition.md
artifacts/_project/data/irt_data_matrices.md
artifacts/_project/data/domain_decomposition_s42.md
artifacts/_project/data/sensitivity_sweep_v2.md
artifacts/_project/data/error_analysis_old_models.md
artifacts/_project/data/treated_untreated_analysis.md
artifacts/eval_results_v2_summary.md
artifacts/phase2_eval_diagnosis.md
artifacts/paper_analysis
…[truncated 2154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T13:15:41.325843+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/sft_tax_analysis.md",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/sft_tax_analysis.md",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T13:15:41.325989+00:00_

1	# SFT Tax Analysis: Pre-training vs Post-SFT d000 Baseline
2	
3	**Date**: 2026-05-22
4	**Definition**: SFT tax = Pre-training MMLU baseline (raw base model) − d000 Post-SFT MMLU baseline (clean SFT, 0% contamination). Positive = SFT degraded MMLU.
5	
6	## MMLU 5-shot
7	
8	| Model Family | Pre-training Baseline | d000 Post-SFT | SFT Tax (Δ) | Pre-training Source | d000 Source |
9	|---|---|---|---|---|---|
10	| Phi-4 14.7B | 84.8% | 76.44% | **+8.36 pp** | Phi-4 Technical Report (arXiv:2412.08905) | registry: memory.md 6-family summary |
11	| Qwen2.5-14B | 79.7% | 69.44% | **+10.26 pp** | Qwen2.5 Technical Report (arXiv:2412.15115) | registry: memory.md 6-family summary |
12	| Qwen2.5-7B | 74.2% | 66.11% | **+8.09 pp** | Qwen2.5 Technical Report (arXiv:2412.15115) | registry: memory.md 6-family summary |
13	| Gemma-2 9B | 71.3% | 61.86% | **+9.44 pp** | Gemma 2 Technical Report (arXiv:2408.00118) | registry: memory.md 6-family summary |
14	| Falcon3-7B-Base | 67.4% | 58.77% | **+8.63 pp** | Falcon 3 Blog (TII, falcon-lm.github.io) | registry: eval_falcon3_d000_s42_v2 |
15	| LLaMA-3.1 8B | 66.7% | 53.50% | **+13.20 pp** | Meta eval_details.md (github.com/meta-llama) | registry: memory.md LLaMA-3 validation |
16	| OLMo-2 7B | 63.7% | 53.79% | **+9.91 pp** | OLMo 2 Paper (AI2, arXiv:2501.00656) | registry: memory.md 6-family summary (rerun verified) |
17	
18	**Mean SFT Tax**: 9.70 pp (std: 1.64 pp)
19	**Range**: 8.09 pp (Qwen2.5-7B) to 13.20 pp (LLaMA-3.1 8B)
20	
21	## Key Findings
22	
23	1. **Universal SFT tax**: All 7 families show positive SFT tax (8–13 pp). LoRA SFT on QA-format data consistently degrades MMLU 5-shot performance relative to the raw base model.
24	
25	2. **LLaMA-3.1 is an outlier** (13.20 pp, 1.5 std above mean). Possible causes: (a) LLaMA-3.1 architecture is more sensitive to LoRA-based SFT; (b) format mismatch between SFT data and LLaMA-3.1's pretraining distribution; (c) LLaMA-3.1's tokenizer handling of MC options differs.
26	
27	3. **Qwen2.5-14
…[truncated 1892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T13:15:41.326154+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport sys\nsys.path.insert(0, 'artifacts')\nfrom profile_classifier import classify_profile\n\n# Falcon3-7B-Base data\nfalcon3_mmlu = {'d000': 58.77, 'd005': 59.02, 'd025': 61.23, 'd050': 62.09, 'd100': 62.96}\nfalcon3_arc  = {'d000': 81.57, 'd005': 83.11, 'd025': 84.81, 'd050': 83.28, 'd100': 85.58}\n\nprint('='*70)\nprint('  Falcon3-7B-Base: MMLU 5-shot')\nprint('='*70)\nr_mmlu = classify_profile(falcon3_mmlu)\nfor k, v in r_mmlu.items():\n    print(f'  {k}: {v}')\n\nprint()\nprint('='*70)\nprint('  Falcon3-7B-Base: ARC 25-shot')\nprint('='*70)\nr_arc = classify_profile(falcon3_arc)\nfor k, v in r_arc.items():\n    print(f'  {k}: {v}')\n\n# Trajectory analysis\nprint()\nprint('='*70)\nprint('  Trajectory Statistics')\nprint('='*70)\n\nfor name, accs in [('MMLU', falcon3_mmlu), ('ARC', falcon3_arc)]:\n    vals = [accs[d] for d in ['d000','d005','d025','d050','d100']]\n    delta = vals[-1] - vals[0]\n    dips = [v for v in vals[1:-1] if v < vals[0]]\n    monotonic = all(vals[i] <= vals[i+1] for i in range(len(vals)-1))\n    \n    # Step-by-step changes\n    dosages = ['d000','d005','d025','d050','d100']\n    steps = []\n    for i in range(1, len(dosages)):\n        steps.append(f'{dosages[i-1]}->{dosages[i]}: {vals[i]-vals[i-1]:+.2f}pp')\n    \n    print(f'  {name}:')\n    print(f'    Delta(d100-d000) = {delta:+.2f}pp')\n    print(f'    Min dip below d000: {min(dips) - vals[0]:+.2f}pp' if dips else '    No dip below d000')\n    print(f'    Monotonic increasing: {monotonic}')\n    print(f'    Steps: {\\\" | \\\".join(steps)}')\n    # Saturation check\n    first_half = accs['d025'] - accs['d000']\n    second_half = accs['d100'] - accs['d025']\n    late_gain = accs['d100'] - accs['d050']\n    print(f'    First-half gain (d000->d025): {first_half:+.2f}pp')\n    print(f'    Second-half gain (d025->d100): {second_half:+.2f}pp')\n    print(f'    Late gain (d050->d100): {late_gain:+.2f}pp')\n    print(f'    Ratio second/first: {second_half/first_half:.3f}' if first_half > 0 else '    N/A')\n    print()\n\n# Cross-family comparison\nprint('='*70)\nprint('  Cross-Family Comparison (6 existing + Falcon3)')\nprint('='*70)\n\nfamilies = {\n    'Phi-4 14.7B': {'d000': 76.44, 'd005': 76.28, 'd025': 76.50, 'd050': 76.10, 'd100': 76.27},\n    'Qwen2.5-14B': {'d000': 69.44, 'd005': 63.76, 'd025': 62.51, 'd050': 61.34, 'd100': 60.07},\n    'Qwen2.5-7B':  {'d000': 66.11, 'd005': 63.42, 'd025': 63.15, 'd050': 63.59, 'd100': 64.33},\n    'Gemma-2 9B':  {'d000': 61.86, 'd005': 63.56, 'd025': 64.19, 'd050': 64.73, 'd100': 65.62},\n    'Falcon3-7B':  {'d000': 58.77, 'd005': 59.02, 'd025': 61.23, 'd050': 62.09, 'd100': 62.96},\n    'OLMo-2 7B':   {'d000': 53.79, 'd005': 55.17, 'd025': 56.06, 'd050': 56.53, 'd100': 57.00},\n    'LLaMA-3.1 8B': {'d000': 53.50, 'd005': 53.98, 'd025': 54.61, 'd050': 54.23, 'd100': 54.59},\n}\n\nfor name, accs in families.items():\n    r = classify_profile(accs)\n    delta = accs['d100'] - accs['d000']\n    print(f'  {name:<16s}  delta={delta:+6.2f}pp  pattern={r[\\\"pattern\\\"]:<20s}  conf={r[\\\"confidence\\\"]:.3f}')\n\"\n",
  "description": "Run Algorithm 1 classification on Falcon3 data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport sys\nsys.path.insert(0, 'artifacts')\nfrom profile_classifier import classify_profile\n\n# Falcon3-7B-Base data\nfalcon3_mmlu = {'d000': 58.77, 'd005': 59.02, 'd025': 61.23, 'd050': 62.09, 'd100': 62.96}\nfalcon3_arc  = {'d000': 81.57, 'd005': 83.11, 'd025': 84.81, 'd050': 83.28, 'd100': 85.58}\n\nprint('='*70)\nprint('  Falcon3-7B-Base: MMLU 5-shot')\nprint('='*70)\nr_mmlu = classify_profile(falcon3_mmlu)\nfor k, v in r_mmlu.items():\n    print(f'  {k}: {v}')\n\nprint()\nprint('='*70)\nprint('  Falcon3-7B-Base: ARC 25-shot')\nprint('='*70)\nr_arc = classify_profile(falcon3_arc)\nfor k, v in r_arc.items():\n    print(f'  {k}: {v}')\n\n# Trajectory analysis\nprint()\nprint('='*70)\nprint('  Trajectory Statistics')\nprint('='*70)\n\nfor name, accs in [('MMLU', falcon3_mmlu), ('ARC', falcon3_arc)]:\n    vals = [accs[d] for d in ['d000','d005','d025','d050','d100']]\n    delta = vals[-1] - vals[0]\n    dips = [v for v in vals[1:-1] if v < vals[0]]\n    monotonic = all(vals[i] <= vals[i+1] for i in range(len(vals)-1))\n    \n    # Step-by-step changes\n    dosages = ['d000','d005','d025','d050','d100']\n    steps = []\n    for i in range(1, len(dosages)):\n        steps.append(f'{dosages[i-1]}->{dosages[i]}: {vals[i]-vals[i-1]:+.2f}pp')\n    \n    print(f'  {name}:')\n    print(f'    Delta(d100-d000) = {delta:+.2f}pp')\n    print(f'    Min dip below d000: {min(dips) - vals[0]:+.2f}pp' if dips else '    No dip below d000')\n    print(f'    Monotonic increasing: {monotonic}')\n    print(f'    Steps: {\\\" | \\\".join(steps)}')\n    # Saturation check\n    first_half = accs['d025'] - accs['d000']\n    second_half = accs['d100'] - accs['d025']\n    late_gain = accs['d100'] - accs['d050']\n    print(f'    First-half gain (d000->d025): {first_half:+.2f}pp')\n    print(f'    Second-half gain (d025->d100): {second_half:+.2f}pp')\n    print(f'    Late gain (d050->d100): {late_gain:+.2f}pp')\n    print(f'    Ratio second/first: {second_half/first_half:.3f}' if first_half > 0 else '    N/A')\n    print()\n\n# Cross-family comparison\nprint('='*70)\nprint('  Cross-Family Comparison (6 existing + Falcon3)')\nprint('='*70)\n\nfamilies = {\n    'Phi-4 14.7B': {'d000': 76.44, 'd005': 76.28, 'd025': 76.50, 'd050': 76.10, 'd100': 76.27},\n    'Qwen2.5-14B': {'d000': 69.44, 'd005': 63.76, 'd025': 62.51, 'd050': 61.34, 'd100': 60.07},\n    'Qwen2.5-7B':  {'d000': 66.11, 'd005': 63.42, 'd025': 63.15, 'd050': 63.59, 'd100': 64.33},\n    'Gemma-2 9B':  {'d000': 61.86, 'd005': 63.56, 'd025': 64.19, 'd050': 64.73, 'd100': 65.62},\n    'Falcon3-7B':  {'d000': 58.77, 'd005': 59.02, 'd025': 61.23, 'd050': 62.09, 'd100': 62.96},\n    'OLMo-2 7B':   {'d000': 53.79, 'd005': 55.17, 'd025': 56.06, 'd050': 56.53, 'd100': 57.00},\n    'LLaMA-3.1 8B': {'d000': 53.50, 'd005': 53.98, 'd025': 54.61, 'd050': 54.23, 'd100': 54.59},\n}\n\nfor name, accs in families.items():\n    r = classify_profile(accs)\n    delta = accs['d100'] - accs['d000']\n    print(f'  {name:<16s}  delta={delta:+6.2f}pp  pattern={r[\\\"pattern\\\"]:<20s}  conf={r[\\\"confidence\\\"]:.3f}')\n\"\n",
    "description": "Run Algorithm 1 classification on Falcon3 data"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T13:15:41.326384+00:00_

======================================================================
  Falcon3-7B-Base: MMLU 5-shot
======================================================================
  pattern: Benefit
  confidence: 1.0
  delta: 4.19
  reasoning: delta=+4.19pp, monotonic improvement without saturation

======================================================================
  Falcon3-7B-Base: ARC 25-shot
======================================================================
  pattern: Benefit-sat
  confidence: 0.601
  delta: 4.01
  reasoning: delta=+4.01pp (positive), second-half gain (0.77) < 30% of first-half (3.24)

======================================================================
  Trajectory Statistics
======================================================================
  MMLU:
    Delta(d100-d000) = +4.19pp
    No dip below d000
    Monotonic increasing: True
    Steps: d000->d005: +0.25pp | d005->d025: +2.21pp | d025->d050: +0.86pp | d050->d100: +0.87pp
    First-half gain (d000->d025): +2.46pp
    Second-half gain (d025->d100): +1.73pp
    Late gain (d050->d100): +0.87pp
    Ratio second/first: 0.703

  ARC:
    Delta(d100-d000) = +4.01pp
    No dip below d000
    Monotonic increasing: False
    Steps: d000->d005: +1.54pp | d005->d025: +1.70pp | d025->d050: -1.53pp | d050->d100: +2.30pp
    First-half gain (d000->d025): +3.24pp
    Second-half gain (d025->d100): +0.77pp
    Late gain (d050->d100): +2.30pp
    Ratio second/first: 0.238

======================================================================
  Cross-Family Comparison (6 existing + Falcon3)
======================================================================
  Phi-4 14.7B       delta= -0.17pp  pattern=Immune                conf=0.915
  Qwen2.5-14B       delta= -9.37pp  pattern=U-collapse            conf=0.937
  Qwen2.5-7B        delta= -1.78pp  pattern=V-recovery            conf=0.618
  Gemma-2 9B        delta= +3.76pp  pattern=Benefit               conf=1.000
  Falcon3-7B        delta= +4.19pp  pa
…[truncated 192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T13:15:41.326566+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T13:15:41.326727+00:00_

2pl_vs_4pl_ablation.md
3B_s123_eval_matrix_complete.md
__pycache__
_project
algorithm1_pseudocode.tex
analysis_14b_d100_s42.md
analysis_3B_d000_gsm8k_seed_variance.md
appendix_domain_decomposition.md
batch_matrix_commands.md
bib_rebuild_2024_classics.bib
bib_rebuild_2025plus.bib
bootstrap_profile_stability.py
classification_criteria.yaml
classification_sensitivity_sweep.py
compile_eval_summary.py
coverage_report_20260515.md
cross_benchmark_consistency.md
d000_alignment_tax_analysis.md
d108_v4_analysis.md
data_audit_table1.md
data_audit_table4_10_xref.md
data_audit_tables2_3_fig1.md
diag_exp006_pooled_irt_n25.md
diag_exp_001_sft_15B_d005_s123.md
diag_exp_001_sft_d100_3B.md
diag_sft_sweep_failures_westd.md
diagnose_eval_falcon3_failed.md
diagnose_exp001_eval_3B_d000_s42_v3.md
diagnose_exp001_sft_llama32_3B_d005_s42.md
diagnosis_exp002_3B_d000_s123_cuda2.md
did_power_analysis
dose_response_analysis.md
dream_reports
error_analysis.md
error_analysis_summary.yaml
eval_gemma2_arc_s42
eval_gemma2_mmlu_s0_diagnosis.md
eval_metrics_summary.json
eval_metrics_summary.md
eval_qwen14b_d050_arc_s0
eval_qwen7b_mmlu_arc_s0
eval_results_v2_summary.md
eval_summary_matrix.csv
evaluate_batch.py
exp-004
exp-006
exp-008
exp001
exp001_sft_injection
exp002
exp002_signal_pipeline
exp003_rrf_ablation
exp004
exp004_fisher_heatmap
exp004_incremental_analysis.md
exp004_threshold_dgp
exp005_noise_propagation
exp006
exp006-oracle-gsm8k-extended-v2
exp006-s1only-gsm8k-2pl
exp006_baselines
exp006_irt_calibration
exp006_pooled_rrf_irt_05b_15b
exp006_readiness_report.md
exp008
exp008_3regime_analysis.json
exp008_auc_heatmap.json
exp008_v2
exp009_plan.md
exp009_status_check.md
exp_001_eval_3B_d000_s42_a32_batch
exp_001_eval_3B_d005_s42_para_aligned
exp_001_sft_14b_d100_s42
exp_001_sft_injection
exp_002_signals_05B
exp_003_mmlu_item_aligned_gap
exp_004_fisher_heatmap_w4_v2
exp_005_noise_prop_v4
exp_006
exp_006_pooled_irt_2pl_gamma_mmlu_arc
exp_006_scale_stratified_irt
exp_008_base_pretrained_15B_eval
ex
…[truncated 1742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T13:15:41.326880+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/falcon3_algorithm1_classification.md",
  "content": "# Falcon3-7B-Base Algorithm 1 Classification\n\n## Parameters\nτ = 1.0pp, σ = 5.0pp (default thresholds)\n\n## MMLU 5-shot Classification\n- Δ(d100−d000) = **+4.19 pp**\n- Pattern: **Benefit**\n- Confidence: 1.000\n- Trajectory: Monotonic increase across all 5 dosages. Steps: d000→d005 +0.25pp, d005→d025 +2.21pp, d025→d050 +0.86pp, d050→d100 +0.87pp. First-half gain (d000→d025) = +2.46pp, second-half gain (d025→d100) = +1.73pp, ratio = 0.703 (above 0.3 saturation threshold). No dips below baseline.\n\n## ARC 25-shot Classification\n- Δ(d100−d000) = **+4.01 pp**\n- Pattern: **Benefit-sat**\n- Confidence: 0.601\n- Trajectory: Non-monotonic — d025→d050 dip of −1.53pp, then recovery d050→d100 +2.30pp. First-half gain (d000→d025) = +3.24pp, second-half gain (d025→d100) = +0.77pp, ratio = 0.238 (below 0.3 saturation threshold, triggers Benefit-sat). Late gain (d050→d100) = +2.30pp is above 0.5pp floor, so saturation is driven by the second/first ratio, not late stall.\n\n## Combined Classification\n- **MMLU**: Benefit (strong, monotonic)\n- **ARC**: Benefit-sat (saturating, non-monotonic mid-trajectory)\n- Overall: **Benefit / Benefit-sat** — Falcon3 benefits from contaminated SFT data on both benchmarks, with ARC showing early saturation.\n\n## Cross-Family Comparison (MMLU, sorted by Δ)\n\n| Family | d000 | d100 | Δ(d100−d000) | Pattern | Confidence |\n|--------|------|------|---------------|---------|------------|\n| Qwen2.5-14B | 69.44 | 60.07 | −9.37 pp | U-collapse | 0.937 |\n| Qwen2.5-7B | 66.11 | 64.33 | −1.78 pp | V-recovery | 0.618 |\n| Phi-4 14.7B | 76.44 | 76.27 | −0.17 pp | Immune | 0.915 |\n| LLaMA-3.1 8B | 53.50 | 54.59 | +1.09 pp | Benefit-sat | 0.570 |\n| OLMo-2 7B | 53.79 | 57.00 | +3.21 pp | Benefit-sat | 0.515 |\n| Gemma-2 9B | 61.86 | 65.62 | +3.76 pp | Benefit | 1.000 |\n| **Falcon3-7B** | **58.77** | **62.96** | **+4.19 pp** | **Benefit** | **1.000** |\n\nFalcon3 has the largest positive MMLU delta among all 7 families, slightly exceeding Gemma-2 (+3.76pp). Both are high-confidence Benefit patterns. Falcon3 slots into the \"Benefit cluster\" alongside Gemma-2, distinct from the Benefit-sat models (OLMo-2, LLaMA-3.1) which show weaker or plateauing gains.\n\n## Dose-Response Profiles\n\n```\nMMLU 5-shot:\n  d000  d005  d025  d050  d100\n  58.77 59.02 61.23 62.09 62.96  Falcon3  [Benefit, +4.19pp]\n  61.86 63.56 64.19 64.73 65.62  Gemma-2  [Benefit, +3.76pp]\n  53.79 55.17 56.06 56.53 57.00  OLMo-2   [Benefit-sat, +3.21pp]\n\nARC 25-shot:\n  d000  d005  d025  d050  d100\n  81.57 83.11 84.81 83.28 85.58  Falcon3  [Benefit-sat, +4.01pp]\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/falcon3_algorithm1_classification.md",
    "content": "# Falcon3-7B-Base Algorithm 1 Classification\n\n## Parameters\nτ = 1.0pp, σ = 5.0pp (default thresholds)\n\n## MMLU 5-shot Classification\n- Δ(d100−d000) = **+4.19 pp**\n- Pattern: **Benefit**\n- Confidence: 1.000\n- Trajectory: Monotonic increase across all 5 dosages. Steps: d000→d005 +0.25pp, d005→d025 +2.21pp, d025→d050 +0.86pp, d050→d100 +0.87pp. First-half gain (d000→d025) = +2.46pp, second-half gain (d025→d100) = +1.73pp, ratio = 0.703 (above 0.3 saturation threshold). No dips below baseline.\n\n## ARC 25-shot Classification\n- Δ(d100−d000) = **+4.01 pp**\n- Pattern: **Benefit-sat**\n- Confidence: 0.601\n- Trajectory: Non-monotonic — d025→d050 dip of −1.53pp, then recovery d050→d100 +2.30pp. First-half gain (d000→d025) = +3.24pp, second-half gain (d025→d100) = +0.77pp, ratio = 0.238 (below 0.3 saturation threshold, triggers Benefit-sat). Late gain (d050→d100) = +2.30pp is above 0.5pp floor, so saturation is driven by the second/first ratio, not late stall.\n\n## Combined Classification\n- **MMLU**: Benefit (strong, monotonic)\n- **ARC**: Benefit-sat (saturating, non-monotonic mid-trajectory)\n- Overall: **Benefit / Benefit-sat** — Falcon3 benefits from contaminated SFT data on both benchmarks, with ARC showing early saturation.\n\n## Cross-Family Comparison (MMLU, sorted by Δ)\n\n| Family | d000 | d100 | Δ(d100−d000) | Pattern | Confidence |\n|--------|------|------|---------------|---------|------------|\n| Qwen2.5-14B | 69.44 | 60.07 | −9.37 pp | U-collapse | 0.937 |\n| Qwen2.5-7B | 66.11 | 64.33 | −1.78 pp | V-recovery | 0.618 |\n| Phi-4 14.7B | 76.44 | 76.27 | −0.17 pp | Immune | 0.915 |\n| LLaMA-3.1 8B | 53.50 | 54.59 | +1.09 pp | Benefit-sat | 0.570 |\n| OLMo-2 7B | 53.79 | 57.00 | +3.21 pp | Benefit-sat | 0.515 |\n| Gemma-2 9B | 61.86 | 65.62 | +3.76 pp | Benefit | 1.000 |\n| **Falcon3-7B** | **58.77** | **62.96** | **+4.19 pp** | **Benefit** | **1.000** |\n\nFalcon3 has the largest positive MMLU delta among all 7 families, slightly exceeding Gemma-2 (+3.76pp). Both are high-confidence Benefit patterns. Falcon3 slots into the \"Benefit cluster\" alongside Gemma-2, distinct from the Benefit-sat models (OLMo-2, LLaMA-3.1) which show weaker or plateauing gains.\n\n## Dose-Response Profiles\n\n```\nMMLU 5-shot:\n  d000  d005  d025  d050  d100\n  58.77 59.02 61.23 62.09 62.96  Falcon3  [Benefit, +4.19pp]\n  61.86 63.56 64.19 64.73 65.62  Gemma-2  [Benefit, +3.76pp]\n  53.79 55.17 56.06 56.53 57.00  OLMo-2   [Benefit-sat, +3.21pp]\n\nARC 25-shot:\n  d000  d005  d025  d050  d100\n  81.57 83.11 84.81 83.28 85.58  Falcon3  [Benefit-sat, +4.01pp]\n```\n"
  }
}
````

</details>

---

### Tool result

_source line 24 · 2026-05-22T13:15:41.327039+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/falcon3_algorithm1_classification.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T13:15:41.327158+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T13:15:41.327292+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T13:15:41.327433+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "falcon3_algorithm1_classification",
  "type": "report",
  "description": "Falcon3-7B-Base Algorithm 1 dose-response pattern classification: MMLU=Benefit (+4.19pp), ARC=Benefit-sat (+4.01pp). Cross-family comparison with all 7 families.",
  "project": "contamcal-irt-calibration",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/falcon3_algorithm1_classification.md",
  "tags": "['falcon3', 'algorithm1', 'classification', 'dose-response']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "falcon3_algorithm1_classification",
    "type": "report",
    "description": "Falcon3-7B-Base Algorithm 1 dose-response pattern classification: MMLU=Benefit (+4.19pp), ARC=Benefit-sat (+4.01pp). Cross-family comparison with all 7 families.",
    "project": "contamcal-irt-calibration",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/falcon3_algorithm1_classification.md",
    "tags": "['falcon3', 'algorithm1', 'classification', 'dose-response']"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T13:15:41.327573+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_1bdc0e\", \"name\": \"falcon3_algorithm1_classification\", \"type\": \"report\", \"description\": \"Falcon3-7B-Base Algorithm 1 dose-response pattern classification: MMLU=Benefit (+4.19pp), ARC=Benefit-sat (+4.01pp). Cross-family comparison with all 7 families.\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/report/falcon3_algorithm1_classification.md\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T13:15:32.126632+00:00\", \"tags\": [\"falcon3\", \"algorithm1\", \"classification\", \"dose-response\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-22T13:15:41.327734+00:00_

分类结果：

| Benchmark | Pattern | Δ(d100−d000) | Confidence |
|-----------|---------|--------------|------------|
| **MMLU 5-shot** | **Benefit** | +4.19 pp | 1.000 |
| **ARC 25-shot** | **Benefit-sat** | +4.01 pp | 0.601 |

**MMLU**: 单调递增，无饱和，全 7 家族中正向 delta 最大（超过 Gemma-2 的 +3.76pp）。

**ARC**: 正向但饱和——前半段增益 +3.24pp，后半段仅 +0.77pp（ratio=0.238 < 0.3 阈值）。中间 d025→d050 有 −1.53pp 回落，但非 V-recovery（整体 delta 仍为正）。

**跨家族定位**: Falcon3 归入 Benefit 聚类（与 Gemma-2 并列），区别于 Benefit-sat 组（OLMo-2、LLaMA-3.1）和负向组（Qwen-14B U-collapse、Qwen-7B V-recovery）。

产出已注册: `artifacts/falcon3_algorithm1_classification.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_falcon3-algorithm1-classification_20260522T131404"
}
```

</details>

---
