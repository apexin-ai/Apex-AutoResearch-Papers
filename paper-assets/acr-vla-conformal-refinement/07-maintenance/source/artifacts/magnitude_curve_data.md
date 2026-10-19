# Magnitude Curve Data (Figure 2) — LIBERO-Object

> Generated: 2026-05-17

## Reference Baselines

| Model | Seeds | SR per seed | Mean ± SE |
|-------|-------|-------------|-----------|
| VLA-only | seed42=0.12, seed43=0.12, seed44=0.10, seed45=0.09 | 4 seeds | **10.8 ± 0.8%** |
| Argmin (reconvla) | seed43=0.17, seed44=0.13, seed45=0.12, seed46=0.10, seed47=0.10 | 5 seeds | **12.4 ± 1.3%** |
| OpenVLA seed42-v2 | seed42=0.69 | 1 seed | 69% (upper ref) |

---

## obs_only CRM — Magnitude Curve

| ε (norm cap) | Seed42 | Seed43 | Seed44 | Seed45 | Seed46 | Seed47 | N seeds | Mean ± SE |
|---|---|---|---|---|---|---|---|---|
| 0.03 | 0.16 | — | — | — | — | — | 1 | 16.0% |
| 0.05 | 0.13 | — | — | — | — | — | 1 | 13.0% |
| 0.10 | 0.19 | 0.12† | 0.16 | — | — | — | 3 | **15.7 ± 2.0%** |
| 0.20 | 0.22 | 0.16 | 0.16 | 0.16 | 0.15 | 0.20 | 6 | **17.5 ± 1.2%** |
| 0.30 | 0.19 | — | 0.18 | 0.14 | — | — | 3 | **17.0 ± 1.5%** |
| default (~1.42) | 0.17 | — | 0.16 | 0.12 | — | — | 3 | **15.0 ± 1.5%** |

† eval-obs-only-object-seed43 conclusion=negative (SR dropped vs seed42), but data is valid.

### Source Experiments (obs_only)

| ε | Experiment Name | Seed | SR |
|---|---|---|---|
| 0.03 | eval-mag-obsonly-norm003-object | 42 | 0.16 |
| 0.05 | eval-mag-obsonly-norm005-object | 42 | 0.13 |
| 0.10 | eval-acr-object-v4-obs-only | 42 | 0.19 |
| 0.10 | eval-obs-only-object-seed43 | 43 | 0.12 |
| 0.10 | eval-obs-only-object-norm01-seed44 | 44 | 0.16 |
| 0.20 | eval-acr-object-obs-only-norm02 | 42 | 0.22 |
| 0.20 | eval-obs-only-object-norm02-seed43-r2 | 43 | 0.16 |
| 0.20 | eval-obs-only-object-norm02-seed44-r2 | 44 | 0.16 |
| 0.20 | eval-obs-only-object-norm02-seed45 | 45 | 0.16 |
| 0.20 | eval-obs-only-object-norm02-seed46 | 46 | 0.15 |
| 0.20 | eval-obs-only-object-norm02-seed47 | 47 | 0.20 |
| 0.30 | eval-mag-obsonly-norm03-object | 42 | 0.19 |
| 0.30 | eval-obs-only-object-norm03-seed44 | 44 | 0.18 |
| 0.30 | eval-obs-only-object-norm03-seed45-r2 | 45 | 0.14 |
| default | eval-acr-object-obs-only-default | 42 | 0.17 |
| default | eval-obs-only-object-default-seed44 | 44 | 0.16 |
| default | eval-obs-only-object-default-seed45 | 45 | 0.12 |

---

## perdof CRM — Magnitude Curve

| ε (norm cap) | Seed42 | Seed43 | Seed44 | Seed45 | Seed46 | Seed47 | N seeds | Mean ± SE |
|---|---|---|---|---|---|---|---|---|
| 0.03 | 0.14 | — | �� | — | — | — | 1 | 14.0% |
| 0.05 | 0.14 | — | — | — | — | — | 1 | 14.0% |
| 0.10 | 0.11 | 0.12 | 0.08 | 0.11 | 0.10 | — | 5 | **10.4 ± 0.7%** |
| 0.20 | 0.11 | 0.09 | 0.10 | 0.09 | — | — | 4 | **9.8 ± 0.5%** |
| 0.30 | 0.04 | — | 0.04 | 0.06 | — | — | 3 | **4.7 ± 0.7%** |
| default (~1.42) | 0.00 | — | 0.00 | — | — | — | 2 | **0.0 ± 0.0%** |

### Source Experiments (perdof)

| ε | Experiment Name | Seed | SR |
|---|---|---|---|
| 0.03 | eval-mag-perdof-norm003-object | 42 | 0.14 |
| 0.05 | eval-mag-perdof-norm005-object | 42 | 0.14 |
| 0.10 | eval-acr-object-v4-perdof | 42 | 0.11 |
| 0.10 | eval-perdof-object-seed43 | 43 | 0.12 |
| 0.10 | eval-perdof-object-norm01-seed44 / eval-perdof-object-seed44 | 44 | 0.08 |
| 0.10 | eval-perdof-object-norm01-seed45 | 45 | 0.11 |
| 0.10 | eval-perdof-object-norm01-seed46-r2 | 46 | 0.10 |
| 0.20 | eval-mag-perdof-norm02-object | 42 | 0.11 |
| 0.20 | eval-mag-perdof-norm02-seed43-object-r3 | 43 | 0.09 |
| 0.20 | eval-perdof-object-norm02-seed44 | 44 | 0.10 |
| 0.20 | eval-perdof-object-norm02-seed45 | 45 | 0.09 |
| 0.30 | eval-mag-perdof-norm03-object-r3 | 42 | 0.04 |
| 0.30 | eval-perdof-object-norm03-seed44 | 44 | 0.04 |
| 0.30 | eval-perdof-object-norm03-seed45-r2 | 45 | 0.06 |
| default | perdof seed42 (referenced in seed44 hyp) | 42 | 0.00 |
| default | eval-perdof-object-default-seed44 | 44 | 0.00 |

---

## Coverage Summary

| Model | ε=0.03 | ε=0.05 | ε=0.10 | ε=0.20 | ε=0.30 | default |
|-------|--------|--------|--------|--------|--------|---------|
| obs_only | 1 | 1 | 3 | **6** | 3 | 3 |
| perdof | 1 | 1 | **5** | 4 | 3 | 2 |

**Minimum target: 3 seeds per (model, ε).**

---

## Gap Identification — Missing Seeds (< 3)

| Model | ε | Current N | Gap |
|-------|---|-----------|-----|
| obs_only | 0.03 | 1 | needs 2 more seeds |
| obs_only | 0.05 | 1 | needs 2 more seeds |
| perdof | 0.03 | 1 | needs 2 more seeds |
| perdof | 0.05 | 1 | needs 2 more seeds |
| perdof | default | 2 | needs 1 more seed |

---

## Currently RUNNING Experiments (gap-filling)

| Experiment | Model | ε | Seed | Fills gap? |
|---|---|---|---|---|
| eval-obs-only-object-norm005-seed43-r2 | obs_only | 0.05 | 43 | YES (0.05 → 2/3) |
| mag_obs_only_norm01_seed46 | obs_only | 0.10 | 46 | no (already ≥3) |
| mag_obs_only_norm01_seed47 | obs_only | 0.10 | 47 | no (already ≥3) |
| eval-obs-only-object-norm03-seed46 | obs_only | 0.30 | 46 | no (already ≥3) |
| eval-obs-only-object-default-seed46 | obs_only | default | 46 | no (already ≥3) |
| eval-perdof-object-norm02-seed43-r3 | perdof | 0.20 | 43 | no (already ≥3) |
| eval-perdof-object-norm02-seed46 | perdof | 0.20 | 46 | no (already ≥3) |
| eval-perdof-object-norm02-seed47 | perdof | 0.20 | 47 | no (already ≥3) |
| eval-perdof-object-norm01-seed47-bjb1 | perdof | 0.10 | 47 | no (already ≥3) |
| eval-perdof-object-default-seed46 | perdof | default | 46 | YES (default → 3/3) |

---

## Remaining Unfilled Gaps (no RUNNING experiment)

| Model | ε | Still need |
|-------|---|-----------|
| obs_only | 0.03 | 2 seeds |
| obs_only | 0.05 | 1 seed (after running seed43 finishes) |
| perdof | 0.03 | 2 seeds |
| perdof | 0.05 | 2 seeds |

---

## Key Takeaways for Figure 2

1. **obs_only shows flat/robust curve**: 13–17.5% across all ε, no collapse even at default (~1.42)
2. **perdof shows progressive collapse**: 14% at ε=0.05 → 10% at ε=0.1 → 4.7% at ε=0.3 → 0% at default
3. **Crossover point**: obs_only surpasses perdof starting at ε≈0.1, gap widens monotonically
4. **Statistical quality**: ε=0.10 and ε=0.20 have ≥3 seeds for both models (good). ε=0.03/0.05 only have 1 seed each (weaker but still plottable as individual points)
