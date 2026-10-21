## OFT Eval Smoke Test — libero_object

### Result: 6/6 SUCCESS (100%)

### Environment (working)
- Python 3.10.20
- torch 2.2.0+cu121
- tensorflow 2.15.0 (REAL)
- transformers 4.40.1 (custom fork)
- robosuite 1.4.1
- mujoco 3.8.1
- numpy 1.26.4
- timm 0.9.10
- peft 0.11.1
- GPU: NVIDIA RTX 4090 D (24GB)

### Root Cause of Previous 0% SR
The old base conda env (Python 3.12) could not install tensorflow 2.15.0. A dummy TF module was used with PIL fallbacks for:
1. `resize_image_for_policy` — JPEG encode/decode + resize
2. `center_crop_image` — crop_and_resize (TF uses bilinear, PIL used LANCZOS)

The PIL fallback produced subtly different image preprocessing vs the TF pipeline used during training. Combined with robosuite 1.4.0 (instead of 1.4.1), this caused 0% success rate.

### Fix
Created clean conda env at `/root/autodl-tmp/envs/openvla-oft` with Python 3.10, matching the official OFT setup docs exactly. Reverted all code modifications (libero_utils.py, openvla_utils.py) to git HEAD.

### Full Eval
PID 23737, 50 trials × 10 tasks, log at /tmp/eval_full.log
