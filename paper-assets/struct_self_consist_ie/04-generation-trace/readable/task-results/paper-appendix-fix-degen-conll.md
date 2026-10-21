# paper appendix fix degen coNLL

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix-fix-degen-coNLL_20260519T150014_result.json`
- **Structured JSON:** [`276a6d4bb96b4db8d86b.json`](../../sessions/27/276a6d4bb96b4db8d86b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both fixes have already been applied to the current version of the file:

**Fix 1 (L360):** The table headers already show `$N{=}8$` for all three columns:
```
& \shortstack{SciERC 8B\\($N{=}8$)} & \shortstack{SciERC 4B\\($N{=}8$)} & \shortstack{CoNLL 8B\\($N{=}8$)} \\
```

**Fix 2 (L687):** The text already says `38\% for Qwen`, not `41\%`:
```
the valid-instance fraction is low (38\% for Qwen, 11\% for LLaMA)
```

I verified both values against the actual data on the server:

| Seed | Qwen degeneracy | Qwen non-deg |
|------|----------------|-------------|
| 42 | 59.14% | 40.86% |
| 123 | 63.03% | 36.97% |
| 456 | 62.88% | 37.12% |
| **3-seed mean** | **61.68%** | **38.32% ≈ 38%** |

LLaMA seed42: degeneracy 89.22% → non-deg 10.78% ≈ 11%.

The text's "38\% for Qwen, 11\% for LLaMA" is correct. The table at L702 showing 41% is also correct (seed-42 value, as stated in the caption). No changes needed.

---
