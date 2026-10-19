# paper writing experiments reframe

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_reframe_20260520T052606_result.json`
- **Structured JSON:** [`5a4779e0a355568407cb.json`](../../sessions/5a/5a4779e0a355568407cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No em-dashes. The "centering" matches are LaTeX `\centering` commands and the technical term "centering" (not an -ing participial phrase ending), so those are fine.

Verification complete:
1. All numbers match the task data exactly (Table 1, Table 2, decomposition, OOD, signal correlations)
2. No em-dashes
3. All section labels correct (`sec:experiments`, `sec:exp_setup`, `sec:adaptive_k`, `sec:main_results`, `sec:magnitude_results`, `sec:failure_modes`)
4. Both tables use booktabs (`\toprule`/`\midrule`/`\bottomrule`)
5. Environments and braces are balanced

The section is restructured with Adaptive K (Section 4.2) as the core contribution, followed by Main Results (4.3), Conditioning (4.4), and Distribution Shift (4.5) as supporting analysis. Key narrative: the K=2 L2 probe (rho=0.9979) enables P50-threshold adaptive allocation at 87% of fixed-K=10 performance with 38% compute, and the decomposition analysis in 4.3 justifies why correction is the dominant mechanism that the adaptive policy targets.

---
