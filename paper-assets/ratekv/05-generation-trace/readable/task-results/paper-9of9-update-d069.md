# paper 9of9 update d069

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_9of9_update_d069_20260516T033718_result.json`
- **Structured JSON:** [`759e22fe108cbb452aeb.json`](../../sessions/75/759e22fe108cbb452aeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits complete. Summary of changes:

**Modification 1 (8/8 → 9/9):** Updated 5 locations across abstract.tex (1), introduction.tex (2), analysis.tex (1), conclusion.tex (1). No residual "8/8" remains.

**Modification 2 (Table 2 CodeLlama):** Updated `---`/`---` to `$+$0.19`/`$+$0.17` (ΔPPL uniform/constrained, from bf16=8.84). Added constrained eval confirmation text in analysis.tex L23.

**Modification 3 (footnote):** Added at CodeLlama's first mention (experiments.tex model list): "CodeLlama multi-bit profiles synthesized from 2-bit-only profiling; classification robust as constrained allocation is dominated by 4-bit heads."

**Modification 4 (Mistral 8K):** Added to §4.4 long-context paragraph: Mistral-7B (flat, c=0.24) uniform 1.02× / MCKP 1.02× at 8K. Updated conclusion sentence to "Llama and Mistral remain flat."

**Modification 5 (Table 1):** CodeLlama was not in Table 1, so no update needed there. Updated setup text: removed "profiling only", changed "Eight models undergo full constrained evaluation" → "All nine models", added CodeLlama k=2 to constraint list.

---
