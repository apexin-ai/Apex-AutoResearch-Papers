# code d072 early termination

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d072-early-termination_20260515T143303_result.json`
- **Structured JSON:** [`5541a7a4f60266c5792d.json`](../../sessions/55/5541a7a4f60266c5792d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Script syntax is valid and `--help` works. The script:

- Loads SWE windows and trains 3-LF GB (canonical HP) and 2-LF RF on conf≥2
- Loads OH conf≥2 windows for cross-agent evaluation
- Groups OH windows by trajectory, sorted by window_idx
- Simulates k-consecutive-stagnation termination policy for k ∈ {1,2,3,5,7,10}
- Computes precision, recall, compute_saved, false_termination_rate for 4 models (3lf_gb, 2lf_rf, oracle, random)
- Outputs to `artifacts/d072/early_termination_sim.json`

---
