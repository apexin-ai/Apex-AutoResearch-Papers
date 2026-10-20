Temperature-Stratified Seed Variance (SF5 Defense)

| Stratum | n | seed% | seed:item% | item_id% | G_item |
|---------|-------|-------|------------|----------|--------|
| T=0.0 | 66,400 | 0.000 | 0.043 | 68.25 | 0.683 |
| T=0.3 | 86,400 | 0.000 | 6.157 | 56.43 | 0.564 |
| T=0.7 | 86,400 | 0.007 | 17.404 | 49.36 | 0.494 |
| T>0 | 172,800 | 0.000 | 10.556 | 51.95 | 0.520 |

Key: seed:item monotonically increases with temperature.
T=0 non-zero (0.043%) = FP non-associativity trace, negligible magnitude.
Even at T=0.7, item_id (49.4%) >> seed:item (17.4%).
File: results/analysis/temp_stratified_seed.json