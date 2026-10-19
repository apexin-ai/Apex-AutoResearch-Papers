# paper writing

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_20260515T191259_result.json`
- **Structured JSON:** [`43430029b877a5550844.json`](../../sessions/43/43430029b877a5550844.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method section written to `artifacts/_project/paper/method.tex`.

**Structure**: 5 subsections, 5 numbered equations, ~2 pages in CoRL format.

| Subsection | Content |
|---|---|
| 3.1 Problem Setup | Frozen VLA, 7-DOF (6 arm + gripper separate), C=50 chunks truncated to H=5 |
| 3.2 Selection | K=10 samples → Ledoit-Wolf shrinkage covariance (Eq.1) → Mahalanobis score (Eq.2) → argmin selection (Eq.3) |
| 3.3 CRM | obs_only 2-layer MLP, magnitude-bounded correction (Eq.4), L2 training loss (Eq.5), 26,737 training samples |
| 3.4 Magnitude Control | Unbounded → 0% catastrophic failure; ε=0.1 default; obs_only robust across [0.05, 0.3], perdof collapses |
| 3.5 Inference Protocol | Step-by-step pipeline, K=10 overhead + ~3ms CRM |

**Key changes from old draft**: Removed ACI/COC and 40D CGS feature vector entirely. CRM takes only observation embedding. Per-DOF features mentioned only as ablation comparisons. Argmin selection replaces conformal regions. One `% TODO` left for exact parameter count from checkpoint.

---
