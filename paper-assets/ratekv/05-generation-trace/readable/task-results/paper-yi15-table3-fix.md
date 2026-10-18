# paper yi15 table3 fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_yi15_table3_fix_20260514T211702_result.json`
- **Structured JSON:** [`8047e3a5c98744e4cba6.json`](../../sessions/80/8047e3a5c98744e4cba6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All clean:

- `1.3\%` in experiments.tex L64 refers to Qwen seed std, not Yi-1.5 — correct, keep.
- `counterproductive` in analysis.tex L72 refers to Mistral/Gemma-2 (Flat pattern) — correct, keep.
- `counterproductive` in experiments.tex L149 refers to Mistral low heterogeneity — correct, keep.

No stale Yi-1.5 values (0.30, 7.31, 1.3% degradation) remain anywhere.

**Summary of changes across 5 files:**

| File | Change |
|------|--------|
| `analysis.tex` L17 | "counterproductive (+0.30 vs +0.20)" → "matches uniform (+0.20 vs +0.20)" |
| `analysis.tex` L41 (Table 3) | ΔPPL Ours: +0.30 → +0.20 |
| `analysis.tex` L71 | "counterproductive or marginal" → "no benefit or marginal" |
| `experiments.tex` L53 (Table 2) | Yi-1.5-9B → Yi-1.5-9B†, Ours: 7.31 → 7.22 |
| `experiments.tex` L73-74 | "7.31 PPL vs uniform 7.22—a 1.3% degradation" → "7.22 PPL, essentially identical to uniform 7.22 (<0.01%)" + spike explanation |
| `introduction.tex` L35 | "degrades PPL by 1.3% (7.31 vs 7.22)" → "provides no benefit (7.22 vs 7.22 uniform)" |
| `introduction.tex` L53 | "makes MCKP counterproductive" → "means MCKP provides no benefit over uniform" |
| `abstract.tex` L6 | "is counterproductive" → "provides no benefit" |
| `abstract.tex` L7 | "yet degrades under" → "yet gains nothing from" |
| `conclusion.tex` L7 | "are counterproductive" → "show no benefit" |

---
