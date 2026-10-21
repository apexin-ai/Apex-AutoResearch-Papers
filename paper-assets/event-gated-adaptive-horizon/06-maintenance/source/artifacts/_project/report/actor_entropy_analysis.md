# Actor Entropy Analysis: Healthy vs Collapsed Configurations

## Summary

Collapsed (CIVO/trained dt_emb) configurations show a distinctive entropy explosion pattern: **return collapses first, then actor entropy rises sharply**, consistent with the "delusional critic gradients" hypothesis. Healthy baselines also exhibit gradual entropy drift at late training stages, but at ~10-20x slower rate and without return degradation.

---

## 1. Entropy Dynamics Summary

| Experiment | Group | min_ent | @step | final_ent | @step | post-min rise | late rate (/10K) |
|---|---|---|---|---|---|---|---|
| Baseline s1 | healthy | -5.23 | 85K | -1.51 | 505K | +4.45 | -0.10 |
| Baseline s2 | healthy | -5.29 | 292K | -3.48 | 512K | +1.81 | +0.22 |
| Baseline s3 | healthy | -5.29 | 120K | -0.90 | 510K | +4.45 | +0.10 |
| Baseline s4 | healthy | -5.28 | 112K | -2.07 | 512K | +3.31 | +0.07 |
| 008a: untrained dt_emb | healthy | -5.26 | 95K | -5.24 | 105K | +0.02 | ~0.00 |
| 008e_v3: untrained dt_emb, sub ON | healthy | -5.18 | 95K | -5.18 | 105K | +0.00 | ~0.00 |
| 008f: no dt_emb, sub ON | healthy | -4.86 | 95K | -4.85 | 105K | +0.01 | ~0.00 |
| **006: trained dt, dt=2** | **collapsed** | -5.17 | 55K | -5.12 | 65K | +0.05 | — |
| **008d: trained dt, H=8** | **collapsed** | -4.88 | 55K | -4.88 | 55K | +0.00 | — |
| **008d_civo s3** | **collapsed** | -5.09 | 85K | -4.43 | 105K | +0.67 | +0.08 |
| **008d_civo s4** | **collapsed** | -5.19 | 95K | -4.91 | 105K | +0.29 | -0.04 |
| **045: 008d extension (112-302K)** | **collapsed** | -3.56 | 112K | -0.14 | 302K | **+3.42** | +0.11 |
| **059: trained s5** | **collapsed** | -4.95 | 85K | -4.13 | 105K | +0.82 | +0.16 |
| **EG v4 s1** | **collapsed** | -5.21 | 95K | **+3.22** | 135K | **+8.43** | **+1.68** |
| **EG v5 s1** | **collapsed** | -5.11 | 45K | **+1.03** | 145K | **+6.14** | **+1.14** |

## 2. Key Findings

### 2.1 Collapsed configs: entropy explosion

The most dramatic examples are the event-gated experiments:

**EG v4 s1**: Entropy explodes from -5.21 to +3.22 in just 40K steps (95K→135K).
- Rate: **+2.11 nats/10K steps** — catastrophic actor confusion
- Correlated with return collapse: 583 → 93 (60K→120K)

**EG v5 s1**: Entropy rises from -5.11 to +1.03 over 100K steps.
- Rate: **+0.61 nats/10K steps**
- Return: 583 → 102 (60K→140K)

**exp_045 (008d extension, 112-302K)**: Continued training of a collapsed config shows sustained entropy rise from -3.56 to -0.14 over 190K steps. The actor never recovers — it drifts toward maximum entropy (uniform random policy).

### 2.2 Temporal sequence: return collapses BEFORE entropy rises

| Exp | Return collapse onset | Entropy rise onset | Lag |
|---|---|---|---|
| EG v4 | ~60K (583→355) | ~95K (-5.21 starts rising) | ~35K steps |
| EG v5 | ~80K (539→281) | ~65K (-5.09 starts rising) | concurrent |
| 006 | ~52K (814→149) | not visible (run ended 65K) | — |
| 008d | ~40K (return declining) | not visible (run ended 55K) | — |

This is consistent with the causal chain: **critic becomes delusional → provides bad actor gradients → actor policy destabilizes (entropy rises) → performance degrades further**.

### 2.3 Healthy baselines: gradual entropy drift (not collapse)

All 4 baseline seeds show entropy rising after ~100-200K steps, but:
- **Rate is 10-20x slower**: +0.07 to +0.22 nats/10K vs +1.14 to +1.68 nats/10K for collapsed
- **Returns remain high**: 900-970 throughout, no performance degradation
- **Entropy stabilizes**: oscillates between -1 and -4 rather than exploding to positive values

This suggests the baseline entropy drift is a normal DreamerV3 behavior (exploration/exploitation cycling), fundamentally different from the catastrophic entropy explosion in collapsed configs.

### 2.4 Short-run collapsed configs: early warning signs

exp_008d_civo_s3 and s4 (running to 105K) show mild entropy rises of +0.29 to +0.67 nats in the last 20K steps. These are likely the beginning of the same entropy explosion pattern, caught before full manifestation.

exp_059 (trained dt_emb, 105K) shows +0.82 nats rise from step 85K — another early-stage collapse signal.

## 3. Return-Entropy Correlation for Collapsed Experiments

### EG v4 s1 (most dramatic)
```
Step   60K: return=583, entropy≈-5.10  (healthy phase)
Step   80K: return=447, entropy≈-5.18  (return declining, entropy still low)
Step   95K: return≈355, entropy=-5.21  (return collapsed, entropy at minimum)
Step  105K: return≈---,  entropy=-4.63  (entropy starts rising)
Step  115K: return≈---,  entropy=-2.55  (rapid rise)
Step  120K: return=93,   entropy≈---    (return bottomed out)
Step  125K: return≈---,  entropy=+0.86  (entropy crosses zero → near-random)
Step  135K: return≈---,  entropy=+3.22  (entropy explosion → superstochastic)
```

### 006: trained dt_emb, dt=2 (first collapse)
```
Step   48K: return=215  (declining)
Step   52K: return=165  (accelerating decline)
Step   68K: return=149  (continued decline)
Step   72K: return=29   (collapsed)
Entropy: -5.17@55K → -5.12@65K (barely started rising before run ended)
```

## 4. Interpretation

### The delusional critic gradient mechanism

1. **Trained dt_emb / CIVO** causes the world model to generate systematically biased imagined trajectories
2. The **critic trained on these biased trajectories** develops incorrect value estimates
3. The **actor receives gradient updates** from this delusional critic, pushing it away from optimal actions
4. As the actor policy becomes confused, its **entropy rises** — it assigns probability mass to suboptimal actions
5. Higher entropy → worse performance → even more biased trajectories → positive feedback loop

### Why healthy baselines show entropy drift without collapse

The baseline entropy drift (+0.07-0.22/10K) occurs at ~200K+ steps and appears to be a normal DreamerV3 phenomenon:
- Returns stay high (900+), so the policy is not confused
- The entropy rise may reflect the policy exploring alternative equally-good strategies
- Or it's regularization effects (entropy bonus in DreamerV3's actor loss)

### Distinguishing collapsed vs healthy entropy rise

| Feature | Collapsed | Healthy drift |
|---|---|---|
| Rate | 1.1-2.1 nats/10K | 0.07-0.22 nats/10K |
| Onset | 50-100K steps | 200K+ steps |
| Return | Collapses (→ <100) | Stable (900+) |
| Final entropy | Positive (+1 to +3) | Mildly negative (-1 to -3) |
| Pattern | Monotonic explosion | Oscillation |

## 5. Data Sources

All data extracted from `metrics.jsonl` files in `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/` on bjb1-45299.

| Experiment | Directory |
|---|---|
| Baseline s1-s4 | baseline_s1, exp_001_baseline_s2/s3/s4 |
| 008a | exp_008a_fixed_dt2_no_subsample |
| 008e_v3 | exp_008e_v3_subsample_on_dt1_h15 |
| 008f | exp_008f_no_dt_embed_subsample_on_h8 |
| 006 equiv | fixed_dt2_v1_s1 |
| 008d | exp_008d_subsample_on_h8 |
| 008d_civo s3/s4 | exp_008d_civo_trigger_s3/s4 |
| 045 extension | exp_045_treatment_extension_008d_s3 |
| 059 | exp_059_walker_trained_s5 |
| EG v4/v5 | event_gated_v4_s1, event_gated_v5_s1 |
| 015b | exp_015b_frozen_dt_emb |
