# code behavioral pilot w4

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_behavioral_pilot_w4_20260518T093458_result.json`
- **Structured JSON:** [`bdbee60cf3392400837c.json`](../../sessions/bd/bdbee60cf3392400837c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment is running — Task 0 baseline condition, first episode initializing. The experiment has 3 tasks × 2 conditions × 10 episodes = 60 episodes total. Each episode runs up to 300 steps with model inference per step, so this will take a while within the 3h timeout.

Summary of what was done:

1. **Phase 1 (EGL rendering)**: Already fixed in the previous session — `libegl-mesa0 libegl-dev` installed, `MUJOCO_GL=egl` works.

2. **Phase 2 (behavioral_pilot.py)**: Rewrote the script with two critical fixes:
   - **`prepare_inputs_for_generation` bug**: transformers 4.57.6 passes an empty `DynamicCache` (not `None`), causing the old code to truncate all input_ids to 1 token on every call — including prefill. This made the model ignore the image and instruction entirely. Fixed by bypassing `generate()` with manual autoregressive generation that calls `model.forward()` directly.
   - **Ablation now works**: With proper prefill (full sequence processed in the multimodal branch), `eager_attention_forward` replacement triggers correctly. Verified: 8 ablation triggers per action (1 prefill + 7 generation steps), actions differ between baseline and ablated (max diff 0.957).
   - Also reverted LIBERO patches that were incorrectly applied for robosuite 1.5.2 (actual version is 1.4.1): `base_types` → `mount_types`, `renderer="mjviewer"` → `"mujoco"`, restored `controller_configs`.

3. **Phase 3**: Submitted as `behavioral_pilot_w4` on `westd-19183`, GPU `cuda:0`, 3h timeout. Log at `~/runs/vla-ssd/behavioral_pilot_w4.log`.

---
