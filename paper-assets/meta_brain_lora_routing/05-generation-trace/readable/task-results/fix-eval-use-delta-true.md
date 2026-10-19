# fix eval use delta true

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_use_delta_true_20260516T143449_result.json`
- **Structured JSON:** [`3445d41be4476624c86d.json`](../../sessions/34/3445d41be4476624c86d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`ablation_ladder.py` doesn't pass `use_delta_actions`, so it gets the default `True` — correct.

**Summary of changes:**

1. **`meta_brain_assembly.py:from_checkpoints()`** — Added `use_delta_actions: bool = True` parameter. Changed line 697-699 to discard `_build_norm_stats`'s `use_delta` flag and use the explicit parameter instead. This ensures LeRobot-format checkpoints (which return `use_delta=False` from `_build_norm_stats`) now correctly get `use_delta_actions=True` by default.

2. **`evaluate_libero_plus.py:558`** — Wired `use_delta_actions=not args.no_delta_actions` through to `from_checkpoints()`, matching the existing behavior in the `from_dummy` path.

The data flow is now correct for pi0_libero:
```
model_output → unnormalize(×std + mean) → AbsoluteActions(actions[:6] += state[:6]) → LiberoOutputs([:7]) → env.step()
```

---
