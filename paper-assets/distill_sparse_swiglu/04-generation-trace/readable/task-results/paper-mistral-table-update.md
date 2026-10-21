# paper mistral table update

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_mistral-table-update_20260519T055314_result.json`
- **Structured JSON:** [`fafa0c7b75a05ecb3fd5.json`](../../sessions/fa/fafa0c7b75a05ecb3fd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Data already present, caption fixed. Summary:

1. **Table data**: HellaSwag and PIQA already in `tab:mistral_downstream` with correct numbers (KL: 68.9/75.2, TEAL: 60.1/72.1). No changes needed.
2. **Caption fix**: Corrected "largest" claim from HellaSwag +8.8pp to ARC-c +9.0pp (the actual largest delta).
3. **Text references**: experiments.tex (line 228) already mentions "HellaSwag +8.8pp, ARC +9.0pp, WG +5.6pp". Abstract/introduction list selected deltas without explicit task counts. No updates needed.
4. **Task counts**: Caption "5 of 6 tasks" is correct. No "N tasks" claims elsewhere need updating.

One discrepancy to flag: the Dense PPL in `tab:mistral_downstream` is 5.06, but `tab:cross_arch` section text (line 344) says "dense PPL 5.52", and the task context also says 5.52. You may want to verify which is correct.

---
