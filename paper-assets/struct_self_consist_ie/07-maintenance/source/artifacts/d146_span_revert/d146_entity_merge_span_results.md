# D146: Span-Based Entity Merge Results

## Modification Summary

**File changed:** `code/evaluation.py` — `entity_strict_match` function

**Before (text-based):**
```python
pred_set = {(e["text"], e["type"]) for e in pred_entities}
gold_set = {(e["text"], e["type"]) for e in gold_entities}
```

**After (span-based):**
```python
pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
```

**Downstream impact:**
- `analysis_d141_entity_merge.py` imports `entity_strict_match` — automatically span-based after revert
- `analysis_d141_conditional_decomp.py` imports `entity_strict_match` — automatically span-based after revert
- Conditional decomp not re-run (already had span-based results: SciERC +2.52pp, CoNLL -1.88pp, FewNERD +0.69pp)

---

## Span-Based Entity Merge Results (Full)

| Dataset | Greedy | LP_Sel | Oracle_Sel | Majority_Merge | LP_Weighted | Best_Thresh | Best_k |
|---------|--------|--------|------------|----------------|-------------|-------------|--------|
| SciERC | 0.6439 | 0.6501 | 0.7758 | 0.6515 | 0.6458 | 0.6596 | 3 |
| CoNLL | 0.9070 | 0.8989 | 0.9494 | 0.9006 | 0.9002 | 0.9032 | 3 |
| FewNERD | 0.7478 | 0.7610 | 0.8686 | 0.7157 | 0.7137 | 0.7435 | 2 |

### Gap Recovery

| Dataset | Gap (Oracle-Greedy) | Best Merge - Greedy | Gap Recovery % |
|---------|--------------------|--------------------|----------------|
| SciERC | 0.1319 | +0.0157 | +11.9% |
| CoNLL | 0.0424 | -0.0038 | -9.0% |
| FewNERD | 0.1208 | -0.0043 | -3.6% |

---

## Comparison: Span-Based vs Text-Based

| Dataset | Metric | Text-Based | Span-Based | Delta |
|---------|--------|------------|------------|-------|
| SciERC | Greedy | 0.6439 | 0.6439 | 0 |
| SciERC | Best Merge (k=3) | 0.6596 | 0.6596 | 0 |
| SciERC | Gap Recovery | +11.9% | +11.9% | 0 |
| CoNLL | Greedy | 0.9070 | 0.9070 | 0 |
| CoNLL | Best Merge (k=3) | 0.9032 | 0.9032 | 0 |
| CoNLL | Gap Recovery | -9.0% | -9.0% | 0 |
| FewNERD | Greedy | 0.7478 | 0.7478 | 0 |
| FewNERD | Best Merge (k=2) | 0.7435 | 0.7435 | 0 |
| FewNERD | Gap Recovery | -3.6% | -3.6% | 0 |

**All numbers identical.** No change between text-based and span-based matching for entity merge.

---

## Bootstrap 95% CI

### SciERC
| Method | Mean | 95% CI |
|--------|------|--------|
| greedy | 0.6439 | [0.6173, 0.6711] |
| lp_selection | 0.6501 | [0.6247, 0.6754] |
| oracle_selection | 0.7758 | [0.7526, 0.7976] |
| majority_merge | 0.6515 | [0.6260, 0.6789] |
| lp_weighted_merge | 0.6458 | [0.6199, 0.6717] |
| best_threshold_merge | 0.6596 | [0.6353, 0.6851] |

### CoNLL
| Method | Mean | 95% CI |
|--------|------|--------|
| greedy | 0.9070 | [0.8974, 0.9158] |
| lp_selection | 0.8989 | [0.8888, 0.9082] |
| oracle_selection | 0.9494 | [0.9422, 0.9560] |
| majority_merge | 0.9006 | [0.8903, 0.9098] |
| lp_weighted_merge | 0.9002 | [0.8898, 0.9095] |
| best_threshold_merge | 0.9032 | [0.8933, 0.9119] |

### FewNERD
| Method | Mean | 95% CI |
|--------|------|--------|
| greedy | 0.7478 | [0.7375, 0.7578] |
| lp_selection | 0.7610 | [0.7511, 0.7704] |
| oracle_selection | 0.8686 | [0.8613, 0.8761] |
| majority_merge | 0.7157 | [0.7059, 0.7262] |
| lp_weighted_merge | 0.7137 | [0.7036, 0.7241] |
| best_threshold_merge | 0.7435 | [0.7349, 0.7527] |

---

## Degenerate Subset Analysis

| Dataset | Degen% | N_degen | Greedy | Merge_on_Degen | Oracle_on_Degen | Delta_Merge_vs_Greedy |
|---------|--------|---------|--------|----------------|-----------------|----------------------|
| SciERC | 17.8% | 94 | 0.6270 | 0.6191 | 0.6199 | -0.0078 |
| CoNLL | 58.0% | 1597 | 0.9401 | 0.9387 | 0.9401 | -0.0013 |
| FewNERD | 14.4% | 628 | 0.6139 | 0.6020 | 0.6105 | -0.0119 |

## Non-Degenerate Subset

| Dataset | N | Greedy | Oracle | Majority_Merge | Best_Thresh |
|---------|---|--------|--------|----------------|-------------|
| SciERC | 435 | 0.6476 | 0.8095 | 0.6586 | 0.6702 |
| CoNLL | 1159 | 0.8614 | 0.9622 | 0.8480 | 0.8548 |
| FewNERD | 3723 | 0.7703 | 0.9122 | 0.7349 | 0.7680 |

---

## Conclusion

Switching from text-based `(text, type)` to span-based `(start, end, type)` matching in `entity_strict_match` produces **identical entity merge results** across all three datasets. This is expected because:

1. The merge script groups entities by `(text, type)` for voting, then outputs full entity dicts with correct span info
2. Within a single sentence, the same `(text, type)` almost always maps to a unique `(start, end)` span
3. The span-based evaluation therefore matches the same entities as text-based

The qualitative conclusions are unchanged:
- SciERC: merge recovers +11.9% of the greedy-to-oracle gap
- CoNLL/FewNERD: merge slightly hurts (-9.0% / -3.6%), entity-level voting loses coherence on these datasets
- Degenerate instances (all samples identical) see slight degradation from merge on all datasets
