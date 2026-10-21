# Baseline Script Fix: Sync & Dry Run Verification Report

**Date:** 2026-05-23
**Script:** `train_pi05_lora_baseline.py` (dummy scalar fix for Phase 1 frozen params)

## 1. File Sync Verification

| Server | md5sum | Match |
|--------|--------|-------|
| westd-45947 | `3809d1a0a56748a86552c4d09aa572ac` | ✓ |
| westd-35807 | `3809d1a0a56748a86552c4d09aa572ac` | ✓ |

## 2. Dry Run Results

### westd-45947 (conda base, RTX PRO 6000 x2)

```
Phase 1 (step 0):
  - loss=0.1203, grad_norm=0.00, time=17.0s
  - GPU mem: allocated=7.62GB, reserved=19.26GB
  - No RuntimeError

Phase transition (step 1):
  - "Phase 2: unfroze 33472512 LoRA params at step 1 (LoRA grad warmup: 100 steps)"

Phase 2 (step 1):
  - loss=0.1677, grad_norm=0.00, time=20.1s
  - GPU mem: allocated=7.69GB, reserved=27.45GB
  - No RuntimeError

Training: 100% | 2/2 completed
```

### westd-35807 (conda libero, RTX PRO 6000 x4)

```
Phase 1 (step 0):
  - loss=0.1203, grad_norm=0.00, time=13.6s
  - GPU mem: allocated=7.62GB, reserved=19.26GB
  - No RuntimeError

Phase transition (step 1):
  - "Phase 2: unfroze 33472512 LoRA params at step 1 (LoRA grad warmup: 100 steps)"

Phase 2 (step 1):
  - loss=0.1677, grad_norm=0.00, time=23.8s
  - GPU mem: allocated=7.69GB, reserved=27.45GB
  - No RuntimeError

Training: 100% | 2/2 completed
```

## 3. Model Architecture (both servers identical)

- Backbone params: 3650.23M
- LoRA PaliGemma (rank=16): 19.61M
- LoRA Action Expert (rank=32): 13.86M
- LoRA total: 33.47M

## 4. Note on Trainable Param Count

`[Step 0] Trainable params: 0` — the dummy scalar is stored on the hooks object, not as a named parameter of the model. It reaches the optimizer via `extra_params()` and keeps the gradient graph alive through `action_loss + 0.0 * self._dummy`. This is correct behavior.

## 5. Conclusion

**PASS** — Both servers synced and verified. The dummy scalar fix resolves the Phase 1 frozen-params crash. Phase 1 to Phase 2 transition works correctly with 33.47M LoRA params unfreezing at the specified step.
