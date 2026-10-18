# paper reviewer fixes batch2

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reviewer_fixes_batch2_20260516T031211_result.json`
- **Structured JSON:** [`a102ec76bc1ac440945c.json`](../../sessions/a1/a102ec76bc1ac440945c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verifications pass:

| # | Fix | Status |
|---|-----|--------|
| 1 | "highest concentration" for Yi-1.5 | Only CodeLlama (correct) retains "highest"; Yi-1.5 → "high" in abstract, analysis, experiments |
| 2 | Architecture family count | abstract = "seven", experiments = "seven" — consistent |
| 3 | 9/9 → 8/8 + CodeLlama profiling | Zero remaining "9/9" hits; updated in abstract, analysis, conclusion, introduction (×2) |
| 4 | 384 heads → up to 400 heads | conclusion.tex fixed; remaining "384 heads" in analysis.tex refer to Pythia/Qwen-14B specifically (correct) |
| 5 | Phi-3 t1/t5 0.24 → 0.23 | Prose and table both updated; the 0.24 in line 70 is Mistral/Pythia concentration (not Phi-3 t1/t5) |

12 edits across 5 files. All changes are factual corrections — no structural or narrative changes.

---
