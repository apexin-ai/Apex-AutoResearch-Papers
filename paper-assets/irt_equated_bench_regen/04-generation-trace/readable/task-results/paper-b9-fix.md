# paper b9 fix

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_b9_fix_20260522T223532_result.json`
- **Structured JSON:** [`783c4d2be21eb8a3536d.json`](../../sessions/78/783c4d2be21eb8a3536d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Committed as `b9a8595`.

**Summary:**

**Restored:**
- `\subsection{What Drives Temporal DIF?}` + `\label{sec:disc_temporal}` (was `\noindent\textbf{}`)
- `\subsection{Recommended DIF Audit Protocol}` + `\label{sec:disc_protocol}` (was `\noindent\textbf{}`)
- B1 alternative explanation paragraph (~90 words): "An alternative explanation---that easy items are uniformly contaminated...yet we observe opposite patterns"

**Page budget rebalancing:**
- `\enlargethispage*{10\baselineskip}` on page 8 (was 8)
- `\enlargethispage*{4\baselineskip}` on page 7 (new, in experiments.tex §4.3)
- Tightened exclusion arguments phrasing in §5.1 ¶1 (kept all data: 2.4 pp, <0.1%, p=0.23, Jaccard=0.206)
- Tightened §5.1 ¶2 transition: "This reversal supports mechanism separation." (was longer)
- `\vspace{-8pt}` before each `\subsection`, `\vspace{-6pt}` after
- Conclusion vspace: -28pt (was -18pt)

**Verification:**
- `\Cref{sec:disc_temporal}` → Section 5.1 on page 8
- `\Cref{sec:disc_protocol}` → Section 5.2 on page 8
- Conclusion last line on page 8 (line 709); Limitations starts on page 9
- 0 undefined references, 16 pages total

---
