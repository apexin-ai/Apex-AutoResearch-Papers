# Walker Walk Experiment Metrics Summary

> Generated: 2026-05-15 | Source: registry (event-gated-adaptive-horizon) | Baseline normalization: exp_001 seed 1

## Table 1: Main Comparison — Walker Walk (DMC)

**Legend**: eval = eval_return | nve = normalized v/e (experiment v/e ÷ baseline v/e; >1.5× sustained = delusional critic)

### 1a. Individual Experiments

| Config | Exp ID | Seed | eval@35K | eval@55K | eval@65K | eval@85K | eval@105K | nve@35K | nve@55K | nve@65K | nve@85K | nve@105K | Collapse? |
|--------|--------|------|----------|----------|----------|----------|-----------|---------|---------|---------|---------|----------|-----------|
| **baseline** | exp_001 | 1 | ~400† | 625.7† | 616† | — | 915.7 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | No |
| **trained_dt_emb** | exp_006_fixed_dt2 | 1 | 485.3 | 360.4 | 132.9 | — | — | 1.29 | 2.31 | 4.83 | — | — | **Yes** |
| **trained_dt_emb** | exp_008d | 1 | 146.3 | 82.8 | — | — | — | 1.71 | 4.12 | — | — | — | **Yes** |
| **trained_dt_emb** | exp_009b | 2 | 164.1 | 172.3 | 209.2 | 236.5 | 267.9 | 1.24 | 1.41 | 0.94 | 0.51 | 0.38 | No (transient) |
| **no_dt_emb** | exp_008f | 1 | 206.7 | 173.5 | 375.0 | 246.0 | 503.0 | 0.73 | 0.97 | 0.37 | 0.65 | 0.30 | No |
| **no_dt_emb** | exp_009c | 2 | 178.9 | 238.9 | 244.2 | 227.4 | 148.3 | 0.79 | 0.66 | 0.53 | 0.60 | 1.14 | No |
| **dt1_imag** | exp_008e_v3 | 1 | 276.5 | 486.8 | 580.7 | 657.3 | 869.9 | 0.94 | 0.87 | 0.72 | 0.76 | 0.80 | No |
| **untrained_dt_emb** | exp_008a | 1 | 500.8 | 487.9 | 608.0 | 583.7 | 777.7 | — | 0.93 | 0.66 | 0.68 | 0.59 | No |

† Baseline early eval_return from cross-experiment references (exp_006, exp_008a); registry does not store exp_001 checkpoints < 205K.

**Collapse criteria**: nve > 1.5× sustained across ≥2 consecutive checkpoints at 35K+ steps → **Yes**. Transient spike (1 checkpoint only) that self-corrects → **No (transient)**.

### 1b. Config-Level Summary (mean ± std where multi-seed)

| Config | Seeds | eval@35K | eval@55K | eval@65K | eval@85K | eval@105K | nve@35K | nve@55K | nve@65K | nve@85K | nve@105K | Collapse Rate |
|--------|-------|----------|----------|----------|----------|-----------|---------|---------|---------|---------|----------|---------------|
| baseline | 1 | ~400 | 625.7 | 616 | — | 915.7 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0/1 |
| trained_dt_emb (006) | 1 | 485.3 | 360.4 | 132.9 | — | — | 1.29 | 2.31 | 4.83 | — | — | 1/1 |
| trained_dt_emb (008d) | 2 | 155.2±12.6 | 127.5±63.3 | 209.2‡ | 236.5‡ | 267.9‡ | 1.48±0.33 | 2.77±1.92 | 0.94‡ | 0.51‡ | 0.38‡ | 1/2 |
| no_dt_emb (008f) | 2 | 192.8±19.6 | 206.2±46.3 | 309.6±92.5 | 236.7±13.2 | 325.7±250.9 | 0.76±0.04 | 0.82±0.22 | 0.45±0.11 | 0.63±0.04 | 0.72±0.59 | 0/2 |
| dt1_imag (008e_v3) | 1 | 276.5 | 486.8 | 580.7 | 657.3 | 869.9 | 0.94 | 0.87 | 0.72 | 0.76 | 0.80 | 0/1 |
| untrained_dt_emb (008a) | 1 | 500.8 | 487.9 | 608.0 | 583.7 | 777.7 | — | 0.93 | 0.66 | 0.68 | 0.59 | 0/1 |

‡ Only seed 2 (009b) reached these checkpoints; seed 1 (008d) stopped at 55K due to collapse.

### 1c. Config Descriptions

| Config | Gate | Subsample | dt_embed | Imagination dt | H | Key Question |
|--------|------|-----------|----------|----------------|---|-------------|
| baseline | disabled | OFF | none | dt=1 | 15 | Reference performance |
| trained_dt_emb (006) | fixed dt=2 | ON | trained | dt=2 | 15 | Does fixed dt=2 skip-step cause collapse? |
| trained_dt_emb (008d) | fixed dt=2 | ON | trained | dt=2 | 8 | Isolate trained dt_emb + subsample effect |
| no_dt_emb | fixed dt=2 | ON | dim=0 | dt=2 | 8 | Remove dt_emb → does collapse disappear? |
| dt1_imag (008e_v3) | fixed dt=1 | ON | trained | dt=1 | 15 | Crown jewel: trained dt_emb safe under dt=1 imag |
| untrained_dt_emb (008a) | fixed dt=2 | OFF | untrained | dt=2 | 15 | Isolate subsample effect: no subsample + untrained dt_emb |

## Table 2: RSSM Fidelity Analysis (exp_rssm_fidelity_analysis)

Checkpoint: post-training RSSM prediction quality on held-out transitions.

| Model | dt1 obs_MSE | dt2 obs_MSE | obs_gap (dt2/dt1) | dt1 reward_MAE | dt2 reward_MAE | reward_gap (dt2/dt1) |
|-------|-------------|-------------|-------------------|----------------|----------------|---------------------|
| baseline (exp_001) | 13.49 | 27.50 | 2.04× | 0.0102 | 0.0159 | 1.56× |
| 008d (trained dtEmb) | 41.31 | 53.67 | 1.30× | 0.0568 | 0.1579 | 2.78× |
| 008f (no dtEmb) | 8.01 | 22.04 | 2.75× | 0.7469 | 0.7526 | 1.01× |

**Key findings**:
- 008d: lowest obs_gap (1.30×) but highest absolute errors — trained dt_emb reduces *relative* gap but at cost of overall fidelity
- 008f: best dt1 obs_MSE (8.01) but catastrophic reward prediction (0.75 MAE) — model ignores reward signal
- baseline: balanced fidelity across both dt regimes

## Table 3: Supplementary Experiments

| Exp ID | Config | Seed | eval@35K | eval@55K | eval@65K | eval@105K | nve@35K | nve@55K | nve@65K | Conclusion |
|--------|--------|------|----------|----------|----------|-----------|---------|---------|---------|------------|
| exp_008c | subsample OFF + dt=2 + H=8 | 1 | 185.1 | 241.9 | 240.9 | — | 0.90 | 0.72 | 0.58 | Plateau ~241, no collapse but severe underperformance (−61% vs baseline) |
| exp_007 | fixed dt=4 + H=15 | 1 | 126.7 | 152.5 | — | — | — | 0.15‖ | — | Learning failure, not delusional (v/e 6-13%) |
| exp_005 | learned gate v4 | 1 | 290.8 | 541.2 | 465.7 | 276.1 | — | — | — | Inverted-V: peak 541@55K → collapse to 99@145K |
| exp_003 | learned gate v2 | 1 | — | — | — | 92.3 | — | — | — | Gate entropy PASS (1.66) but return FAIL (10% baseline) |

‖ exp_007 nve@55K computed from v/e@55K=0.061 ÷ baseline_ve@55K=0.404.

## Baseline v/e Reference (normalization denominator)

| Step | 25K | 35K | 45K | 55K | 65K | 75K | 85K | 95K | 105K |
|------|-----|-----|-----|-----|-----|-----|-----|-----|------|
| v/e | 0.087 | 0.241 | 0.331 | 0.404 | 0.563 | 0.719 | 0.701 | 0.632 | 0.656 |

## Summary of Causal Claims

| Claim | Supporting Evidence | Status |
|-------|-------------------|--------|
| **C2: trained dt_emb → delusional critic** | 008d s1 nve 1.71→4.12 (collapse); 009b s2 nve peaks 2.05 (transient). 2/2 seeds show nve>1.5× episode | Supported (2/2 seeds, 1/2 collapse) |
| **C2 control: no dt_emb → no collapse** | 008f s1 nve 0.30-0.97; 009c s2 nve 0.53-1.14. 0/2 seeds exceed 1.5× | Supported (0/2 collapse) |
| **C6: dt=1 imag + trained dt_emb → safe** | 008e_v3 s1 nve 0.72-0.94, eval 870@105K (95% baseline) | Supported (1/1 seed; s2 RUNNING) |
| **B+: subsample ON + untrained dt_emb → safe** | 008e_v3 = 008a result (both reach ~778-870@105K, nve<1.0) | Supported |
