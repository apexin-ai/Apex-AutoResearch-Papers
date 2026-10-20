# code dgs persistence fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dgs_persistence_fix_20260518T164426_result.json`
- **Structured JSON:** [`b1cbcdb967119337cd2c.json`](../../sessions/b1/b1cbcdb967119337cd2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## DGS Results

JSON persisted at `output/dgs_selection_results.json`. Key numbers:

| Dataset | Greedy | LP-all | DGS | Oracle | DGS-Greedy | DGS-LP |
|---------|--------|--------|-----|--------|------------|--------|
| SciERC  | .6436  | .6495  | .6507 | .7775 | +0.71pp (n.s.) | +0.12pp (n.s.) |
| CoNLL   | .9087  | .8985  | .8985 | .9520 | **-1.02pp (sig.)** | 0.00pp |
| FewNERD | .7713  | .7800  | .7805 | .8831 | +0.92pp (sig.) | +0.04pp (n.s.) |

**DGS is not a viable method contribution:**

1. **CoNLL: DGS significantly worse than greedy** (-1.02pp, 95% CI [-1.41, -0.64]). LP is 2.69pp worse than greedy on non-degenerate instances, so gating to LP hurts.
2. **SciERC: not significant** (CI crosses zero).
3. **FewNERD: significant vs greedy, but DGS adds nothing over plain LP-all** (+0.04pp, n.s.). The gating mechanism itself has no value.
4. **DGS vs LP-all is never significantly positive** across any dataset.

The paper stays pure diagnostic. Full report at `artifacts/dgs_results/dgs_selection_results.md`.

---
