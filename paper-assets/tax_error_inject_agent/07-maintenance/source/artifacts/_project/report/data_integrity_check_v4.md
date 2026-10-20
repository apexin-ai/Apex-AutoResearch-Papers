# Data Integrity Check — v4 Eval Results
Date: 2026-05-15

## Result: ALL 18 NUMBERS VERIFIED, NO DISCREPANCIES

All success_rate values in eval JSON files match the claimed numbers exactly.
All total_episodes = 47 across all files.

## Dose-response (seed=42) — 6/6 match
- v4_taxei_fixed_inject10_eval.json: 0.617 = 61.7% (29/47) ✓
- v4_taxei_fixed_inject25_eval.json: 0.489 = 48.9% (23/47) ✓
- v4_taxei_fixed_inject50_eval.json: 0.511 = 51.1% (24/47) ✓
- v4_random_fixed_inject10_eval.json: 0.681 = 68.1% (32/47) ✓
- v4_random_fixed_inject25_eval.json: 0.553 = 55.3% (26/47) ✓
- v4_random_fixed_inject50_eval.json: 0.574 = 57.4% (27/47) ✓

## 3-seed evals — 9/9 match
- v4_vanilla_eval.json (seed42): 0.617 = 61.7% ✓
- v4_vanilla_seed0_eval.json: 0.681 = 68.1% ✓
- v4_vanilla_seed123_eval.json: 0.66 = 66.0% ✓
- v4_taxei_eval.json (seed42): 0.617 = 61.7% ✓
- v4_taxei_seed0_eval.json: 0.468 = 46.8% ✓
- v4_taxei_seed123_eval.json: 0.617 = 61.7% ✓
- v4_random_eval.json (seed42): 0.66 = 66.0% ✓
- v4_random_seed0_eval.json: 0.553 = 55.3% ✓
- v4_random_seed123_eval.json: 0.681 = 68.1% ✓

## Recovery eval — 3/3 match
- v4_vanilla_recovery_eval.json: 0.617 = 61.7% ✓
- v4_taxei_recovery_eval.json: 0.596 = 59.6% ✓
- v4_random_recovery_eval.json: 0.638 = 63.8% ✓

## Fraction cross-check
All count/47 ratios are internally consistent with stored 3-decimal success_rate values.