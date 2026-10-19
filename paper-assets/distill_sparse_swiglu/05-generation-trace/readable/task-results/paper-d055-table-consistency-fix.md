# paper d055 table consistency fix

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d055-table-consistency-fix_20260518T050839_result.json`
- **Structured JSON:** [`a1c4ae8a5fa51ed4efeb.json`](../../sessions/a1/a1c4ae8a5fa51ed4efeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All updates applied and verified. Summary of changes in `experiments.tex`:

| Metric | Old | New |
|--------|-----|-----|
| PPL std | 0.03 | 0.02 |
| ARC-C | 43.9±3.9 | 43.8±3.6 |
| WG | 70.6±0.7 | 70.2±0.9 |
| GSM8K | 8.9±0.2 | 8.0±0.7 |
| MMLU | 35.7±9.5 | (unchanged, already correct) |

Updated 3 locations: inline text (line 28), Table 1 (line 49), Table 3 (line 166). Bold markings remain correct (KL global still best for ARC-C, WG, GSM8K at 30%). The "7.5×" MMLU stability ratio and "9.5pp" references are unchanged since MMLU data didn't change. Compilation passes cleanly.

---
