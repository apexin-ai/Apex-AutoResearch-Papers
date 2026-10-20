# paper table7 docs fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table7_docs_fix_20260518T131014_result.json`
- **Structured JSON:** [`6fec526a69024db36274.json`](../../sessions/6f/6fec526a69024db36274.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits applied correctly. Summary of changes:

**L336**: "single seed" → seed description split by condition type (architecture=single, scale/domain=two seeds s42/s43)

**L341 (Caption)**: Removed "single seed per condition", removed "[TBD]", removed GPT-2m 6-pair exception text; added `$n_{\text{perm}}{=}5{,}000$`, "8~pairs per condition", two-seed replicability note

**L347-357 (Table rows + footnotes)**:
- Baseline: `7/8, 6/8, 6/8, 6/8, 0/8, 6/8, 6/8` → `8/8, 8/8, 8/8, 6/8, 3/8, 4/8, 6/8`
- GPT-2m: `6/6` format → `8/8` format (8-pair)
- OPT-1.3B: `6/8, 6/8, 8/8, 6/8, 0/8, 2/8, 6/8` → `8/8, 6/8, 8/8, 6/8, 2/8, 6/8, 6/8`
- Scale: `[TBD]` → two rows (s42: 5/8 consensus, s43: 6/8 consensus)
- Domain: `[TBD]` → two rows (both 6/8 consensus)
- Added two footnotes (PG reverse explanation, perplexity 0/14)

**L363-364 (Architecture text)**: Updated reverse-direction claim from "0 reverse" to "2/8 to 3/8, concentrated in distinct→ECE pairs"

**L367-369 (Method variation)**: Threshold "8/8 on both GPT-2-medium and OPT-1.3B"; TY "4/8 (Pythia) to 6/8 (OPT), GPT-2m at 5/8"; simplified consensus sentence

**L372 removed**: TODO comment

**L378-389 (new)**: Scale paragraph (seed-dependent consensus, s42=5/8, s43=6/8) and Domain paragraph (both seeds 6/8, seed-dependent reverse) replacing the commented placeholder. Cross-condition paragraph already existed at L371, not duplicated.

---
