## CCS Selection Results (gold_filter=True, N=8)

| Dataset | Greedy | LP | DGS | **CCS** | Oracle | CCS-Greedy CI |
|---------|--------|--------|--------|---------|--------|---------------|
| SciERC  | 0.6439 | 0.6501 | 0.6513 | 0.6501  | 0.7758 | +0.61pp [-0.70, +2.00] |
| CoNLL   | 0.9070 | 0.8989 | 0.8989 | 0.8964  | 0.9494 | -1.05pp [-1.49, -0.62] |
| FewNERD | 0.7478 | 0.7610 | 0.7615 | 0.7277  | 0.8686 | -2.01pp [-2.59, -1.43] |

Stage2 entity MV hurts on FewNERD (-3.4pp vs DGS). Span-based matching too strict.

⚠️ Pending unified_metrics revalidation.