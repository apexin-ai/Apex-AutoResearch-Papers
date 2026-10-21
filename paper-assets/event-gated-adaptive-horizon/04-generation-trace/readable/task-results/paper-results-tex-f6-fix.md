# paper results tex f6 fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_results_tex_f6_fix_20260525T161849_result.json`
- **Structured JSON:** [`0789c6df18b3ef238d6b.json`](../../sessions/07/0789c6df18b3ef238d6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits applied, no residual old data in results.tex. Summary of changes:

### Diff

**Edit 1 — Subsection title (line 108)**
- Before: `\subsection{F6--F7: Interventions and Multiple Pathways}`
- After: `\subsection{F6--F7: Interventions}`

**Edit 2 — F6 paragraph (lines 111-112)**
- Before: `\paragraph{F6: Trained embedding creates multiple vulnerability pathways.}` + "Two of four seeds collapse (50%): Pathway A (CIVO, nve=4.02×) and preliminary Pathway B (entropy increase, nve=3.78×; 2 seeds only)... Pathway B produces one of three non-CIVO false positives (n=30)."
- After: `\paragraph{F6: $\dt{=}1$ imagination eliminates CIVO.}` + "All four tested seeds avoid CIVO onset (peak NVE 0.5–0.6×), three-seed mean eval 781.2 ± 159.5 (84% baseline). Confirms multi-step imagination is necessary for CIVO induction."

**Edit 3 — Figure caption (line 117)**
- Before: "evaluation crash with entropy increase"
- After: "no CIVO onset (NVE 0.5×, eval 64% baseline)"

### Issue 3 (footnote separation): Not applicable
No shared `$^\dagger$` between exp_059 and 008e_v3 in results.tex. The only `$^\dagger$` (lines 145/158) is TCN-specific.

### Remaining inconsistencies (outside results.tex)
appendix.tex still has extensive old-data references to IRD/Pathway B that need separate updating:
- Line 143: 008e_v3_s2 listed as "IRD" with NVE 3.78×, 008e_v3_s3 as "CIVO" with NVE 4.02×
- Line 158: NVE raw table lists 008e_v3_s2 = 3.78 (IRD)
- Lines 197, 243: false positive references to 008e_v3_s2
- Line 777: failure mode taxonomy with "IRD collapse"
- Line 947: "Multiple Vulnerability Pathways" appendix subsection

---
