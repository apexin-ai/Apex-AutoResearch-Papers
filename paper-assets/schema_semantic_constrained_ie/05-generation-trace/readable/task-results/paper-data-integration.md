# paper data integration

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_data_integration_20260521T115741_result.json`
- **Structured JSON:** [`2cf2c666194c3f933834.json`](../../sessions/2c/2cf2c666194c3f933834.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Zero errors. Here's the summary of all modifications:

### Modified files and changes

| File | Lines | Change |
|------|-------|--------|
| `appendix_discussion.tex` | ~492-519 | Expanded trie-only table: DR-only → full metrics (ET/RV/DR/CF/R-F1/PF) + S1 vs trie DR gap comparison |
| `section6_related_work.tex` | ~12 | Added GoLLIE-7B experimental data (E-F1=9.17, R-F1=0.0, 46% empty docs) + explicit complementarity argument |
| `appendix_beam_search.tex` | ~142 | Added Table `beam-docred-998-zs` for 998-doc DocRED ZS beam=4 results (Qwen: DR=0%, CF=4.94%, R-F1=8.72; Llama: DR=0%, CF=1.00%, R-F1=8.83) |
| `section7_conclusion_compressed.tex` | 3 | Added KG value reference: "100% schema compliance at <0.5% recall cost" |
| `section5_runtime.tex` | 15-19 | Updated 70B paragraph: Llama-3.3-70B SciERC (DR 6.41%→0%, E-F1=35.19, R-F1=11.24) + Llama-3.1-70B DocRED, separated by model |
| `abstract.tex` | 8 | "four" → "five" autoregressive LMs |
| `section1_introduction_draft.tex` | 19, 27 | "four models" → "five models" (×2) |
| `checklist.tex` | 20 | Added Llama-3.3-70B to model list |

Compilation: 0 errors, main text fits in 8 pages (§7 ends on p8, Limitations starts on p9).

---
