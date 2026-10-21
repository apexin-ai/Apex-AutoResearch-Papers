# MBR Span-Fix Results

Date: 2026-05-18

## Confounds Addressed

1. **Utility/evaluation metric misalignment**: original MBR used (text, type) Jaccard as utility but evaluation uses (start, end, type) span F1. Added span-based Jaccard utility for fair comparison.
2. **gold_filter inconsistency**: CoNLL had gold_filter=False while SciERC/FewNERD had True. Unified to gold_filter=True for all datasets.

## Results (all gold_filter=True, N=8 samples)

| Dataset | N_inst | Greedy | LP | MBR-text | MBR-span | Oracle | MBR_text-Greedy | MBR_span-Greedy | Span-Text |
|---------|--------|--------|----|----------|----------|--------|-----------------|-----------------|-----------|
| SciERC  | 529    | 0.6439 | 0.6501 | 0.6444 | 0.6451 | 0.7758 | +0.0005 | +0.0011 | +0.0007 |
| CoNLL   | 2756   | 0.9070 | 0.8989 | 0.9023 | 0.9028 | 0.9494 | -0.0047 | -0.0042 | +0.0005 |
| FewNERD | 4351   | 0.7478 | 0.7610 | 0.7208 | 0.7214 | 0.8686 | -0.0269 | -0.0263 | +0.0006 |

## Text/Span Selection Agreement

| Dataset | Agreement |
|---------|-----------|
| SciERC  | 98.9%     |
| CoNLL   | 99.7%     |
| FewNERD | 99.1%     |

## Conclusion

**MBR confirmed dead.** Neither confound explains MBR's negative results:

1. **Metric misalignment is negligible.** Span-based and text-based MBR select the same sample 98.9-99.7% of the time. The span-based fix improves F1 by only +0.05-0.07pp per dataset.
2. **gold_filter unification does not change the picture.** CoNLL with gold_filter=True shows MBR-span at -0.42pp (was -0.4pp with False). FewNERD remains strongly negative at -2.63pp.
3. **MBR underperforms greedy on 2/3 datasets** (CoNLL, FewNERD) and is essentially tied on SciERC (+0.11pp). The oracle gap (7-14pp above greedy) confirms substantial room for improvement exists, but MBR's consensus-based selection fails to exploit it.

## Artifacts

- Script: `/root/autodl-tmp/struct_self_consist_ie/code/analysis_mbr_span_fix.py`
- JSON results: `/root/autodl-tmp/struct_self_consist_ie/output/mbr_selection_results.json`
