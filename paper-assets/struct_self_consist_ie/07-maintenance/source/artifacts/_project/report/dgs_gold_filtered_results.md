## DGS Gold-Filtered Results

| Dataset | Used | Degen% | Greedy | LP-all | DGS | Oracle | DGS-Greedy CI |
|---------|------|--------|--------|--------|-----|--------|---------------|
| SciERC  | 529  | 18.5%  | 0.6417 | 0.6403 | 0.6400 | 0.7785 | -0.17pp [-1.54, +1.22] n.s. |
| CoNLL   | 2756 | 57.9%  | 0.9070 | 0.8989 | 0.8989 | 0.9494 | -0.81pp [-1.22, -0.40] sig |
| FewNERD | 4351 | 14.4%  | 0.7478 | 0.7610 | 0.7615 | 0.8686 | +1.37pp [+0.91, +1.86] sig |

⚠️ SciERC Greedy=0.6417 inconsistent with other scripts (0.6439). Pending unified_metrics fix.