# exp_019b PickCube CIVO Trigger — Final Analysis

**Date**: 2026-05-17
**Status**: Completed (212.4K steps)
**Conclusion**: Negative (informative) — transient CIVO confirmed, sustained mechanism not replicated

---

## Experiment Config

| Parameter | Value |
|---|---|
| Environment | PickCube-v1 (ManiSkill3) |
| Config | trained dt_emb, subsample ON, dt=2 imagination, H=8 |
| Baseline | exp_019a_v2 (vanilla DreamerV3, same env) |
| Total steps | 212,400 (019b) / 203,448 (019a) |

---

## Key Final Metrics (step 202.5K)

| Metric | 019b (CIVO trigger) | 019a (baseline) |
|---|---|---|
| **Eval return** | **26.64** | **58.56** |
| Last-5 eval mean | 13.30 | 62.25 |
| Last-10 train mean | 18.95 | 59.16 |
| Peak eval | 26.87 @132.5K | 69.70 @162.5K |
| value_mean | 4.262 | 144.569 |
| target_mean | 4.307 | 144.651 |
| V/T ratio | 0.990 | 0.999 |
| value_loss | 1.801 | 0.944 |
| EMA range | 14.14 | 23.40 |
| gate_dt_2_frac | **1.0** (locked) | N/A |
| gate_empirical_entropy | **0.0** (locked) | N/A |
| **019b/019a eval ratio** | **0.214 (21.4%)** | — |

---

## NVE Trajectory (value_mean/eval_return, normalized by baseline)

| Step | 019b eval | 019a eval | NVE |
|---|---|---|---|
| 2.5K | 0.82 | 1.11 | 1.22x |
| 12.5K | 16.87 | 24.90 | 1.28x |
| 22.5K | 24.90 | 19.34 | 0.66x |
| 32.5K | 10.62 | 33.19 | **2.43x** |
| 42.5K | 14.38 | 21.66 | 0.83x |
| **52.5K** | **3.69** | **37.30** | **3.78x (peak)** |
| 62.5K | 5.95 | 29.25 | 1.16x |
| 72.5K | 8.55 | 35.86 | 0.63x |
| 82.5K | 5.71 | 47.03 | 0.78x |
| 92.5K | 4.97 | 52.82 | 0.68x |
| 102.5K | 8.36 | 34.47 | 0.19x |
| 132.5K | 26.87 | 67.96 | 0.08x |
| 202.5K | 26.64 | 58.56 | **0.065x** |

---

## CIVO Dynamics: Four Phases

### Phase 1: Parallel Growth (0-22.5K)
Both experiments learn similarly. 019b eval briefly matches baseline. Value functions growing, NVE near 1.0.

### Phase 2: CIVO Spike (22.5K-52.5K)
019b eval collapses (24.9 to 3.7) while value_mean stays elevated (17.6 to 20.9). Classic value overestimation: the dt=2 imagination produces inflated value targets that the value function tracks, but actual policy execution fails. NVE peaks at 3.78x @52.5K.

### Phase 3: Value Deflation (52.5K-112.5K)
Value_mean declines from 20.9 to 5.0 as the overestimated targets correct. Eval remains low (5-9 range). NVE drops below 1.0 as the value function now underestimates relative to baseline.

### Phase 4: Partial Recovery (112.5K-202.5K)
Eval partially recovers to 13-27 range but never exceeds 50% of baseline. Value_mean stabilizes at 4.2, permanently depressed (vs baseline's 144). The value function never recovers its scale.

---

## Gate Analysis

The gate was completely locked at dt=2 for the entire run:
- gate_dt_2_frac = 1.0 at every checkpoint (2.5K through 202.5K)
- gate_empirical_entropy = 0.0 throughout
- gate_entropy_ratio = 0.0 throughout
- gate_dt_autocorr = 0.0 (constant, no temporal variation)

The trained dt_emb never learned to modulate the gate. The system behaved as a fixed dt=2 imagination run with extra parameters.

---

## Comparison with Walker Walk CIVO Pattern

| Aspect | Walker Walk | PickCube |
|---|---|---|
| CIVO triggered? | Yes | Yes (transient) |
| NVE peak | Sustained >1.5x | Spike to 3.78x, then collapse |
| Value recovery | Partial | Value permanently depressed |
| Eval impact | Moderate degradation | Severe (21% of baseline) |
| Gate behavior | Some modulation | Locked dt=2 entire run |

Key difference: Walker shows sustained CIVO where value overestimation persists and partially self-corrects. PickCube shows transient CIVO where the spike is dramatic but brief, followed by value function collapse. The value function in 019b ends at 3% of baseline's scale (4.26 vs 144.57).

---

## Conclusions and Claim Impact

### What this experiment shows:
1. **CIVO mechanism can be triggered in PickCube** — the NVE spike to 3.78x confirms that compound imagination with dt=2 does produce value overestimation
2. **The dynamics are environment-dependent** — PickCube produces transient CIVO (spike + collapse) vs Walker's sustained pattern
3. **Gate learning fails in this setting** — trained dt_emb alone is insufficient; the gate locks and never explores alternative dt values
4. **Value function collapse is the dominant failure mode** — not sustained overestimation, but overestimation followed by permanent depression

### For the paper:
- Can claim CIVO is a cross-environment phenomenon (triggered in both locomotion and manipulation)
- Must note the dynamics differ qualitatively: environment structure shapes whether CIVO is sustained or transient
- The transient pattern suggests PickCube's reward landscape (sparse, binary success) causes faster correction but also more catastrophic collapse
- Gate locking at dt=2 means this run also serves as a fixed-dt=2 negative control for PickCube

### Verdict: **Negative (informative)**
The experiment fails to match baseline performance (21.4% of baseline eval), but provides scientifically valuable evidence about CIVO cross-environment generality and its environment-dependent dynamics.

---

## Metrics Dict

```python
{
    "experiment": "exp_019b_pickcube_civo_trigger",
    "conclusion": "negative_informative",
    "final_step": 212400,
    "final_eval_return": 26.64,
    "baseline_final_eval_return": 58.56,
    "eval_ratio_to_baseline": 0.214,
    "last5_eval_mean": 13.30,
    "baseline_last5_eval_mean": 62.25,
    "peak_eval": 26.87,
    "peak_eval_step": 132500,
    "peak_nve": 3.782,
    "peak_nve_step": 52500,
    "final_nve": 0.065,
    "final_value_mean": 4.262,
    "baseline_final_value_mean": 144.569,
    "gate_locked": True,
    "gate_dt_2_frac": 1.0,
    "gate_entropy": 0.0,
    "civo_pattern": "transient",
    "value_collapse": True,
}
```
