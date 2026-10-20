# paper writing method

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260519T035043_result.json`
- **Structured JSON:** [`c35c9b294e20be3cf69a.json`](../../sessions/c3/c35c9b294e20be3cf69a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The rewrite is complete. Changes made:

1. **Added §3.1** (Condorcet Independence Assumption): Frames SC as majority voting under CJT, explains the independence violation from same-model sampling, introduces the $K_{\text{eff}}$ formula with Fleiss' $\kappa$, and establishes the "independence bottleneck" framing.

2. **Restructured §3.2** (SICA Pipeline): Reorganized into clear paragraphs (trace generation, constraint extraction, deduplication, MAX-SAT, scoring, degeneration, $C_0$). Added extraction temperature $T_{\text{ext}} = 0.3$. Preserved all equations (Eq 1-5) and the degeneration analysis. $C_0$ is now a brief paragraph (3 sentences + equation) instead of a full subsection.

3. **Added §3.3** (Oracle Control Design): Promoted from implicit mention to explicit subsection. Framed as causal intervention.

4. **Updated §3.4** (Scope): Changed "six" to "nine" remediation strategies.

5. **Updated TikZ figure**: Added red dashed box around sampling+extraction stages labeled "Independence Bottleneck". Updated caption with $K_{\text{eff}}$ context.

6. **Section title**: Changed from "Method: The SICA Pipeline" to "Method".

7. **Added 4 bib entries**: `condorcet1785`, `austensmith1996`, `ladha1992correlated`, `fleiss1971kappa`.

8. All style rules pass: zero em-dashes/en-dashes, no banned words, no -ing phrase endings.

---
