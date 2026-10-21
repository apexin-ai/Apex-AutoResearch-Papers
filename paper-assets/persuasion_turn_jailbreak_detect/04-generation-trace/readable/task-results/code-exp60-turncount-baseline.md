# code exp60 turncount baseline

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp60_turncount_baseline_20260522T164013_result.json`
- **Structured JSON:** [`0b01bf7b8e7da0ff92cc.json`](../../sessions/0b/0b01bf7b8e7da0ff92cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results are in. The findings are **stronger than expected** — turn count has almost zero discriminative power even at full length:

```
=== Turn Count Statistics ===
iid:       jailbreak=8.7±2.1 (5-12), benign=7.9±1.5 (6-10)
dd:        jailbreak=8.1±1.5 (6-10), benign=7.9±1.5 (6-10)  ← almost identical
fitd:      jailbreak=7.8±1.4 (6-10), benign=7.9±1.5 (6-10)  ← almost identical
aa:        jailbreak=5.1±1.7 (3-8),  benign=7.9±1.5 (6-10)
toxicchat: all 1 turn

=== Results ===
Test Set     TC Full    TC K=1     DisPeD Full  DisPeD K=1
--------------------------------------------------------
iid          0.5429     0.0000     1.0000       N/A
dd           0.5581     0.0000     0.9968       N/A
fitd         0.4237     0.0000     1.0000       1.0000
aa           0.0000     0.0000     0.9719       0.7730
toxicchat    0.0000     0.0000     0.5960       0.5960
```

Key takeaways:

1. **Turn counts overlap heavily** between jailbreak and benign for IID/DD/FITD (both ~6-10 user turns). The data was well-constructed to avoid this confound.

2. **Turn-count-only classifier fails across the board**: Full F1 is 0.00–0.56 (not ~1.0 as hypothesized), while DisPeD achieves 0.97–1.0. The gap is massive.

3. **K=1 F1 = 0.0** for all test sets (LR predicts all benign since the intercept drives the decision when all features are identical at 1).

4. **AA inversion**: AA jailbreaks have *fewer* turns (5.1) than benign (7.9), opposite to the training distribution, so the classifier gets 0.0 F1 even at full length.

The original hypothesis assumed "benign 12-20 vs jailbreak 3-10" but the actual data shows near-identical turn counts. This makes the argument even stronger — turn count is **not** a confound at all, and DisPeD's performance is entirely content-driven.

Results saved to `/root/persuasion_turn_jailbreak_detect/results/exp60_turncount_baseline.json`. DisPeD IID/DD K=1 values are marked null — those early detection experiments don't exist yet.

---
