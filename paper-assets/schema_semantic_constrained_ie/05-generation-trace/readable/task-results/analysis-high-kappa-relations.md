# analysis high kappa relations

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_high-kappa-relations_20260522T141222_result.json`
- **Structured JSON:** [`124ae6dffad073ea2b3e.json`](../../sessions/12/124ae6dffad073ea2b3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Output written to `artifacts/_project/paper/appendix_high_kappa_analysis.tex`.

**Summary of findings:**

- **SciERC**: All 7 relations have α ≥ 0.67 (range 0.67–0.83) — the small schema (7 rels × 6 entity types) makes every relation ambiguous. Exclusion analysis is vacuous, but OntoCoDec still achieves DR 15.4%→0.9% (Qwen), 13.3%→0.08% (Llama).

- **DocRED**: Only 12/96 relations have α ≥ 0.36, covering just 3.8% of gold triples. The highest-ambiguity relations (sister city, basin country, mouth of watercourse, all α=0.42) share the single valid pair LOC→LOC with 40 other relations. These relations have much higher unconstrained DR (43.8% vs 29.9%) but converge under S1 constraints for Llama (3.2% vs 2.5%).

- **Excluding high-α relations** barely changes overall DR: 2.55%→2.51% (Llama), 10.21%→9.53% (Qwen) — their small gold footprint limits aggregate impact despite elevated per-relation rates.

---
