# exp_hopper_trained_s0_ext — NVE/CIVO Analysis Report

**Date**: 2026-05-27
**Hypothesis**: Continuing trained_s0 from 105K to 150K will confirm delayed CIVO: ve_ratio (0.897 at 105K, exponentially rising) will cross NVE>1.5 threshold by ~115-125K.
**Conclusion**: **NEGATIVE** — hypothesis falsified.

---

## 1. Training Status

- **Completed normally** (EXIT_CODE=0)
- **Final step**: 168K (exceeded target of 150K)
- **No errors** in log
- Server: westd-51268
- Log: `~/runs/event-gated-adaptive-horizon/exp_hopper_trained_s0_ext.log`

---

## 2. NVE Trajectory (Full Precision from metrics.jsonl)

### Pre-extension (parent exp_hopper_trained_s0):
| Step | ve_ratio | delta_ve | alert | eval_return |
|------|----------|----------|-------|-------------|
| 15K  | 0.488    | 0.0      | 0.0   | 0.089       |
| 25K  | 67750.3* | 67749.8  | 0.0   | 0.0         |
| 35K  | 0.200    | —        | 0.0   | 0.333       |
| 85K  | 0.060    | -0.618   | 0.0   | 8.014       |
| 95K  | 0.257    | 0.197    | 0.0   | 5.003       |
| **105K** | **0.897** | **0.640** | **1.0** | 3.260   |

*25K spike is a numerical artifact (near-zero actual return causing division blow-up).

### Extension (108K → 168K):
| Step | ve_ratio | delta_ve | alert | eval_return |
|------|----------|----------|-------|-------------|
| 108K | —        | —        | —     | 5.433       |
| 118K | 0.376    | 0.0      | 0.0   | 15.077      |
| **128K** | **5.519** | **5.142** | 0.0 | 2.055    |
| 138K | 0.370    | -5.149   | 0.0   | 47.403      |
| 148K | 0.550    | 0.181    | 0.0   | 46.901      |
| 158K | 0.439    | -0.111   | 0.0   | 81.581      |

---

## 3. D155 NVE Diagnostic

| Criterion | Required | Observed | Pass? |
|-----------|----------|----------|-------|
| NVE_peak > 1.5× | τ=1.5 | 5.519 at 128K | ✅ Technically |
| NVE sustained ≥2 eval points | ≥2 consecutive | 1 point only (128K) | ❌ |
| Temporal causality: onset after trained dt_emb | gate variation | gate_dt locked at 2.0, entropy=0.0 | ❌ |

**CIVO NOT confirmed.** Fails criteria #2 and #3.

---

## 4. Key Observations

### 4.1 The 105K→118K ve_ratio DROP
The "exponentially rising" trend (0.06→0.26→0.90 from 85K-105K) **broke upon continuation**. ve_ratio dropped from 0.897 to 0.376 at 118K. The rising trend was not robust.

### 4.2 The 128K Transient Spike
- ve_ratio spiked to 5.519 at 128K, but eval_return simultaneously cratered to 2.055 (vs. 15.077 at 118K and 47.403 at 138K).
- This is a **transient performance dip** where the critic's value predictions temporarily overshot actual returns.
- Not genuine value estimation inflation — it's a momentary eval fluctuation artifact.
- Immediately reverted to 0.370 at 138K.

### 4.3 Gate Behavior: Completely Locked
- gate_dt_mean = 2.0 at every eval point
- gate_dt_2_frac = 1.0 (100%)
- gate_empirical_entropy = 0.0
- gate_entropy_ratio = 0.0
- **The event-gated mechanism is NOT engaging.** No adaptive horizon selection whatsoever.

### 4.4 Performance Improvement is Strong
Despite no CIVO and no gate variation, performance improved dramatically:
- eval_return: 3.26 (105K) → 81.58 (158K) — **25× improvement**
- train_return at 168K: 82-115 range
- Value predictions scaled correctly: value_mean 1.3→35.8, target_mean 1.3→36.1

---

## 5. Comparison with Walker/Cheetah

- **Hopper**: Gate locked at dt=2, zero entropy, ve_ratio stays 0.3-0.9 (one transient spike). No CIVO.
- In environments with confirmed CIVO, ve_ratio elevation is **sustained** across multiple eval points with concurrent gate variation. Hopper shows neither.

---

## 6. Conclusion

**Status: NEGATIVE**

The hypothesis is falsified:
1. The "exponentially rising" ve_ratio trend at 105K did NOT continue — it dropped upon resume.
2. While a single spike to 5.52 occurred at 128K (within predicted window), it was transient and coincided with a performance dip, not genuine value overestimation.
3. The gate is completely locked (dt=2, entropy=0), violating the temporal causality criterion.
4. The 105K alert=1.0 was a **false positive** for delayed CIVO.

**Suggested registry update**:
- conclusion: "Hypothesis falsified. ve_ratio dropped from 0.897 to 0.376 upon continuation. Single transient spike to 5.52 at 128K (performance dip artifact), not sustained. Gate locked at dt=2 with zero entropy. No delayed CIVO in Hopper."
- metrics: {ve_ratio_105K: 0.897, ve_ratio_118K: 0.376, ve_ratio_128K: 5.519, ve_ratio_138K: 0.370, ve_ratio_148K: 0.550, ve_ratio_158K: 0.439, eval_return_final: 81.58, nve_peak: 5.519, nve_sustained_points: 1, gate_entropy: 0.0}
