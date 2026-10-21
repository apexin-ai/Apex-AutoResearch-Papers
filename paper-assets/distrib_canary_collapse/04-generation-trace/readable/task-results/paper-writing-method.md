# paper writing method

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260515T185754_result.json`
- **Structured JSON:** [`41f0228173bbbf44b2cf.json`](../../sessions/41/41f0228173bbbf44b2cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Verification checklist:

1. **3 subsections with `\label`**: `sec:pitfalls` (L9), `sec:consensus` (L35), `sec:calibration` (L85) — pass
2. **`tab:practical_guidance` table**: L70 — pass
3. **`\cite{}` keys in references.bib**:
   - `boettiger2012limits` — present
   - `scheffer2009early` — present
   - `granger1969investigating` — present
   - `shojaie2022granger` — present
   - `li2016diversity` — present
   - All 5 keys verified — pass
4. **Forbidden words**: no "consistently outperforms", no "state-of-the-art", no bare "significantly" — pass
5. **FPR/FNR numbers**: FPR K=1→100%, K=2→75%, K=3→37.5%, K≥4→0%; FNR K≥4/5 S≥3/4→0%, K=5/5 S≥3/4→50%, K=5/5 S=4/4→66.7%; spurious rate 75%/62.5% — all match — pass

Additional constraints verified:
- PC07: no "model collapse" prediction claim
- PC10: no Cohen f² benchmarks
- PC11: Granger ≠ true causality explicitly stated (L48)
- PC15: dual spurious rate reported (L16)

File written to `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex`. ~1300 words across 3 subsections with the practical guidance table.

---
