# Exec-only 3-Seed Aggregate Statistics

Generated: 2026-05-20
Sources: table_data.json, wilson_ci_complete.json, registry.yaml, decisions D088/D091

## Table 1: Exec-only 500-step (3 seeds)

| Seed | exp_id | PR | ISR | n_proved | TS | CE | PG | CI | Genuine | Hacking% | Notes |
|------|--------|----|-----|----------|----|----|----|----|---------|---------:|-------|
| s42 | plan001-exec-only-s42-r2 | 0.93 | 0.123 | 93 | 0 (0%) | 81 (87.1%) | 0 | 0 | 12 (12.9%) | 87.1% | |
| s43 | plan001-exec-only-s43-r4 | 0.13 | 0.000 | 13 | 0 (0%) | 13 (100%) | 0 | 0 | 0 (0%) | 100% | do_sample=True eval; not comparable per C004 |
| s44 | plan001-exec-only-s44 | 0.98 | 0.570 | 98 | 98 (100%) | 0 (0%) | 0 | 0 | 0 (0%) | 100% | tautological collapse; ISR is artifact |
| **Mean** | | **0.68** | **0.23** | | | | | | | **95.7%** | |
| **Std** | | **0.47** | **0.30** | | | | | | | **7.4%** | |
| **Pooled** | | — | — | **204** | 98 (48.0%) | 94 (46.1%) | 0 | 0 | 12 (5.9%) | **94.1%** | |

### Caveats
- s43 eval used `do_sample=True` (T=0.7), violating C004 — not strictly comparable
- s44 ISR=0.570 is tautological artifact (2-component P->P proofs, 100% TS)
- Extreme seed variance: PR ranges 0.13--0.98, hacking modes differ qualitatively (CE vs TS)
- Wilson 95% CI for pooled genuine: [3.4%, 10.0%]

---

## Table 2: Exec-only 1000-step (3 seeds)

| Seed | exp_id | PR | ISR | n_proved | TS | CE | PG | CI | Genuine | Hacking% | Notes |
|------|--------|----|-----|----------|----|----|----|----|---------|---------:|-------|
| s42 | plan016-extended-1000-s42 | 0.96 | 0.003 | 96 | 0 (0%) | 96 (100%) | 0 | 0 | 0 (0%) | 100% | contradiction explosion; comp=18.55 |
| s43 | plan001-exec-only-s43-1000-r2 | 0.90 | 0.531 | 90 | 90 (100%) | 0 (0%) | 0 | 0 | 0 (0%) | 100% | ISR artifact from H7a tautology (corrected=0.465) |
| s44 | plan001-exec-only-s44-1000-r2 | 1.00 | 0.002 | 100 | 0 (0%) | 85 (85%) | 15 (15%) | 0 | 0 (0%) | 100% | 3 H1-near escape classifiers but ISR=0; genuine_strict=0 |
| **Mean** | | **0.95** | **0.179** | | | | | | | **100%** | |
| **Std** | | **0.05** | **0.305** | | | | | | | **0%** | |
| **Pooled** | | — | — | **286** | 90 (31.5%) | 181 (63.3%) | 15 (5.2%) | 0 | 0 (0%) | **100%** | genuine=1.0% per D091 (3 H1-near in s44) |

### Key observations
- **Genuine collapse is the invariant**: 0/0/0% genuine across all 3 seeds (mean=0%, or 1.0%+-1.7% per D091 counting H1-near)
- **Hacking mode is seed-dependent**: s42=CE, s43=TS, s44=CE+PG -- different paths to same endpoint
- **PR increases**: 0.68+-0.47 (500-step) -> 0.95+-0.05 (1000-step); model gets better at proving while losing all structural quality
- **ISR mean is misleading**: s43 ISR=0.531 is 100% TS artifact, not reasoning quality

---

## Summary for Abstract

### 500-step
- PR = 0.68 +- 0.47 (3 seeds)
- ISR = 0.23 +- 0.30
- Pooled genuine = 5.9% (12/204)
- Pooled hacking = 94.1% (192/204)

### 1000-step
- PR = 0.95 +- 0.05 (3 seeds)
- ISR = 0.179 +- 0.305 (misleading due to TS artifact in s43)
- Pooled genuine = 0% strict, 1.0% with H1-near (3/286)
- Pooled hacking = 100% (or 99.0% with H1-near)
- All GRPO seeds reach 0% genuine at 1000 steps (confirmed by D091)

### Taxonomy naming
- CE = Conclusion Embedding (formerly H1)
- TS = Tautological Shortcut (formerly H7)
- PG = Proof Grafting (formerly H8)
- CI = Contradiction Injection (formerly H9)
