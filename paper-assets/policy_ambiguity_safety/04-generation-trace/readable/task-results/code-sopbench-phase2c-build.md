# code sopbench phase2c build

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sopbench_phase2c_build_20260522T144319_result.json`
- **Structured JSON:** [`9c5759029d489dc80350.json`](../../sessions/9c/9c5759029d489dc80350.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three deliverables complete:

1. **`run_full_experiment.py`** — Full experiment script supporting all 4 domains, 47 pairs, matched-pair design. Supports `--dry-run`, `--resume`, `--pair-filter`, per-episode JSON output, and retry logic.

2. **`analyze_results.py`** — Analysis script computing per-type/per-domain violation rates, Newcombe 95% CIs, and τ²-bench comparison.

3. **`sopbench_phase2c_dryrun.md`** — Dry-run validation confirms:
   - 47 pairs all loaded successfully (10 excluded as specified)
   - Every pair found exactly 3 negative tasks
   - 141 episodes × 2 conditions = **282 total runs**
   - Domain distribution: healthcare 63, bank 48, hotel 21, library 9
   - All 6 ambiguity types covered

---
