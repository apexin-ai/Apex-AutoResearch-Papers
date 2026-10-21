Sensitivity Sweep V2 (with volatility check)

180/180 correct classifications (6 families × 30 τ×σ combos)

V1 → V2 changes: 35 fixes, 0 regressions
- Qwen-7B s123: 0/30 → 30/30 correct (was Immune, now V-recovery)
- Qwen-7B s42 at τ=2.0: 0/5 → 5/5 correct (was Immune, now V-recovery)
- Phi-4: 30/30 Immune (unchanged)
- All other families: 30/30 unchanged

Remote: westd:/root/contamcal-irt-calibration/analysis/results/sensitivity_v2/