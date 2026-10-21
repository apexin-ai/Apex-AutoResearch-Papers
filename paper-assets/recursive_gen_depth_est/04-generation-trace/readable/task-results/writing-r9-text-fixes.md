# writing r9 text fixes

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_r9_text_fixes_20260517T090838_result.json`
- **Structured JSON:** [`67674263e56bd5e8dd4c.json`](../../sessions/67/67674263e56bd5e8dd4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Here's the summary:

| Task | File | Change | Lines |
|------|------|--------|-------|
| **W-MF1** | section_appendix.tex | Added GPT-2 XL row (67.3 ± 0.7) to Table 16 | +1 |
| **W-SF1** | generalization.tex:108 | "signal universality" → "signal robustness across model boundaries" | 0 |
| **W-SF2** | atlas.tex, generalization.tex | Added "5-fold CV std ≤ 0.9pp" to Table 2 and Table 5 captions | 0 |
| **W-SF3** | abstract.tex:4 | "70--85%" → "$\approx$70--85%" | 0 |
| **W-SF4** | introduction.tex:28-30 | Split contribution bullet 3 into "Generalization axes" + "Diagnostic ablations" | +2 |
| **W-SF5** | conclusion.tex:7-10 | Added strategy-unknown deployment paragraph (3 sentences) | +4 |
| W-SF5 comp | conclusion.tex:16-20 | Compressed "Controlled vs ecological" paragraph | -3 |
| W-SF5 comp | conclusion.tex (caveats) | Compressed "Additional caveats" paragraph | -1 |
| **M1** | references.bib | Deleted `c2pa2024` (uncited), `chen2024spin` (uncited); kept `wenzek2020_ccnet` | -15 |
| **M2** | references.bib + related_work.tex:13 | Added RAID \cite{dugan2024_raid} bib + citation in AI Text Detection paragraph | +10/+0 |
| **M3** | section_appendix.tex:218 | Added "(crawled 2019--2020; pre-LLM deployment)" to C4 mention | 0 |
| **M4** | method.tex:81 | "We introduce...formalize the frontier" → "We propose...as an operational measure" | 0 |
| **M5** | abstract.tex:6 | "(including" → "(e.g.," | 0 |

**Net line change in main text**: +2 (bullet split) + 4 (new para) - 3 (eco compress) - 1 (caveats compress) = **+2** (in Limitations, which is outside the 8-page limit).

**Compilation**: 0 errors, 0 undefined references, 0 undefined citations. Discussion on p8, Limitations on p9.

---
