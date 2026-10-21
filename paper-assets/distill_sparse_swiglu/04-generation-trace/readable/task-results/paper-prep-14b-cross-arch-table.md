# paper prep 14b cross arch table

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_prep_14b_cross_arch_table_20260518T001836_result.json`
- **Structured JSON:** [`f555da2ff5a4c42e532c.json`](../../sessions/f5/f555da2ff5a4c42e532c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Good. Now let me also check the `paper_framing.md` mention about the Dense PPL — the current text uses 5.19 consistently in the table (eval-time PPL), which matches the user's instruction. The old paragraph had "dense PPL 5.18" which I've now corrected to 5.19 in the table.

Let me also check if there's a cross-reference issue — the `\label{sec:cross_arch}` was on line 204 previously and the new `\label{sec:14b}` is inside the same subsection, which is fine.

**Status report:**

**Current 14B coverage in the paper:**
- Expanded from a 2-line paragraph + TODO into a full table (`tab:14b`) with all verified global top-k data (Dense, KL, TEAL, BCE) across 5 metrics.
- Fixed dense PPL from 5.18 to 5.19 (eval-time value).
- TEAL PPL correctly shown as 8.73 (not the previously misattributed 8.76).
- BCE native sparsity collapse point retained as separate narrative (different eval mode than the table).

**What to do when uniform results arrive:**
1. Uncomment the `KL uniform` row in `tab:14b` (line 247) and fill in the numbers.
2. If uniform shows better downstream stability (as at 8B), add a sentence noting this mirrors the budget-surplus regime finding.
3. Consider whether uniform data warrants a second 14B row in `tab:phase` (Table 5) for the regime analysis section.

---
