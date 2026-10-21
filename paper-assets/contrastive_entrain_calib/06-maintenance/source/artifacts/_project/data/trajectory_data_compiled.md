# D027 Eval Trajectory — Complete Compiled Data

**Compiled**: 2026-05-21
**Eval protocol**: eval_unified_preset.py (D027 standard), n=362 (181 valid + 181 invalid)
**Vanilla baseline (D027)**: SYCONScore=0.1335, ToF=0.0718, NoF=0.9448

---

## Condition 1: R3-only Seed 1 (exp-003)

| Step | SYCONScore | ToF    | NoF    | vs Vanilla% |
|------|-----------|--------|--------|-------------|
| 1000 | 0.0743    | 0.0387 | 0.9448 | −44.3%      |
| 2000 | 0.0846    | 0.0442 | 0.9834 | −36.6%      |
| 3000 | 0.0946    | 0.0497 | 0.9724 | −29.1%      |
| 4000 | 0.1144    | 0.0608 | 0.9669 | −14.3%      |
| 4500 | 0.1337    | 0.0718 | 0.9613 | +0.1%       |
| 5000 | 0.1144    | 0.0608 | 0.9669 | −14.3%      |
| 5500 | 0.1144    | 0.0608 | 0.9724 | −14.3%      |
| 6000 | 0.0846    | 0.0442 | 0.9724 | −36.6%      |
| 6500 | 0.1529    | 0.0829 | 0.9834 | +14.5%      |
| 7000 | 0.1046    | —      | —      | −21.6%      |
| 7500 | 0.1046    | —      | —      | −21.6%      |
| 8000 | PENDING   | —      | —      | —           |

> ckpt-7000/7500: ToF/NoF not recorded in registry (only SYCONScore available).
> ckpt-8000: eval RUNNING as of 2026-05-21.

### Summary Stats (Seed 1, steps 1000–7500, n=11)

| Metric     | SYCONScore |
|------------|-----------|
| Mean       | 0.1070    |
| Max        | 0.1529 (ckpt-6500) |
| Min        | 0.0743 (ckpt-1000) |
| Final      | 0.1046 (ckpt-7500) |
| Peak vs Vanilla | +14.5% |

---

## Condition 2: R3-only Seed 2 (exp-003-s2)

| Step | SYCONScore | ToF    | NoF    | vs Vanilla% |
|------|-----------|--------|--------|-------------|
| 500  | 0.0845    | 0.0442 | 0.9503 | −36.7%      |
| 1000 | 0.0844    | 0.0442 | 0.9448 | −36.8%      |
| 1500 | 0.1044    | 0.0552 | 0.9503 | −21.8%      |
| 2000 | 0.0846    | —      | —      | −36.6%      |
| 2500 | 0.1046    | 0.0552 | 0.9724 | −21.6%      |
| 3000 | 0.0945    | 0.0497 | 0.9503 | −29.2%      |
| 3500 | 0.0744    | 0.0387 | 0.9724 | −44.3%      |

> ckpt-2000: ToF/NoF not recorded in registry.
> exp-003-s2 training still RUNNING — more checkpoints may become available.

### Summary Stats (Seed 2, steps 500–3500, n=7)

| Metric     | SYCONScore |
|------------|-----------|
| Mean       | 0.0902    |
| Max        | 0.1046 (ckpt-2500) |
| Min        | 0.0744 (ckpt-3500) |
| Final      | 0.0744 (ckpt-3500) |
| Peak vs Vanilla | −21.6% |

---

## Condition 3: SFT ACT (exp-004)

| Step | SYCONScore | ToF    | NoF    | vs Vanilla% |
|------|-----------|--------|--------|-------------|
| 1000 | 0.2048    | 0.1160 | 0.8729 | +53.4%      |
| 1500 | 0.1699    | 0.0939 | 0.8895 | +27.3%      |
| 2500 | 0.2389    | 0.1381 | 0.8840 | +78.9%      |
| 3000 | 0.2058    | 0.1160 | 0.9116 | +54.2%      |
| 3500 | 0.2312    | 0.1326 | 0.9006 | +73.2%      |
| 4000 | 0.2140    | 0.1215 | 0.8950 | +60.3%      |
| 4500 | 0.1875    | 0.1050 | 0.8785 | +40.4%      |
| 5000 | 0.2631    | 0.1547 | 0.8785 | +97.1%      |
| 5500 | 0.2383    | 0.1381 | 0.8674 | +78.5%      |
| 6000 | 0.2618    | 0.1547 | 0.8508 | +96.1%      |
| 6500 | 0.2526    | 0.1492 | 0.8232 | +89.1%      |
| 7000 | 0.2858    | 0.1713 | 0.8619 | +114.1%     |
| 7500 | 0.2771    | 0.1657 | 0.8453 | +107.6%     |
| 8000 | 0.3010†   | —      | —      | +125.5%     |

> † ckpt-8000 SYCONScore from parent exp-004 summary (best_sycon_score=0.301). No separate eval entry; ToF/NoF unavailable.
> Missing checkpoints: ckpt-500, ckpt-2000 (no eval experiments registered).

### Summary Stats (SFT ACT, steps 1000–8000, n=14)

| Metric     | SYCONScore |
|------------|-----------|
| Mean       | 0.2380    |
| Max        | 0.3010 (ckpt-8000) |
| Min        | 0.1699 (ckpt-1500) |
| Final      | 0.3010 (ckpt-8000) |
| Peak vs Vanilla | +125.5% |

---

## Cross-seed Comparison: R3-only Seed 1 vs Seed 2

Overlapping evaluation steps (1000, 2000, 3000):

| Step | Seed 1 | Seed 2 | Δ (S2−S1) | Relative Δ |
|------|--------|--------|-----------|------------|
| 1000 | 0.0743 | 0.0844 | +0.0101   | +13.6%     |
| 2000 | 0.0846 | 0.0846 | 0.0000    | 0.0%       |
| 3000 | 0.0946 | 0.0945 | −0.0001   | −0.1%      |

| Summary | Seed 1 (full) | Seed 2 (full) |
|---------|---------------|---------------|
| Mean SYCONScore | 0.1070 | 0.0902 |
| Max SYCONScore  | 0.1529 | 0.1046 |
| Eval range       | 1000–7500 (11 pts) | 500–3500 (7 pts) |
| Ever ≥ Vanilla?  | Yes (ckpt-4500, 6500) | No |

Cross-seed findings:
- At overlapping steps (1000–3000), scores nearly identical (max Δ = 0.01), confirming reproducibility.
- Seed 1 later develops higher variance with a spike at ckpt-6500 (0.1529); seed 2 trajectory not yet evaluated beyond 3500.
- Neither seed consistently exceeds vanilla baseline; R3-only GRPO does not reliably improve SYCONScore.

---

## Data Gaps

| Condition | Missing | Status |
|-----------|---------|--------|
| R3-only Seed 1 | ckpt-8000 eval | RUNNING |
| R3-only Seed 1 | ckpt-7000/7500 ToF/NoF | Not recorded |
| R3-only Seed 2 | ckpt-2000 ToF/NoF | Not recorded |
| R3-only Seed 2 | ckpt ≥ 4000 | Training RUNNING |
| SFT ACT | ckpt-500, ckpt-2000 eval | Not registered |
| SFT ACT | ckpt-8000 ToF/NoF | Not separately evaluated |
