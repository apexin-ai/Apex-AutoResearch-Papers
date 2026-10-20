# experiment e7 probe oh gold

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_e7-probe-oh-gold_20260515T141437_result.json`
- **Structured JSON:** [`cd5b222acba9c3539d99.json`](../../sessions/cd/cd5b222acba9c3539d99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Bottom line:** OH gold windows DO have embeddings (158/169 covered), but both probes essentially fail on OH — they predict almost everything as progress, achieving macro-F1 ≈ 0.48. This is due to (a) training only on SWE data and (b) OH having fundamentally different stagnation patterns. The 5 OH stagnation windows in the gold set are too few for reliable evaluation anyway. For the paper, probe results should be reported on SWE-only gold or clearly caveated when including OH.

---
