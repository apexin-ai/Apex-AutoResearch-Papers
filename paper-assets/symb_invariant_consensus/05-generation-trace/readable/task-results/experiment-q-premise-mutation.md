# experiment q premise mutation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_q-premise-mutation_20260520T103427_result.json`
- **Structured JSON:** [`3e00c3949e71685ed8c6.json`](../../sessions/3e/3e00c3949e71685ed8c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pilot report:

## Direction Q: Premise Mutation Pilot Results (N=10, K=12, FOLIO)

| Mutation | SC Acc | SICA Acc | SC Flip% | SICA Flip% |
|----------|--------|----------|----------|------------|
| original | 60.0% | 60.0% | — | — |
| synonym | 80.0% | 60.0% | 20.0% | 20.0% |
| reorder | 70.0% | 70.0% | 30.0% | 30.0% |
| inject | 80.0% | 80.0% | 20.0% | **30.0%** |
| combined | 50.0% | 40.0% | 30.0% | **40.0%** |

**Key observations (pilot, N=10 — treat with caution):**

1. **Baseline parity**: SC and SICA have identical accuracy (60%) on original problems.
2. **Synonym mutation**: Both flip at 20%. SC accuracy rises to 80% (likely noise), SICA stays at 60%. No differential.
3. **Reorder mutation**: Both flip at 30%. No differential.
4. **Inject mutation**: SICA flips more (30%) than SC (20%). SICA's constraint extraction may be sensitive to irrelevant premises generating spurious constraints.
5. **Combined mutation**: SICA is more unstable (40% flip) vs SC (30% flip). SICA accuracy drops to 40% vs SC's 50%.
6. **Overall pattern**: SICA shows slightly higher instability than SC under inject and combined mutations, suggesting the symbolic pipeline amplifies perturbations rather than filtering them. The full 204-question run will determine if this holds at scale.

**Full 204-question run**: launched as PID 314817 on `westd-16639`, ETA ~5-6 hours. Output: `/root/symb_invariant_consensus/results/direction_q_premise_mutation/results.json`, log: `/tmp/direction_q_full.log`.

---
