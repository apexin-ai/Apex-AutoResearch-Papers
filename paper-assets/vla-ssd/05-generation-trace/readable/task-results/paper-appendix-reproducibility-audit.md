# paper appendix reproducibility audit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_reproducibility_audit_20260519T150435_result.json`
- **Structured JSON:** [`3f74efd36c450b0f387d.json`](../../sessions/3f/3f74efd36c450b0f387d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Here's the audit report:

---

## Appendix Reproducibility Audit

### Per-Subsection Check (✓ present / ✗ missing / -- N/A)

| Subsection | Model | Dataset | Hyperparams | Metric Def | Hardware |
|---|---|---|---|---|---|
| CKA Analysis Method | ✓* | ✓* | -- | ✓ | ✓* |
| Metric Sensitivity: RSA vs CKA | ✓* | ✓* | -- | ✓ | ✓* |
| Branch-Split Detailed Analysis | ✓* | ✓* | -- | ✓ | ✓* |
| RSA Across Representation Sources | ✓* | ✓* | -- | ✓ | ✓* |
| Per-Layer RSA Profiles | ✓* | ✓* | -- | ✓ | ✓* |
| Per-Layer Action Decoding (3 cond) | ✓* | ✓ | ✓ (3 seeds, 50 demos) | ✓ | ✓* |
| Random-Subset Ablation | ✓* | ✓* | ✓ (10 subsets, 24/32) | ✓ | ✓* |
| Action Trajectory Analysis | ✓* | ✓ (5×10 demos, 3 tasks) | ✓ (10K bootstrap) | ✓ | ✓* |
| Pretrained LLM OOD Diagnostics | ✓* | ✓* | -- | ✓ | ✓* |
| Probe Architecture Sensitivity | ✓* | ✓* | ✓ (linear 4096→7) | ✓ | ✓* |
| Functional Probe Comparison | ✓* | ✓* | ✓* | ✓ | ✓* |
| Training Effect & Instr Invariance | ✓* | ✓* | -- | ✓ | ✓* |
| Additional RSA Values | ✓* | ✓* | -- | ✓ | ✓* |
| Cross-Benchmark: LIBERO-Spatial | ✓* | ✓ **fixed** | ✓* | ✓ | ✓* |
| Distance Metric Invariance | ✓* | ✓* | -- | ✓ | ✓* |
| Per-DOF Decomposition | ✓* | ✓* | -- | ✓ | ✓* |
| Permutation Test | ✓* | ✓* | ✓ (1K shuffles) | ✓ | ✓* |
| Probe Seed Sensitivity | ✓* | ✓* | ✓ (5 seeds) | ✓ | ✓* |
| Demo Subsample Sensitivity | ✓* | ✓ (25 vs 50) | -- | ✓ | ✓* |
| Detailed Training Effects | ✓* | ✓* | ✓ (10K bootstrap) | ✓ | ✓* |
| Training Effect Size Summary | ✓* | ✓* | -- | ✓ | ✓* |
| Cross-Instruction Dense Profile | ✓* | ✓* | ✓* | ✓ | ✓* |
| LOOCV Validation | ✓* | ✓* | ✓ (10 folds) | ✓ | ✓* |
| QA Probe | ✓* | ✓* | ✓ **fixed** | ✓ | ✓* |
| Probe Profiles | ✓* | ✓* | ✓* | ✓ | ✓* |
| Four-Condition Probe | ✓* | ✓* | ✓* | ✓ | ✓* |
| L1 Attention Pattern | ✓* | ✓* | -- | ✓ | ✓* |
| Multi-Layer Attention | ✓* | ✓* | -- | ✓ | ✓* |
| Threshold Sensitivity | ✓* | ✓* | -- | ✓ | ✓* |
| L1 Attention Decomposition | ✓* | ✓* | -- | ✓ | ✓* |
| Per-Dimension MAE | ✓* | ✓* | -- | ✓ | ✓* |
| Per-Task R² Distribution | ✓* | ✓ (5 demos/task) | ✓ (MLP) | ✓ | ✓* |
| Task Complexity & Routing | ✓* | ✓* | -- | ✓ (Mann-Whitney) | ✓* |
| Specificity Control | ✓* | ✓* | ✓ (5 seeds random) | ✓ | ✓* |

✓* = covered by the new shared setup paragraph referencing §3.1--§3.6

### Changes Made

| Location | Change |
|---|---|
| `appendix.tex:9-12` | Added shared setup paragraph: checkpoint source (`openvla/openvla-7b`), dataset (LIBERO-Goal, N=63,228), hardware (2× RTX PRO 6000 Ada, 48 GB), seed (42), cross-refs to §3.1--§3.6, LIBERO-Spatial protocol |
| `appendix.tex:287` | Added explicit sample count for LIBERO-Spatial: "10 out-of-distribution tasks × 50 demonstrations each" |
| `appendix.tex:517` | QA Probe: specified logistic regression (C=1.0, max_iter=1000), corrected labeling (4-class progress from equal temporal segments, binary subtask), added 80/20 split |

### Compilation
- 0 errors
- 27 pages (within ≤ 28 limit)

---
