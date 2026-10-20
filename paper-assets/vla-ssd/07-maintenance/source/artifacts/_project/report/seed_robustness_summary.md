# Probe Seed Robustness Check

Seeds: [0, 1, 2, 42] | Metric: ΔR² = R²(peak layer) − R²(exit layer L31) | Position: `last_preaction`

## Summary Table — last_preaction ΔR²

| Cell | Seed 0 | Seed 1 | Seed 2 | Seed 42 | Mean ± Std | Stable? |
|------|--------|--------|--------|---------|------------|---------|
| TracVLA Goal | 0.2178 | 0.2432 | 0.2195 | 0.2283 | **0.2272 ± 0.0101** | ✓ |
| TracVLA Spatial | 0.1366 | 0.1371 | 0.1326 | 0.1378 | **0.1360 ± 0.0020** | ✓ |
| OpenVLA Goal | 0.0145 | 0.0105 | 0.0129 | 0.0130 | **0.0127 ± 0.0014** | ✓ |

**All cells pass stability threshold (std < 0.02).**

## Peak Layer Details (last_preaction)

| Cell | Seed 0 | Seed 1 | Seed 2 | Seed 42 | Peak R² range | Exit R² range |
|------|--------|--------|--------|---------|---------------|---------------|
| TracVLA Goal | L6 | L6 | L6 | L18 | 0.793–0.806 | 0.550–0.586 |
| TracVLA Spatial | L11 | L17 | L6 | L17 | 0.793–0.809 | 0.660–0.671 |
| OpenVLA Goal | L28 | L21 | L19 | L25 | 0.669–0.698 | 0.658–0.684 |

## Supplementary: image_mean ΔR²

| Cell | Mean ± Std | Stable? |
|------|------------|---------|
| TracVLA Goal | 0.0367 ± 0.0031 | ✓ |
| TracVLA Spatial | 0.0436 ± 0.0072 | ✓ |
| OpenVLA Goal | 0.0000 ± 0.0000 | ✓ |

## Conclusion

The ΔR² metric is robust to train/test split randomness across all 3 cells. Standard deviations are well below the 0.02 threshold (max std = 0.0101 for TracVLA Goal). The core finding — TracVLA exhibits large action-information loss in late layers (ΔR² ≈ 0.14–0.23), while OpenVLA preserves action information through exit (ΔR² ≈ 0.01) — is stable and not an artifact of a particular data split.

## Raw Results

- `/root/autodl-tmp/vla-ssd/results/seed_robustness/tracvla_goal_seed_robustness.json`
- `/root/autodl-tmp/vla-ssd/results/seed_robustness/tracvla_spatial_seed_robustness.json`
- `/root/autodl-tmp/vla-ssd/results/seed_robustness/openvla_goal_seed_robustness.json`

Server: westd-19183 | Date: 2026-05-24
