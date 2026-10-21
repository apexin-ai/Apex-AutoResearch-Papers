# run frontier sc gpt55

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_frontier_sc_gpt55_20260521T044801_result.json`
- **Structured JSON:** [`6c4dd59653637551e1ec.json`](../../sessions/6c/6c4dd59653637551e1ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment running stably. 8/200 instances done in 301s (avg 37.6s/instance). ETA ~2 hours.

**Status summary:**
- Script: `code/run_frontier_sc.py` on autodl-5090-c
- PID: 282842
- Log: `logs/frontier_sc_gpt55_fewnerd.log`
- Checkpoint: `output/frontier_sc_gpt55_fewnerd/checkpoint.jsonl` (allows resume)
- Registry: `exp_frontier_sc_gpt55_fewnerd_v2` → RUNNING

**Key findings from first 8 instances:**
| # | greedy | mv | oracle | agree | degen |
|---|--------|-----|--------|-------|-------|
| 1 | 0.800 | 0.800 | 0.889 | 0.878 | N |
| 2 | 0.000 | 0.000 | 0.000 | 1.000 | Y |
| 3 | 0.000 | 0.000 | 0.000 | 1.000 | Y |
| 4 | 0.500 | 1.000 | 1.000 | 0.643 | N |
| 5 | 1.000 | 1.000 | 1.000 | 1.000 | Y |
| 6 | 0.667 | 0.500 | 0.667 | 0.786 | N |
| 7 | 0.400 | 0.400 | 0.500 | 0.857 | N |
| 8 | 0.824 | 0.824 | 0.824 | 1.000 | Y |

**Early observations:**
- High degeneracy rate (4/8 = 50%)
- Instance 4: clear SC benefit (greedy=0.5 → mv=1.0)
- Instance 6: SC hurts (greedy=0.667 → mv=0.500) — correlation-selection gap confirmed
- Oracle > MV in non-degenerate cases → selection gap exists in frontier model
- Instances 2&3: type taxonomy mismatch (model uses different entity types than FewNERD gold)

**Technical notes:**
- GPT-5.5 uses ~1024 reasoning tokens internally → max_tokens=4096 needed
- ~22s per API call, 4 parallel workers → ~35s per instance
- Offset correction applied (API models produce wrong char offsets)
- Checkpoint enables resume on API credit exhaustion

---
