Result Aggregation Summary (2026-05-15)

33 experiments, 25 with standalone eval, 3 fallback (adaptive_fix), 5 no eval (1 not started + 4 running).

Key metrics:
- Uniform baseline: 17.6938 ± 0.0077
- Grid-best (b=0.5): 17.6448 ± 0.0065 (all 3 seeds select b=0.5)
- Adaptive (old, n_min=3): 17.6389 ± 0.0071, ratio = 1.119 (exceeds grid-best)
- Adaptive_fix (n_min=2): eval_ppl from registry = 17.65/17.643/17.66, mean ~17.651 ± 0.007, ratio ~87.8%
  NOTE: CSV marked these as fallback (trainer_state ppl≈21.9). Registry has correct standalone eval values.

Running: ess_only, golden_ratio, nmin1, tau_06

CSV location (remote): /root/provenance_weight_training/results/summary_table.csv
Issue: adaptive_fix standalone eval exists in registry but script didn't locate it on filesystem.