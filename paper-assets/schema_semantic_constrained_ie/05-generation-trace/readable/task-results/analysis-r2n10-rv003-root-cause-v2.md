# analysis r2n10 rv003 root cause v2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r2n10_rv003_root_cause_v2_20260518T130606_result.json`
- **Structured JSON:** [`5e29266a59d10b891091.json`](../../sessions/5e/5e29266a59d10b891091.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written to `artifacts/r2n10_rv_root_cause.md`.

**Summary**: All 5 RV cases are a single xgrammar 0.1.33 bug, not a fundamental limitation. The chimeric relation "membericipant of" forms when xgrammar's enum automaton incorrectly allows token "icipant" (from "participant of") after token "member" (from "member of"). I reproduced this directly with xgrammar's GrammarMatcher, confirming 8 tokens are allowed after "member" when only " of"-continuing tokens should be. The TypeConstraintProcessor (Layer 2) is uninvolved since it doesn't mask relation type values at all.

Paper Agent's description ("tokenization edge cases where multi-token relation names span grammar-state boundaries") is directionally correct but imprecise. The report includes three revision options at different verbosity levels.

---
