# code span realignment and gate0

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_span_realignment_and_gate0_20260514T070233_result.json`
- **Structured JSON:** [`112d9c6804afee541281.json`](../../sessions/11/112d9c6804afee541281.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary:

**Part A — Span realignment implementation**: Complete. Added `_find_closest_span` and `realign_spans` to `sampling.py`, integrated into `run_sampling_pipeline` with `realign: bool = True` parameter, and added `--no_realign` flag to `run_mvp_pilot.py`.

**Part B — Server sync & Gate 0 evaluation**: Complete. All 5 Python files synced to `autodl-5090`. Ran realignment evaluation on existing 551 test predictions:

| Metric | Raw | Realigned | Delta |
|--------|-----|-----------|-------|
| NER strict F1 | 11.4% | **60.4%** | **+49.0pp** |
| RE strict F1 | 1.3% | **33.8%** | **+32.6pp** |
| Entity offset accuracy | 16.6% | **100.0%** | |
| Relation offset accuracy | 2.7% | **100.0%** | |

**Gate 0**: NER **PASS** (60.4% >= 56%), RE **FAIL** (33.8% < 40%). The realignment completely solves the offset hallucination problem (100% offset accuracy after fix). RE is close to the 40% threshold — the gap is from the model predicting wrong entity text for relation arguments, not from offset errors. Registry updated with all realigned metrics.

---
