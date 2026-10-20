# Reactive Intervention Analysis: intervention_reactive_s42

## Summary

Reactive intervention (monitoring distinct_1 drop >10%) successfully triggered at generation 2 after a 15.58% decline in distinct_1. Switching α from 1.0 to 0.0 immediately halted model collapse: perplexity recovered from 157.1 (gen 2) to 21.9 (gen 3) and stabilized at 21.2 by gen 10. However, by the time the reactive trigger fired, the model had already suffered 2 generations of full synthetic contamination, causing severe transient damage (ppl 26.9→157.1, entropy 3.23→1.48). The final state (gen 10) is statistically indistinguishable from the α=0.0 pure-real-data baseline, meaning the reactive intervention effectively "erased" the contamination but also forfeited any potential benefit from synthetic data augmentation.

## Experiment Configuration

| Parameter | Value |
|---|---|
| Model | Pythia-410M |
| Seed | 42 |
| Data | WikiText-103 (5k samples) |
| Generations | 10 |
| Steps/gen | 5000 |
| Intervention mode | reactive |
| Trigger metric | distinct_1 |
| Trigger threshold | >10% drop from gen 0 |
| Post-trigger α | 0.0 (stop synthetic data) |
| Initial α | 1.0 (100% synthetic) |

## Intervention Timeline

- **Gen 0** (baseline): distinct_1 = 0.0982. No intervention check (baseline measurement).
- **Gen 1**: distinct_1 = 0.0975 (−0.7% from gen 0). Below threshold, no trigger.
- **Gen 2**: distinct_1 = 0.0823 (−16.2% from gen 0). **INTERVENTION TRIGGERED** (logged as −15.58%). α switches from 1.0 → 0.0 starting gen 3.
- **Gen 3-10**: All subsequent generations train on real data only (α = 0.0).

The trigger fired after 2 full generations of α=1.0 contamination. During those 2 generations, the model experienced severe degradation: perplexity spiked from 26.95 to 157.09 (+483%) and token entropy collapsed from 3.234 to 1.478 (−54%).

## Metrics Trajectory

| Gen | α_eff | distinct_1 | distinct_2 | distinct_3 | ppl | token_entropy | ece | eff_rank | mauve |
|-----|-------|-----------|-----------|-----------|------|--------------|------|----------|-------|
| 0 | 1.0 | 0.0982 | 0.5178 | 0.8127 | 26.95 | 3.234 | 0.0108 | 46.6 | 0.0341 |
| 1 | 1.0 | 0.0975 | 0.5141 | 0.8104 | 56.27 | 1.912 | 0.2046 | 79.8 | 0.0323 |
| 2 | 1.0 | **0.0823** | 0.4310 | 0.7116 | **157.09** | **1.478** | 0.3201 | 93.7 | 0.0315 |
| 3 | 0.0 | 0.0764 | 0.3918 | 0.6551 | 21.92 | 3.111 | 0.0149 | 48.9 | 0.0306 |
| 4 | 0.0 | 0.0838 | 0.4624 | 0.7689 | 21.48 | 3.095 | 0.0107 | 46.8 | 0.0320 |
| 5 | 0.0 | 0.0844 | 0.4648 | 0.7702 | 21.34 | 3.072 | 0.0135 | 44.9 | 0.0310 |
| 6 | 0.0 | 0.0846 | 0.4711 | 0.7790 | 21.19 | 3.053 | 0.0160 | 44.3 | 0.0306 |
| 7 | 0.0 | 0.0841 | 0.4683 | 0.7784 | 21.40 | 3.070 | 0.0145 | 43.4 | 0.0308 |
| 8 | 0.0 | 0.0852 | 0.4689 | 0.7750 | 21.06 | 3.081 | 0.0121 | 43.0 | 0.0291 |
| 9 | 0.0 | 0.0856 | 0.4744 | 0.7799 | 21.26 | 3.050 | 0.0168 | 42.6 | 0.0287 |
| 10 | 0.0 | 0.0844 | 0.4698 | 0.7812 | 21.24 | 3.071 | 0.0152 | 43.7 | 0.0289 |

### Key observations:
1. **Immediate recovery (gen 2→3)**: ppl 157.1→21.9, entropy 1.48→3.11, ece 0.32→0.015. The model's internal calibration recovers within a single generation of real-data training.
2. **Delayed diversity recovery (gen 3→4)**: distinct_1 dips further to 0.0764 at gen 3 before rebounding to 0.0838 at gen 4. Diversity metrics lag behind calibration metrics by ~1 generation.
3. **Stable plateau (gen 4-10)**: All metrics stabilize. distinct_1 fluctuates in [0.0838, 0.0856], ppl in [21.06, 21.48], entropy in [3.05, 3.10].

## Comparison with No-Intervention Baseline

### vs α=1.0 no-intervention (mvp_v4_rep42, same seed)

| Metric | Gen 0 | Reactive Gen 10 | No-Interv Gen 10 | Reactive Drift | No-Interv Drift |
|--------|-------|-----------------|-------------------|---------------|-----------------|
| distinct_1 | 0.0982 | 0.0844 | 0.0704 | −14.1% | −28.3% |
| distinct_2 | 0.5178 | 0.4698 | 0.3355 | −9.3% | −35.2% |
| distinct_3 | 0.8127 | 0.7812 | 0.5556 | −3.9% | −31.6% |
| ppl | 26.95 | 21.24 | 1003.73 | −21.2% | +3624.6% |
| entropy | 3.234 | 3.071 | 1.276 | −5.0% | −60.5% |
| ece | 0.0108 | 0.0152 | 0.4173 | +40.7% | +3762.5% |
| mauve | 0.0341 | 0.0289 | — | −15.2% | — |

The reactive intervention reduced distinct_1 degradation from −28.3% to −14.1% and completely prevented the catastrophic perplexity explosion (+3624.6% → −21.2%).

### vs α=0.0 pure-real-data baseline (alpha_sweep_a000_s42)

| Metric | α=0.0 Gen 10 | Reactive Gen 10 | Difference |
|--------|-------------|-----------------|------------|
| distinct_1 | 0.0847 | 0.0844 | −0.4% |
| ppl | 21.11 | 21.24 | +0.6% |
| entropy | 3.069 | 3.071 | +0.1% |
| ece | 0.0164 | 0.0152 | −7.3% |
| eff_rank | 43.72 | 43.74 | +0.0% |

The reactive intervention final state is **indistinguishable from never having used synthetic data** (all differences <1% except ece, which is actually slightly better). The 2 generations of α=1.0 contamination left no lasting damage after 8 generations of real-data recovery.

## Conclusion and Implications

### Verdict: SUCCESS

The reactive distinct_1-based intervention successfully:
1. Detected ongoing collapse (triggered at gen 2 with −15.58% distinct_1 drop)
2. Halted further degradation (ppl stabilized at ~21 instead of spiraling to 1000+)
3. Allowed full recovery (final state matches α=0.0 baseline)

### Implications for Predictive vs Reactive Comparison

The reactive approach works but has a fundamental limitation: **it can only react after observable damage has occurred.** By gen 2, the model had already experienced severe transient damage (ppl 157, entropy 1.48). While the damage was reversible in this setting, there are scenarios where it might not be:

1. **Earlier trigger = less transient damage**: A predictive (canary-based) intervention that triggers before gen 2 would avoid the ppl=157 spike entirely.
2. **The reactive approach converges to α=0.0**: Since it completely stops synthetic data, the model "forgets" the contamination but also loses any potential benefit. A predictive approach that modulates α (e.g., α=0.5 instead of α=0.0) could potentially preserve some synthetic data benefit while avoiding collapse.
3. **Latency of diversity metrics**: distinct_1 is a lagging indicator (compared to canary metrics like token_entropy and ece). Token entropy collapsed −40.9% by gen 1, but distinct_1 only dropped −0.7%. The reactive trigger based on distinct_1 inherently cannot fire as early as a canary-based trigger.

### Key numbers for the paper
- Reactive trigger: gen 2, distinct_1 drop = 15.58%
- Peak transient damage: ppl = 157.09 (gen 2), 5.8x baseline
- Recovery complete by: gen 4 (within 2 generations of intervention)
- Final distinct_1 drift: −14.1% (vs −28.3% without intervention)
- Final ppl drift: −21.2% (vs +3624.6% without intervention)
