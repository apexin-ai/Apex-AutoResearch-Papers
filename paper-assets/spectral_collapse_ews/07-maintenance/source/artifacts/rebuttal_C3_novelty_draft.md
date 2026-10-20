# C3 Novelty Defense: Signal Attenuation

**Anticipated attack**: "Signal attenuation (mixing suppresses spectral warning signals) is trivially expected — of course if you prevent collapse, there's no collapse signal to detect."

**Response** (~200 words):

The observation that intervention suppresses warning signals is indeed anticipated by the EWS literature (Scheffer 2009, Siteur 2016). Our contribution is not the qualitative observation but three quantitative findings that theory alone does not predict:

1. **Continuous degradation curve**: Signal attenuation is not binary (present/absent). We show that the controller signal degrades *continuously* as the mixing ratio approaches r_crit, with a smooth transition from strong signal (r=0, Δ_max=0.08) through attenuated signal (r=0.2, Δ_max=0.002) to complete silence (r≥0.3, Δ_max<0.0003). This continuous relationship — empirically characterized across 5 mixing ratios × 3 seeds — has not been quantified before.

2. **τ-independence**: The signal vanishes entirely above r_crit for *any* positive threshold τ, not just our chosen τ=0.002. This means the limitation cannot be resolved by tuning sensitivity — it is structural. This extends to cumulative variants of the controller signal.

3. **Cross-indicator generality**: All 7 EWS indicators (SLV, RankMe, isotropy, stable rank, spectral norm, token entropy, perplexity growth rate) exhibit the same attenuation pattern. The phenomenon is not SLV-specific but affects any rate-based spectral/output indicator, suggesting a fundamental geometric property of the mixed-training regime.

**Empirical anchor**: Table 3 phase diagram + §4.3 controller analysis + §4.5 alt-EWS comparison provide the quantitative evidence chain.

**Framing**: C3 is positioned as "demonstrating an inherent limitation" with "quantitative characterization," not as "discovering" something new. The verb choice is deliberate (commit 473d4fb).
