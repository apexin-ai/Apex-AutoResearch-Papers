# code human edit robustness

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_human-edit-robustness_20260516T215920_result.json`
- **Structured JSON:** [`5782a5d73b03bb37ef58.json`](../../sessions/57/5782a5d73b03bb37ef58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No errors. Experiment completed cleanly. Let me verify the 0% baseline sanity check against the expected ~0.70 binary F1.

Results summary:

| Perturbation | Binary F1 | Multiclass F1 | Binary 95% CI |
|---|---|---|---|
| 0% (baseline) | 0.6953 | 0.7371 | [0.6798, 0.7102] |
| 5% | 0.6496 | 0.6407 | [0.6351, 0.6655] |
| 10% | 0.6139 | 0.4916 | [0.5989, 0.6287] |
| 20% | 0.5912 | 0.3669 | [0.5761, 0.6049] |

**Degradation from baseline (binary F1):**
- 5% replacement: -0.046 (6.6% relative drop)
- 10% replacement: -0.081 (11.7% relative drop)
- 20% replacement: -0.104 (15.0% relative drop)

**Sanity check passed**: 0% baseline binary F1 = 0.695 matches the expected ~0.70 from v6.

The binary classification (gen-1 vs gen-2+) degrades gracefully: even at 20% word replacement, F1 remains at 0.59 (vs 0.70 baseline). The multiclass task is more sensitive because distinguishing gen-0 from gen-1/2+ relies heavily on lexical features (ttr, hapax) that are directly disrupted by word replacement.

---
