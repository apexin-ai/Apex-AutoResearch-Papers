# Experiment Status Summary

Generated: 2026-05-15

## Status Counts (39 total experiments)

| Status | Count | Experiments |
|--------|-------|-------------|
| DONE | 30 | All uniform, grid-b, adaptive, adaptive-fix, detector, datagen, diagnostic |
| RUNNING | 4 | tau_06_seed42, nmin1_seed42, golden_ratio_seed42, ess_only_seed42 |
| PREPARING | 4 | tau_095_seed42, tau_09_seed42, tau_07_seed42, tau_05_seed42 |
| QUEUED | 1 | detector_modernbert |

## Conclusion Breakdown (DONE experiments)

| Conclusion | Count | Experiments |
|------------|-------|-------------|
| success | 22 | 3× uniform, 6× grid-b seed42 (batch), 6× grid-b seed123, 6× grid-b seed456, 3× adaptive, 3× adaptive-fix, detector_tfidf_lr, datagen_synthetic_4gpu |
| killed | 7 | tau_0.6_seed42 (name bug), detector_modernbert, 3× adaptive_v2 (superseded), diagnostic_contamination100, grid_b_low_seed42 |
| failed | 1 | grid_b_low_seed42 (infra bug: cron framework killed process) |

Note: 3 grid-b seed456 results (*b*=2.0/3.0/5.0) marked **invalidated** (D026, checkpoint resume artifact) but conclusion remains "success".

## GPU Hours

| Category | Hours |
|----------|-------|
| Uniform (3 seeds) | 10.29 |
| Grid-b seed42 batch (6 configs) | 22.53 |
| Grid-b seed123 (6 runs) | 23.10 |
| Grid-b seed456 (6 runs) | 18.20 |
| Adaptive original (3 seeds) | 12.63 |
| Adaptive-fix (3 seeds) | 9.69 |
| Grid-b low (failed) | 0.22 |
| **Total (completed)** | **~96.7** |

Note: GPU hours for detector, datagen, diagnostic, and currently running experiments not included in total (separate workloads or incomplete).
