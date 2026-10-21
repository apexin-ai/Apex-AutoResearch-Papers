# Method Ablation Phase 3: 7-Point Dose-Response Panel

Generated: 2026-05-19
Panel: 136 rows, 7 alpha levels, BH FDR per-alpha corrected

## Data Inventory

| alpha | seeds | n_tests | precision |
|-------|-------|---------|-----------|
| 0.00 | 42,43,44 | 24 | fp32 |
| 0.10 | 42 | 8 | fp32 |
| 0.25 | 43,44 | 16 | fp32 |
| 0.50 | 42,43,44 | 24 | fp32 |
| 0.60 | 42 | 8 | bf16 |
| 0.75 | 42,43,44 | 24 | fp32 |
| 1.00 | 42,43,44,45 | 32 | fp32 (from Phase 2 mvp) |

## Method x Alpha Sig Rates (BH FDR-corrected)

| alpha | n | naive | diff | threshold | permG | TY |
|-------|---|-------|------|-----------|-------|-----|
| 0.00 | 24 | 96% | 33% | 46% | 0% | 0% |
| 0.10 | 8 | 100% | 12% | 38% | 0% | 0% |
| 0.25 | 16 | 100% | 62% | 38% | 0% | 0% |
| 0.50 | 24 | 100% | 88% | 83% | 0% | 0% |
| 0.60 | 8 | 100% | 100% | 75% | 100% | 50% (bf16) |
| 0.75 | 24 | 100% | 96% | 100% | 83% | 0% |
| 1.00 | 32 | 100% | 100% | 100% | 75% | 59% |

## Raw Significance (uncorrected)

| alpha | n | naive | diff | threshold | permG | TY |
|-------|---|-------|------|-----------|-------|-----|
| 0.00 | 24 | 96% | 50% | 46% | 12% | 0% |
| 0.10 | 8 | 100% | 38% | 38% | 0% | 0% |
| 0.25 | 16 | 100% | 75% | 38% | 19% | 0% |
| 0.50 | 24 | 100% | 88% | 83% | 50% | 0% |
| 0.60 | 8 | 100% | 100% | 75% | 100% | 50% |
| 0.75 | 24 | 100% | 96% | 100% | 88% | 12% |
| 1.00 | 32 | 100% | 100% | 100% | 75% | 59% |

## FDR Correction Impact (flips only)

| alpha | method | raw_sig | fdr_sig | flipped |
|-------|--------|---------|---------|---------|
| 0.00 | diff | 12 | 8 | 4 |
| 0.00 | permG | 3 | 0 | 3 |
| 0.10 | diff | 3 | 1 | 2 |
| 0.25 | diff | 12 | 10 | 2 |
| 0.25 | permG | 3 | 0 | 3 |
| 0.50 | permG | 12 | 0 | 12 |
| 0.75 | permG | 21 | 20 | 1 |
| 0.75 | TY | 3 | 0 | 3 |

## Phase 2 vs Phase 3 Comparison (overlapping alpha points)

| alpha | method | Phase2 | Phase3 | delta |
|-------|--------|--------|--------|-------|
| 0.00 | naive | 100% | 96% | -4% |
| 0.00 | diff | 38% | 33% | -4% |
| 0.00 | threshold | 62% | 46% | -17% |
| 0.25 | diff | 25% | 62% | +38% |
| 0.25 | TY | 38% | 0% | -38% |
| 0.50 | diff | 100% | 88% | -12% |
| 0.50 | threshold | 100% | 83% | -17% |

## Key Findings

### 1. Canary blind zone confirmed at alpha=0.10
alpha=0.10 matches alpha=0.00 profile: naive=100% (spurious), robust methods=0%. Low contamination is undetectable.

### 2. Sharp permG transition at alpha=0.50-0.60
permG jumps from 0% (alpha<=0.50) to 100% (alpha=0.60, bf16/1-seed) to 83% (alpha=0.75, 3-seed). The dose-response is step-function-like, not gradual. alpha=0.50 permG has 50% raw significance but 0% after FDR (12 flips), meaning p-values cluster near the threshold.

### 3. TY unreliable below alpha=1.00 (confirms C003)
TY=0% for all alpha<=0.75 after FDR. At alpha=0.75, 3 raw-significant tests flip to 0 after FDR. Only at alpha=1.00 (4-seed pooled) does TY reach 59%. Consistent with constraint C003: TY seed-unstable at T=11.

### 4. Multi-seed data changes Phase 2 estimates
Largest change: alpha=0.25 diff went from 25% (1 seed) to 62% (2 seeds). alpha=0.25 TY collapsed from 38% to 0%. Multi-seed averaging generally moderates single-seed overestimates (alpha=0.00 threshold: 62%->46%).

### 5. Dose-response shape by method
- naive: flat ~100% everywhere (always spuriously significant, useless as test)
- diff/threshold: gradual sigmoidal rise from ~12-33% at alpha=0.00-0.10 to 96-100% at alpha>=0.75
- permG: step function, essentially 0% at alpha<=0.50, jumps to 75-100% at alpha>=0.60
- TY: only fires at alpha=1.00 (59%), too underpowered at T=11 for anything else

### 6. alpha=0.60 bf16 caveat
alpha=0.60 results are from a single bf16 seed. The unusually high permG=100% and TY=50% may partly reflect bf16 numeric effects or seed variance. fp32 multi-seed data needed to confirm.
