# paper model count fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_model_count_fix_20260516T024526_result.json`
- **Structured JSON:** [`7b46c67a32a03ce95bd9.json`](../../sessions/7b/7b46c67a32a03ce95bd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Here's the summary of changes:

### Modified files

**`analysis.tex`** (2 changes):
- Line 29: Updated Phi-3 description from "predicting neutral MCKP benefit" to "confirmed by evaluation (constrained +0.18 vs. uniform +0.16 PPL)" with exp_id
- Line 52: Table 2 Phi-3 row: `--- & ---` → `$+$0.16 & $+$0.18`

**`experiments.tex`** (6 changes):
- Line 8: "seven models spanning five architecture families" → "eight models spanning six architecture families"
- Line 15: Added `\textbf{Phi-3-medium-14B} (GQA 4:1, 40 × 10 = 400)` to model list
- Line 29: Added "Phi-3-medium" to k=8 group in compression paragraph
- Line 45: Table 1 caption: "5/7 models" → "6/8 models"
- Line 59: Added Table 1 row: `Phi-3-medium-14B & 5.64 & 5.80 & 6.07 & 6.07 & 5.81`
- Line 78: Added Phi-3 discussion paragraph in §4.2 Main Results

### Count consistency audit
| Scope | Count | Files |
|-------|-------|-------|
| Profiling/diagnostic (Table 2) | 9 models, 9/9 | abstract, analysis, intro, conclusion |
| Main eval (Table 1) | 8 models, 6/8 identical | experiments |
| "eight of nine don't benefit" | 8 remaining | abstract, intro |

The only model with `---` in both tables is CodeLlama-7B (Table 2, profiling-only) — this is correct since it has no constrained eval data.

---
