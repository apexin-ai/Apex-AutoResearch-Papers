## Entity-Level Merge Results

| Dataset | Greedy | LP_Sel | Oracle_Sel | Majority_Merge | LP_Weighted | Best_Thresh | Best_k |
|---------|--------|--------|------------|----------------|-------------|-------------|--------|
| SciERC | 0.6182 | 0.6241 | 0.7448 | 0.6255 | 0.6200 | 0.6333 | 3 |
| CoNLL | 0.7239 | 0.7165 | 0.7639 | 0.7175 | 0.7167 | 0.7223 | 5 |
| FewNERD | 0.6507 | 0.6671 | 0.7850 | 0.6193 | 0.6189 | 0.6571 | 4 |

**Ceiling NOT broken on any dataset.** Merge vs Oracle differences all statistically significant (p<0.05 via bootstrap).

## Gap Recovery
| Dataset | Oracle-Greedy Gap | Best Merge - Greedy | % Gap Recovered |
|---------|-------------------|---------------------|-----------------|
| SciERC | 0.1266 | +0.0151 | 11.9% |
| CoNLL | 0.0400 | -0.0016 | -4.0% |
| FewNERD | 0.1343 | +0.0064 | 4.8% |

## Degenerate Subset Analysis
| Dataset | Degen% | N_degen | Greedy | Merge_on_Degen | Oracle_on_Degen | Delta |
|---------|--------|---------|--------|----------------|-----------------|-------|
| SciERC | 21.1% | 116 | 0.5080 | 0.5017 | 0.5023 | -0.0063 |
| CoNLL | 58.0% | 2002 | 0.6146 | 0.6142 | 0.6146 | -0.0004 |
| FewNERD | 19.1% | 956 | 0.1562 | 0.1539 | 0.1562 | -0.0024 |

## Key Findings
1. Entity-level voting merge cannot break instance-level selection ceiling
2. On degenerate instances, merge slightly hurts (negative delta on all 3 datasets)
3. Optimal thresholds are low (k=3-5), suggesting inclusive merge helps more than conservative
4. LP-weighted merge offers no advantage over simple frequency voting
5. This motivates instance-level quality estimation over entity-level aggregation

## Files
- Script: analysis_d141_entity_merge.py
- Results: output/d141_entity_merge/results.json
- Plot: output/d141_entity_merge/threshold_curve.png