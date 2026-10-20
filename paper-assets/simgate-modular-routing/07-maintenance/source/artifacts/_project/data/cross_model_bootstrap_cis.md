## Cross-Model Bootstrap CIs (B=10000, seed=42)

| Model | Int DR [95% CI] | Det DR [95% CI] | ΔDR [95% CI] | DAF [95% CI] |
|---|---|---|---|---|
| Qwen2.5-7B (245 eps) | 42.9% [36.7, 49.0] | 16.3% [11.8, 21.2] | +26.5 [20.4, 32.7] | 90.4% [81.3, 99.1] |
| Llama-3.1-8B (220 eps) | 41.4% [35.0, 47.7] | 11.4% [7.3, 15.9] | +30.0 [23.6, 36.4] | 88.2% [80.2, 95.1] |

## ⚠️ Discrepancy
Qwen det_DR = 16.3% (40/245 in plan_c data) vs previously reported ≈4.5%. Needs verification — may be different data subset or definition.

## Files
- Script: westb-13313:/root/autodl-tmp/simgate-modular-routing/src/compute_cross_model_cis.py
- JSON: westb-13313:/root/autodl-tmp/simgate-modular-routing/results/cross_model_bootstrap_cis.json
- LaTeX: westb-13313:/root/autodl-tmp/simgate-modular-routing/results/cross_model_bootstrap_cis.tex