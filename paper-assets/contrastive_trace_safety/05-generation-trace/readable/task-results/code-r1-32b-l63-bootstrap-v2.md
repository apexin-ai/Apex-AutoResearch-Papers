# code r1 32b l63 bootstrap v2

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r1_32b_l63_bootstrap_v2_20260517T143538_result.json`
- **Structured JSON:** [`56d701bb13af297cb7dd.json`](../../sessions/56/56d701bb13af297cb7dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results complete. Here's the summary:

## R1-32B Layer 63 HS vs Text Bootstrap v2 (null-centered p-values)

| W | BalAcc D | p | Prec D | p | FPR D | p | Bonf |
|---|---------|-----|--------|-----|-------|-----|------|
| 1 | +18.7pp | **0.000** | +15.4pp | **0.000** | -14.6pp | **0.007** | **3/3** |
| 3 | +11.2pp | 0.020 | +13.0pp | 0.032 | -11.4pp | 0.077 | 0/3 |
| 5 | +9.7pp | 0.046 | +13.1pp | 0.061 | -7.7pp | 0.274 | 0/3 |
| 10 | +4.3pp | 0.384 | +9.4pp | 0.241 | -5.4pp | 0.491 | 0/3 |
| 15 | +7.8pp | 0.075 | +11.2pp | 0.130 | -7.8pp | 0.344 | 0/3 |

**Bonferroni threshold = 0.0167**

- **W=1: 3/3 Bonferroni pass** (all three metrics significant)
- W=3-15: 0/3 (nominally significant for some, but not after Bonferroni)
- **Position baseline accuracy: 0.6842**

One CI/p inconsistency at W=5 precision (CI excludes 0 but p=0.061). This is expected: the percentile CI comes from the raw bootstrap distribution while the p-value is from the null-centered test, which is more conservative.

Compared to v1 (non-null-centered), the null-centered p-values are uniformly larger. W=1 remains strongly significant; W=3 dropped from Bonf 2/3 to 0/3.

Results saved to `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_r1_32b_l63_bootstrap_v2/results.json` (316 lines, all 5 windows + position baseline).

---
