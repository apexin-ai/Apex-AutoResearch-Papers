# ops westd38929 gpu2 smolvla baseline spatial

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-gpu2-smolvla-baseline-spatial_20260521T003643_result.json`
- **Structured JSON:** [`f4b03ba325ab47f95f80.json`](../../sessions/f4/f4b03ba325ab47f95f80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval running smoothly. Summary:

- **Experiment**: `eval_smolvla_baseline_spatial_seed42` — RUNNING on westd-38929 GPU 2
- **PID**: 224849 (2.8 GB VRAM, GPUs 0/1/3 untouched)
- **tmux session**: `smolvla_baseline_spatial`
- **Log**: `logs/smolvla_baseline_spatial_seed42.log`
- **Output**: `eval_results/smolvla_baseline_spatial_seed42.json`
- **Progress**: Task 0, Ep 9/50 — 4 SUCCESS out of 8 (50% so far on task 0)
- **Rate**: ~8s/episode (280 max steps for fails, faster for successes)
- **Estimated total time**: 10 tasks × 50 eps × ~8s ≈ ~65 min

Key fixes applied:
1. Replaced `LiberoEnv` with `OffScreenRenderEnv` (raw robosuite obs format)
2. Bypassed LIBERO-Plus benchmark class (returns perturbation variants with missing XML assets) — hardcoded original 10 base task names
3. Adapted `extract_state()` and `obs_to_batch()` for raw robosuite obs keys (`robot0_eef_pos`, `agentview_image`, etc.)
4. Patched `torch.load` for PyTorch 2.6+ `weights_only=True` default
5. Registered in experiment registry with full provenance metadata

---
