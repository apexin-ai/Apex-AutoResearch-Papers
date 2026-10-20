# research literature scan

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan_20260515T043905_result.json`
- **Structured JSON:** [`fd5bc10fc01bc187d161.json`](../../sessions/fd/fd5bc10fc01bc187d161.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Scan complete.

**Results summary**: 14+ searches across 4 directions (delusional value estimation, temporal abstraction + dt embedding, DreamerV3/TD-MPC critic pathology, critic diagnostics). Found 6 new papers not in the existing scan, added to `artifacts/literature_scan_20260515.md`.

**No novelty threat.** No paper reports the specific causal chain: trained dt_embedding → pathological value overestimation (nve>1.5x) → stochastic collapse in imagination-based MBRL. The closest work (TAWM, ICML 2025) reaches the *opposite* conclusion — Δt conditioning is *beneficial* in MPC — which actually strengthens our novelty.

**New citations to add to paper**:
1. **TD-M(PC)²** (NeurIPS 2025) — value overestimation in TD-MPC2 from policy mismatch; different mechanism, same symptom
2. **"On Training in Imagination"** (arXiv 2025) — theoretical framework predicting systematic bias (like ours) is problematic in imagination training

---
