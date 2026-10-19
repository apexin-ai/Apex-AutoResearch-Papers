# Pareto Dominance Analysis — Verification Report

**Date**: 2026-05-21
**Script**: `code/pareto_analysis.py`
**Data**: Qwen2.5-7B MVP (westd-13176), zero_shot method

## Verification Summary

Script ran successfully on MVP data. All 3 output files produced: `pareto_detail.csv`, `pareto_summary.csv`, `pareto_results.json`.

## Results (Qwen2.5-7B, 8 layers x 5 languages)

| Language | Pareto Layers | HV | Spearman rho | p-value | Tradeoff? |
|----------|---------------|------|------------|---------|-----------|
| zh | [24, 27] | 0.0456 | +0.857 | 0.0065 | Local only |
| ar | [24, 27] | 0.0370 | +0.857 | 0.0065 | Local only |
| hi | [20, 27] | 0.0369 | +0.310 | 0.4556 | Local only |
| ko | [24, 27] | 0.0360 | +0.714 | 0.0465 | Local only |
| sw | [27] | 0.0148 | +0.762 | 0.0280 | None |

## Key Findings

### L27 is universally Pareto-optimal
L27 (EN AUROC = 0.746, best) appears on every language's Pareto front, confirming it as the best EN probe layer.

### Tradeoff is local, not global
Spearman rho is **positive** for all languages (EN and ZS AUROC generally co-increase with depth). The tradeoff manifests only at the top of the frontier:

- **zh**: L24 (ZS=0.686) > L27 (ZS=0.661), but L27 EN > L24 EN -- both Pareto-optimal
- **ar**: L24 (ZS=0.651) > L27 (ZS=0.635), same pattern
- **hi**: L20 (ZS=0.652) > L27 (ZS=0.626), deeper tradeoff -- middle layer wins transfer
- **ko**: L24 (ZS=0.648) > L27 (ZS=0.607), similar to zh/ar
- **sw**: L27 dominates all layers on both objectives -- no tradeoff

### Interpretation for C4 response
The Pareto analysis reveals a **nuanced** tradeoff:
1. The global correlation is positive -- deeper layers are generally better for both EN and transfer.
2. But the **frontier** shows a local tradeoff at L24-L27: the best EN layer (L27) is NOT the best transfer layer for 4/5 languages.
3. Hypervolume is largest for zh (0.046) and smallest for sw (0.015), suggesting the tradeoff is language-dependent and correlates with typological distance.

### Validation checks
- L27 on Pareto front for all languages (expected: best EN)
- L24 or L20 as second Pareto point where tradeoff exists (expected: best transfer)
- sw has no tradeoff -- L27 dominates (consistent with sw being lowest-resource, weakest transfer overall)
- Hypervolume ordering (zh > ar > hi > ko > sw) roughly tracks overall transfer quality

## Output Files
- `results/pareto/pareto_detail.csv` -- 40 rows (8 layers x 5 langs), with is_pareto_optimal and pareto_rank
- `results/pareto/pareto_summary.csv` -- 5 rows, per-language hypervolume + Spearman
- `results/pareto/pareto_results.json` -- combined structured output
