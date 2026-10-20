# code data audit experiments tables — Part 2 of 2

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../code-data-audit-experiments-tables.md) · [Structured JSON](../../../sessions/73/73729c7de1d1b74e2e89.json)

## Before a recorded user message

### Tool result

_source line 627 · 2026-05-23T19:54:33.891865+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/metabench_data_summary.md:127:**YES, but only 2 annual cohorts (2023, 2024).** With 63% unclassified models, name-based classification has limited coverage. For finer temporal granularity, external metadata (HF Hub API) would be needed.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/semisynthetic_gradient_report.md:108:## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/metabench_data_summary_ec3bbf.md:127:**YES, but only 2 annual cohorts (2023, 2024).** With 63% unclassified models, name-based classification has limited coverage. For finer temporal granularity, external metadata (HF Hub API) would be needed.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/arr_checklist_draft.md:28:**Justification**: All artifacts are cited: METABENCH (Kipnis, 2024), MMLU (Hendrycks et al., 2021), GSM8K, HellaSwag (Zellers et al., 2019), ARC, WinoGrande, TruthfulQA, PSN-IRT (Zhou et al., 2026), and the web-overlap contamination labels (Li et al., 2024). The ETS classification system and MH method (Holland & Thayer, 1988) are also cited.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/arr_checklist_draft.md:44:**Justification**: §2 and §4 describe the METABENCH dataset dimensions (5,227 models × 12,508 MMLU items), temporal cohort definitions (2023 vs. 2024 by release date, N_ref=1,080, N_focal=807), and cross-benchmark coverage (6 benchmarks with item counts in Table 5). MMLU's 57-subject domain structure is discussed with subject-level DIF rates.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/circularity_ablation_report.md:72
…[truncated 6463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-23T19:54:33.892023+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_16.md | grep -n \"0.41\\|0.51\\|difficulty.*dep\\|overestim\" | head -20",
  "description": "Check round_16 review for 0.41 ΔTPR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_16.md | grep -n \"0.41\\|0.51\\|difficulty.*dep\\|overestim\" | head -20",
    "description": "Check round_16 review for 0.41 ΔTPR"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-23T19:54:33.892162+00:00_

5:timestamp: 2026-05-23T10:41:35.678595+00:00
99:Uniform binary flipping 是检测的 best-case scenario。论文已加 difficulty-dependent injection（ΔTPR ≈ 0.41 vs 0.51 uniform, ~20% reduction）和 "stylized/may overestimate" 措辞，改善明显。残余问题：instruct 模型残差 gap 13×（无法复制 near-zero direction reversal）。
138:**Q4.** Difficulty × model-type interaction 能解释多大比例的 observed temporal DIF？是否存在 difficulty-dependent capability improvements（无 contamination）即可产生类似幅度 DIF 的可能性？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-23T19:54:33.892299+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/semisynthetic_gradient_report.md | head -80",
  "description": "Read semisynthetic gradient report for ΔTPR=0.41"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/semisynthetic_gradient_report.md | head -80",
    "description": "Read semisynthetic gradient report for ΔTPR=0.41"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-23T19:54:33.892432+00:00_

# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection

**Date**: 2026-05-22 19:01

**Config**: 5 seeds, 1080 ref models (2023), 807 foc models (2024), 12508 items

**Injection**: 242 foc models (30%), ~3001 items (24%)


## Baseline (no injection)

- C%: 31.32%
- ρ(difficulty, δ_MH) among C: -0.587
- % focal-favoring (δ>0): 43.9%
- % ref-favoring (δ<0): 56.1%
- N DIF-C: 3918

## Scheme A — Capability

| Metric | Mean ± SD |
|--------|-----------|
| C% (all items) | 31.88 ± 0.65 |
| C% (injected items) | 27.33 ± 0.94 |
| C% (non-injected) | 33.32 ± 0.82 |
| ρ(diff, δ) all C | -0.532 ± 0.021 |
| ρ(diff, δ) injected C | -0.229 ± 0.058 |
| **ρ(diff, Δδ) injected items** | **0.771 ± 0.029** |
| ρ(diff, Δδ) all items | -0.160 ± 0.131 |
| % focal-favoring (all C, δ>0) | 45.8 ± 1.3 |
| % focal-favoring (inj C, δ>0) | 85.2 ± 1.5 |
| N DIF-C items | 3988 ± 81 |
| N DIF-C (injected) | 820 ± 28 |
| Newly flagged C | 725 ± 74 |
| Mean Δδ (injected items) | 0.796 ± 0.049 |
| Responses flipped | 102528 ± 3208 |
| Items injected | 3001 |

### Quintile Breakdown

| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |
|----------|----------|----------|---------|---------------|-----|-------|
| Q1 | 34.1 | 35.4 | 88.4 | -0.080 | 853 | 585 |
| Q2 | 38.5 | 35.9 | 60.3 | 0.426 | 961 | 602 |
| Q3 | 32.4 | 30.0 | 33.3 | 1.045 | 811 | 620 |
| Q4 | 31.4 | 24.5 | 21.0 | 1.378 | 777 | 596 |
| Q5 | 23.2 | 10.9 | 10.0 | 1.188 | 587 | 598 |

## Scheme B — Contamination

| Metric | Mean ± SD |
|--------|-----------|
| C% (all items) | 32.07 ± 0.79 |
| C% (injected items) | 39.22 ± 6.34 |
| C% (non-injected) | 31.46 ± 0.23 |
| ρ(diff, δ) all C | -0.599 ± 0.015 |
| ρ(diff, δ) injected C | -0.729 ± 0.047 |
| **ρ(diff, Δδ) injected items** | **-0.517 ± 0.107** |
| ρ(diff, Δδ) all items | 0.181 ± 0.136 |
| % focal-favoring (all C, δ>0) | 43.6 ± 0.4 |
| % focal-favoring (inj C, δ>0) | 85.7 ± 3.4 |
| N DIF-C items | 4011 ± 99 |
| N DIF-C (injected) | 351 ± 136 |
| Newly flagged 
…[truncated 581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 632 · 2026-05-23T19:54:33.892583+00:00_

=== TABLE 1 VERIFICATION ===

Row: Temporal (2023 vs 2024)
  N_ref/N_focal = 1080/807 -> plan_001: N=1080/N=807 MATCH
  C% = 31.3 -> dif_summary.csv: 31.32% MATCH
  C% (web-clean) = 0.318 -> plan_001: fpr_vs_li_clean=0.3184 MATCH
  Enrich = 0.964 -> plan_001: enrichment_ratio=0.9641 MATCH

Row: Ability quintile (Q1-2 vs Q4-5)
  N_ref/N_focal = ~2600/~2600 -> model_metadata: Q1-2=2092, Q4-5=2089 MISMATCH
  C% = 2.9 -> dif_summary.csv: 2.9021% MATCH
  C% (web-clean) = 0.027 -> plan_001: fpr_vs_li_clean=0.0269 MATCH
  Enrich = 1.19 -> plan_001: enrichment_ratio=1.1949 MATCH

Row: Within-family (Llama-2 vs 3)
  N_ref/N_focal = 161/308 -> model_metadata: 161/315, plan_027: 161/315 MISMATCH (~7 off)
    (earlier metabench_data_summary.md says 308 -- stale metadata)
  C% = 61.3 -> within_family analysis: 61.34% MATCH

Row: Random split 2023 (sanity)
  N = 540/540 -> random_split_report.md: N=540/540 MATCH
  C% = 0.62 -> _project/data/random_split_report.md: mean null C%=0.6247% MATCH

Row: Random split 2024 (sanity)
  N = ~400/~400 -> r15_random_split_control: ~403/404 MATCH
  C% = 1.3 -> r15_random_split_report: mean C%=1.335% (rounds to 1.3%) MATCH

Row: Within-subject (avg, 5 subj.)
  N = varies (ok)
  C% = 38.1 -> plan_014: average within-subject C%=38.1% MATCH

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 633 · 2026-05-23T19:54:33.892747+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nprint('=== TABLE 2 VERIFICATION ===')\nprint()\nprint('Row: Baseline (ext.)')\nprint('  Mechanism = Cross-bench total score (OK, descriptive)')\nprint('  Temp C% = 0.314±.009 -> plan_011/plan_012 external_5: FPR=0.314±0.009 MATCH')\nprint('  TPR(p=0.5) = 0.834±.027 -> plan_011 external_5 temporal p=0.5: TPR=0.834±0.027 MATCH')\nprint('  Outcome = Reference (OK, descriptive)')\nprint()\nprint('Row: Matched-ability')\nprint('  Mechanism = Within-quintile temp DIF (OK, descriptive)')\nprint('  Temp C% = ~0.31 -> plan_027 NN matched: 28.9%; r22 composition: 30.25%')\nprint('    The ~0.31 claim is INCONSISTENT with best source (plan_027 NN matched = 28.9%)')\nprint('    plan_001b CMH gives 33.3%; r22 gives 30.25%; NN gives 28.9%')\nprint('    No source gives exactly ~31% for ability-matched temporal DIF')\nprint('  TPR = -- (N/A, consistent)')\nprint('  Enrich = 0.94-1.04 -> plan_001b per-quintile: Q1=1.04, Q2=0.94, Q3=0.97, Q4=0.99, Q5=0.96')\nprint('    Range 0.94-1.04 = correct MATCH')\nprint()\nprint('Row: theta-cond (sens.)')\nprint('  Temp C% = 0.312 -> plan_012 theta_qt_20: FPR=0.312±0.008 MATCH')\nprint('  TPR(p=0.5) = 0.876 -> plan_012 theta_qt_20: TPR@p=0.5=0.876 MATCH')\nprint('  r(theta,total) = 0.9986 -> plan_012: correlation = 0.9986 MATCH')\nprint()\nprint('Row: Within-subject')\nprint('  C% = 38.1% -> plan_014: average C%=38.1% MATCH')\nprint('  TPR = -- (consistent with no injection shown for within-subject)')\n\"\n",
  "description": "Compile Table 2 verification results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nprint('=== TABLE 2 VERIFICATION ===')\nprint()\nprint('Row: Baseline (ext.)')\nprint('  Mechanism = Cross-bench total score (OK, descriptive)')\nprint('  Temp C% = 0.314±.009 -> plan_011/plan_012 external_5: FPR=0.314±0.009 MATCH')\nprint('  TPR(p=0.5) = 0.834±.027 -> plan_011 external_5 temporal p=0.5: TPR=0.834±0.027 MATCH')\nprint('  Outcome = Reference (OK, descriptive)')\nprint()\nprint('Row: Matched-ability')\nprint('  Mechanism = Within-quintile temp DIF (OK, descriptive)')\nprint('  Temp C% = ~0.31 -> plan_027 NN matched: 28.9%; r22 composition: 30.25%')\nprint('    The ~0.31 claim is INCONSISTENT with best source (plan_027 NN matched = 28.9%)')\nprint('    plan_001b CMH gives 33.3%; r22 gives 30.25%; NN gives 28.9%')\nprint('    No source gives exactly ~31% for ability-matched temporal DIF')\nprint('  TPR = -- (N/A, consistent)')\nprint('  Enrich = 0.94-1.04 -> plan_001b per-quintile: Q1=1.04, Q2=0.94, Q3=0.97, Q4=0.99, Q5=0.96')\nprint('    Range 0.94-1.04 = correct MATCH')\nprint()\nprint('Row: theta-cond (sens.)')\nprint('  Temp C% = 0.312 -> plan_012 theta_qt_20: FPR=0.312±0.008 MATCH')\nprint('  TPR(p=0.5) = 0.876 -> plan_012 theta_qt_20: TPR@p=0.5=0.876 MATCH')\nprint('  r(theta,total) = 0.9986 -> plan_012: correlation = 0.9986 MATCH')\nprint()\nprint('Row: Within-subject')\nprint('  C% = 38.1% -> plan_014: average C%=38.1% MATCH')\nprint('  TPR = -- (consistent with no injection shown for within-subject)')\n\"\n",
    "description": "Compile Table 2 verification results"
  }
}
```

</details>

---


### Tool result

_source line 634 · 2026-05-23T19:54:33.892894+00:00_

=== TABLE 2 VERIFICATION ===

Row: Baseline (ext.)
  Mechanism = Cross-bench total score (OK, descriptive)
  Temp C% = 0.314±.009 -> plan_011/plan_012 external_5: FPR=0.314±0.009 MATCH
  TPR(p=0.5) = 0.834±.027 -> plan_011 external_5 temporal p=0.5: TPR=0.834±0.027 MATCH
  Outcome = Reference (OK, descriptive)

Row: Matched-ability
  Mechanism = Within-quintile temp DIF (OK, descriptive)
  Temp C% = ~0.31 -> plan_027 NN matched: 28.9%; r22 composition: 30.25%
    The ~0.31 claim is INCONSISTENT with best source (plan_027 NN matched = 28.9%)
    plan_001b CMH gives 33.3%; r22 gives 30.25%; NN gives 28.9%
    No source gives exactly ~31% for ability-matched temporal DIF
  TPR = -- (N/A, consistent)
  Enrich = 0.94-1.04 -> plan_001b per-quintile: Q1=1.04, Q2=0.94, Q3=0.97, Q4=0.99, Q5=0.96
    Range 0.94-1.04 = correct MATCH

Row: theta-cond (sens.)
  Temp C% = 0.312 -> plan_012 theta_qt_20: FPR=0.312±0.008 MATCH
  TPR(p=0.5) = 0.876 -> plan_012 theta_qt_20: TPR@p=0.5=0.876 MATCH
  r(theta,total) = 0.9986 -> plan_012: correlation = 0.9986 MATCH

Row: Within-subject
  C% = 38.1% -> plan_014: average C%=38.1% MATCH
  TPR = -- (consistent with no injection shown for within-subject)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 635 · 2026-05-23T19:54:33.893038+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/semisynthetic_gradient_report.md | grep -A 50 \"Scheme C\" | head -50",
  "description": "Read Scheme C from gradient report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/semisynthetic_gradient_report.md | grep -A 50 \"Scheme C\" | head -50",
    "description": "Read Scheme C from gradient report"
  }
}
```

</details>

---


### Tool result

_source line 636 · 2026-05-23T19:54:33.893171+00:00_

## Scheme C — Mixed

| Metric | Mean ± SD |
|--------|-----------|
| C% (all items) | 31.98 ± 0.54 |
| C% (injected items) | 31.28 ± 2.87 |
| C% (non-injected) | 32.18 ± 0.25 |
| ρ(diff, δ) all C | -0.561 ± 0.017 |
| ρ(diff, δ) injected C | -0.496 ± 0.028 |
| **ρ(diff, Δδ) injected items** | **0.394 ± 0.053** |
| ρ(diff, Δδ) all items | -0.008 ± 0.101 |
| % focal-favoring (all C, δ>0) | 45.8 ± 1.6 |
| % focal-favoring (inj C, δ>0) | 83.8 ± 2.7 |
| N DIF-C items | 4000 ± 67 |
| N DIF-C (injected) | 749 ± 99 |
| Newly flagged C | 626 ± 51 |
| Mean Δδ (injected items) | 0.850 ± 0.039 |
| Responses flipped | 93752 ± 14432 |
| Items injected | 2407 |

### Quintile Breakdown

| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |
|----------|----------|----------|---------|---------------|-----|-------|
| Q1 | 37.2 | 53.8 | 89.2 | 0.600 | 931 | 469 |
| Q2 | 39.1 | 36.4 | 60.0 | 0.554 | 978 | 493 |
| Q3 | 32.6 | 30.1 | 29.5 | 0.926 | 815 | 467 |
| Q4 | 29.7 | 23.6 | 17.8 | 1.169 | 735 | 474 |
| Q5 | 21.4 | 12.5 | 8.3 | 1.029 | 542 | 503 |

## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated

Δδ = δ_after − δ_baseline isolates the injection-induced DIF shift.

| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |
|--------|---------------------|-----------------|----------|
| A_capability | 0.771 ± 0.029 | -0.160 ± 0.131 | positive (easy→more focal DIF) |
| B_contamination | -0.517 ± 0.107 | 0.181 ± 0.136 | ≈ 0 (uniform) |
| C_mixed | 0.394 ± 0.053 | -0.008 ± 0.101 | intermediate |

## Interpretation

**Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring. Δδ = δ_after − δ_before; positive Δδ = injection shifted item toward focal-favoring.

### Key finding: three schemes produce cleanly separable ρ(diff, Δδ) signatures

1. **Scheme A** (capability-like): ρ(diff, Δδ) ≈ **+0.77**. Injection probability ∝ item accuracy → easy items receive more flips → larger focal-favoring Δδ on easy items. Strong positive correlation.
2. *
…[truncated 429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 637 · 2026-05-23T19:54:33.893336+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"0.41\\|ΔTPR\\|delta.*tpr\\|tpr.*delta\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/semisynthetic_gradient_report.md | head -15",
  "description": "Find ΔTPR values in gradient report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"0.41\\|ΔTPR\\|delta.*tpr\\|tpr.*delta\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/semisynthetic_gradient_report.md | head -15",
    "description": "Find ΔTPR values in gradient report"
  }
}
```

</details>

---


### Tool result

_source line 638 · 2026-05-23T19:54:33.893462+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-23T19:54:33.893641+00:00_

Here is the complete audit:

---

## Table 1 核查

- Cell [Temporal, N_ref/N_focal] = 1,080 / 807 ← `plan_001/dif_summary.csv` + `plan_029_permutation_null/run_final.log`: N_ref=1080, N_foc=807 ✅
- Cell [Temporal, C%] = 31.3 ← `plan_001/dif_summary.csv`: pct_c=31.3240% ✅
- Cell [Temporal, C% (web-clean)] = 0.318 ← `plan_001/dif_summary.csv`: fpr_vs_li_clean=0.31840 ✅
- Cell [Temporal, Enrich.] = 0.964 ← `plan_001/dif_summary.csv`: enrichment_ratio=0.96415 ✅

- Cell [Ability quintile, N_ref/N_focal] = ~2,600 / ~2,600 ← `model_metadata.csv` + `plan_001_report.md`: Q1-2=2,092, Q4-5=2,089 ❌ (paper overstates by ~500 per group; source consistently shows 2,092/2,089)
- Cell [Ability quintile, C%] = 2.9 ← `plan_001/dif_summary.csv`: pct_c=2.9021% ✅
- Cell [Ability quintile, C% (web-clean)] = 0.027 ← `plan_001/dif_summary.csv`: fpr_vs_li_clean=0.026862 ✅
- Cell [Ability quintile, Enrich.] = 1.19 ← `plan_001/dif_summary.csv`: enrichment_ratio=1.1949 ✅

- Cell [Within-family, N_ref/N_focal] = 161 / 308 ← `model_metadata.csv` (current): llama-2=161, llama-3=315; `plan_027_temporal_overlap/temporal_overlap_report.md`: 161/315 ⚠️ (paper matches an earlier metadata version that shows 308; current data shows 315. The earlier count of 308 appears in `artifacts/metabench_data_summary.md`. The 61.3% C% is unaffected either way.)
- Cell [Within-family, C%] = 61.3 ← `plan_001_real_data_dif_mmlu/report/plan_001_report.md`: llama-2 vs llama-3 C=7672 (61.34%) ✅

- Cell [Random split 2023, N] = 540 / 540 ← `artifacts/_project/data/random_split_report.md`: "100 random permutations (each 540 ref vs 540 foc)" ✅
- Cell [Random split 2023, C%] = 0.62 ← `artifacts/_project/data/random_split_report.md`: "Mean null C% per split: 0.6247%" ✅

- Cell [Random split 2024, N] = ~400 / ~400 ← `r15_random_split_control/random_split_report.md`: 807 models split 50/50 → ~403/404 ✅
- Cell [Random split 2024, C%] = 1.3 ← `r15_random_split_control/random_split_report.md`: mean C%=1.335% ✅

- Cell [Within-subject
…[truncated 2630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Agent",
  "elapsed_ms": 92
}
```

</details>

---


### Tool result

_source line 640 · 2026-05-23T19:54:33.893902+00:00_

Based on all the data gathered, here is the complete audit report:

---

## §5.1 Validation: DIF Detection Power

- `N ≥ 80` per cohort threshold ← dif_phase2_results.csv: N=80 rows present ✅
- `TPR of 0.68--0.80` (ETS C, uniform injection, |Δ_MH|≥1.4) ← dif_phase2_results.csv: N=80,delta=1.4: ets_c_tpr=0.6823; N=80,delta=1.6: ets_c_tpr=0.7223; N=100,delta=1.4: ets_c_tpr=0.7582; N=100,delta=1.6: ets_c_tpr=0.7966 → range 0.68–0.80 spans both N=80 and N=100 rows ✅
- `AUC of 0.93--0.94` (|Δ_MH|≥1.4) ← dif_phase2_results.csv: N=80,delta=1.4: auc=0.8950; N=80,delta=1.6: auc=0.8936; N=100,delta=1.4: auc=0.9231; N=100,delta=1.6: auc=0.9254 → 0.93–0.94 only matches N=100 rows; N=80 AUC=0.89–0.90 ⚠️ (range accurate if referencing N=100, but paper says "at N≥80" implying N=80 suffices; AUC at N=80 is ~0.89–0.90, not 0.93–0.94)
- `ā = 1.2` ← sf8_power_sensitivity/sf8_report.md: PSN-IRT a mean=1.197 → rounds to 1.2 ✅
- `b̄ = -0.84` ← sf8_power_sensitivity/sf8_report.md: b mean=-0.838 → rounds to -0.84 ✅
- `N_ref = 1,080` ← plan_001/dif_summary.csv: N_ref=1080 ✅
- `N_focal = 807` ← plan_001/dif_summary.csv: N_focal=807 ✅
- `TPR 0.40--0.95 across a = 0.5--2.0` ← sf8_report.md: TPR range 0.398–0.949 → rounds to 0.40–0.95 ✅

## §5.2 Temporal DIF: ~29% of Items Exhibit Differential Functioning

- `31.3%` ETS C classification ← plan_001/dif_summary.csv: 31.323% ✅
- `|Δ_MH| ≥ 1.5` threshold used ← plan_001/dif_summary.csv: criterion confirmed ✅
- bootstrap 95% CI `[29.4%, 38.1%]` (model-level) ← sf1_cluster_bootstrap/bootstrap_results.csv: computed [29.2%, 37.8%] ⚠️ (paper's lower bound 29.4% vs computed 29.2%; upper bound 38.1% vs computed 37.8%)
- family-level cluster bootstrap `[26.7%, 53.2%]` ← sf1_cluster_bootstrap/cluster_bootstrap_ci.md: [26.73%, 53.17%] → rounds to [26.7%, 53.2%] ✅
- simple-mean DEFF → `29.2%` ← mf2_deff_estimation/deff_summary.md: 29.2% ✅
- weighted-mean DEFF → `13.5%` ← mf2_deff_estimation/deff_summary.md: 13.5% ✅
- under weighted-mean DEFF: `ρ = 0.999` ← _p
…[truncated 8505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Agent",
  "elapsed_ms": 81
}
```

</details>

---


### Tool call

_source line 641 · 2026-05-23T19:54:33.894110+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv 2>/dev/null | head -5",
  "description": "Check bootstrap CI source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv 2>/dev/null | head -5",
    "description": "Check bootstrap CI source"
  }
}
```

</details>

---


### Tool result

_source line 642 · 2026-05-23T19:54:33.894246+00:00_

bootstrap_type,iteration,c_pct
cluster,0,0.3675247841381516
cluster,1,0.37663895107131434
cluster,2,0.43316277582347296
cluster,3,0.3580108730412536

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 643 · 2026-05-23T19:54:33.894370+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_phase2_results.csv 2>/dev/null | head -3 && echo \"---\" && grep \"N_per_group,80\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_phase2_results.csv 2>/dev/null | head -5",
  "description": "Check AUC at N=80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_phase2_results.csv 2>/dev/null | head -3 && echo \"---\" && grep \"N_per_group,80\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_phase2_results.csv 2>/dev/null | head -5",
    "description": "Check AUC at N=80"
  }
}
```

</details>

---


### Tool result

_source line 644 · 2026-05-23T19:54:33.894492+00:00_

n_per_group,delta,method,tpr_raw,fpr_raw,tpr_bh,fpr_bh,ets_c_tpr,ets_c_fpr,auc,n_reps,verdict
50,0.8,MH,0.2411,0.0273,0.0127,0.0001,0.2346,0.027,0.7302,1000,N/A
50,0.8,LR,0.3036,0.0641,0.0334,0.0011,,,0.7105,1000,N/A
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 645 · 2026-05-23T19:54:33.894614+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/benchmark_rho_summary.csv 2>/dev/null",
  "description": "Check τ and flip rate across benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/benchmark_rho_summary.csv 2>/dev/null",
    "description": "Check τ and flip rate across benchmarks"
  }
}
```

</details>

---


### Tool result

_source line 646 · 2026-05-23T19:54:33.894758+00:00_

benchmark,n_items_total,n_items_c,n_items_stable,pct_c,n_models,spearman_rho,spearman_p,kendall_tau,flip_rate
TruthfulQA,817,243,574,29.74,5228,0.997123,0.00e+00,0.958635,0.020682
ARC,1172,315,857,26.88,5227,0.996209,0.00e+00,0.953791,0.023104
WinoGrande,1267,384,883,30.31,6558,0.994255,0.00e+00,0.943166,0.028417
GSM8K,1319,249,1070,18.88,6702,0.999303,0.00e+00,0.984311,0.007844
HellaSwag,10042,1797,8245,17.89,5227,0.998623,0.00e+00,0.972166,0.013917
MMLU,12508,3918,8590,31.32,5227,0.9965,0.00e+00,0.959986,0.020007

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 647 · 2026-05-23T19:54:33.894894+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"quintile\\|Q1.*Q2\\|ability\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_summary.csv 2>/dev/null | head -5 && echo \"===\" && grep -i \"2092\\|2089\\|2600\\|quintile\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md 2>/dev/null | head -10",
  "description": "Check ability quintile N"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"quintile\\|Q1.*Q2\\|ability\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_summary.csv 2>/dev/null | head -5 && echo \"===\" && grep -i \"2092\\|2089\\|2600\\|quintile\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md 2>/dev/null | head -10",
    "description": "Check ability quintile N"
  }
}
```

</details>

---


### Tool result

_source line 648 · 2026-05-23T19:54:33.895017+00:00_

ability,all,12508,11052,1093,363,2.9021426287176206,0.026862464183381087,1.1949300411522636
===
- Ability cohort: ref = Q1-2 (N=2092), foc = Q4-5 (N=2089), 10 strata

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 649 · 2026-05-23T19:54:33.895138+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check bootstrap CI percentiles\npython3 -c \"\nimport csv\nvals = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv') as f:\n    r = csv.DictReader(f)\n    for row in r:\n        if row['bootstrap_type'] == 'cluster':\n            vals.append(float(row['c_pct']))\nvals.sort()\nn = len(vals)\nprint(f'N bootstrap samples: {n}')\nlo = vals[int(0.025*n)]\nhi = vals[int(0.975*n)]\nprint(f'2.5th percentile: {lo:.4f} = {lo*100:.2f}%')\nprint(f'97.5th percentile: {hi:.4f} = {hi*100:.2f}%')\n# Also check model-level bootstrap\nvals2 = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv') as f:\n    r = csv.DictReader(f)\n    for row in r:\n        if row['bootstrap_type'] != 'cluster':\n            vals2.append(float(row['c_pct']))\nif vals2:\n    vals2.sort()\n    n2 = len(vals2)\n    print(f'Model-level N: {n2}')\n    lo2 = vals2[int(0.025*n2)]\n    hi2 = vals2[int(0.975*n2)]\n    print(f'Model 2.5th: {lo2:.4f} = {lo2*100:.2f}%')\n    print(f'Model 97.5th: {hi2:.4f} = {hi2*100:.2f}%')\n\"\n",
  "description": "Compute bootstrap CI from raw data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check bootstrap CI percentiles\npython3 -c \"\nimport csv\nvals = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv') as f:\n    r = csv.DictReader(f)\n    for row in r:\n        if row['bootstrap_type'] == 'cluster':\n            vals.append(float(row['c_pct']))\nvals.sort()\nn = len(vals)\nprint(f'N bootstrap samples: {n}')\nlo = vals[int(0.025*n)]\nhi = vals[int(0.975*n)]\nprint(f'2.5th percentile: {lo:.4f} = {lo*100:.2f}%')\nprint(f'97.5th percentile: {hi:.4f} = {hi*100:.2f}%')\n# Also check model-level bootstrap\nvals2 = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv') as f:\n    r = csv.DictReader(f)\n    for row in r:\n        if row['bootstrap_type'] != 'cluster':\n            vals2.append(float(row['c_pct']))\nif vals2:\n    vals2.sort()\n    n2 = len(vals2)\n    print(f'Model-level N: {n2}')\n    lo2 = vals2[int(0.025*n2)]\n    hi2 = vals2[int(0.975*n2)]\n    print(f'Model 2.5th: {lo2:.4f} = {lo2*100:.2f}%')\n    print(f'Model 97.5th: {hi2:.4f} = {hi2*100:.2f}%')\n\"\n",
    "description": "Compute bootstrap CI from raw data"
  }
}
```

</details>

---


### Tool result

_source line 650 · 2026-05-23T19:54:33.895265+00:00_

N bootstrap samples: 1000
2.5th percentile: 0.2673 = 26.73%
97.5th percentile: 0.5325 = 53.25%
Model-level N: 1000
Model 2.5th: 0.2923 = 29.23%
Model 97.5th: 0.3779 = 37.79%

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 651 · 2026-05-23T19:54:33.895380+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check AUC at N=80 specifically\ngrep \"^80,\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_phase2_results.csv | head -10",
  "description": "Check AUC values at N=80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check AUC at N=80 specifically\ngrep \"^80,\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_phase2_results.csv | head -10",
    "description": "Check AUC values at N=80"
  }
}
```

</details>

---


### Tool result

_source line 652 · 2026-05-23T19:54:33.895497+00:00_

80,0.8,MH,0.3931,0.0335,0.0661,0.0003,0.3911,0.0334,0.8037,1000,N/A
80,0.8,LR,0.4155,0.0598,0.0951,0.0014,,,0.7777,1000,N/A
80,1.0,MH,0.5181,0.0347,0.1608,0.0006,0.5136,0.0346,0.8544,1000,N/A
80,1.0,LR,0.5358,0.0622,0.2035,0.0026,,,0.8327,1000,N/A
80,1.2,MH,0.6214,0.0357,0.2862,0.001,0.6075,0.0357,0.8793,1000,N/A
80,1.2,LR,0.6333,0.0638,0.3329,0.0034,,,0.8717,1000,N/A
80,1.4,MH,0.7045,0.0361,0.4001,0.0016,0.6823,0.0361,0.895,1000,PASS
80,1.4,LR,0.7186,0.065,0.4496,0.0046,,,0.9003,1000,N/A
80,1.6,MH,0.7645,0.0386,0.4864,0.0019,0.7223,0.0386,0.8936,1000,PASS
80,1.6,LR,0.7726,0.068,0.5365,0.0062,,,0.9242,1000,N/A

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 653 · 2026-05-23T19:54:33.895622+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Compute cross-benchmark mean τ and max flip rate\npython3 -c \"\ntaus = [0.958635, 0.953791, 0.943166, 0.984311, 0.972166, 0.959986]\nflips = [0.020682, 0.023104, 0.028417, 0.007844, 0.013917, 0.020007]\nprint(f'Mean tau: {sum(taus)/len(taus):.4f}')\nprint(f'Min tau: {min(taus):.4f}')\nprint(f'Max flip: {max(flips)*100:.2f}%')\n# Also check: paper says rho=0.997\nrhos = [0.997123, 0.996209, 0.994255, 0.999303, 0.998623, 0.9965]\nprint(f'Mean rho: {sum(rhos)/len(rhos):.4f}')\nprint(f'Min rho: {min(rhos):.4f}')\n\"\n",
  "description": "Compute cross-benchmark means"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Compute cross-benchmark mean τ and max flip rate\npython3 -c \"\ntaus = [0.958635, 0.953791, 0.943166, 0.984311, 0.972166, 0.959986]\nflips = [0.020682, 0.023104, 0.028417, 0.007844, 0.013917, 0.020007]\nprint(f'Mean tau: {sum(taus)/len(taus):.4f}')\nprint(f'Min tau: {min(taus):.4f}')\nprint(f'Max flip: {max(flips)*100:.2f}%')\n# Also check: paper says rho=0.997\nrhos = [0.997123, 0.996209, 0.994255, 0.999303, 0.998623, 0.9965]\nprint(f'Mean rho: {sum(rhos)/len(rhos):.4f}')\nprint(f'Min rho: {min(rhos):.4f}')\n\"\n",
    "description": "Compute cross-benchmark means"
  }
}
```

</details>

---


### Tool result

_source line 654 · 2026-05-23T19:54:33.895772+00:00_

Mean tau: 0.9620
Min tau: 0.9432
Max flip: 2.84%
Mean rho: 0.9970
Min rho: 0.9943

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 655 · 2026-05-23T19:54:33.895898+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check score inflation for ±800 claim\ngrep -i \"max\\|displace\\|800\\|849\\|589\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/score_inflation_report.md 2>/dev/null | head -10",
  "description": "Check displacement claims"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check score inflation for ±800 claim\ngrep -i \"max\\|displace\\|800\\|849\\|589\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/score_inflation_report.md 2>/dev/null | head -10",
    "description": "Check displacement claims"
  }
}
```

</details>

---


### Tool result

_source line 656 · 2026-05-23T19:54:33.896023+00:00_

| Sao10K/14B-Glacier-Stack | other | base | 0.7047 | 0.7168 | +1.20 | -849 |
Despite measurable score changes, the overall ranking is highly preserved (ρ = 0.9965), indicating that DIF primarily shifts absolute scores rather than relative ordering. However, individual models can experience rank displacements exceeding ±561 positions (99th percentile).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 657 · 2026-05-23T19:54:33.896170+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check the 18.3% at |Δ_MH|≥2.0\npython3 -c \"\nimport csv\ncount = 0\ntotal = 0\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv') as f:\n    r = csv.DictReader(f)\n    for row in r:\n        total += 1\n        if abs(float(row.get('delta_mh', row.get('MH_delta', 0)))) >= 2.0:\n            count += 1\nprint(f'Total items: {total}')\nprint(f'Count |Δ_MH|≥2.0: {count}')\nprint(f'Pct: {count/total*100:.2f}%')\n\"\n",
  "description": "Check 18.3% threshold claim"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check the 18.3% at |Δ_MH|≥2.0\npython3 -c \"\nimport csv\ncount = 0\ntotal = 0\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv') as f:\n    r = csv.DictReader(f)\n    for row in r:\n        total += 1\n        if abs(float(row.get('delta_mh', row.get('MH_delta', 0)))) >= 2.0:\n            count += 1\nprint(f'Total items: {total}')\nprint(f'Count |Δ_MH|≥2.0: {count}')\nprint(f'Pct: {count/total*100:.2f}%')\n\"\n",
    "description": "Check 18.3% threshold claim"
  }
}
```

</details>

---


### Tool result

_source line 658 · 2026-05-23T19:54:33.896309+00:00_

Total items: 12508
Count |Δ_MH|≥2.0: 2297
Pct: 18.36%

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 659 · 2026-05-23T19:54:33.896440+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check max downward displacement\ngrep -E \"\\-[5-9][0-9]{2}\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/score_inflation_report.md 2>/dev/null | head -5\necho \"===\"\n# Check plan_032 for displacement info\ngrep -i \"max\\|displace\\|800\\|rank_change\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_report.md 2>/dev/null | head -10",
  "description": "Check max displacement values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check max downward displacement\ngrep -E \"\\-[5-9][0-9]{2}\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/score_inflation_report.md 2>/dev/null | head -5\necho \"===\"\n# Check plan_032 for displacement info\ngrep -i \"max\\|displace\\|800\\|rank_change\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_report.md 2>/dev/null | head -10",
    "description": "Check max displacement values"
  }
}
```

</details>

---


### Tool result

_source line 660 · 2026-05-23T19:54:33.896576+00:00_

| Sao10K/14B-Glacier-Stack | other | base | 0.7047 | 0.7168 | +1.20 | -849 |
| AA051611/A0118 | other | base | 0.6986 | 0.7036 | +0.50 | -827 |
| DeepMount00/Phi-3-Mini-4K-Boost | 2024 | base | 0.7024 | 0.7143 | +1.20 | -811 |
| DeepMount00/phi_3 | 2024 | base | 0.7024 | 0.7143 | +1.20 | -811 |
| Mihaiii/Pallas-0.5-frankenmerge | other | base | 0.7131 | 0.7191 | +0.60 | -809 |
===
- Min: -589 | Max: 849
| model_name | family | cohort_temporal | score_full | score_cleaned | rank_full | rank_cleaned | rank_change |
| model_name | family | cohort_temporal | score_full | score_cleaned | rank_full | rank_cleaned | rank_change |
| family | n_models | mean_rank_change | median_rank_change | mean_abs_change | mean_score_full |
| family | n_models | mean_rank_change | median_rank_change | mean_abs_change | mean_score_full |
| rank_change_std | +127.087 | +60.245 | 7.837 | +8.53 |
| mean_abs_rank_change | +74.685 | +36.013 | 3.626 | +10.66 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 661 · 2026-05-23T19:54:33.896731+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check the within-family N_focal=308 vs 315\ngrep -i \"llama.*3\\|308\\|315\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/metabench_data_summary.md 2>/dev/null | head -5\necho \"===\"\ngrep \"llama-3\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv 2>/dev/null | wc -l",
  "description": "Check Llama-3 model count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check the within-family N_focal=308 vs 315\ngrep -i \"llama.*3\\|308\\|315\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/metabench_data_summary.md 2>/dev/null | head -5\necho \"===\"\ngrep \"llama-3\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv 2>/dev/null | wc -l",
    "description": "Check Llama-3 model count"
  }
}
```

</details>

---


### Tool result

_source line 662 · 2026-05-23T19:54:33.896869+00:00_

| llama-3 | 308 |
| llama-1 | 135 |
Note: these are models with explicit RL signals in names. Many models (Llama-3, Qwen-2.5, etc.) used RLHF but don't advertise it in their names. The DPO-labeled models alone provide a substantial pool for RL contamination analysis.
**YES.** 477 explicitly labeled (mostly DPO). Many more used RLHF implicitly (Llama-3, Qwen-2, etc.) but aren't detectable from names alone.
===
316

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 663 · 2026-05-23T19:54:33.897034+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check N=100 AUC values\ngrep \"^100,\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_phase2_results.csv | grep \"MH\" | head -5",
  "description": "Check AUC at N=100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check N=100 AUC values\ngrep \"^100,\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_phase2_results.csv | grep \"MH\" | head -5",
    "description": "Check AUC at N=100"
  }
}
```

</details>

---


### Tool result

_source line 664 · 2026-05-23T19:54:33.897162+00:00_

100,0.8,MH,0.4813,0.0353,0.1215,0.0005,0.4793,0.0347,0.8358,1000,N/A
100,1.0,MH,0.6089,0.0368,0.2729,0.0011,0.6058,0.0364,0.8816,1000,N/A
100,1.2,MH,0.7088,0.0399,0.4082,0.0018,0.7013,0.0394,0.9103,1000,N/A
100,1.4,MH,0.7745,0.0407,0.5211,0.0022,0.7582,0.0401,0.9231,1000,PASS
100,1.6,MH,0.8241,0.0429,0.6066,0.0029,0.7966,0.0424,0.9254,1000,PASS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 665 · 2026-05-23T19:54:33.897295+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check if there's a τ=0.958 anywhere in plan_032 or score_inflation\ngrep -r \"0.958\\b\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/ 2>/dev/null | head -5\necho \"===\"\ngrep -r \"0.958\\b\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/ 2>/dev/null | head -5\necho \"===\"\ngrep -r \"kendall\\|tau\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_report.md 2>/dev/null | head -5",
  "description": "Search for τ=0.958 source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check if there's a τ=0.958 anywhere in plan_032 or score_inflation\ngrep -r \"0.958\\b\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/ 2>/dev/null | head -5\necho \"===\"\ngrep -r \"0.958\\b\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/ 2>/dev/null | head -5\necho \"===\"\ngrep -r \"kendall\\|tau\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_report.md 2>/dev/null | head -5",
    "description": "Search for τ=0.958 source"
  }
}
```

</details>

---


### Tool result

_source line 666 · 2026-05-23T19:54:33.897441+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/data/cleaned_mmlu_analysis.csv:llmixer/BigWeave-v12-90b,0.7274544291653342,0.7419091967403958,387,363,-24,24,unknown,other
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/data/cleaned_mmlu_analysis.csv:wannaphong/han-llm-7b-v1,0.6113687240166293,0.6419091967403958,3471,3445,-26,26,unknown,other
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/data/cleaned_mmlu_analysis.csv:yeontaek/Platypus2xOpenOrca-13B-IA3-ensemble,0.6160057563159578,0.6419091967403958,3437,3446,9,9,orca,other
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv:llmixer/BigWeave-v12-90b,0.7274544291653342,0.7419091967403958,387,363,-24,24,unknown,other
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv:wannaphong/han-llm-7b-v1,0.6113687240166293,0.6419091967403958,3471,3445,-26,26,unknown,other
===
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/model_scores.csv:flemmingmiguel/DareBeagle-7B,other,base,unknown,0.7049888071634154,0.7265424912689173,0.021553684105501958,535,574,-39,0.7255259679234803,554
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/model_scores.csv:itsliupeng/llama_9b_long,other,base,unknown,0.7153821554205309,0.7284051222351572,0.013022966814626336,449,494,-45,0.7359193161805958,451
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/model_scores.csv:llmixer/BigWeave-v12-90b,other,base,unknown,0.7274544291653342,0.7419091967403958,0.014454767575061589,387,
…[truncated 595 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 667 · 2026-05-23T19:54:33.897596+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# The paper §5.7 says \"across all six benchmarks (ρ=0.997, τ=0.958)\" — check if there's a cross-benchmark summary\ngrep -r \"kendall\\|tau\\|0.958\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/mf2_report.md 2>/dev/null | head -10\necho \"===\"\ngrep -r \"spearman\\|0.997\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/mf2_report.md 2>/dev/null | head -10",
  "description": "Check mf2 report for summary stats"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# The paper §5.7 says \"across all six benchmarks (ρ=0.997, τ=0.958)\" — check if there's a cross-benchmark summary\ngrep -r \"kendall\\|tau\\|0.958\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/mf2_report.md 2>/dev/null | head -10\necho \"===\"\ngrep -r \"spearman\\|0.997\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/mf2_report.md 2>/dev/null | head -10",
    "description": "Check mf2 report for summary stats"
  }
}
```

</details>

---


### Tool result

_source line 668 · 2026-05-23T19:54:33.897748+00:00_

| TruthfulQA | 817 | 243 | 574 | 29.74% | 5228 | 0.9971 | 0.00e+00 | 0.9586 | 0.0207 |
===
| TruthfulQA | 817 | 243 | 574 | 29.74% | 5228 | 0.9971 | 0.00e+00 | 0.9586 | 0.0207 |
- **Mean Spearman ρ**: 0.9970 (range: 0.9943–0.9993)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 669 · 2026-05-23T19:54:33.897881+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Get the full summary section from mf2_report\ngrep -A 20 \"Mean\\|Summary\\|Across\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/mf2_report.md 2>/dev/null | head -30",
  "description": "Check mf2 cross-benchmark summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Get the full summary section from mf2_report\ngrep -A 20 \"Mean\\|Summary\\|Across\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/mf2_report.md 2>/dev/null | head -30",
    "description": "Check mf2 cross-benchmark summary"
  }
}
```

</details>

---


### Tool result

_source line 670 · 2026-05-23T19:54:33.898008+00:00_

## Cross-Benchmark Summary

- **Mean Spearman ρ**: 0.9970 (range: 0.9943–0.9993)
- **Mean flip rate**: 0.0190 (range: 0.0078–0.0284)

## Interpretation

- **WinoGrande** shows the lowest ρ (0.9943) with 30.31% C items.
- **GSM8K** is the most stable (ρ=0.9993, flip rate=0.0078).
- Overall, removing ETS class C items produces minimal rank disruption (mean flip rate 0.0190), but the effect is benchmark-dependent.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 671 · 2026-05-23T19:54:33.898223+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/data_audit_part2.md",
  "content": "# Data Audit Part 2: Experiments & Discussion 数字核查\n\n**日期**: 2026-05-23\n**范围**: experiments.tex (§5) + discussion.tex (§6) 所有数字 + Table 1–3\n\n---\n\n## Table 1 核查 (tab:temporal_landscape)\n\n| Cell | 论文值 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| [Temporal, N_ref/N_focal] | 1,080 / 807 | plan_001/dif_summary.csv | 1080 / 807 | ✅ |\n| [Temporal, C%] | 31.3 | plan_001/dif_summary.csv | 31.324% | ✅ |\n| [Temporal, C% web-clean] | 0.318 | plan_001/dif_summary.csv | 0.31840 | ✅ |\n| [Temporal, Enrich.] | 0.964 | plan_001/dif_summary.csv | 0.96415 | ✅ |\n| [Ability quintile, N_ref/N_focal] | ~2,600 / ~2,600 | plan_001_report.md | Q1-2=2,092 / Q4-5=2,089 | ❌ |\n| [Ability quintile, C%] | 2.9 | plan_001/dif_summary.csv | 2.9021% | ✅ |\n| [Ability quintile, C% web-clean] | 0.027 | plan_001/dif_summary.csv | 0.02686 | ✅ |\n| [Ability quintile, Enrich.] | 1.19 | plan_001/dif_summary.csv | 1.1949 | ✅ |\n| [Within-family, N_ref/N_focal] | 161 / 308 | metabench_data_summary.md / model_metadata.csv | 161 / 308 (旧) or 315-316 (新) | ⚠️ |\n| [Within-family, C%] | 61.3 | plan_001_report.md | 61.34% | ✅ |\n| [Random 2023, N] | 540 / 540 | _project/data/random_split_report.md | 540 / 540 | ✅ |\n| [Random 2023, C%] | 0.62 | _project/data/random_split_report.md | 0.6247% | ✅ |\n| [Random 2024, N] | ~400 / ~400 | r15_random_split_control/random_split_report.md | ~403/404 | ✅ |\n| [Random 2024, C%] | 1.3 | r15_random_split_control/random_split_report.md | 1.335% | ✅ |\n| [Within-subject, C%] | 38.1 | plan_014/plan_014_report.md | 38.1% | ✅ |\n\n---\n\n## Table 2 核查 (tab:structural_comparison)\n\n| Cell | 论文值 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| [Baseline, Temp C%] | 0.314±.009 | plan_011/plan_011_report.md | 0.314±0.009 | ✅ |\n| [Baseline, TPR] | 0.834±.027 | plan_011/plan_011_report.md | 0.834±0.027 | ✅ |\n| [Matched-ability, C%] | ~0.31 | plan_027/temporal_overlap_report.md | 28.9% (1:1 NN); r22: 30.25% | ⚠️ |\n| [Matched-ability, Enrich.] | 0.94–1.04 | plan_001b/plan_001b_report.md | Q1=1.04, Q2=0.94 (range) | ✅ |\n| [θ-cond., C%] | 0.312 | plan_012/plan_012_report.md | 0.312±0.008 | ✅ |\n| [θ-cond., TPR] | 0.876 | plan_012/plan_012_report.md | 0.876 | ✅ |\n| [θ-cond., r(θ,total)] | 0.9986 | plan_012/plan_012_report.md | 0.9986 | ✅ |\n| [Within-subject, C%] | 38.1% | plan_014/plan_014_report.md | 38.1% | ✅ |\n\n---\n\n## Table 3 核查 (tab:cross_benchmark)\n\n| Cell | 论文值 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| [MMLU, Items] | 12,508 | plan_028/multi_bench_summary.csv | 12508 | ✅ |\n| [MMLU, C%] | 31.3 | plan_028 | 31.32% | ✅ |\n| [MMLU, ρ] | 0.9965 | benchmark_rho_summary.csv | 0.9965 | ✅ |\n| [MMLU, τ] | 0.9600 | benchmark_rho_summary.csv | 0.959986 | ✅ |\n| [MMLU, Flip%] | 2.00 | benchmark_rho_summary.csv | 0.020007 → 2.00% | ✅ |\n| [MMLU, Rand C%] | 0.62 | random_split_report.md (100-run mean) | 0.6247% | ✅ |\n| [MMLU, Ratio] | 50× | 31.3/0.62=50.5 | — | ✅ |\n| [WinoGrande, Items] | 1,267 | plan_028 | 1267 | ✅ |\n| [WinoGrande, C%] | 30.3 | plan_028 | 30.31% | ✅ |\n| [WinoGrande, ρ] | 0.9943 | benchmark_rho_summary.csv | 0.994255 | ✅ |\n| [WinoGrande, τ] | 0.9432 | benchmark_rho_summary.csv | 0.943166 | ✅ |\n| [WinoGrande, Flip%] | 2.84 | benchmark_rho_summary.csv | 0.028417 → 2.84% | ✅ |\n| [WinoGrande, Rand C%] | 0.32 | plan_028 random_pct_c | 0.32 | ✅ |\n| [WinoGrande, Ratio] | 95× | 30.3/0.32=94.7 | — | ✅ |\n| [TruthfulQA, Items] | 817 | plan_028 | 817 | ✅ |\n| [TruthfulQA, C%] | 29.7 | plan_028 | 29.74% | ✅ |\n| [TruthfulQA, ρ] | 0.9971 | benchmark_rho_summary.csv | 0.997123 | ✅ |\n| [TruthfulQA, τ] | 0.9586 | benchmark_rho_summary.csv | 0.958635 | ✅ |\n| [TruthfulQA, Flip%] | 2.07 | benchmark_rho_summary.csv | 0.020682 → 2.07% | ✅ |\n| [TruthfulQA, Rand C%] | 0.37 | plan_028 | 0.37 | ✅ |\n| [TruthfulQA, Ratio] | 80× | 29.7/0.37=80.3 | — | ✅ |\n| [ARC, Items] | 1,172 | plan_028 | 1172 | ✅ |\n| [ARC, C%] | 26.9 | plan_028 | 26.88% | ✅ |\n| [ARC, ρ] | 0.9962 | benchmark_rho_summary.csv | 0.996209 | ✅ |\n| [ARC, τ] | 0.9538 | benchmark_rho_summary.csv | 0.953791 | ✅ |\n| [ARC, Flip%] | 2.31 | benchmark_rho_summary.csv | 0.023104 → 2.31% | ✅ |\n| [ARC, Rand C%] | 0.60 | plan_028 | 0.6 | ✅ |\n| [ARC, Ratio] | 45× | 26.9/0.60=44.8 | — | ✅ |\n| [GSM8K, Items] | 1,319 | plan_028 | 1319 | ✅ |\n| [GSM8K, C%] | 18.9 | plan_028 | 18.88% | ✅ |\n| [GSM8K, ρ] | 0.9993 | benchmark_rho_summary.csv | 0.999303 | ✅ |\n| [GSM8K, τ] | 0.9843 | benchmark_rho_summary.csv | 0.984311 | ✅ |\n| [GSM8K, Flip%] | 0.78 | benchmark_rho_summary.csv | 0.007844 → 0.78% | ✅ |\n| [GSM8K, Rand C%] | 0.30 | plan_028 | 0.3 | ✅ |\n| [GSM8K, Ratio] | 63× | 18.9/0.30=63.0 | — | ✅ |\n| [HellaSwag, Items] | 10,042 | plan_028 | 10042 | ✅ |\n| [HellaSwag, C%] | 17.9 | plan_028 | 17.89% | ✅ |\n| [HellaSwag, ρ] | 0.9986 | benchmark_rho_summary.csv | 0.998623 | ✅ |\n| [HellaSwag, τ] | 0.9722 | benchmark_rho_summary.csv | 0.972166 | ✅ |\n| [HellaSwag, Flip%] | 1.39 | benchmark_rho_summary.csv | 0.013917 → 1.39% | ✅ |\n| [HellaSwag, Rand C%] | 0.28 | plan_028 | 0.28 | ✅ |\n| [HellaSwag, Ratio] | 64× | 17.9/0.28=63.9 | — | ✅ |\n\n**Table 3: 全部 42 cells 核查通过。**\n\n---\n\n## Experiments 正文数字\n\n### §5.1 Validation\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| ā=1.2 | PSN-IRT mean discrimination | sf8_power_sensitivity/sf8_report.md | a mean=1.197 | ✅ |\n| b̄=−0.84 | PSN-IRT mean difficulty | sf8_report.md | b mean=−0.838 | ✅ |\n| N≥80 per cohort | power threshold | dif_phase2_results.csv | N=80 rows present | ✅ |\n| TPR 0.68–0.80 | ETS C under uniform injection | dif_phase2_results.csv | N=80,δ=1.4: 0.6823; N=100,δ=1.6: 0.7966 | ✅ |\n| AUC 0.93–0.94 | for \\|Δ_MH\\|≥1.4 | dif_phase2_results.csv | N=80: AUC=0.895; N=100: AUC=0.923–0.925 | ⚠️ |\n| N_ref=1,080 | temporal cohort | plan_001/dif_summary.csv | 1080 | ✅ |\n| N_focal=807 | temporal cohort | plan_001/dif_summary.csv | 807 | ✅ |\n| TPR 0.40–0.95 | across a=0.5–2.0 | sf8_report.md | 0.398–0.949 | ✅ |\n\n### §5.2 Temporal DIF\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| 31.3% | C items | plan_001/dif_summary.csv | 31.324% | ✅ |\n| \\|Δ_MH\\|≥1.5 | ETS C threshold | plan_001 | criterion confirmed | ✅ |\n| CI [29.4%, 38.1%] | bootstrap 95% CI | sf1_cluster_bootstrap/bootstrap_results.csv | 计算值: [29.23%, 37.79%] | ❌ |\n| CI [26.7%, 53.2%] | family-level cluster bootstrap | sf1_cluster_bootstrap/cluster_bootstrap_ci.md | [26.73%, 53.17%] | ✅ |\n| DEFF simple-mean → 29.2% | DEFF upper | mf2_deff_estimation/deff_summary.md | 29.2% | ✅ |\n| DEFF weighted-mean → 13.5% | DEFF lower | mf2_deff_estimation/deff_summary.md | 13.5% | ✅ |\n| ρ=0.999 | under weighted-mean DEFF | _project/data/weighted_mean_downstream.md | 0.998811 | ✅ |\n| +1.77pp | score shift under weighted-mean | _project/data/weighted_mean_downstream.md | +1.772pp | ✅ |\n| P99 \\|Δ_MH\\|=1.45 | permutation null | _project/data/random_split_report.md | 1.4504 | ✅ |\n| 0.62% | random split 2023 | _project/data/random_split_report.md | 0.6247% | ✅ |\n| 1.3% | random split 2024 | r15_random_split_control | 1.335% | ✅ |\n| ≥24× | below temporal C% | 31.3/1.3=24.1 | — | ✅ |\n| 2.9% | ability quintile C% | plan_001/dif_summary.csv | 2.9021% | ✅ |\n| N=638/group | NN matching | temporal_overlap_report.md | 638 | ✅ |\n| Cohen's d=−0.17 | matching context | temporal_overlap_report.md | −0.17 (pre-match gap) | ⚠️ |\n| C%=28.9%±0.1% | matched C% | temporal_overlap_report.md | 28.9%±0.1% | ✅ |\n| ~2.4pp | ability mismatch | 31.3−28.9=2.4 | — | ✅ |\n| p<0.01 | matching significance | temporal_overlap_report.md | confirmed | ✅ |\n| LOFO \\|ΔC%\\|≤2.93pp | max LOFO | lofo_robustness/lofo_results.csv | 2.93pp (mixtral) | ✅ |\n| 20.7%–48.4% | subject C% range | plan_033_report.md | confirmed | ✅ |\n| mean≈30% | subject mean C% | plan_033_report.md | 30.6% | ✅ |\n| KW p=0.78 | domain invariance | plan_033_report.md | 0.7797 | ✅ |\n| STEM 55.4% | favor 2024 | plan_033_report.md | 55.4% | ✅ |\n| Humanities 64.4% | favor 2023 | plan_033_report.md | 100−35.58=64.42% | ✅ |\n| <0.1% variance | domain accuracy → DIF | interaction_report.md | R²<0.001 | ✅ |\n| ρ=−0.597 | difficulty–direction | interaction_report.md | −0.597 | ✅ |\n| 18.3% at \\|Δ_MH\\|≥2.0 | threshold sensitivity | plan_001/dif_results_temporal.csv | 2297/12508=18.37% → 18.4% | ⚠️ |\n| 10.2% at \\|Δ_MH\\|≥2.5 | threshold sensitivity | plan_001/dif_results_temporal.csv | 1278/12508=10.22% | ✅ |\n\n### §5.3 Comparison with Web-Overlap Labels\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| 9,229 | annotated items | plan_001/plan_001_report.md | 9229 | ✅ |\n| enrichment=0.964 | DIF vs web-overlap | plan_001/dif_summary.csv | 0.96415 | ✅ |\n| Jaccard=0.206 | DIF–web overlap | r17_jaccard_permutation | 0.2063 | ✅ |\n| p=0.88 | Fisher exact | computed | 0.8806 | ✅ |\n| 30.7% | DIF-C among web-contam | plan_001_report.md | 0.3070 | ✅ |\n| 31.8% | DIF-C among clean | plan_001_report.md | 0.3184 | ✅ |\n| χ²=562.7 | base/instruct reversal | r18_base_vs_instruct_dif | 562.70 | ✅ |\n| ΔTPR=+0.508 | semi-synthetic p=0.5 | plan_011_report.md | +0.508 | ✅ |\n\n### §5.4 Structural Analysis\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| 17.7% | non-uniform DIF | r16_dif_union | 317/1787=17.74% | ✅ |\n| union 47% | total flagged | r16_dif_union | 47.0% | ✅ |\n| ~28–29% | ability-matched convergence | temporal_overlap_report.md | 28.9% | ✅ |\n| r(θ,total)=0.9986 | IRT conditioning | plan_012_report.md | 0.9986 | ✅ |\n\n### §5.5 Detection Power (Semi-synthetic Injection)\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| ΔFPR=0.000 | cross-subject, 5 subjects | plan_011_report.md | 0.000 | ✅ |\n| 4/5 with ΔTPR>0.3 | at p=0.5 | plan_011_report.md | confirmed | ✅ |\n| +0.186 avg | within-subject FPR inflation | plan_011_report.md | +0.186 | ✅ |\n| k≤5: ΔFPR<0.007 | single-subject contamination | summary_by_k_full.csv | k=5: 0.0065 | ✅ |\n| k=10: ΔFPR=0.069 | 18% of domains | summary_by_k_full.csv | 0.069 | ✅ |\n| k=20: ΔFPR=0.167 | multi-subject | summary_by_k_full.csv | 0.1673 | ✅ |\n| k≥30: ΔFPR>0.36 | >50% domains | summary_by_k_full.csv | k=30: 0.3618 | ✅ |\n| ΔTPR≈0.41 | difficulty-dependent | mixed_mechanism_report.md | ~0.41 | ✅ |\n| 0.51 | uniform reference | plan_011_report.md | ~0.508 | ✅ |\n| ~20% | overestimation bound | (0.51−0.41)/0.51=19.6% | — | ✅ |\n\n### §5.6 Downstream Impact\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| ρ=0.997 | across 6 benchmarks | benchmark_rho_summary.csv | mean=0.9970 | ✅ |\n| τ=0.958 | across 6 benchmarks | benchmark_rho_summary.csv | mean=0.9620; 无单值=0.958 | ❌ |\n| flip rate ≤2.8% | max flip | benchmark_rho_summary.csv | WinoGrande=2.84% > 2.8% | ❌ |\n| z=−8 to −49 | vs random removal | plan_017_report.md | −8.16 to −49.44 | ✅ |\n| 33.6% | pairwise reversals (top 200) | mf1_worked_examples/mf1_report.md | 6694/19900=33.6% | ✅ |\n| 96.2 positions | cohort gap | plan_032/dif_vs_random_comparison.csv | 96.16 | ✅ |\n| 40× random | cohort gap ratio | 96.16/2.36=40.7 | — | ✅ |\n| p<0.001 | cohort gap significance | plan_032_report | confirmed | ✅ |\n| +2.12pp | avg accuracy shift | score_inflation_report.md | +2.116pp | ✅ |\n| 0.29pp | cohort-differential | score_inflation_report.md | 2.351−2.060=0.291pp | ✅ |\n| d=0.31 | Cohen's d | score_inflation_report.md | \\|d\\|=0.3051 | ✅ |\n| ±800 | individual displacements | score_inflation_report.md | max down=−849; report P99=±561 | ⚠️ |\n\n### §5.7 Cross-Benchmark Validation\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| 17.9%–31.3% | C% range | plan_028/multi_bench_summary.csv | confirmed | ✅ |\n| 26.9–31.3% | knowledge/reasoning | multi_bench_summary.csv | ARC=26.9, others higher | ✅ |\n| 17.9–18.9% | procedural | multi_bench_summary.csv | HellaSwag=17.9, GSM8K=18.9 | ✅ |\n| 45–95× | above random | Table 3 Ratio column | confirmed | ✅ |\n| ΔTPR=+0.514 | GSM8K semi-synthetic | gsm8k_dose_response_summary.csv | +0.514 | ✅ |\n\n---\n\n## Discussion 正文数字\n\n### §6.1 Temporal DIF as Structured Signal\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| N=1,409 | base models | r18_base_vs_instruct_dif | Ref=861+Foc=548=1409 | ✅ |\n| 60.1% | ref-favoring (base) | r18_base_vs_instruct_dif | 2413 (60.1%) | ✅ |\n| ρ=−0.570 | base difficulty–direction | r18_base_vs_instruct_dif | −0.570 | ✅ |\n| N=478 | instruct models | r18_base_vs_instruct_dif | Ref=219+Foc=259=478 | ✅ |\n| 65.6% | focal-favoring (instruct) | r18_base_vs_instruct_dif | 2994 (65.6%) | ✅ |\n| ρ=−0.079 | instruct difficulty–direction | r18_base_vs_instruct_dif | −0.079 | ✅ |\n| χ²=562.7 | direction reversal | r18_base_vs_instruct_dif | 562.70 | ✅ |\n| p<10^−124 | significance | r18_base_vs_instruct_dif | 2.178e-124 | ✅ |\n| Δ=1.08pp | composition downsampling | r22_composition_control | 1.08pp | ✅ |\n| C%=29.2% | DEFF-adjusted headline | r20_size_stratified_deff | simple-mean DEFF→29.2% | ⚠️ |\n| CI [26.7%, 53.2%] | cluster bootstrap | sf1_cluster_bootstrap | [26.73%, 53.17%] | ✅ |\n| Jaccard=0.206 | DIF–web overlap | r17_jaccard_permutation | 0.2063 | ✅ |\n| OR=4.75 | base/instruct interaction | interaction_report.md | 4.754 | ✅ |\n\n### §6.2 Recommended DIF Audit Protocol\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| AUROC=0.60 | predictive model | predictive_model/phase2_results.md | LR=0.6026, GBM=0.5994 | ✅ |\n| ≥500 models | threshold | 无单一源文件 | 来自 rebuttal 实践建议 | ⚠️ |\n| K=3 | smaller corpora | k3_power_simulation/k3_power_report.md | K=3≈K=5 confirmed | ✅ |\n| C%≈12% | 20× baseline for MMLU | 20×0.62%=12.4% | 算术一致 | ✅ |\n\n---\n\n## ⚠️ 不一致 / ❌ 无法追溯\n\n### ❌ 需要修正（3项）\n\n1. **Table 1, Ability quintile N: `~2,600 / ~2,600` → 实际 `~2,090 / ~2,090`**\n   - 源: plan_001_report.md: \"ref = Q1-2 (N=2092), foc = Q4-5 (N=2089)\"\n   - 偏差: 论文多报约500/组\n   - 建议: 改为 `${\\sim}$2,090 / ${\\sim}$2,090`\n\n2. **§5.6 Downstream: τ=0.958 无法追溯**\n   - 源: benchmark_rho_summary.csv 六个 benchmark 的 Kendall τ 值: 0.9432, 0.9538, 0.9586, 0.9600, 0.9722, 0.9843\n   - 均值 = 0.9620, 中位数 = 0.9593, 最小值 = 0.9432 — 无论哪种解释都不等于 0.958\n   - 建议: 改为 `τ = 0.962`（均值）或 `τ \\geq 0.943`（最小值）\n\n3. **§5.6 Downstream: flip rate ≤ 2.8% 不成立**\n   - 源: benchmark_rho_summary.csv WinoGrande flip_rate=0.028417 = **2.84%** > 2.8%\n   - 建议: 改为 `flip rate $\\leq$ 2.9\\%`\n\n### ❌ 需要修正但较小（1项）\n\n4. **§5.2 bootstrap CI [29.4%, 38.1%] 与计算值不符**\n   - 源: sf1_cluster_bootstrap/bootstrap_results.csv 1000次 model-level bootstrap\n   - 计算 2.5th/97.5th percentile: **[29.23%, 37.79%]**\n   - 论文写 [29.4%, 38.1%]，偏差 0.17pp (lower) 和 0.31pp (upper)\n   - 建议: 改为 `[29.2\\%, 37.8\\%]`\n\n### ⚠️ 可接受但需注意（6项）\n\n5. **§5.1 AUC 0.93–0.94 \"at N≥80\"**: N=80 时 AUC=0.895–0.894; 0.93–0.94 仅在 N=100 时成立。论文措辞 \"at N≥80\" 暗示 N=80 即可达到，实际需 N≈100。建议: 改措辞为 \"at N=100\" 或注明 \"0.89–0.94 across N=80–200\"。\n\n6. **§5.2 18.3% at |Δ_MH|≥2.0**: 精确值 2297/12508=18.37%→四舍五入应为 18.4% 而非 18.3%。差异极小，可保留或改为 18.4%。\n\n7. **§5.2 Cohen's d=−0.17**: 值本身正确（temporal_overlap_report.md），但这是 pre-matching 能力差距，不是 post-matching 残差（post-match d=−0.010）。论文上下文可能让读者误以为匹配后仍有 d=0.17 的差距。\n\n8. **§5.6 individual displacements ±800**: score_inflation 中最大负位移 −849（Sao10K），但 P99=±561。report 说 \"exceeding ±561 positions (99th percentile)\"。±800 作为极值描述基本准确（max down=−849），但对称的 \"±\" 表述有误导性（正向最大值需要确认是否也接近 800）。\n\n9. **Table 1, Within-family N_focal=308**: metabench_data_summary.md 记录 308（分析时数据），当前 model_metadata.csv 为 315-316。C% 不受影响。轻微数据版本差异。\n\n10. **Table 2, Matched-ability C%=~0.31**: 最严格的 1:1 NN 匹配得 28.9%，composition-balanced 得 30.25%，CMH quintile 得 33.3%。`~0.31` 依赖于对 \"matched\" 的定义。波浪号（~）做了较多工作。\n\n11. **§6.1 C%=29.2%**: 值来自 DEFF simple-mean 校正结果。§5.2 报告原始 C%=31.3%。Discussion 中使用 29.2% 未注明是 DEFF 校正值，可能让读者困惑。\n\n---\n\n## 统计\n\n- **Tables**: 62 cells checked (Table 1: 15, Table 2: 8, Table 3: 42 — 含 Ratio 推导)\n  - ✅ 57 | ⚠️ 3 | ❌ 2 (Ability quintile N; Within-family N_focal 轻微)\n- **Experiments 正文**: ~55 个数字\n  - ✅ 46 | ⚠️ 6 | ❌ 3 (bootstrap CI, τ, flip rate)\n- **Discussion 正文**: ~17 个数字\n  - ✅ 14 | ⚠️ 3\n\n**需立即修正**: 4 项 (Ability quintile N, bootstrap CI, τ=0.958, flip rate ≤2.8%)\n**建议修正**: 2 项 (AUC at N≥80 措辞, 18.3%→18.4%)\n**建议注意**: 5 项 (Cohen's d 语境, ±800 对称性, Within-family N, Matched C% ~0.31, Discussion C% 29.2% 来源)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/data_audit_part2.md",
    "content": "# Data Audit Part 2: Experiments & Discussion 数字核查\n\n**日期**: 2026-05-23\n**范围**: experiments.tex (§5) + discussion.tex (§6) 所有数字 + Table 1–3\n\n---\n\n## Table 1 核查 (tab:temporal_landscape)\n\n| Cell | 论文值 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| [Temporal, N_ref/N_focal] | 1,080 / 807 | plan_001/dif_summary.csv | 1080 / 807 | ✅ |\n| [Temporal, C%] | 31.3 | plan_001/dif_summary.csv | 31.324% | ✅ |\n| [Temporal, C% web-clean] | 0.318 | plan_001/dif_summary.csv | 0.31840 | ✅ |\n| [Temporal, Enrich.] | 0.964 | plan_001/dif_summary.csv | 0.96415 | ✅ |\n| [Ability quintile, N_ref/N_focal] | ~2,600 / ~2,600 | plan_001_report.md | Q1-2=2,092 / Q4-5=2,089 | ❌ |\n| [Ability quintile, C%] | 2.9 | plan_001/dif_summary.csv | 2.9021% | ✅ |\n| [Ability quintile, C% web-clean] | 0.027 | plan_001/dif_summary.csv | 0.02686 | ✅ |\n| [Ability quintile, Enrich.] | 1.19 | plan_001/dif_summary.csv | 1.1949 | ✅ |\n| [Within-family, N_ref/N_focal] | 161 / 308 | metabench_data_summary.md / model_metadata.csv | 161 / 308 (旧) or 315-316 (新) | ⚠️ |\n| [Within-family, C%] | 61.3 | plan_001_report.md | 61.34% | ✅ |\n| [Random 2023, N] | 540 / 540 | _project/data/random_split_report.md | 540 / 540 | ✅ |\n| [Random 2023, C%] | 0.62 | _project/data/random_split_report.md | 0.6247% | ✅ |\n| [Random 2024, N] | ~400 / ~400 | r15_random_split_control/random_split_report.md | ~403/404 | ✅ |\n| [Random 2024, C%] | 1.3 | r15_random_split_control/random_split_report.md | 1.335% | ✅ |\n| [Within-subject, C%] | 38.1 | plan_014/plan_014_report.md | 38.1% | ✅ |\n\n---\n\n## Table 2 核查 (tab:structural_comparison)\n\n| Cell | 论文值 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| [Baseline, Temp C%] | 0.314±.009 | plan_011/plan_011_report.md | 0.314±0.009 | ✅ |\n| [Baseline, TPR] | 0.834±.027 | plan_011/plan_011_report.md | 0.834±0.027 | ✅ |\n| [Matched-ability, C%] | ~0.31 | plan_027/temporal_overlap_report.md | 28.9% (1:1 NN); r22: 30.25% | ⚠️ |\n| [Matched-ability, Enrich.] | 0.94–1.04 | plan_001b/plan_001b_report.md | Q1=1.04, Q2=0.94 (range) | ✅ |\n| [θ-cond., C%] | 0.312 | plan_012/plan_012_report.md | 0.312±0.008 | ✅ |\n| [θ-cond., TPR] | 0.876 | plan_012/plan_012_report.md | 0.876 | ✅ |\n| [θ-cond., r(θ,total)] | 0.9986 | plan_012/plan_012_report.md | 0.9986 | ✅ |\n| [Within-subject, C%] | 38.1% | plan_014/plan_014_report.md | 38.1% | ✅ |\n\n---\n\n## Table 3 核查 (tab:cross_benchmark)\n\n| Cell | 论文值 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| [MMLU, Items] | 12,508 | plan_028/multi_bench_summary.csv | 12508 | ✅ |\n| [MMLU, C%] | 31.3 | plan_028 | 31.32% | ✅ |\n| [MMLU, ρ] | 0.9965 | benchmark_rho_summary.csv | 0.9965 | ✅ |\n| [MMLU, τ] | 0.9600 | benchmark_rho_summary.csv | 0.959986 | ✅ |\n| [MMLU, Flip%] | 2.00 | benchmark_rho_summary.csv | 0.020007 → 2.00% | ✅ |\n| [MMLU, Rand C%] | 0.62 | random_split_report.md (100-run mean) | 0.6247% | ✅ |\n| [MMLU, Ratio] | 50× | 31.3/0.62=50.5 | — | ✅ |\n| [WinoGrande, Items] | 1,267 | plan_028 | 1267 | ✅ |\n| [WinoGrande, C%] | 30.3 | plan_028 | 30.31% | ✅ |\n| [WinoGrande, ρ] | 0.9943 | benchmark_rho_summary.csv | 0.994255 | ✅ |\n| [WinoGrande, τ] | 0.9432 | benchmark_rho_summary.csv | 0.943166 | ✅ |\n| [WinoGrande, Flip%] | 2.84 | benchmark_rho_summary.csv | 0.028417 → 2.84% | ✅ |\n| [WinoGrande, Rand C%] | 0.32 | plan_028 random_pct_c | 0.32 | ✅ |\n| [WinoGrande, Ratio] | 95× | 30.3/0.32=94.7 | — | ✅ |\n| [TruthfulQA, Items] | 817 | plan_028 | 817 | ✅ |\n| [TruthfulQA, C%] | 29.7 | plan_028 | 29.74% | ✅ |\n| [TruthfulQA, ρ] | 0.9971 | benchmark_rho_summary.csv | 0.997123 | ✅ |\n| [TruthfulQA, τ] | 0.9586 | benchmark_rho_summary.csv | 0.958635 | ✅ |\n| [TruthfulQA, Flip%] | 2.07 | benchmark_rho_summary.csv | 0.020682 → 2.07% | ✅ |\n| [TruthfulQA, Rand C%] | 0.37 | plan_028 | 0.37 | ✅ |\n| [TruthfulQA, Ratio] | 80× | 29.7/0.37=80.3 | — | ✅ |\n| [ARC, Items] | 1,172 | plan_028 | 1172 | ✅ |\n| [ARC, C%] | 26.9 | plan_028 | 26.88% | ✅ |\n| [ARC, ρ] | 0.9962 | benchmark_rho_summary.csv | 0.996209 | ✅ |\n| [ARC, τ] | 0.9538 | benchmark_rho_summary.csv | 0.953791 | ✅ |\n| [ARC, Flip%] | 2.31 | benchmark_rho_summary.csv | 0.023104 → 2.31% | ✅ |\n| [ARC, Rand C%] | 0.60 | plan_028 | 0.6 | ✅ |\n| [ARC, Ratio] | 45× | 26.9/0.60=44.8 | — | ✅ |\n| [GSM8K, Items] | 1,319 | plan_028 | 1319 | ✅ |\n| [GSM8K, C%] | 18.9 | plan_028 | 18.88% | ✅ |\n| [GSM8K, ρ] | 0.9993 | benchmark_rho_summary.csv | 0.999303 | ✅ |\n| [GSM8K, τ] | 0.9843 | benchmark_rho_summary.csv | 0.984311 | ✅ |\n| [GSM8K, Flip%] | 0.78 | benchmark_rho_summary.csv | 0.007844 → 0.78% | ✅ |\n| [GSM8K, Rand C%] | 0.30 | plan_028 | 0.3 | ✅ |\n| [GSM8K, Ratio] | 63× | 18.9/0.30=63.0 | — | ✅ |\n| [HellaSwag, Items] | 10,042 | plan_028 | 10042 | ✅ |\n| [HellaSwag, C%] | 17.9 | plan_028 | 17.89% | ✅ |\n| [HellaSwag, ρ] | 0.9986 | benchmark_rho_summary.csv | 0.998623 | ✅ |\n| [HellaSwag, τ] | 0.9722 | benchmark_rho_summary.csv | 0.972166 | ✅ |\n| [HellaSwag, Flip%] | 1.39 | benchmark_rho_summary.csv | 0.013917 → 1.39% | ✅ |\n| [HellaSwag, Rand C%] | 0.28 | plan_028 | 0.28 | ✅ |\n| [HellaSwag, Ratio] | 64× | 17.9/0.28=63.9 | — | ✅ |\n\n**Table 3: 全部 42 cells 核查通过。**\n\n---\n\n## Experiments 正文数字\n\n### §5.1 Validation\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| ā=1.2 | PSN-IRT mean discrimination | sf8_power_sensitivity/sf8_report.md | a mean=1.197 | ✅ |\n| b̄=−0.84 | PSN-IRT mean difficulty | sf8_report.md | b mean=−0.838 | ✅ |\n| N≥80 per cohort | power threshold | dif_phase2_results.csv | N=80 rows present | ✅ |\n| TPR 0.68–0.80 | ETS C under uniform injection | dif_phase2_results.csv | N=80,δ=1.4: 0.6823; N=100,δ=1.6: 0.7966 | ✅ |\n| AUC 0.93–0.94 | for \\|Δ_MH\\|≥1.4 | dif_phase2_results.csv | N=80: AUC=0.895; N=100: AUC=0.923–0.925 | ⚠️ |\n| N_ref=1,080 | temporal cohort | plan_001/dif_summary.csv | 1080 | ✅ |\n| N_focal=807 | temporal cohort | plan_001/dif_summary.csv | 807 | ✅ |\n| TPR 0.40–0.95 | across a=0.5–2.0 | sf8_report.md | 0.398–0.949 | ✅ |\n\n### §5.2 Temporal DIF\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| 31.3% | C items | plan_001/dif_summary.csv | 31.324% | ✅ |\n| \\|Δ_MH\\|≥1.5 | ETS C threshold | plan_001 | criterion confirmed | ✅ |\n| CI [29.4%, 38.1%] | bootstrap 95% CI | sf1_cluster_bootstrap/bootstrap_results.csv | 计算值: [29.23%, 37.79%] | ❌ |\n| CI [26.7%, 53.2%] | family-level cluster bootstrap | sf1_cluster_bootstrap/cluster_bootstrap_ci.md | [26.73%, 53.17%] | ✅ |\n| DEFF simple-mean → 29.2% | DEFF upper | mf2_deff_estimation/deff_summary.md | 29.2% | ✅ |\n| DEFF weighted-mean → 13.5% | DEFF lower | mf2_deff_estimation/deff_summary.md | 13.5% | ✅ |\n| ρ=0.999 | under weighted-mean DEFF | _project/data/weighted_mean_downstream.md | 0.998811 | ✅ |\n| +1.77pp | score shift under weighted-mean | _project/data/weighted_mean_downstream.md | +1.772pp | ✅ |\n| P99 \\|Δ_MH\\|=1.45 | permutation null | _project/data/random_split_report.md | 1.4504 | ✅ |\n| 0.62% | random split 2023 | _project/data/random_split_report.md | 0.6247% | ✅ |\n| 1.3% | random split 2024 | r15_random_split_control | 1.335% | ✅ |\n| ≥24× | below temporal C% | 31.3/1.3=24.1 | — | ✅ |\n| 2.9% | ability quintile C% | plan_001/dif_summary.csv | 2.9021% | ✅ |\n| N=638/group | NN matching | temporal_overlap_report.md | 638 | ✅ |\n| Cohen's d=−0.17 | matching context | temporal_overlap_report.md | −0.17 (pre-match gap) | ⚠️ |\n| C%=28.9%±0.1% | matched C% | temporal_overlap_report.md | 28.9%±0.1% | ✅ |\n| ~2.4pp | ability mismatch | 31.3−28.9=2.4 | — | ✅ |\n| p<0.01 | matching significance | temporal_overlap_report.md | confirmed | ✅ |\n| LOFO \\|ΔC%\\|≤2.93pp | max LOFO | lofo_robustness/lofo_results.csv | 2.93pp (mixtral) | ✅ |\n| 20.7%–48.4% | subject C% range | plan_033_report.md | confirmed | ✅ |\n| mean≈30% | subject mean C% | plan_033_report.md | 30.6% | ✅ |\n| KW p=0.78 | domain invariance | plan_033_report.md | 0.7797 | ✅ |\n| STEM 55.4% | favor 2024 | plan_033_report.md | 55.4% | ✅ |\n| Humanities 64.4% | favor 2023 | plan_033_report.md | 100−35.58=64.42% | ✅ |\n| <0.1% variance | domain accuracy → DIF | interaction_report.md | R²<0.001 | ✅ |\n| ρ=−0.597 | difficulty–direction | interaction_report.md | −0.597 | ✅ |\n| 18.3% at \\|Δ_MH\\|≥2.0 | threshold sensitivity | plan_001/dif_results_temporal.csv | 2297/12508=18.37% → 18.4% | ⚠️ |\n| 10.2% at \\|Δ_MH\\|≥2.5 | threshold sensitivity | plan_001/dif_results_temporal.csv | 1278/12508=10.22% | ✅ |\n\n### §5.3 Comparison with Web-Overlap Labels\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| 9,229 | annotated items | plan_001/plan_001_report.md | 9229 | ✅ |\n| enrichment=0.964 | DIF vs web-overlap | plan_001/dif_summary.csv | 0.96415 | ✅ |\n| Jaccard=0.206 | DIF–web overlap | r17_jaccard_permutation | 0.2063 | ✅ |\n| p=0.88 | Fisher exact | computed | 0.8806 | ✅ |\n| 30.7% | DIF-C among web-contam | plan_001_report.md | 0.3070 | ✅ |\n| 31.8% | DIF-C among clean | plan_001_report.md | 0.3184 | ✅ |\n| χ²=562.7 | base/instruct reversal | r18_base_vs_instruct_dif | 562.70 | ✅ |\n| ΔTPR=+0.508 | semi-synthetic p=0.5 | plan_011_report.md | +0.508 | ✅ |\n\n### §5.4 Structural Analysis\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| 17.7% | non-uniform DIF | r16_dif_union | 317/1787=17.74% | ✅ |\n| union 47% | total flagged | r16_dif_union | 47.0% | ✅ |\n| ~28–29% | ability-matched convergence | temporal_overlap_report.md | 28.9% | ✅ |\n| r(θ,total)=0.9986 | IRT conditioning | plan_012_report.md | 0.9986 | ✅ |\n\n### §5.5 Detection Power (Semi-synthetic Injection)\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| ΔFPR=0.000 | cross-subject, 5 subjects | plan_011_report.md | 0.000 | ✅ |\n| 4/5 with ΔTPR>0.3 | at p=0.5 | plan_011_report.md | confirmed | ✅ |\n| +0.186 avg | within-subject FPR inflation | plan_011_report.md | +0.186 | ✅ |\n| k≤5: ΔFPR<0.007 | single-subject contamination | summary_by_k_full.csv | k=5: 0.0065 | ✅ |\n| k=10: ΔFPR=0.069 | 18% of domains | summary_by_k_full.csv | 0.069 | ✅ |\n| k=20: ΔFPR=0.167 | multi-subject | summary_by_k_full.csv | 0.1673 | ✅ |\n| k≥30: ΔFPR>0.36 | >50% domains | summary_by_k_full.csv | k=30: 0.3618 | ✅ |\n| ΔTPR≈0.41 | difficulty-dependent | mixed_mechanism_report.md | ~0.41 | ✅ |\n| 0.51 | uniform reference | plan_011_report.md | ~0.508 | ✅ |\n| ~20% | overestimation bound | (0.51−0.41)/0.51=19.6% | — | ✅ |\n\n### §5.6 Downstream Impact\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| ρ=0.997 | across 6 benchmarks | benchmark_rho_summary.csv | mean=0.9970 | ✅ |\n| τ=0.958 | across 6 benchmarks | benchmark_rho_summary.csv | mean=0.9620; 无单值=0.958 | ❌ |\n| flip rate ≤2.8% | max flip | benchmark_rho_summary.csv | WinoGrande=2.84% > 2.8% | ❌ |\n| z=−8 to −49 | vs random removal | plan_017_report.md | −8.16 to −49.44 | ✅ |\n| 33.6% | pairwise reversals (top 200) | mf1_worked_examples/mf1_report.md | 6694/19900=33.6% | ✅ |\n| 96.2 positions | cohort gap | plan_032/dif_vs_random_comparison.csv | 96.16 | ✅ |\n| 40× random | cohort gap ratio | 96.16/2.36=40.7 | — | ✅ |\n| p<0.001 | cohort gap significance | plan_032_report | confirmed | ✅ |\n| +2.12pp | avg accuracy shift | score_inflation_report.md | +2.116pp | ✅ |\n| 0.29pp | cohort-differential | score_inflation_report.md | 2.351−2.060=0.291pp | ✅ |\n| d=0.31 | Cohen's d | score_inflation_report.md | \\|d\\|=0.3051 | ✅ |\n| ±800 | individual displacements | score_inflation_report.md | max down=−849; report P99=±561 | ⚠️ |\n\n### §5.7 Cross-Benchmark Validation\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| 17.9%–31.3% | C% range | plan_028/multi_bench_summary.csv | confirmed | ✅ |\n| 26.9–31.3% | knowledge/reasoning | multi_bench_summary.csv | ARC=26.9, others higher | ✅ |\n| 17.9–18.9% | procedural | multi_bench_summary.csv | HellaSwag=17.9, GSM8K=18.9 | ✅ |\n| 45–95× | above random | Table 3 Ratio column | confirmed | ✅ |\n| ΔTPR=+0.514 | GSM8K semi-synthetic | gsm8k_dose_response_summary.csv | +0.514 | ✅ |\n\n---\n\n## Discussion 正文数字\n\n### §6.1 Temporal DIF as Structured Signal\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| N=1,409 | base models | r18_base_vs_instruct_dif | Ref=861+Foc=548=1409 | ✅ |\n| 60.1% | ref-favoring (base) | r18_base_vs_instruct_dif | 2413 (60.1%) | ✅ |\n| ρ=−0.570 | base difficulty–direction | r18_base_vs_instruct_dif | −0.570 | ✅ |\n| N=478 | instruct models | r18_base_vs_instruct_dif | Ref=219+Foc=259=478 | ✅ |\n| 65.6% | focal-favoring (instruct) | r18_base_vs_instruct_dif | 2994 (65.6%) | ✅ |\n| ρ=−0.079 | instruct difficulty–direction | r18_base_vs_instruct_dif | −0.079 | ✅ |\n| χ²=562.7 | direction reversal | r18_base_vs_instruct_dif | 562.70 | ✅ |\n| p<10^−124 | significance | r18_base_vs_instruct_dif | 2.178e-124 | ✅ |\n| Δ=1.08pp | composition downsampling | r22_composition_control | 1.08pp | ✅ |\n| C%=29.2% | DEFF-adjusted headline | r20_size_stratified_deff | simple-mean DEFF→29.2% | ⚠️ |\n| CI [26.7%, 53.2%] | cluster bootstrap | sf1_cluster_bootstrap | [26.73%, 53.17%] | ✅ |\n| Jaccard=0.206 | DIF–web overlap | r17_jaccard_permutation | 0.2063 | ✅ |\n| OR=4.75 | base/instruct interaction | interaction_report.md | 4.754 | ✅ |\n\n### §6.2 Recommended DIF Audit Protocol\n\n| 数字 | 上下文 | 源文件 | 源值 | 状态 |\n|------|--------|--------|------|------|\n| AUROC=0.60 | predictive model | predictive_model/phase2_results.md | LR=0.6026, GBM=0.5994 | ✅ |\n| ≥500 models | threshold | 无单一源文件 | 来自 rebuttal 实践建议 | ⚠️ |\n| K=3 | smaller corpora | k3_power_simulation/k3_power_report.md | K=3≈K=5 confirmed | ✅ |\n| C%≈12% | 20× baseline for MMLU | 20×0.62%=12.4% | 算术一致 | ✅ |\n\n---\n\n## ⚠️ 不一致 / ❌ 无法追溯\n\n### ❌ 需要修正（3项）\n\n1. **Table 1, Ability quintile N: `~2,600 / ~2,600` → 实际 `~2,090 / ~2,090`**\n   - 源: plan_001_report.md: \"ref = Q1-2 (N=2092), foc = Q4-5 (N=2089)\"\n   - 偏差: 论文多报约500/组\n   - 建议: 改为 `${\\sim}$2,090 / ${\\sim}$2,090`\n\n2. **§5.6 Downstream: τ=0.958 无法追溯**\n   - 源: benchmark_rho_summary.csv 六个 benchmark 的 Kendall τ 值: 0.9432, 0.9538, 0.9586, 0.9600, 0.9722, 0.9843\n   - 均值 = 0.9620, 中位数 = 0.9593, 最小值 = 0.9432 — 无论哪种解释都不等于 0.958\n   - 建议: 改为 `τ = 0.962`（均值）或 `τ \\geq 0.943`（最小值）\n\n3. **§5.6 Downstream: flip rate ≤ 2.8% 不成立**\n   - 源: benchmark_rho_summary.csv WinoGrande flip_rate=0.028417 = **2.84%** > 2.8%\n   - 建议: 改为 `flip rate $\\leq$ 2.9\\%`\n\n### ❌ 需要修正但较小（1项）\n\n4. **§5.2 bootstrap CI [29.4%, 38.1%] 与计算值不符**\n   - 源: sf1_cluster_bootstrap/bootstrap_results.csv 1000次 model-level bootstrap\n   - 计算 2.5th/97.5th percentile: **[29.23%, 37.79%]**\n   - 论文写 [29.4%, 38.1%]，偏差 0.17pp (lower) 和 0.31pp (upper)\n   - 建议: 改为 `[29.2\\%, 37.8\\%]`\n\n### ⚠️ 可接受但需注意（6项）\n\n5. **§5.1 AUC 0.93–0.94 \"at N≥80\"**: N=80 时 AUC=0.895–0.894; 0.93–0.94 仅在 N=100 时成立。论文措辞 \"at N≥80\" 暗示 N=80 即可达到，实际需 N≈100。建议: 改措辞为 \"at N=100\" 或注明 \"0.89–0.94 across N=80–200\"。\n\n6. **§5.2 18.3% at |Δ_MH|≥2.0**: 精确值 2297/12508=18.37%→四舍五入应为 18.4% 而非 18.3%。差异极小，可保留或改为 18.4%。\n\n7. **§5.2 Cohen's d=−0.17**: 值本身正确（temporal_overlap_report.md），但这是 pre-matching 能力差距，不是 post-matching 残差（post-match d=−0.010）。论文上下文可能让读者误以为匹配后仍有 d=0.17 的差距。\n\n8. **§5.6 individual displacements ±800**: score_inflation 中最大负位移 −849（Sao10K），但 P99=±561。report 说 \"exceeding ±561 positions (99th percentile)\"。±800 作为极值描述基本准确（max down=−849），但对称的 \"±\" 表述有误导性（正向最大值需要确认是否也接近 800）。\n\n9. **Table 1, Within-family N_focal=308**: metabench_data_summary.md 记录 308（分析时数据），当前 model_metadata.csv 为 315-316。C% 不受影响。轻微数据版本差异。\n\n10. **Table 2, Matched-ability C%=~0.31**: 最严格的 1:1 NN 匹配得 28.9%，composition-balanced 得 30.25%，CMH quintile 得 33.3%。`~0.31` 依赖于对 \"matched\" 的定义。波浪号（~）做了较多工作。\n\n11. **§6.1 C%=29.2%**: 值来自 DEFF simple-mean 校正结果。§5.2 报告原始 C%=31.3%。Discussion 中使用 29.2% 未注明是 DEFF 校正值，可能让读者困惑。\n\n---\n\n## 统计\n\n- **Tables**: 62 cells checked (Table 1: 15, Table 2: 8, Table 3: 42 — 含 Ratio 推导)\n  - ✅ 57 | ⚠️ 3 | ❌ 2 (Ability quintile N; Within-family N_focal 轻微)\n- **Experiments 正文**: ~55 个数字\n  - ✅ 46 | ⚠️ 6 | ❌ 3 (bootstrap CI, τ, flip rate)\n- **Discussion 正文**: ~17 个数字\n  - ✅ 14 | ⚠️ 3\n\n**需立即修正**: 4 项 (Ability quintile N, bootstrap CI, τ=0.958, flip rate ≤2.8%)\n**建议修正**: 2 项 (AUC at N≥80 措辞, 18.3%→18.4%)\n**建议注意**: 5 项 (Cohen's d 语境, ±800 对称性, Within-family N, Matched C% ~0.31, Discussion C% 29.2% 来源)\n"
  }
}
```

</details>

---


### Tool result

_source line 672 · 2026-05-23T19:54:33.898623+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/data_audit_part2.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 673 · 2026-05-23T19:54:33.898831+00:00_

报告已写入 `artifacts/data_audit_part2.md`。

核查覆盖了 3 个 Table（62 cells）+ experiments.tex（~55 个数字）+ discussion.tex（~17 个数字）。

**需立即修正的 4 项**：

1. **Table 1 Ability quintile N**: 论文写 `~2,600/~2,600`，实际 `2,092/2,089` — 多报约 500/组
2. **§5.2 bootstrap CI [29.4%, 38.1%]**: 从 bootstrap_results.csv 计算为 `[29.2%, 37.8%]`
3. **§5.6 τ=0.958**: 六个 benchmark 的均值 τ=0.962、中位数 0.959、最小值 0.943 — 无解释可得 0.958
4. **§5.6 flip rate ≤2.8%**: WinoGrande=2.84%，超过 2.8%

其余 ⚠️ 项为措辞/四舍五入/上下文问题（AUC at N≥80 措辞、18.3%→18.4% 四舍五入、±800 对称性等），不影响结论但值得注意。

k=10/20/30 ΔFPR 值（summary_by_k_full.csv）、Table 3 全部 42 cells、base/instruct 分层数据均与源文件完全匹配。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629"
}
```

</details>

---
