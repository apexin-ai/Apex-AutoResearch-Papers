# computation fleiss kappa

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_computation_fleiss_kappa_20260519T025427_result.json`
- **Structured JSON:** [`e92330a0c828b3dd01d7.json`](../../sessions/e9/e92330a0c828b3dd01d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved to `artifacts/_project/data/fleiss_kappa_results.yaml`.

**Summary of computed results:**

| Experiment | Model | Dataset | κ (Fleiss) | Eff-K | Unanimous |
|---|---|---|---|---|---|
| exp-026/041 | Qwen2.5-14B | FOLIO-204 | 0.7442 | 1.306 | 58.3% |
| exp-038 | Qwen2.5-14B | LogiQA-200 | 0.8210 | 1.196 | 63.0% |
| exp-052 | Mistral-7B | FOLIO-204 (seed123) | 0.4122 | 2.168 | 14.2% |
| exp-053 | Mistral-7B | FOLIO-204 (seed456) | 0.4013 | 2.216 | 14.2% |

**Validation:** exp-026 computed κ=0.7442 vs reference κ≈0.739 (delta +0.005). Match confirmed.

**5 experiments unavailable:**
- **exp-033, exp-046**: on westd-25068, SSH key auth failed (no config entry existed; added one but key not authorized)
- **exp-020**: likely on decommissioned westd-32608
- **exp-035, exp-027**: data not found on westd-16639 or locally

**Note on exp-026 vs exp-041:** Both map to the same directory (`exp036_qwen25_14b_folio204` on westd-16639). The registry names it `exp-041-14b-folio204-16639`. If these are truly separate runs, the second one's data wasn't found.

To compute the remaining 5 experiments, westd-25068 SSH access needs to be restored, and exp-020/035/027 data needs to be located or re-synced.

---
