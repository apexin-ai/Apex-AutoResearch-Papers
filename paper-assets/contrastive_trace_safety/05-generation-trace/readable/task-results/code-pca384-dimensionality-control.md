# code pca384 dimensionality control

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pca384_dimensionality_control_20260517T190710_result.json`
- **Structured JSON:** [`e20394a939aa1d83c130.json`](../../sessions/e2/e20394a939aa1d83c130.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment completed successfully. Results summary:

```
Model      | Metric     | PCA384-HS | Text-384 |    Delta |  p-value | Holm-Bonf
------------------------------------------------------------------------------------------
r1-8b      | bal_acc    |    0.7001 |   0.6875 |  +0.0126 |   0.7310 |       fail
r1-8b      | precision  |    0.8162 |   0.5852 |  +0.2310 |   0.0000 |     REJECT
r1-8b      | FPR        |    0.0668 |   0.1614 |  -0.0947 |   0.0030 |     REJECT
ot-7b      | bal_acc    |    0.7558 |   0.6430 |  +0.1128 |   0.0000 |     REJECT
ot-7b      | precision  |    0.5225 |   0.3545 |  +0.1681 |   0.0000 |     REJECT
ot-7b      | FPR        |    0.1207 |   0.2477 |  -0.1270 |   0.0000 |     REJECT
qwq-32b    | bal_acc    |    0.8116 |   0.6504 |  +0.1612 |   0.0000 |     REJECT
qwq-32b    | precision  |    0.6080 |   0.4213 |  +0.1867 |   0.0000 |     REJECT
qwq-32b    | FPR        |    0.1730 |   0.2871 |  -0.1141 |   0.0380 |       fail
r1-32b     | bal_acc    |    0.7471 |   0.6461 |  +0.1011 |   0.0110 |     REJECT
r1-32b     | precision  |    0.6343 |   0.4503 |  +0.1840 |   0.0020 |     REJECT
r1-32b     | FPR        |    0.2256 |   0.3809 |  -0.1553 |   0.0060 |     REJECT
```

**10/12 tests reject H0 after Holm-Bonferroni correction.** Even when HS features are PCA-reduced to exactly 384d (matching text dimensionality), they significantly outperform text embeddings. The two non-significant results (r1-8b bal_acc at p=0.731, qwq-32b FPR at p_adj=0.076) are both cases where the HS probe still has better raw numbers.

PCA explained variance: r1-8b 79.3%, ot-7b 82.8%, qwq-32b 88.1%, r1-32b 92.4%.

Script at `/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r5_pca384_control.py`, results at `artifacts/exp_r5_pca384/results.json`.

---
