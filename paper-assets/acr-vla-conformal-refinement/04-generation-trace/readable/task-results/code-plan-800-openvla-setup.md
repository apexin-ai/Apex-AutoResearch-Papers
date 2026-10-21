# code plan 800 openvla setup

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_800-openvla-setup_20260517T132218_result.json`
- **Structured JSON:** [`05a4d89fa05cc706eb42.json`](../../sessions/05/05a4d89fa05cc706eb42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Task plan_800 complete. Summary:

**OpenVLA on bjb1-18228 is fully set up and validated.**

- **Model**: `openvla-7b-libero-spatial`, 15.1 GB VRAM (bf16), loaded at `/root/autodl-tmp/models/openvla-libero-spatial/`
- **4 compatibility patches** applied to bridge transformers 4.40.1 → 5.8.0 (auto class rename, local module loading, import path fixes, init signature fixes)
- **3 new files**: `openvla_wrapper.py` (interface-compatible with SmolVLAWrapper), `openvla_eval.py` (standalone LIBERO eval), `test_openvla_load.py` (sanity check)
- **Pipeline validated**: single-episode LIBERO-Spatial rollout ran successfully at ~180ms/step
- **Setup report** registered as artifact `art_20260517_4013ce`

Key CRM integration consideration: OpenVLA has hidden_dim=4096 (vs 960) and chunk_size=1 (vs 5), so CRM/CGS dimensions need adaptation for cross-VLA generalization.

---
