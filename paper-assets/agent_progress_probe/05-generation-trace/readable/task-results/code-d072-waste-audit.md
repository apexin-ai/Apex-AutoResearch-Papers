# code d072 waste audit

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d072-waste-audit_20260515T143232_result.json`
- **Structured JSON:** [`cbb948db18c5e20f1ca3.json`](../../sessions/cb/cbb948db18c5e20f1ca3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Output matches the spec. Results:

- **5,000 SWE-Agent trajectories** analyzed
- **863 (17.3%)** have a stagnation tail (all remaining conf≥2 windows are stagnation from some point onward)
- **Mean tail ratio: 38.5%**, median: 22.0% — among trajectories with stagnation tails, a substantial fraction of compute is wasted
- Distribution is bimodal: most tails are short (10-20% of trajectory) but there's a second peak at 80-100%
- OH data was not available locally; the script will pick it up when run on the server with `--oh_dir /root/autodl-tmp/openhands_data`

Script is at `compute_waste_audit.py`, output at `artifacts/d072/compute_waste_audit.json`.

---
