# ops check exp progress 0521b

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_exp_progress_0521b_20260521T024825_result.json`
- **Structured JSON:** [`7adb7b4557e33a3991e2.json`](../../sessions/7a/7adb7b4557e33a3991e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the full report:

---

```
exp_013: Gen 8/10 [RUNNING] — pure_collapse, seed=44
```

Gen 0-7 complete. Currently generating 50000 synthetic samples for Gen 8 (was at 14720/50000).

| Gen | eff_rank | log_det | ppl | distinct4 | train_loss |
|-----|----------|---------|-----|-----------|------------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7305 | — |
| 1 | 490.77 | 2459.40 | 11.36 | 0.6019 | 1.6255 |
| 2 | 495.83 | 2467.38 | 13.54 | 0.4943 | 1.2333 |
| 3 | 493.45 | 2442.40 | 16.22 | 0.4283 | 1.0236 |
| 4 | 488.35 | 2408.35 | 19.97 | 0.3731 | 0.9047 |
| 5 | 480.04 | 2362.67 | 24.30 | 0.3569 | 0.8166 |
| 6 | 472.30 | 2318.17 | 30.21 | 0.3326 | 0.7677 |
| 7 | 463.93 | 2283.98 | 37.14 | 0.2862 | 0.7125 |

Pace: ~2.6 hours/gen. **ETA completion: ~May 21 18:30 CST** (3 gens remaining).

Clear collapse pattern: log_det peaks at Gen 2 (2467.38) then monotonically declines; eff_rank peaks at Gen 2 (495.83) then declines; ppl steadily increases 4x (9.55→37.14); distinct4 drops from 0.73 → 0.29.

---

```
exp_014: Gen 3/10 [RUNNING] — fixed_mix r=0.25, seed=43
```

Gen 0-2 complete. Currently generating 37500 synthetic samples for Gen 3 (at 6400/37500).

| Gen | eff_rank | log_det | ppl | distinct4 | train_loss |
|-----|----------|---------|-----|-----------|------------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7415 | — |
| 1 | 475.66 | 2365.35 | 10.23 | 0.6584 | 1.8020 |
| 2 | 483.00 | 2362.54 | 10.65 | 0.5574 | 1.7222 |

Pace: ~1.75 hours/gen. **ETA completion: ~May 22 01:00 CST** (8 gens remaining).

### Gen 2 EMA violation analysis (α=0.5)

```
S̃_0 = 2366.68
S̃_1 = 0.5 × 2365.35 + 0.5 × 2366.68 = 2366.02
S̃_2 = 0.5 × 2362.54 + 0.5 × 2366.02 = 2364.28

Δ(S̃_1 → S̃_2) = 2364.28 − 2366.02 = −1.74  ← VIOLATION
```

**Yes, exp_014 violates non-decreasing at Gen 2**, and the violation is **larger** than exp_009 seed42:

| Experiment | S̃_1 | S̃_2 | Δ | Violation |
|-----------|------|------|---|-----------|
| exp_009 (pure, seed42) | 2364.4 | 2363.8 | −0.6 | mild |
| exp_014 (mix25%, seed43) | 2366.0 | 2364.3 | −1.7 | ~3x worse |

Notably, exp_014's raw log_det is monotonically decreasing from Gen 0 (2366.68 → 2365.35 → 2362.54), unlike exp_013 (pure collapse) which **first inflates** to 2467 at Gen 2 before collapsing. The 25% real data mixing prevents the initial spectral inflation but doesn't prevent the eventual decline — it just starts the slide immediately.

---
