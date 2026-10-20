# Vanilla Recovery Eval: Per-Operator Breakdown

Source: `eval_results/v4_vanilla_recovery_eval.json` (seed=42, 47 episodes)

## Vanilla Per-Operator Recovery

| Operator | Recovered | Total | Rate |
|----------|-----------|-------|------|
| C1_context_truncation | 9 | 12 | 75.0% |
| C4_observation_masking | 6 | 11 | 54.5% |
| P1_step_order_swap | 7 | 12 | 58.3% |
| P2_sub_goal_deletion | 7 | 12 | 58.3% |
| **Overall** | **29** | **47** | **61.7%** |

## TaxEI Per-Operator Recovery (known, from v4-taxei-recovery-eval)

| Operator | Recovered | Total | Rate |
|----------|-----------|-------|------|
| C1_context_truncation | 8 | 12 | 66.7% |
| C4_observation_masking | 7 | 11 | 63.6% |
| P1_step_order_swap | 7 | 12 | 58.3% |
| P2_sub_goal_deletion | 6 | 12 | 50.0% |
| **Overall** | **28** | **47** | **59.6%** |

## Delta Table (TaxEI - Vanilla)

| Operator | Vanilla | TaxEI | Delta (pp) | Fig 2 Claimed | Match? |
|----------|---------|-------|------------|---------------|--------|
| C1_context_truncation | 75.0% | 66.7% | **-8.3** | -5.6 | NO |
| C4_observation_masking | 54.5% | 63.6% | **+9.1** | +6.1 | NO |
| P1_step_order_swap | 58.3% | 58.3% | **0.0** | -2.7 | NO |
| P2_sub_goal_deletion | 58.3% | 50.0% | **-8.3** | -8.4 | ~YES (rounding) |

## Fig 2 Delta Verification

**3 of 4 deltas are INCORRECT in Fig 2:**

1. **C1**: Fig 2 claims -5.6pp, actual is -8.3pp (off by 2.7pp)
2. **C4**: Fig 2 claims +6.1pp, actual is +9.1pp (off by 3.0pp)
3. **P1**: Fig 2 claims -2.7pp, actual is 0.0pp (off by 2.7pp)
4. **P2**: Fig 2 claims -8.4pp, actual is -8.3pp (off by 0.1pp — acceptable rounding)

Directional patterns are preserved (C4 is the only positive delta, C1/P2 are negative), but magnitudes are wrong. P1 direction is also wrong (claimed negative, actually zero).

**Possible explanation**: Fig 2 may have used a different run (different seed or r2) for either vanilla or TaxEI baseline. The r2 TaxEI eval has identical per-operator numbers to r1, so the discrepancy is not from TaxEI side.
