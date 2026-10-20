# NVE Baseline Unification — Modification Log
Date: 2026-05-15

## Motivation
Reviewer flagged inconsistency: nve_trajectories.csv used exp_001 baseline for all experiments,
but metrics_table.md used exp_009a baseline for seed=2 experiments. This caused 009b@45K nve
to show 1.62 in CSV but 1.48 in metrics_table. Director decision: unify on exp_001 (seed=1).

## Changes Made

### Item 1: metrics_table.md — unified baseline
- Notation updated: "Baseline = exp_001 (DreamerV3 baseline, seed=1) for all experiments"
- exp_009a nve: 1.00/1.00/1.00/1.00 → 1.27/1.10/0.84/0.98
- exp_009b nve: 0.98/1.48/1.12/0.39 → 1.24/**1.62**/0.94/0.38 (45K now >1.5x ✓)
- exp_009c nve: 0.63/0.65/0.63/1.16 → 0.79/0.72/0.53/1.14
- exp_008e_v3 s2 nve: 0.81/0.97/1.07 → 1.03/1.06/0.90

### Item 2: method.md — normalization statement
- Section 3.2: replaced provisional baseline text with:
  "We normalize all v/e ratios against exp_001 (DreamerV3 baseline, seed 1) at matched training steps.
   Sensitivity to baseline choice is reported in Appendix X."

### Item 3: exp_001 registry — complete eval trajectory
- Added full eval trajectory (5K-505K, 51 checkpoints) to registry
- Previously missing: 5K-195K and 465K-505K
- Peak: 970.41@505K (was 964.96@435K)

### Item 4: summary_table.csv — at-step baseline comparison
- vs_baseline_pct now uses baseline eval_return at matched step, not fixed baseline@455K
- Key changes: 008a -18.43→-15.07, 008c -74.74→-60.89, 008d -91.32→-86.78,
  008e_v3_s1 -8.76→-5.00, 006 -86.06→-78.42, 007 -84.01→-75.63
- exp_001 final_eval updated: 953.37→970.41 (was stale, now uses 505K data)

### Item 5: D035 dedup
- Removed exp_008e_v3_subsample_on_dt1_h15 ("s0") from summary_table and nve_trajectories
- Kept exp_008e_v3_walker_s1 ("s1") — same seed=1, more recent registration
- Reason: both used --seed 1, s0 was early registration before plan_014 naming convention

### Item 6: Claim column corrections
- 008d: C1,C3 → C1,C2 (trained dt_emb → pathological nve, not untrained protection)
- 008a: C2 → C3 (untrained dt_emb → value suppression, not trained dt_emb pathology)
- 008c: C2 → C3 (same logic as 008a)
- 008f: C1,C3 → C1,C2 (no dt_emb = C2 causal control, not C3 untrained protection)
- 009b: C1,C3 → C1,C2 (trained dt_emb seed 2)
- 009c: C1,C3 → C1,C2 (no dt_emb seed 2, C2 control)

## Files Modified
- artifacts/_project/report/metrics_table.md (+ synced to artifacts/analysis/)
- artifacts/_project/data/metrics_table.csv (+ synced to artifacts/analysis/)
- artifacts/_project/data/summary_table.csv (+ synced to artifacts/figures_data/)
- artifacts/_project/data/nve_trajectories.csv (+ synced to artifacts/figures_data/)
- paper/method.md (+ synced to artifacts/_project/paper/)
- Registry: exp_001_baseline metrics field

## Validation
- 009b@45K nve = 0.536/0.331 = 1.62 > 1.5x ✓ (consistent with CSV)
- 4/4 threshold separation preserved: trained dt_emb seeds (008d 2.09x, 009b 1.62x) > 1.5x;
  no-dt_emb seeds (008f 1.02x, 009c 1.26x@25K only) < 1.5x at 35K+
- nve_trajectories.csv already used exp_001 baseline — no changes needed (except dedup)
