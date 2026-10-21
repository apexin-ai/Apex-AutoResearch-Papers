# fix hidden probe entity matching

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_hidden_probe_entity_matching_20260518T111442_result.json`
- **Structured JSON:** [`de4bce8c2e35af5412ce.json`](../../sessions/de/de4bce8c2e35af5412ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

**Fix applied**: `entity_set` now uses `(e["text"], e["type"])` at line 40 of `code/probe/hidden_state_probe.py`. Labels recomputed with text-based matching. MLP needed `OMP_NUM_THREADS=4` to avoid being killed.

**Greedy F1 = 0.6099**, not the expected 0.645. The fix IS effective (span-based was 0.6094, now 0.6099 text-based) — the two methods rarely disagree on this data. The 0.645 discrepancy is NOT about span vs text matching. Verified:

| Metric | Value |
|--------|-------|
| Micro F1 (text-based) | 0.6252 |
| Micro F1 (span-based) | 0.6243 |
| Macro F1 (text-based, 529 nonempty) | 0.6099 |

Even micro-average only reaches 0.625. The 0.645 likely comes from a different evaluation path or dataset split than the probe's `samples_with_logprobs.jsonl`.

---

**Text-based (text, type) matching — gold-filtered 529 instances:**

| Method | Spearman ρ | Selection F1 | Gap Closure |
|--------|-----------|-------------|-------------|
| Greedy | — | 0.6099 | — |
| LP | 0.2214 | 0.6087 | -0.7% |
| Hidden Linear | 0.2327±0.0212 | 0.6199 | 6.3% |
| Hidden MLP | 0.4535±0.0081 | 0.6348 | 15.6% |
| Oracle | — | 0.7692 | 100% |

Results saved to `output/hidden_state_probe/results_textbased_goldfiltered.json`.

---
