# D129 Complete 1.7B 3×3 Data (2026-05-18)

## Per-seed 表 (% of n_proved)

| Condition | Seed | n_proved | PR | ISR* | H7 | H1 | H8 | Genuine | CI | S-Gen |
|-----------|------|----------|------|------|------|------|------|---------|------|-------|
| ISR 0.1 | s42 | 100 | 1.00 | 0.600 | 0 (0%) | 100 (100%) | 0 (0%) | 0 (0%) | 100 (100%) | 0 |
| ISR 0.1 | s43 | 60 | 0.60 | 0.750 | 60 (100%) | 0 (0%) | 0 (0%) | 0 (0%) | 60 (100%) | 0 |
| ISR 0.1 | s44 | 82 | 0.82 | 0.440 | 0 (0%) | 32 (39.0%) | 15 (18.3%) | 35 (42.7%) | 77 (93.9%) | 3 |
| Random 0.1 | s42 | 93 | 0.93 | 0.028 | 0 (0%) | 78 (83.9%) | 1 (1.1%) | 15 (16.1%) | 93 (100%) | 0 |
| Random 0.1 | s43 | 100 | 1.00 | 0.051 | 0 (0%) | 76 (76.0%) | 0 (0%) | 24 (24.0%) | 100 (100%) | 0 |
| Random 0.1 | s44 | 100 | 1.00 | 0.007 | 0 (0%) | 84 (84.0%) | 0 (0%) | 16 (16.0%) | 100 (100%) | 0 |
| ISR 0.3 | s42 | 17 | 0.17 | 0.182 | 0 (0%) | 12 (70.6%) | 0 (0%) | 5 (29.4%) | 1 (5.9%) | 5 |
| ISR 0.3 | s43 | 52 | 0.52 | 0.231 | 0 (0%) | 14 (26.9%) | 0 (0%) | 38 (73.1%) | 52 (100%) | 0 |
| ISR 0.3 | s44 | 92 | 0.92 | 0.236 | 0 (0%) | 1 (1.1%) | 1 (1.1%) | 90 (97.8%) | 92 (100%) | 0 |

## Pooled 表 (mean±std across 3 seeds)

| Condition | PR mean±std | ISR* mean±std | H1% pooled | H7% pooled | Genuine% pooled | CI% pooled | S-Gen pooled |
|-----------|-------------|---------------|------------|------------|-----------------|------------|--------------|
| ISR 0.1 | 0.81±0.20 | 0.597±0.155 | 132/242=54.5% | 60/242=24.8% | 35/242=14.5% | 237/242=97.9% | 3/242=1.2% |
| Random 0.1 | 0.98±0.04 | 0.029±0.022 | 238/293=81.2% | 0/293=0% | 55/293=18.8% | 293/293=100% | 0/293=0% |
| ISR 0.3 | 0.54±0.38 | 0.216±0.030 | 27/161=16.8% | 0/161=0% | 133/161=82.6% | 145/161=90.1% | 5/161=3.1% |

## H9 audit status

- ISR b01 s44: H9 audited (28-30/35 genuine are H9 conjunction aggregation)
- Random b01 s42: H9 audited in pilot era (100% H9 ex falso)
- **Remaining 7 runs: NO H9 audit** — "Genuine" column may overestimate

## Caveats

1. classify_h7.py only detects H1/H7/H8. H9 (conjunction aggregation, ex falso) is NOT detected.
2. The "Genuine" column = samples not matching H1/H7/H8. True genuine requires additional H9 audit + CI check.
3. S-Gen (strict genuine) = Genuine AND NOT content-independent. Does NOT subtract H9.
4. Random s42 in registry shows H9=100% (from pilot manual audit), but classify_h7.py reports H1=83.9%. Both are correct under different classification scopes.
