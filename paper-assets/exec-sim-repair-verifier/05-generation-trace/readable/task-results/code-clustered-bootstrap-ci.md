# code clustered bootstrap ci

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_clustered-bootstrap-ci_20260512T090633_result.json`
- **Structured JSON:** [`f77bc262dc2a5d6e906e.json`](../../sessions/f7/f77bc262dc2a5d6e906e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The full pipeline completed. Here are the results:

## Clustered Bootstrap CI Results

**Key finding: When properly aligned at the code-variant level, cls and traj show no significant difference.**

### Per-Seed Clustered Bootstrap (cls_problem_acc − traj_acc, at variant level)

| Seed | cls_problem_acc | traj_acc | Gap (pp) | 95% CI | p-value | DEFF |
|------|----------------|----------|----------|--------|---------|------|
| 42   | 85.17% | 85.66% | −0.30 | [−2.46, 1.94] | 0.779 | 1.28 |
| 123  | 87.02% | 85.47% | +1.36 | [−0.73, 3.41] | 0.185 | 1.29 |
| 456  | 85.37% | 87.40% | −2.16 | [−4.30, −0.18] | 0.031 | 1.52 |

### Pooled Across Seeds

- **Mean gap**: −0.37pp
- **Clustered bootstrap 95% CI**: [−1.89, +1.07]
- **p-value**: 0.646
- **DEFF**: 0.84

### Seed-Level Paired Analysis (original eval-level comparison)

- Per-seed gap (cls_eval_acc − traj_acc): {42: +2.17, 123: +4.05, 456: +0.48}
- Mean gap: +2.23pp, p=0.163 (not significant, K=3)

### Interpretation

The seed-level analysis (mean gap +2.23pp) was misleading because it compared **per-test classification accuracy** (1890 tests) with **per-variant trajectory accuracy** (1032 variants) — an apples-to-oranges comparison. When cls predictions are aggregated to the variant level (cls_problem_acc), the gap shrinks drastically and even reverses direction. The pooled clustered bootstrap finds no significant difference (gap=−0.37pp, p=0.65).

Full results saved to `/home/sonny/exec-sim-repair-verifier/clustered_bootstrap_results.json`.

---
