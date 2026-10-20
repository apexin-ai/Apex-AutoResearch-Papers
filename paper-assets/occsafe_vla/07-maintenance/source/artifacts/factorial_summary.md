# v2 Factorial Study Summary

> Generated: 2026-05-27 | Source: experiment registry (status=DONE, conclusion=success)

## 2×2 Factorial: gradient_flow (ON/OFF) × norm_type (BN/LN) + Vanilla Baseline

| Cell | Condition | n | CAR mean±std | TSR mean±std | vs Vanilla |
|------|-----------|---|-------------|-------------|------------|
| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.725±0.064 | 0.854±0.052 | -2.0pp |
| 2 | Full OCC LN (Grad ON + LN) | 1 | 0.740 | 0.842 | -0.5pp |
| 3 | Detach BN (Grad OFF + BN) | 4 | 0.767±0.024 | 0.908±0.026 | +2.2pp |
| 4 | Detach LN (Grad OFF + LN) | 1 | 0.802 | 0.886 | +5.7pp |
| — | Vanilla (no OCC) | 3 | 0.745±0.024 | 0.878±0.032 | baseline |

## Per-Cell Data Points

### Cell 1: Full OCC BN (Grad ON + BN)

| exp_id | seed | CAR | TSR |
|--------|------|-----|-----|
| full_occ_retrain_s0_eval_v2 | 42 | 0.746 | 0.802 |
| full_occ_bn_v2_s1_eval | 43 | 0.654 | 0.854 |
| mvp_occ_s3_v2_eval | 45 | 0.776 | 0.906 |

High variance (std=0.064) driven by s1 outlier (CAR=0.654).

### Cell 2: Full OCC LN (Grad ON + LN)

| exp_id | seed | CAR | TSR |
|--------|------|-----|-----|
| full_occ_ln_s3_v2_eval | 45 | 0.740 | 0.842 |

n=1 only. full_occ_ln_s4 blocked on GPU (10894 hardware failure).

### Cell 3: Detach BN (Grad OFF + BN)

| exp_id | seed | CAR | TSR |
|--------|------|-----|-----|
| detach_bn_v2_s0_eval | 42 | 0.774 | 0.870 |
| detach_bn_v2_s1_eval | 43 | 0.736 | 0.926 |
| detach_bn_v2_s2_eval | 44 | 0.762 | 0.914 |
| ablation_occ_detach_s3_v2_eval | 45 | 0.794 | 0.922 |

### Cell 4: Detach LN (Grad OFF + LN)

| exp_id | seed | CAR | TSR |
|--------|------|-----|-----|
| detach_ln_s3_eval | 45 | 0.802 | 0.886 |

n=1 only. detach_ln_v2_s1_35 and detach_ln_s4 training on 34685.

### Vanilla

| exp_id | seed | CAR | TSR |
|--------|------|-----|-----|
| vanilla_retrain_s0_eval | 42 | 0.768 | 0.882 |
| vanilla_v2_s1_eval | 43 | 0.748 | 0.908 |
| vanilla_v2_s2_eval | 44 | 0.720 | 0.844 |

vanilla_retrain_s0_eval (created 2026-05-24) included per ROADMAP D063. Vanilla has no OCC code, so v1/v2 distinction does not apply.

## v2 Filtering Criteria

Included as v2:
- exp_id containing "v2" (detach_bn_v2_s0_eval, full_occ_bn_v2_s1_eval, etc.)
- exp_id containing "_s3_v2" (full_occ_ln_s3_v2_eval, ablation_occ_detach_s3_v2_eval)
- detach_ln_s3_eval: hypothesis states "v2 code", created 2026-05-26
- vanilla_retrain_s0_eval: Vanilla has no OCC head, v1/v2 irrelevant

Excluded v1:
- occ_s1_fresh / occ_s1_fresh_eval_* (v1 Full OCC BN)
- ablation_occ_detach_s0/s1/s2 (v1 Detach BN)
- full_occ_ln_s0_eval (v1, created 2026-05-24 before v2 rebuild)
- detach_ln_s0/s1/s2_eval (v1, created 2026-05-24)
- mvp_vanilla_s0/s1/s2 (v1 Vanilla)
- ablation_occ_detach_s0_retrain_eval (retrain for gradient analysis, not v2 rebuild)

## ROADMAP Consistency Check

| Field | ROADMAP | Registry | Match |
|-------|---------|----------|-------|
| Cell 1 n=3, CAR=0.725±0.064 | ✓ | 0.725±0.064 | ✅ |
| Cell 2 n=1, CAR=0.740 | ✓ | 0.740 | ✅ |
| Cell 3 n=4, CAR=0.767±0.024 | ✓ | 0.767±0.024 | ✅ |
| Cell 4 n=1, CAR=0.802 | ✓ | 0.802 | ✅ |
| Vanilla n=3, CAR=0.745±0.024 | ✓ | 0.745±0.024 | ✅ |

**All entries consistent. No discrepancies.**

## Pending Experiments (on 34685)

| GPU | Training | Target Cell | Will become |
|-----|----------|-------------|-------------|
| 34685:0 | detach_ln_v2_s1_35 | Cell 4 | n=2 |
| 34685:1 | detach_ln_s4 | Cell 4 | n=3 |
| 34685:2 | ablation_occ_detach_s4 | Cell 3 | n=5 |
| 34685:3 | mvp_occ_s4 | Cell 1 | n=4 |
