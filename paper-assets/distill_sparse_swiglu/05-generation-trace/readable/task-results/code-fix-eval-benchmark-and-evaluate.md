# code fix eval benchmark and evaluate

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_eval_benchmark_and_evaluate_20260515T222904_result.json`
- **Structured JSON:** [`dde76bf33666b03d7b5a.json`](../../sessions/dd/dde76bf33666b03d7b5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

C4 still downloading. Here are the final deliverables:

---

## eval_benchmark.py Code Diff (4 Bugs Fixed)

**Bug 1 — TEAL function** (`compute_static_masks`):
```diff
-    from evaluate import teal_activation_magnitude_masks
-    return teal_activation_magnitude_masks(model, calib_ids, sparsity_target)
+    from evaluate import vanilla_teal_global_masks
+    return vanilla_teal_global_masks(model, calib_ids, sparsity_target)
```
`teal_activation_magnitude_masks` = greedy per-layer allocation (no cross-layer normalization). `vanilla_teal_global_masks` = global top-k with per-layer mean normalization.

**Bug 2 — WINA function**:
```diff
-    from baselines import wina_greedy_allocation_masks
-    device = next(model.parameters()).device
-    return wina_greedy_allocation_masks(model, calib_ids, sparsity_target, device=device)
+    from evaluate import wina_global_masks
+    return wina_global_masks(model, calib_ids, sparsity_target)
```

**Bug 3 — Sample limit**:
```diff
-    p.add_argument("--max_ppl_samples", type=int, default=200,
+    p.add_argument("--max_ppl_samples", type=int, default=0,
```

**Bug 4 — Missing uniform baseline** (added to CONDITIONS + `compute_static_masks`):
```python
("uniform_50", {"mode": "static_mask", "method": "uniform"}),
```
```python
elif method == "uniform":
    from evaluate import _collect_swiglu_magnitudes
    avg_mag = _collect_swiglu_magnitudes(model, calib_ids)
    # per-layer topk by activation magnitude
    ...
```

## evaluate.py Part B

`_global_topk_masks` (line 125) **already has per-layer mean normalization** — no change needed.

## WikiText-2 PPL Comparison Table (50% sparsity, LLaMA-3.1-8B)

| Condition | Mode | Measured PPL | Registry | Match |
|-----------|------|-------------|----------|-------|
| Dense | — | **6.1173** | 6.12 | ✓ |
| KL-only s42 | predictor hard_mask | **9.2142** | 9.21 | ✓ |
| STE s42 | predictor hard_mask | **8.1762** | 8.18 | ✓ |
| SPON s42 | spon bias | **8.9968** | 8.99 | ✓ |
| Uniform 50% | static per-layer topk | **23.8998** | 23.90 | ✓ |
| Vanilla TEAL | static global topk | **23.3113** | 23.31 | ✓ |
| BCE+comp s42 | predictor+comp | **25.4384** | 25.44 | ✓ |
| WINA | static global topk | **27.9262** | 27.93 | ✓ |
| BCE s42 | predictor hard_mask | **27.9603** | 27.96 | ✓ |
| R-Sparse | static global topk | **151.2021** | — | new |

### Sparsity 70% (kl_sparsity70_s42_v2)

| Metric | Before Fix | After Fix |
|--------|-----------|-----------|
| TEAL sparse PPL | **136,069.61** | **17.91** |
| Predictor hard_mask PPL | 13.84 | 13.84 (unchanged) |

## C4 Cache Status

PID 169446 still downloading C4 validation split via streaming. Will save to `/root/autodl-tmp/data/c4_val/`. Check `/tmp/cache_c4.log` for completion.

## Registry Updates Applied

- `kl_sparsity70_s42_v2.metrics.teal_sparse_ppl`: 136069.61 → **17.91** (old value preserved as `teal_sparse_ppl_old_broken`)
- `training_free_baselines.metrics.rsparse_global_ppl`: added **151.2**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "mode": "static_mask",
    "method": "uniform"
  }
}
```

</details>

---
