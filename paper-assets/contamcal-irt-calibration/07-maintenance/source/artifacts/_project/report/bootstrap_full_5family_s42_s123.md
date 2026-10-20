## Bootstrap Full Rerun (5 families × s42+s123)

Generated: 2026-05-20T16:03Z
Script: westd-29999:/root/contamcal-irt-calibration/analysis/bootstrap_triple_seed.py
Coverage: 58/75 cells (s0 data pending)

| Family | n | Baseline | Δ(d100) | 95% CI | Pattern | ρ |
|---|---|---|---|---|---|---|
| Phi-4 | 2 | 76.40% | +0.83pp | [-11.84, +13.49]^t | Incomplete† | -0.10 |
| Qwen2.5-14B | 2 | 69.05% | -11.05pp | [-32.41, +10.30]^t | Collapse | 0.80 |
| Qwen2.5-7B | 2 | 66.35% | -0.89pp | [-12.16, +10.37]^t | V-recovery | 0.40 |
| Gemma-2-9B | 2 | 63.85% | +2.62pp | [-11.81, +17.06]^t | V-recovery† | 0.30 |
| OLMo-2-7B | 3 | 54.93% | +1.35pp | [-0.55, +2.60] | Benefit-sat† | 0.03 |

### Key changes vs previous run
- Phi-4: Immune → Incomplete† (s42 Immune vs s123 Benefit-sat, inconsistent)
- Qwen-7B: n=1→2, both seeds V-recovery ✅ consistent
- Gemma-2: Benefit-sat → V-recovery† (s123 dip-detection triggered)
- All n=2 CIs use t-distribution (df=1), appropriately wide