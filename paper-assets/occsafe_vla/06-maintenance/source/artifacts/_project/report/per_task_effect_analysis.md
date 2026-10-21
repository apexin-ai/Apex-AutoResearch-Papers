# Per-Task Effect Analysis (v2 Factorial)

Date: 2026-05-29

## Data Coverage

| Cell | Seeds with per-task | Overall n | Missing |
|------|-------------------|-----------|---------|
| Cell 1 (BN+ON) | 2 | 3 | full_occ_retrain_s0 (format issue) |
| Cell 2 (LN+ON) | 4 | 4 | — |
| Cell 3 (BN+OFF) | 4 | 4 | — |
| Cell 4 (LN+OFF) | 2 | 3 | detach_ln_v2_s0c (format issue) |
| Vanilla | 2 | 3 | vanilla_v2_s2 (format issue) |

## Per-Task Mean CAR

| Task | Group | C1:ON+BN | C2:ON+LN | C3:OFF+BN | C4:OFF+LN | Vanilla |
|------|-------|----------|----------|-----------|-----------|---------|
| T0 | Easy | 0.970 | 0.980 | 0.980 | 0.970 | 0.980 |
| T1 | Easy | 0.960 | 0.970 | 0.915 | 0.980 | 0.900 |
| T2 | Easy | 0.880 | 0.925 | 0.930 | 0.920 | 0.940 |
| T3 | HARD | 0.290 | 0.375 | 0.360 | 0.380 | 0.350 |
| T4 | Med  | 0.980 | 0.955 | 0.950 | 0.930 | 0.970 |
| T5 | HARD | 0.180 | 0.175 | 0.080 | 0.220 | 0.060 |
| T6 | HARD | 0.250 | 0.505 | 0.495 | 0.500 | 0.390 |
| T7 | Easy | 0.730 | 0.855 | 0.965 | 1.000 | 0.990 |
| T8 | Easy | 1.000 | 0.995 | 0.995 | 1.000 | 1.000 |
| T9 | Easy | 0.910 | 0.995 | 0.995 | 1.000 | 1.000 |

## Main Effects by Task Group

| Group | Gradient (ON-OFF) | Normalization (LN-BN) |
|-------|------------------|-----------------------|
| Hard (T3,T5,T6) | -1.6pp | **+6.9pp** |
| Easy (6 tasks) | -3.0pp | +1.7pp |
| All (10 tasks) | -2.1pp | +2.9pp |
| **Hard/Easy ratio** | **0.5×** | **4.1×** |

## Key Findings

### 1. Normalization effect amplifies 4× on hard tasks
LN advantage over BN is +6.9pp on safety-critical tasks vs +1.7pp on easy tasks. This is the dominant and most consistent effect on hard tasks. Per-task: T6 (+9.0pp), T5 (+7.7pp), T3 (+4.0pp) — all positive and substantial.

### 2. Gradient flow harm does NOT concentrate on hard tasks
Gradient ON-OFF effect is -1.6pp on hard tasks vs -3.0pp on easy tasks (ratio 0.5×). The gradient harm is actually more pronounced on easy tasks, driven largely by T7 (-16.3pp single task). Per-task direction is noisy: T5 shows +5.0pp (opposite direction), T6 shows -7.7pp.

### 3. Cell 1 instability concentrates on hard tasks + T7
Cell 1 (BN+Grad ON) cross-seed variance:
- Hard tasks mean std: 0.217
- Easy tasks mean std: 0.092
- Ratio: 2.4×
- Highest: T7 (Easy, std=0.354, range=0.50), T3 (Hard, std=0.297, range=0.42)

## Per-Task Individual Effects

| Task | Group | Grad(ON-OFF) | Norm(LN-BN) | C4 vs Vanilla |
|------|-------|-------------|-------------|---------------|
| T0 | Easy | +0.0pp | +0.0pp | -1.0pp |
| T1 | Easy | +3.0pp | +4.3pp | +8.0pp |
| T2 | Easy | -1.7pp | +1.0pp | -2.0pp |
| T3 | HARD | -2.0pp | +4.0pp | +3.0pp |
| T4 | Med | +2.0pp | -1.3pp | -4.0pp |
| T5 | HARD | +5.0pp | +7.7pp | +16.0pp |
| T6 | HARD | -7.7pp | +9.0pp | +11.0pp |
| T7 | Easy | -16.3pp | +1.7pp | +1.0pp |
| T8 | Easy | +0.0pp | +0.0pp | +0.0pp |
| T9 | Easy | -3.0pp | +3.0pp | +0.0pp |

## Caveats
- Cell 1, Cell 4, Vanilla each missing 1 seed's per-task data (registry format inconsistency)
- n=2 per-task seeds for these cells limits reliability of per-task variance estimates
- Per-task effects on individual tasks are highly variable across seeds
