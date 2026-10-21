# ops t10a075 kill d102

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_t10a075-kill-d102_20260522T191455_result.json`
- **Structured JSON:** [`6a414341564e33eec531.json`](../../sessions/6a/6a414341564e33eec531.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All phases complete. Here's the report.

---

## D102 5-Method Analysis — Pythia-1.4B | α=0.75 | seed=42 | T=10 | fp32

### PermG Forward/Reverse (FDR-corrected, n_perm=5000)

| Direction | Sig count |
|-----------|-----------|
| **Forward** | **5/8** |
| **Reverse** | **0/8** |

Forward PermG detail:

| Pair | F-stat | p_raw | p_FDR | Sig |
|------|--------|-------|-------|-----|
| token_entropy→distinct_1 | 2087.73 | 0.0024 | 0.0048 | ✓ |
| token_entropy→distinct_2 | 1009.79 | ~0.002 | ~0.004 | ✓ |
| token_entropy→distinct_3 | 298.80 | — | — | ✗ |
| token_entropy→mauve | N/A | N/A | N/A | ✗ |
| ece→distinct_1 | 4974.46 | ~0.001 | ~0.002 | ✓ |
| ece→distinct_2 | 4005.76 | ~0.001 | ~0.002 | ✓ |
| ece→distinct_3 | 933.93 | ~0.002 | ~0.004 | ✓ |
| ece→mauve | N/A | N/A | N/A | ✗ |

Reverse: all 0 significant (F-stats 2.8–7.4, all p > 0.05)

### K≥3 Consensus (≥3/5 methods agree on forward causation)

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy→distinct_1 | **3/5** | naive, diff, perm |
| token_entropy→distinct_2 | **3/5** | naive, diff, perm |
| token_entropy→distinct_3 | 2/5 | diff, ty |
| token_entropy→mauve | 0/5 | — |
| ece→distinct_1 | **4/5** | naive, diff, perm, ty |
| ece→distinct_2 | **3/5** | naive, diff, perm |
| ece→distinct_3 | **4/5** | naive, diff, perm, ty |
| ece→mauve | 0/5 | — |

**Robust pairs: 5/8**

### Per-method forward significance

| Method | Sig/8 |
|--------|-------|
| PermG (FDR) | 5/8 |
| Diff XCorr (FDR) | 6/8 |
| Threshold Onset | 0/8 |
| TY Granger | 3/8 |

### Drift metrics (gen_0 → gen_10)

| Metric | Gen 0 | Gen 10 | Δ |
|--------|-------|--------|---|
| token_entropy | 2.973 | 1.968 | −1.005 (−33.8%) |
| ece | 0.008 | 0.266 | +0.258 (×32.8) |
| perplexity | 19.83 | 89.37 | +69.54 (×4.5) |
| distinct_1 | 0.099 | 0.081 | −0.019 (−18.7%) |
| distinct_2 | 0.522 | 0.407 | −0.115 (−22.1%) |
| distinct_3 | 0.821 | 0.670 | −0.151 (−18.4%) |
| mauve | null | 0.031 | — |

### KEY DISCRIMINATOR verdict

**1.4B α=0.75 → 5/8** (PermG fwd & K≥3 consensus both 5/8, reverse 0/8).

410M at α=0.75 was 6/8. 1.4B is 5/8 — close but 1 pair below. The 2 failing pairs are both **mauve** pairs (token_entropy→mauve, ece→mauve), where mauve=null at gen_0 truncates the effective series. The 6 distinct_N pairs show 5/6 significant. Directionality is clean: 5/8 forward vs 0/8 reverse.

**Output saved on server:**
- `results/phase_diagram/t10_a075_s42_fp32_14b/analysis/5method_leadlag.json`
- `results/phase_diagram/t10_a075_s42_fp32_14b/analysis/5method_summary.txt`

---
