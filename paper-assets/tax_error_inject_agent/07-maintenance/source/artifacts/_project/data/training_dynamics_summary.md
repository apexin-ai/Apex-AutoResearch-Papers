## Training Dynamics Summary

Source: /root/autodl-tmp/tax_error_inject_agent/analysis/training_dynamics.csv

| Experiment | Init Loss | Final Loss | Min Loss | Final Acc | Max Acc |
|---|---|---|---|---|---|
| vanilla_0pct | 1.3425 | 0.2937 | 0.2461 | 0.8936 | 0.9119 |
| random_10pct | 1.4128 | 0.2907 | 0.2369 | 0.8959 | 0.9212 |
| random_25pct | 1.4255 | 0.2635 | 0.2178 | 0.9074 | 0.9202 |
| random_50pct | 1.4772 | 0.2600 | 0.1901 | 0.9076 | 0.9307 |
| taxei_50pct | 1.4780 | 0.2601 | 0.1873 | 0.9088 | 0.9330 |

Key finding: Higher injection → better training metrics but worse downstream eval.
TaxEI 50% ≈ Random 50% in training dynamics (loss 0.2601 vs 0.2600).
