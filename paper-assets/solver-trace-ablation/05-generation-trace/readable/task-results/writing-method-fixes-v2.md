# writing method fixes v2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_method-fixes-v2_20260515T024843_result.json`
- **Structured JSON:** [`4946da9dae4e2791d35d.json`](../../sessions/49/4946da9dae4e2791d35d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes are clean. Here's the summary:

## Changes made

### Task 1 (Version sync) — already done
The paper/method.tex already contained the Algorithm environment (lines 29-44), Reward conditions table (lines 69-86), and complete 7-mode taxonomy definitions (lines 96-120). No changes needed.

### Task 2 (Remove percentages) — already done
The taxonomy definitions in method.tex are already purely conceptual with no percentage numbers. No changes needed.

### Task 3 (FOLIO dataset)
- **1,204 is correct.** The `tasksource/folio` HuggingFace dataset has 1,204 examples with human-annotated FOL formalizations. The original FOLIO paper reports 1,435 total, so 1,204 is a filtered subset.
- **Fixed `paper/limitations.tex`**: Changed "reflecting the FOLIO dataset's total size of 1,435 annotated examples" → "drawn from the 1,204 FOL-annotated examples available in FOLIO"
- **proofwriter naming**: Already handled by the footnote on method.tex line 17. The paper text consistently cites FOLIO; the "proofwriter" filename is only an internal artifact. The experiments.tex (line 8) says "FOLIO" and never mentions "proofwriter" — no change needed there.

### Task 4 (Solver call count) — already done
Line 26 already reads "The protocol requires $n$ additional solver calls per proved sample." The Algorithm (lines 29-44) shows exactly $n$ iterations. Consistent.

### Additional fix
- **Fixed duplicate `\label{alg:sta}`** in `paper/appendix.tex`. The appendix STA Algorithm section previously duplicated the algorithm from the main body with the same label. Replaced with a forward reference to Algorithm 1 in Section 3.2.

---
