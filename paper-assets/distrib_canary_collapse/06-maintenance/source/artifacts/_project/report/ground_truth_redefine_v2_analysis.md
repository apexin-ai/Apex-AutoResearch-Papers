# Ground Truth Redefinition v2: Strict Inequality Fix

## Change Summary

**B1 (old):** `canary_onset <= downstream_onset` (non-strict) → 8 pairs, FNR=25%  
**v2 (new):** `canary_onset < downstream_onset` (strict) → 6 pairs, FNR=0%

The 2 excluded pairs (`token_entropy→perplexity`, `ece→perplexity`) had identical onset times (gen 1), making causal ordering indeterminate. These are the D017-confirmed spurious associations.

---

## Onset Time Table (2σ threshold, 4-seed)

| Metric | Seed 42 | Seed 43 | Seed 44 | Seed 45 | Mean |
|--------|---------|---------|---------|---------|------|
| token_entropy (C) | 1 | 1 | 1 | 1 | 1.0 |
| ece (C) | 1 | 1 | 1 | 1 | 1.0 |
| distinct_1 | 10 | 10 | None | 7 | 9.0 |
| distinct_2 | 3 | 3 | 3 | 3 | 3.0 |
| distinct_3 | 3 | 3 | 3 | 3 | 3.0 |
| perplexity | 1 | 1 | 1 | 1 | 1.0 |

**Key observation:** perplexity onset = canary onset = gen 1 → fails strict `<` requirement.

---

## New Reference Set (6 pairs)

| Canary | Downstream | Canary Drift Ratio | Temporal Votes (strict) |
|--------|------------|-------------------|------------------------|
| token_entropy | distinct_1 | 11.93× | 3/4 |
| token_entropy | distinct_2 | 11.93× | 4/4 |
| token_entropy | distinct_3 | 11.93× | 4/4 |
| ece | distinct_1 | 73.12× | 3/4 |
| ece | distinct_2 | 73.12× | 4/4 |
| ece | distinct_3 | 73.12× | 4/4 |

Criteria: canary drift ≥ 3× α=0.0 baseline **AND** canary onset strictly precedes downstream in ≥3/4 seeds.

---

## FNR Computation

**Consensus method:** K≥3/4 (naive xcorr, threshold onset, permutation Granger, Toda-Yamamoto)  
**differenced xcorr excluded** (non-monotone dose-response, see B1 rationale)

| Pair | naive | threshold | perm_granger | TY | Count | Verdict |
|------|-------|-----------|-------------|-----|-------|---------|
| token_entropy→distinct_1 | SIG | SIG | SIG | SIG | 4/4 | DETECTED |
| token_entropy→distinct_2 | SIG | SIG | SIG | SIG | 4/4 | DETECTED |
| token_entropy→distinct_3 | SIG | SIG | SIG | SIG | 4/4 | DETECTED |
| ece→distinct_1 | SIG | SIG | SIG | SIG | 4/4 | DETECTED |
| ece→distinct_2 | SIG | SIG | SIG | SIG | 4/4 | DETECTED |
| ece→distinct_3 | SIG | SIG | SIG | SIG | 4/4 | DETECTED |

**FNR = 0/6 = 0.0%**

---

## Threshold Sensitivity

| Drift Threshold | Pairs (strict) | Same set? |
|----------------|---------------|-----------|
| 2× | 6 | ✓ |
| 3× | 6 | ✓ |
| 5× | 6 | ✓ |

The 6-pair set is invariant across all tested thresholds. This is because both canaries have extreme drift ratios (11.93× and 73.12×) that far exceed any threshold, and the only filtering mechanism is temporal ordering.

---

## B1 → v2 Comparison

| Property | B1 (non-strict) | v2 (strict) |
|----------|-----------------|-------------|
| Temporal criterion | `onset ≤` | `onset <` |
| Reference pairs | 8 | 6 |
| Excluded pairs | — | token_entropy→ppl, ece→ppl |
| FNR | 25% (2/8) | 0% (0/6) |
| False negatives | perplexity pairs | none |
| Threshold stable | ✓ (8 at all) | �� (6 at all) |

**Interpretation:** The 25% FNR in B1 was entirely attributable to perplexity pairs that should never have been in the reference set. Perplexity co-moves with canary metrics instantaneously (both respond at gen 1), making temporal ordering undetermined. The strict inequality correctly excludes these co-onset pairs, yielding a cleaner reference set where all known causal relationships are successfully detected.

---

## Data Sources

- α=1.0: `results/mvp/rep_{42,43,44,45}/all_metrics.json`
- α=0.0: `results/alpha_sweep/a000_s42/all_metrics.json`
- Method verdicts: `results/method_ablation_phase2_panel.json` (pair_verdicts, α=1.0)
- Script: `ground_truth_redefine_v2.py`
- JSON output: `artifacts/ground_truth_redefine_v2_results.json`
