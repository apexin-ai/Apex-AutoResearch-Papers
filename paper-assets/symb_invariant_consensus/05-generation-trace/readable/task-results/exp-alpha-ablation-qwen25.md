# exp alpha ablation qwen25

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_alpha-ablation-qwen25_20260523T194840_result.json`
- **Structured JSON:** [`08477f8ba06092fa4da1.json`](../../sessions/08/08477f8ba06092fa4da1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. 28 problems have different scores between α=0 and α=1, but the score differences (1-4 points) never change the winning answer. This confirms α is robust.

## Qwen2.5-14B FOLIO (n=204, seed=123)

| α | SICA (%) | SC (%) | Δ (pp) | McNemar p | count-only (%) | SICA=SC agree (%) |
|---|----------|--------|--------|-----------|----------------|-------------------|
| 0.0 | 73.04 | 74.51 | -1.47 | 0.3750 | 74.51 | 97.5 |
| 1.0 | 73.04 | 74.51 | -1.47 | 0.3750 | 74.51 | 97.5 |

**Key findings:**
- α=0 and α=1 produce **identical** final answers for all 204 problems
- 176/204 problems have 0 excluded constraints (α irrelevant by definition)
- 28 problems have 1-5 excluded constraints, but the score perturbation (1-4 pts) never flips the winner
- No division-by-zero or anomalous behavior at α=0
- SICA≠SC on 5 problems (all gt=Unknown): folio_7 SICA correct, folio_{30,96,130,151} SC correct
- McNemar discordant pair: b=1, c=4 → p=0.375 (not significant)

Results saved to `/root/symb_invariant_consensus/results/alpha_ablation/Qwen25-14B_FOLIO_alpha_endpoints.json`.

---
