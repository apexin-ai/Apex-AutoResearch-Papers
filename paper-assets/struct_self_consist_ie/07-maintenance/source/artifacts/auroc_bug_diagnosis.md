# AUROC Binarization Bug Diagnosis Report

**Date**: 2026-05-14
**Affected experiment**: exp-012 (logprob baseline), exp-003 (WNUT-17 eval)
**Severity**: P1 — invalidated logprob baseline AUROC on WNUT-17 conditional set

## Bug Root Cause

`compute_auroc()` in `evaluation.py` binarizes continuous F1 labels at the median using strict `>`:

```python
pos = [s for s, l in zip(scores, labels_continuous) if l > med]   # BUG
neg = [s for s, l in zip(scores, labels_continuous) if l <= med]
```

On WNUT-17 NER conditional set (n=334, all F1 > 0):
- **67.1% of instances have F1 = 1.0** (224/334)
- Median F1 = 1.0
- `f > 1.0` matches **zero** instances → pos set is **empty**
- Function returns 0.5 (degenerate fallback)

The same bug existed in `analyze_logprob_baseline.py`, `analyze_exact_match_voting.py`, and `analyze_entity_voting.py` which used `1 if f > median else 0` for label creation.

## Fix Applied

Added a fallback: when `> median` produces an empty positive class, retry with `>= median` vs `< median`.

**Files modified** (on server `/root/autodl-tmp/struct_self_consist_ie/code/`):
1. `evaluation.py` — `compute_auroc()` function
2. `analyze_logprob_baseline.py` — median-split label creation
3. `analyze_exact_match_voting.py` — median-split label creation
4. `analyze_entity_voting.py` — median-split label creation

After fix, WNUT-17 conditional split becomes:
- pos (F1 >= 1.0): 224 instances
- neg (F1 < 1.0): 110 instances

## AUROC Before/After Comparison

### WNUT-17 NER (n_full=689, n_cond=334)

| Signal | Set | OLD AUROC | NEW AUROC | Changed? |
|--------|-----|-----------|-----------|----------|
| logprob | full | 0.2189 | 0.2189 | No |
| **logprob** | **conditional** | **0.5000** | **0.7092** | **YES (bug)** |
| soft_jaccard | full | 0.5170 | 0.5170 | No |
| soft_jaccard | conditional | 0.6535 | 0.6535 | No |
| fleiss_kappa | full | 0.5551 | 0.5551 | No |
| fleiss_kappa | conditional | 0.5849 | 0.5849 | No |

### SciERC NER (n_cond=451) and RE (n_cond=218)

| Subtask | Signal | Set | OLD AUROC | NEW AUROC | Changed? |
|---------|--------|-----|-----------|-----------|----------|
| NER | logprob | full | 0.5907 | 0.5907 | No |
| NER | logprob | cond | 0.5986 | 0.5986 | No |
| NER | soft_jaccard | cond | 0.6772 | 0.6772 | No |
| RE | logprob | full | 0.6186 | 0.6186 | No |
| RE | logprob | cond | 0.5468 | 0.5468 | No |
| RE | soft_jaccard | cond | 0.6452 | 0.6452 | No |

**SciERC is NOT affected** — its F1 distributions are more spread out and median never coincides with extreme values.

## Impact on Conclusions

The fix reveals that on WNUT-17 conditional set:
- **Logprob AUROC (0.7092) > SJ AUROC (0.6535) > FK AUROC (0.5849)**
- Logprob is actually the strongest discriminator in the conditional set, not a random baseline

Combined with the already-known rho values:
- Logprob conditional rho = +0.3501 (p < 1e-10)
- SJ conditional rho = +0.2884 (p < 1e-7)

**Logprob baseline is stronger than structural consistency on WNUT-17 in both rho and AUROC for the conditional set.** This means the SJ vs logprob comparison conclusion needs updating — on WNUT-17 specifically, logprob is a competitive or better baseline.

## Experiments with AUROC Numbers Needing Update

1. **exp-003 WNUT-17 eval** (`output/exp003_wnut17_eval/report.json`): `logprob_baseline.conditional.auroc` should be 0.7092 (was 0.5000)
2. Any downstream reports or tables citing WNUT-17 conditional logprob AUROC = 0.5
