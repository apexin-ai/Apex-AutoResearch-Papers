# fix pooled rho computation

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_pooled-rho-computation_20260516T060056_result.json`
- **Structured JSON:** [`ce716279f5f37e891947.json`](../../sessions/ce/ce716279f5f37e891947.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

```
=== POOLED RHO (all 27,529 samples) ===
hapax_ratio:  -0.6467
ttr:          -0.6302
entropy_mean: -0.6098
entropy_min:  -0.4061
entropy_max:   0.0503
tail_decay:   -0.0403
entropy_std:  -0.1996

=== PER-GEN MEDIAN RHO ===
hapax_ratio:  -0.6624
ttr:          -0.6428
entropy_mean: -0.6204
entropy_min:  -0.3968
entropy_max:   0.0764
tail_decay:   -0.0796
entropy_std:  -0.2088
```

The wrong values (Qwen3-8B only) were systematically attenuated — the true pooled correlations are substantially stronger for all drifting features (e.g., hapax: -0.558 → -0.6467, entropy_mean: -0.475 → -0.6098, entropy_std: -0.076 → -0.1996).

Completed:
1. `results/pooled_rho_fix.json` — saved with both pooled and per-gen median values
2. `scripts/plot_fig1_strip.py` — `overall` dict updated with true pooled rho
3. `fig1_differential_response.{pdf,png}` — regenerated with corrected values

---
