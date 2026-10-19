# code augment spatial v2

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_augment_spatial_v2_20260516T024435_result.json`
- **Structured JSON:** [`57b50a899907fba07db3.json`](../../sessions/57/57b50a899907fba07db3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done.

**Approach chosen: Plan B (image-level distractor compositing)**

**Why not Plan A:** LIBERO env API works (verified `OffScreenRenderEnv` loads `_add_N` BDDLs and renders 128×128 agentview), but full re-render needs (a) GPU rendering while cuda:0–3 are running training, (b) per-frame init_state + action replay (~2 s reset + ~50 ms/step), and (c) restructuring the LeRobot parquet pipeline. Online per-batch is infeasible; offline preprocess collides with the GPU constraint.

**What changed (server `/root/meta_brain_lora_routing/phase1/`):**
- `augment_spatial.py` (new, 151 lines) — `SpatialAugmentation` pastes 1–N synthetic distractor patches per image (random ellipse/rect masks, soft alpha, per-color shading, lower-frame bias, center-keepout). Operates on `(B,C,H,W)` or `(C,H,W)` in `[-1,1]`.
- `data_loader.py` — added `from phase1.augment_spatial import SpatialAugmentation`; replaced `SpatialAugmentationPlaceholder` class with a back-compat alias; `build_perturbation_augmenter("spatial")` now routes spatial as `image_aug` (it modifies images, not state); `apply_perturbation` universal branch routes `kind in ("visual","spatial")` to the images dict; module docstring + dispatch comments updated. Pre-edit copy kept at `data_loader.py.bak_pre_spatial`.

**Verification:**
- Spatial bundle: `image_aug=SpatialAugmentation, state_aug=None` ✓
- `apply_perturbation` on Observation: images change, state untouched ✓
- Universal end-to-end (15 iters, mixed picks) no crash ✓
- All outputs in `[-1,1]` ✓
- `phase1/spatial_augmentation_preview.png` (224×448) saved for visual inspection
- GPU 0–3 still 8.2 GB each (training untouched) ✓

---
