# Provenance Audit: c032 / c023 / c021

**Date**: 2026-05-16
**Auditor**: automated provenance trace
**Scope**: Three claims in paper_provenance.yaml where registered values diverge from paper text

---

## c032: logprob conditional RE ρ

- **Provenance yaml claim**: paper says ρ=0.002
- **Registry value**: exp_015_metrics_expansion → re.logprob_rho_cond = 0.1457
- **Current paper text**: ρ=0.011 (experiments.tex:50, appendix.tex:137)

### Source trace

The **current paper** says ρ=0.011 in two places:
1. `experiments.tex:50` — "LP †RE collapses to ρ=0.011"
2. `appendix.tex:137` — heatmap caption: "LP RE collapses to near-zero (ρ=0.011)"

The value **0.01119** is in:
- `output/exp_012_rerun_1024/report.json:100` — `re_logprob_baseline.conditional.rho = 0.011185364740047766`
- `output/exp_012_rerun_1024/all_signals_5signal.json:403` — same value
- Conditions: SciERC RE, N=8, T=1.0, max_tokens=1024, **correct conditional filter** (greedy_f1 > 0, n=238)

### Why the discrepancy

| Value | Source | Filter | n_cond | Status |
|-------|--------|--------|--------|--------|
| 0.002 | provenance yaml claim | unknown | — | **STALE** — paper was updated to 0.011; 0.002 untraceable in any output file |
| 0.1457 | exp_015_metrics_expansion | WRONG: any sample F1 > 0 | 331 | Wrong filter inflates n, changes correlation |
| **0.011** | exp_012_rerun_1024 | CORRECT: greedy_f1 > 0 | 238 | Current paper value |

The `conditional_filter_diagnosis.json` documents that exp_015 (and several other scripts) used the wrong conditional filter ("any sample F1 > 0" instead of "greedy_f1 > 0"), inflating the conditional set from n=238 to n=331 for RE. This is the root cause of the registry's 0.1457.

### Conclusion

**Provenance yaml is stale.** The paper was already corrected from 0.002 to 0.011. The current paper value (0.011 from exp_012_rerun_1024, correct conditional filter) is correct. The registry value (0.1457) uses a known-wrong conditional filter and should be annotated as deprecated.

---

## c023: RE SJ ρ by sentence length (Q1/Q4)

- **Paper values**: Q1=0.110, Q4=0.473, Fisher z p=0.004
- **Registry values**: exp_009_capability_stratification → Q1=0.447, Q4=0.540

### Source trace

Paper values match **exp_009_v2_re_rerun** exactly:

From `output/exp_009_v2_re_rerun/summary.txt`:
```
Stratification by Sentence Length QUARTILES (primary, independent)
  Q1 (low)   n=117  SJ 0.110[-0.08,0.29]
  Q2         n=93   SJ 0.308[0.09,0.50]
  Q3         n=92   SJ 0.372[0.18,0.54]
  Q4 (high)  n=95   SJ 0.473[0.28,0.62]

Fisher z-test low_vs_high:
  sj   z=-2.878  p=0.004*
```

All three paper values (Q1=0.110, Q4=0.473, p=0.004) match the v2 rerun output character-for-character.

From `output/exp_009_v2_re_rerun/results.json`:
- `by_sent_len_quartiles."Q1 (low)".signals.sj.rho = 0.10961735` → rounds to 0.110
- `by_sent_len_quartiles."Q4 (high)".signals.sj.rho = 0.47332...` → rounds to 0.473
- Fisher z low_vs_high sj p = 0.00435... → rounds to 0.004

### Why the registry differs

The registry values (Q1=0.447, Q4=0.540) come from the **original exp_009_capability_stratification**, which:
1. Did NOT apply gold-empty filtering (included 154 instances with empty gold RE annotations)
2. Used all 551 raw instances instead of the filtered 397

The v2 rerun applied proper gold-filtering (551 → 397 after removing gold-empty), which is the mandated pipeline for all ρ values in the paper.

| Value set | Source | Gold filter | n_RE | Status |
|-----------|--------|-------------|------|--------|
| Q1=0.447, Q4=0.540 | exp_009 original | No | 551 | **Outdated** — pre-gold-filter |
| **Q1=0.110, Q4=0.473** | exp_009_v2_re_rerun | Yes | 397 | Current paper value |

### Conclusion

**Paper values are correct.** They come from exp_009_v2_re_rerun with proper gold-filtering. The registry entry for exp_009_capability_stratification is outdated and should be annotated as superseded by exp_009_v2_re_rerun.

---

## c021: WNUT SJ ρ

- **Provenance yaml claim**: paper says ρ=0.062 (p=0.106)
- **Registry values**: exp_003_ner_wnut17 → 0.082; exp_003_wnut17_eval → 0.089

### Source trace — current paper

The **current paper** (appendix.tex:222, Table tab:wnut) shows:
```
SJ  .089  .020  .517  .288  <1e-7
```
i.e., SJ full-set ρ = **0.089**, p = 0.020

This matches `output/exp003_wnut17_eval/report.json`:
- `correlation_softjaccard_vs_f1_full.rho = 0.08883161` → rounds to 0.089
- `correlation_softjaccard_vs_f1_full.p_value = 0.01970` → rounds to 0.020
- n = 689 (after gold-empty filtering)

### Tracing the 0.062

The value ρ=0.062 appears ONLY in the **old deprecated paper** at:
- `artifacts/_project/paper/experiments.tex:181` — "SJ achieves ρ=0.062 (p=0.106, not statistically significant)"

This file is in `artifacts/_project/paper/` which is excluded from compilation per constraint C001. The current compiled paper at `docs/paper/sections/` does NOT contain 0.062 for WNUT.

Searching all output files for 0.062 in WNUT context yields **no matches**. The closest values found are:
- exp003_wnut17_pilot: SJ full rho = 0.0825 (different seed)
- exp003_wnut17_eval: SJ full rho = 0.0888
- exp_009_v2 global SJ rho (SciERC RE, not WNUT): 0.0625

The value 0.062 for WNUT SJ is **untraceable** — it does not appear in any analysis output file. It may have originated from:
1. An earlier experiment run that was overwritten
2. A different seed/N configuration
3. A manual transcription error in the old draft

### Conclusion

**Provenance yaml is stale.** The current paper correctly uses ρ=0.089 from exp003_wnut17_eval (N=16, T=1.0, gold-filtered n=689). The 0.062 value from the old paper draft is untraceable and no longer appears in the compiled paper.

---

## Summary

| Claim | Provenance yaml | Current paper | Ground truth source | Status |
|-------|----------------|---------------|-------------------|--------|
| c032 LP cond RE ρ | 0.002 | **0.011** | exp_012_rerun_1024 (correct filter, n=238) | Provenance stale; paper correct |
| c023 RE SJ Q1/Q4 | Q1=0.447/Q4=0.540 (registry) | **Q1=0.110/Q4=0.473** | exp_009_v2_re_rerun (gold-filtered) | Registry outdated; paper correct |
| c021 WNUT SJ ρ | 0.062 | **0.089** | exp003_wnut17_eval (n=689) | Provenance stale; paper correct |

**All three paper values are correct in the current compiled paper.** The discrepancies exist only between the provenance yaml / registry entries and the paper — not between the paper and the ground truth data. The provenance yaml and registry entries need updating.
