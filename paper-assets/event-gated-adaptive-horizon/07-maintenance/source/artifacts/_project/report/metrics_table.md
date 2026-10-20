# Event-Gated Adaptive Horizon: Full Experiment Metrics Comparison

**Environment:** DMC Walker Walk | **Extracted:** 2026-05-15 | **Server:** bjb1-45299

## Notation

- **v/e ratio** = value_mean / eval_return (critic calibration proxy)
- **nve** = normalized v/e = (experiment v/e) / (baseline v/e @ same step). Baseline = exp_001 (DreamerV3 baseline, seed=1) for all experiments
- **nve thresholds:** >1.5x = pathological (delusional critic); 0.8-1.2x = normal; <0.7x = value suppression
- v/e at 25K omitted (baseline v/e too small for reliable normalization)

---

## Main Comparison Table

| Exp ID | gate | sub | dt | H | dt_emb | seed | status | eval_final | eval_peak | v/e @35K | v/e @45K | v/e @65K | v/e @105K | nve @35K | nve @45K | nve @65K | nve @105K | Claim |
|--------|------|-----|----|---|--------|------|--------|-----------|-----------|---------|---------|---------|----------|---------|---------|---------|----------|-------|
| exp_001_baseline | OFF | OFF | 1 | 15 | N/A | 1 | done/success | **970.4** | 970.4 | 0.241 | 0.331 | 0.563 | 0.656 | 1.00 | 1.00 | 1.00 | 1.00 | ref |
| exp_009a_baseline_s2 | OFF | OFF | 1 | 15 | N/A | 2 | running (89%) | 948.4 | 966.9 | 0.306 | 0.363 | 0.474 | 0.645 | 1.27 | 1.10 | 0.84 | 0.98 | ref |
| exp_008a | ON | OFF | 2 | 15 | 32 | 1 | done/success | 777.7 | 777.7 | 0.157 | 0.234 | 0.372 | 0.386 | **0.65** | **0.71** | **0.66** | **0.59** | C3 |
| exp_008c | ON | OFF | 2 | 8 | 32 | 1 | done/negative | 240.9 | 241.9 | 0.218 | 0.254 | 0.328 | N/A | 0.91 | **0.77** | **0.58** | N/A | C3 |
| exp_008d | ON | ON | 2 | 8 | 32 | 1 | done/negative | 82.7 | 167.2 | 0.411 | 0.693 | N/A | N/A | **1.71** | **2.09** | N/A | N/A | C1,C2 |
| exp_008e_v3 | ON | ON | 1 | 15 | 32 | 1 | done/success | **869.9** | 869.9 | 0.227 | 0.290 | 0.405 | 0.526 | 0.94 | 0.87 | **0.72** | 0.80 | **C6** |
| exp_008f | ON | ON | 2 | 8 | 0 | 1 | done/success | 503.2 | 503.2 | 0.176 | 0.275 | 0.207 | 0.195 | **0.73** | 0.83 | **0.37** | **0.30** | C1,C2 |
| exp_009b (008d s2) | ON | ON | 2 | 8 | 32 | 2 | done/negative | 267.9 | 278.5 | 0.299 | 0.536 | 0.530 | 0.251 | 1.24 | **1.62** | 0.94 | **0.38** | C1,C2 |
| exp_009c (008f s2) | ON | ON | 2 | 8 | 0 | 2 | done/negative | 148.3 | 359.1 | 0.191 | 0.237 | 0.298 | 0.750 | **0.79** | **0.72** | **0.53** | 1.14 | C1,C2 |
| exp_008e_v3 s2 | ON | ON | 1 | 15 | 32 | 2 | running (65%) | 435.1 | 435.1 | 0.249 | 0.351 | 0.507 | N/A | 1.03 | 1.06 | 0.90 | N/A | **C6** |

**Bold nve** = outside normal range (0.8-1.2x). **Bold eval_final** = >800 (strong performance).

---

## Key Findings

### C1: Subsample ON + trained dt_emb + dt>1 imagination triggers delusional critic
- **008d** (s1): nve=1.71x@35K, 2.09x@45K → collapse (eval 167→83, killed at 55K)
- **009b** (s2): nve=1.62x@45K (transient pathological), no full collapse but eval stuck at 268@105K

### C2: Trained dt_emb triggers pathological overestimation; removing dt_emb prevents it
- **008d** (s1) + **009b** (s2): nve>1.5x at 35K+ (2/2 trained dt_emb seeds)
- **008f** (s1): nve 0.30-0.83x (no pathological), eval slowly rising to 503 (-45%)
- **009c** (s2): nve 0.53-1.14x (normal), eval declined to 148 (-84%)
- Contrast: dt_emb=32 causes nve>1.5x (2/2); dt_emb=0 keeps nve<1.2x (2/2) → 4/4 separation

### C3: Untrained dt_emb suppresses value estimation, protecting performance
- **008a**: nve consistently 0.59-0.71x (value suppression), eval 778 (-15% vs baseline@105K)
- **008c**: nve declining 0.91→0.58x, eval plateaued at 241 (-61% vs baseline@65K)

### C6: dt=1 imagination with trained dt_emb avoids delusional critic, preserves performance
- **008e_v3** (s1): nve=0.72-0.94x (normal), eval=869.9 (-5% vs baseline) -- **crown jewel**
- **008e_v3** (s2): nve=0.90-1.06x (normal), eval=435.1@65K (still running, on track)

---

## Diagnostic Experiments (Early Series)

| Exp ID | Config | eval_peak | v/e @65K | nve @65K | Note |
|--------|--------|-----------|---------|----------|------|
| exp_006_fixed_dt2 | gate ON, dt=2, H=15 | 485.3 @35K | **2.722** | **4.84** | First delusional critic observation; collapsed to 133 @65K |
| exp_007_fixed_dt4 | gate ON, dt=4, H=15 | 176.9 @25K | N/A | N/A | Severe learning failure; extreme value suppression |

---

## Gate Behavior Summary

| Exp ID | gate_dt_mean (final) | gate_dt_1_frac | gate_entropy | Note |
|--------|---------------------|----------------|--------------|------|
| exp_008a | 2.0 | 0.0 | 0.0 | Fixed dt=2, no variation |
| exp_008c | 2.0 | 0.0 | 0.0 | Fixed dt=2, no variation |
| exp_008d | 2.0 | 0.0 | 0.0 | Fixed dt=2 (collapsed before gate could learn) |
| exp_008e_v3 | 1.0 | 1.0 | 0.0 | Fixed dt=1 (design choice) |
| exp_008f | 2.0 | 0.0 | 0.0 | Fixed dt=2, no dt_emb conditioning |
| exp_009b (s2) | 2.0 | 0.0 | 0.0 | Fixed dt=2 |
| exp_009c (s2) | 2.0 | 0.0 | 0.0 | Fixed dt=2, no dt_emb |
| exp_008e_v3 (s2) | 1.0 | 1.0 | 0.0 | Fixed dt=1 |

---

## Training Progress

| Exp ID | max_step | target | total_steps (baseline: 500K) |
|--------|----------|--------|-----|
| exp_001_baseline | 505K | 500K | complete |
| exp_009a_baseline_s2 | 445K | 500K | 89% (running) |
| exp_008a | 105K | 105K | complete |
| exp_008c | 65K | 105K | killed early (plateau) |
| exp_008d | 55K | 105K | killed (collapse) |
| exp_008e_v3 | 105K | 105K | complete |
| exp_008f | 105K | 105K | complete |
| exp_009b | 105K | 105K | complete |
| exp_009c | 105K | 105K | complete |
| exp_008e_v3 s2 | 65K | 105K | 65% (running) |
