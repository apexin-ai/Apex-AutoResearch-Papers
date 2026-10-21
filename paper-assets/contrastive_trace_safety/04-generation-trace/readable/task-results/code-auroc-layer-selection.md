# code auroc layer selection

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_auroc_layer_selection_20260517T190736_result.json`
- **Structured JSON:** [`3d4e85b70d7e53a43936.json`](../../sessions/3d/3d4e85b70d7e53a43936.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment complete. Here's the full summary:

```
Model     | AUROC-best Layer  | Paper Layer  | Match?  | AUROC@best  | AUROC@paper
----------+------------------+-------------+--------+------------+------------
r1-8b     | L13               | L14          | No      | 0.8060      | 0.8031
ot-7b     | L1                | L16          | No      | 0.7770      | 0.7463
qwq-32b   | L32               | L60          | No      | 0.8390      | 0.7561
r1-32b    | L31               | L63          | No      | 0.8972      | 0.7668
```

**Key findings:**

1. **R1-8B**: Near-match. AUROC selects L13 vs paper's L14 (delta = 0.003, adjacent layers in top-3). Both are "early" within the stored range [12-24]. AUROC confirms early-deep layers are best.

2. **OT-7B**: Mismatch. AUROC selects L1 (shallowest, 0.777) over paper's L16 (0.746). However, the AUROC landscape is flat (range 0.70–0.78 across all 28 layers), suggesting weak layer preference.

3. **QWQ-32B**: AUROC selects L32 (mid-depth, 50th percentile, 0.839) vs paper's L60 (94th percentile, 0.756). A clear broad peak at layers 25-50.

4. **R1-32B**: AUROC selects L31 (0.897) vs paper's L63 (0.767). Strong mid-depth peak at layers 25-50 with second plateau at layers 40-50.

**Answer to key question**: AUROC does NOT consistently select the same deep layers as the paper's multi-metric approach. For 32B models, AUROC prefers mid-depth (~50% of total layers) rather than the very deep layers (>90% depth) selected by the paper. For R1-8B it approximately agrees (all stored layers are already deep). The PCA reduction (256 dims) on 32B models may affect this, but the trend is clear.

Results saved to `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r5_auroc_sweep/results.json`.

---
