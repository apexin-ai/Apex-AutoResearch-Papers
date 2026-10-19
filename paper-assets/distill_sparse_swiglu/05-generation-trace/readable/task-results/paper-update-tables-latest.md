# paper update tables latest

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_update_tables_latest_20260517T185215_result.json`
- **Structured JSON:** [`f4469ab03ab87a3a818c.json`](../../sessions/f4/f4469ab03ab87a3a818c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits look correct. Here's the summary of changes:

**Modified files:**

1. **`experiments.tex`** (2 edits):
   - Line 29: Added forward reference to extended downstream benchmarks (Appendix D)
   - Lines 228-231: Added **Qwen-2.5-14B** paragraph with KL advantage (PPL 7.62 vs TEAL 8.76, 1.15x ratio) and BCE failure evidence (sparsity collapse to 6.4%, confirmed by 10x stronger Lagrangian)

2. **`appendix.tex`** (1 edit):
   - Lines 196-217: Added **Extended Downstream Evaluation** section (Table 8) comparing Dense, KL 30%, and TEAL 30% on HellaSwag (72.70 vs 66.70), PIQA (75.95 vs 73.61), and BoolQ (76.85 vs 68.50)

3. **`references.bib`** (1 edit):
   - Added Qwen-2.5 technical report citation

**Already up to date (no changes needed):**
- Table 2 & Table 5: 30% uniform 3-seed MMLU 40.7±1.3% verified correct (s42=40.61, s123=39.44, s456=41.98)
- F1 oracle analysis at line 66: BCE F1=0.613 vs KL F1=0.540 already present
- All 50% 3-seed data (28.1±0.2 global, 28.0±0.6 uniform) verified correct

---
