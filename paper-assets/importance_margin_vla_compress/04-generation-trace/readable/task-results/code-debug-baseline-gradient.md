# code debug baseline gradient

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_debug-baseline-gradient_20260515T150117_result.json`
- **Structured JSON:** [`cc8430571cf52c75d901.json`](../../sessions/cc/cc8430571cf52c75d901.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Training is healthy and converging:

| Step | Loss | Grad Norm |
|------|------|-----------|
| 0 | 3.4066 | 4.62 |
| 50 | 4.2220 | 4.55 |
| 100 | 0.3337 | 2.18 |
| 150 | 0.1344 | 1.25 |
| 200 | 0.0334 | 0.61 |

---

**Bug**: `SmolVLAPolicy.forward()` applies `action_is_pad` masking (zeros out padded timestep losses) then computes `losses.mean()` dividing by ALL elements including the masked zeros. With `chunk_size=50` and short episodes, most action chunks are heavily padded, so the mean is diluted to near-zero → near-zero gradients. The IMM wrapper bypassed this entirely by computing flow matching loss directly without pad masking.

**Fix**: Added `baseline_forward(policy, batch)` at line 280 of `train.py` that calls `policy.model.forward()` directly (bypassing `SmolVLAPolicy.forward()`'s pad masking), slices to `action_dim=14`, and computes `losses.mean()` without any `action_is_pad` reduction. The baseline training loop now calls this function instead of `model(batch)`.

**Training**: Running in tmux session `mvp_baseline`, loss dropping from 3.4→0.03 by step 200 with non-zero gradients throughout. Matches IMM anchor's convergence behavior.

---
