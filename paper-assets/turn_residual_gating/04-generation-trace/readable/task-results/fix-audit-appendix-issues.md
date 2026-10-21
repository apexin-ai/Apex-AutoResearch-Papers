# fix audit appendix issues

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_audit_appendix_issues_20260525T203522_result.json`
- **Structured JSON:** [`1de8e6a9476b212af4df.json`](../../sessions/1d/1de8e6a9476b212af4df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The remaining 1.3× occurrences are:
- `discussion.tex:3` — "${\leq}$1.3$\times$" for GAR-Dongre shift (different metric, correct as-is)
- `appendix.tex:633` — per-seed values "gap 1.3$\times$" (individual seed data, correct as-is)

Both are unrelated to the SS aggregate gap. All edits complete. Summary:

| # | Issue | File(s) | Fix |
|---|-------|---------|-----|
| 1 | Table 1 IID column | related_work.tex | TG: 0.50→0.49, 2.78→2.63; UG: 2.78→2.62; LoRA: 0.50→0.49, 2.78→2.63 |
| 2 | Gap ratio 7.8×→7.9× | experiments/intro/appendix | All 7.8× → 7.9× (6 locations) |
| 3 | SS gap ~1.3×→~1.2× | experiments/analysis/intro/conclusion/appendix | All ~1.3× → ~1.2× (8 locations) |
| 4 | ≤1pp→≤2pp | experiments.tex | "$\leq$1\,pp" → "$\leq$2\,pp"; also "PPL is 2.78 for all" → "PPL is 2.62--2.78" |
| 5 | MMLU max degradation | appendix.tex | 1.2pp → 1.5pp (text + figure caption) |
| 6 | "Base (LoRA-only)" label | appendix.tex | → "Base (pretrained)" |
| 7 | SS ρ_max 0.5→0.3 | appendix.tex | intro paragraph fixed |
| 8 | SS PPL std | experiments.tex | 0.001 → 0.002 |
| 9 | Llama VRAM caption | appendix.tex | Added "VRAM reports peak allocated memory (excluding optimizer states)." |
| 10 | LoRA-only training time | appendix.tex | 6.0h → 5.7h (table + paragraph range) |

---
