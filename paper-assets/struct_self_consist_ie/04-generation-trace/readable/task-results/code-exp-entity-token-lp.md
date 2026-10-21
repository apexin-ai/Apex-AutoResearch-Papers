# code exp entity token lp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_entity_token_lp_20260516T055007_result.json`
- **Structured JSON:** [`a79e315d6cf21e981448.json`](../../sessions/a7/a79e315d6cf21e981448.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All steps complete. Summary of the **exp_entity_token_lp** experiment:

**Entity-token LP does not improve sample selection F1.** It is strictly worse than full-sequence LP on both datasets:

| | SciERC | CoNLL |
|---|---|---|
| Greedy F1 | 0.6430 | 0.9065 |
| Full-LP Selection | 0.6465 (+0.35pp) | 0.8989 (-0.76pp) |
| Entity-LP Selection | 0.6262 (-1.68pp) | 0.8659 (-4.06pp) |
| Entity-LP vs Full-LP | **-2.03pp** | **-3.30pp** |

**Why it fails:**
- **CoNLL**: Entity tokens are saturated (logprobs ~0.0), yielding zero discriminative variance (79.4% of instances tied). The model generates entity tokens with near-certainty.
- **SciERC**: Entity-LP has 4x higher within-instance variance than full-LP, but the signal is too noisy — entity tokens are only 5.3% of total tokens, making the mean logprob unstable.

Artifacts registered: `art_20260516_6077d0` (results.json), `art_20260516_d4f4aa` (report.md).

---
