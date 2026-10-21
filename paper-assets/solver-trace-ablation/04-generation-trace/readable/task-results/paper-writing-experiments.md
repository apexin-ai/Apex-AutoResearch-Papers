# paper writing experiments

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260514T185007_result.json`
- **Structured JSON:** [`a515c974353d63df34e2.json`](../../sessions/a5/a515c974353d63df34e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass:

- **4 tables**: `tab:goodhart-landscape` (table*), `tab:beta01-3seed`, `tab:prolog-crosslogic`, `tab:hacking-taxonomy`
- **3 figures**: `fig:isr-collapse`, `fig:prolog-comparison`, `fig:hacking-composition`
- **5 section/subsection labels** matching introduction cross-references
- **No 0.716** (gaming-inflated ISR removed from Table 1, replaced with $\ddagger$)
- **No banned phrases**
- **Citations** use `\citep` consistent with the introduction

Key changes from the previous version:
1. **Table 1 expanded** to 10 columns (Condition, Reward, β, n, PR%, ISR*, H7%, H1%, Genuine%, Mode) using `table*` for full width. ISR β=0.1 shows `$\ddagger$` instead of the gaming-inflated 0.716±0.26.
2. **Table 2 created** (hacking taxonomy) with 7 modes × 4 conditions, using `$\bullet$` for seed/step-specific exec-only modes.
3. **Table 3 gains mean±std rows** for both ISR and Random groups, with ISR mean explicitly marked "---" (omitted).
4. **fig:prolog-comparison added** with descriptive caption.
5. **PR formatting standardized** to integer percentages in tables.
6. All numbers verified against the experiment registry.

---
