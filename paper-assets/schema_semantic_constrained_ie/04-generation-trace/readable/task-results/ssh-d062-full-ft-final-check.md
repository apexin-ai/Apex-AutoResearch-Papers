# ssh d062 full ft final check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d062_full_ft_final_check_20260519T044208_result.json`
- **Structured JSON:** [`65be608a641b6ca2c035.json`](../../sessions/65/65be608a641b6ca2c035.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

d062_full_ft_scierc pipeline complete. Summary:

**Registry** — `d062_full_ft_scierc` updated to `DONE/negative` with full metrics, checkpoint_path, log_path.

**Artifact** — Report registered as `art_20260519_37230b` at `artifacts/d062_full_ft_scierc_results.md`.

**Bottom line**: Full FT is worse than LoRA FT on SciERC (E_F1 0.6478 vs 0.6705, R_F1 0.3789 vs 0.4386). The secondary finding holds: unconstrained Full FT still produces DR violations (2.74%), confirming OntoCoDec constraints remain necessary across all fine-tuning strategies.

---
