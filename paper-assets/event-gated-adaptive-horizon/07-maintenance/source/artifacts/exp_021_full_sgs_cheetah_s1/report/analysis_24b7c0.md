# exp_021_full_sgs_cheetah_s1 Analysis

## Configuration
- Environment: Cheetah Run
- gate_enabled=True, gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8
- full_sgs=True (Stop-Gradient on all non-KL gradients from dt_emb)
- seed=1, 105K eval steps (training continued to ~112K)

## Final Metrics

| Metric | Value |
|--------|-------|
| eval_return_final | 221.5 |
| eval_return_peak | 221.5 (step 105K) |
| peak_step | 105000 |
| NVE_peak | 9.94 (step 45K) |
| NVE_peak_step | 45000 |
| NVE_sustained_avg (55K-105K) | 0.338 |
| civo | **True** (transient, self-correcting) |
| actor_grad_norm | 0.0-0.1 (very small under SGS) |

## Eval Return Trajectory

| Step | eval_return | value_mean | NVE (ve_ratio) |
|------|-------------|------------|----------------|
| 5K   | 13.5  | 0.0   | 0.000 |
| 15K  | 105.4 | 1.9   | 0.018 |
| 25K  | 85.0  | 15.0  | 0.177 |
| 35K  | 145.3 | 34.3  | 0.236 |
| 45K  | 4.6   | 45.6  | **9.94** |
| 55K  | 77.4  | 44.9  | 0.580 |
| 65K  | 85.2  | 40.1  | 0.470 |
| 75K  | 129.1 | 33.7  | 0.261 |
| 85K  | 108.7 | 28.3  | 0.261 |
| 95K  | 68.3  | 24.3  | 0.355 |
| 105K | 221.5 | 21.2  | 0.096 |

## Key Observations

1. **Transient CIVO at step 45K**: NVE spiked to 9.94 with eval_return collapsing to 4.6. Unlike 010b (permanent collapse), the agent recovered within ~10K steps.

2. **Value_mean trajectory**: Rose to peak 45.6 at step 45K, then monotonically decreased to 21.2 at 105K. SGS appears to constrain value growth after the initial spike, but did NOT prevent it.

3. **Post-recovery NVE is healthy**: After 55K, NVE sustained average = 0.338, well below 1.5x threshold. SGS maintains value discipline after the transient event.

4. **Actor learning severely impaired**: actor_grad_norm = 0.0-0.1 throughout (vs typical 1-10 in non-SGS runs). Full SGS may be over-aggressive in blocking gradients.

5. **Performance far below baseline**: 221.5 / 572.5 = **38.7% of baseline** (baselines: 023a=624.7, 023b=520.3, mean=572.5).

## Comparison with 010b (Cheetah, no SGS, gate dt=2)

| Metric | 010b (no SGS) | 021 (Full-SGS) |
|--------|---------------|-----------------|
| NVE_peak | 8.27 | 9.94 |
| eval_return_final | 51.7 | 221.5 |
| Collapse | Permanent | Transient (recovered) |
| civo | True | True |

SGS did NOT prevent the CIVO spike, but enabled recovery. Final performance is 4.3x better than 010b but still 61% below baseline.

## Comparison with 018 (Walker, Full-SGS)

| Metric | 018 (Walker SGS) | 021 (Cheetah SGS) |
|--------|-------------------|---------------------|
| NVE_peak | 0.72 | 9.94 |
| NVE_sustained_avg | 0.55 | 0.338 |
| civo | False | True (transient) |
| Cross-env consistent | Yes (Walker) | **No** (Cheetah) |

**Cross-environment consistency NOT confirmed.** SGS fully prevents CIVO in Walker but only partially mitigates it in Cheetah.

## Conclusion: **PARTIAL NEGATIVE**

- Full-SGS does NOT reliably prevent CIVO across environments
- In Cheetah, a transient CIVO event still occurs (NVE=9.94 at 45K)
- SGS enables recovery (unlike permanent collapse in 010b), suggesting partial protective effect
- However, performance remains far below baseline (38.7%), likely due to over-aggressive gradient blocking (actor_grad_norm near zero)
- The hypothesis that SGS eliminates NVE>1.5x is **rejected** for Cheetah

## Suggested Registry Entry

```python
{
    "exp_id": "exp_021_full_sgs_cheetah_s1",
    "env": "cheetah_run",
    "intervention": "full_sgs",
    "seed": 1,
    "steps": 105000,
    "metrics": {
        "eval_return_final": 221.5,
        "eval_return_peak": 221.5,
        "peak_step": 105000,
        "NVE_peak": 9.94,
        "NVE_peak_step": 45000,
        "NVE_sustained_avg": 0.338,
        "civo": True,
        "civo_type": "transient_recovered",
        "baseline_ratio": 0.387,
        "actor_grad_norm_range": [0.0, 0.1]
    },
    "conclusion": "partial_negative",
    "notes": "SGS enables recovery from CIVO (vs 010b permanent collapse) but does NOT prevent initial spike. Cross-env consistency with Walker NOT confirmed. Performance 38.7% of baseline."
}
```

## Next Steps (Suggested)

1. Investigate why CIVO still occurs under SGS in Cheetah but not Walker (environment-specific dynamics?)
2. Consider partial SGS or SGS with warmup to avoid over-blocking actor gradients
3. Run seed=0 variant to check if the transient CIVO at 45K is seed-dependent
