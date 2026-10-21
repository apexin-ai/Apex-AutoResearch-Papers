# code wikievents qwen llama results

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_qwen_llama_results_20260517T192706_result.json`
- **Structured JSON:** [`d263c6fd2b7e89d31afe.json`](../../sessions/d2/d263c6fd2b7e89d31afe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both baselines complete. Here are the results:

---

```
Model: Llama (unconstrained)
Docs: 246/246
Parse Success: 226/246 (91.9%)

Violation Rates:
  ET:  0.0%
  EV:  10.5%
  RoV: 88.8%
  AC:  0.1%
  CF:  0.0%

F1 Scores:
  Trigger F1: 0.0572
  Argument F1: 0.0000
  Entity F1: 0.0000
```

```
Model: Qwen (unconstrained)
Docs: 246/246
Parse Success: 218/246 (88.6%)

Violation Rates:
  ET:  0.0%
  EV:  24.0%
  RoV: 74.9%
  AC:  0.3%
  CF:  0.0%

F1 Scores:
  Trigger F1: 0.1184
  Argument F1: 0.0009
  Entity F1: 0.0000
```

---

**Key observations:**

- Both models produce 0 entities (the unconstrained prompt apparently doesn't elicit entity extraction)
- RoV dominates violations: 88.8% (Llama) / 74.9% (Qwen). The models generate free-form role names (251 unique for Llama) instead of the 59 ontology-defined roles
- Argument F1 is near-zero because matching requires (trigger, event_type, arg_text, role) 4-tuple, and the free-form roles never match gold
- Trigger F1 is very low (5.7% / 11.8%) because both trigger text and event type must match
- Qwen has higher EV violations (24%) vs Llama (10.5%), but slightly better Trigger F1
- Parse failure rate: Llama 8.1%, Qwen 11.4%

Note: I patched `violation_checker_wikievents.py` and `eval_event_extraction.py` on the server to handle the case where `parsed_output` is a bare list instead of `{"events": [...]}` (only affected 1 Llama record).

---
