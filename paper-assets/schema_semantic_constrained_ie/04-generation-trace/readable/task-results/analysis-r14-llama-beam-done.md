# analysis r14 llama beam done

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r14_llama_beam_done_20260521T044404_result.json`
- **Structured JSON:** [`054bba14e2718f121db7.json`](../../sessions/05/054bba14e2718f121db7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment `r14_llama_docred_beam4_998` complete. Cron was not active in this session (already cleared or from a different session).

**Summary:**
- **Status**: DONE (success), 998/998 docs processed (959 success, 39 parse fail)
- **Hypothesis confirmed**: Beam=4 S1 constrained decoding eliminates DR violations on full dataset
- **Key results vs ZS greedy baseline**:
  - DR%: 2.55% → **0.00%** (eliminated)
  - CF%: 8.54% → **1.00%** (−88%)
  - R-F1: 6.27 → **8.83** (+2.56)
  - E-F1: 54.93 → **57.81** (+2.88)
  - Parse fail: 9.1% → **3.9%** (−57%)
- **Note**: d064/d065 results (R-F1~45) are from a different campaign (likely FT models), not comparable to this ZS run

---
