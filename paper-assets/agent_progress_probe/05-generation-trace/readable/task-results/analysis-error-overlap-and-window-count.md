# analysis error overlap and window count

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error-overlap-and-window-count_20260515T032714_result.json`
- **Structured JSON:** [`04e118709f0bcdebfe35.json`](../../sessions/04/04e118709f0bcdebfe35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the definitive summary:

---

```
=== Part 1: Error Overlap (OH Cross-Agent, conf≥2) ===
Test set: N=43,366 common windows (probe ∩ structural)
Probe errors: 8,643 / 43,366 (error rate: 19.9%)
Structural GB errors: 223 / 43,376 (error rate: 0.51%)
Both wrong: 192
Overlap rate: 192 / 8,643 = 2.22%

VERDICT: NEITHER 31/8,643 (0.36%) NOR 358/8,643 (4.14%) is correct.
  - 31 came from GB trained on ALL SWE (54,809 windows), not the canonical
    conf≥2 train split — wrong training setup, inflated F1=0.998
  - 358 came from GB with accidentally changed hyperparams (n=100, lr=0.1)
    in the "fixed" script — produced degraded F1=0.952
  - Canonical: 192/8,643 = 2.22%, using GB(SWE conf≥2 train, n=200,
    lr=0.05, d=5) — the same model that gives 0.9919 cross-agent F1
    and 0.9951 in-domain F1 (both verified from scratch).

=== Part 2: OH conf≥2 Window Count ===
JSONL source: 43,376 conf≥2 windows
Embeddings source: 43,366 conf≥2 windows
Difference: 10 (from 8 trajectories, lost during embedding generation)
Canonical number for paper: 43,376
```

The paper's §6.5 needs to be corrected: structural GB should report 223 errors (consistent with 0.51%), and the overlap should be **192/8,643 = 2.22%**, not 0.36% or 4.14%.

---
