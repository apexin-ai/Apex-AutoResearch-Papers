# code paper tex redline fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paper-tex-redline-fix_20260515T152900_result.json`
- **Structured JSON:** [`62a9b09821b39affb46f.json`](../../sessions/62/62a9b09821b39affb46f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All fixes complete. Summary of changes across 8 files:

**RED LINE fixes:**
- **RL-01** (7→8 modes): Added H8 to taxonomy tables in experiments.tex and appendix.tex. Merged H7a/H7b into single H7 row. Updated method.tex mode list and introduction.tex contribution text.
- **RL-02** (H7 64.5%→69.7%): Updated H7 table values from 65→70. Fixed ISR s44 H7 from 86.5%→100% (FN corrected). Updated figure script and annotation.
- **RL-03** (ISR N-H 17%→6.9%): Updated taxonomy table ISR N-H from 17→7.

**MEDIUM fixes:**
- **ISS-04** (s42 31%→17%): Fixed experiments.tex text ($31\%$→$17\%$), temporal collapse numbers (30.9→17.3%, 92.2→96.7% H7, 3.0→1.1% genuine), and detailed table.
- **ISS-05** (Exec N-H 13%→7.5%): Updated Table 1 (13→8), taxonomy table (13→8), detailed table (12.9→7.5), and Fisher table (5.9%→7.5% with recomputed OR/p).

**LOW fix:**
- **ISS-06** (SFT 91.3%→92.2%): Switched to 1000-step 3-seed data across all mentions (abstract, intro, experiments, conclusion, appendix detailed table, Fisher table). PR 15.3%→13.0%, n=46→39, per-seed range 88-93%→91-93%.

Figure `fig3_hacking_composition.pdf` regenerated with corrected data. Changelog registered as artifact `art_20260515_beda84`.

---
