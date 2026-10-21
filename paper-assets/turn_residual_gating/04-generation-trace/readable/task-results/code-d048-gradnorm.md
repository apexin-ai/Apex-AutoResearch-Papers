# code d048 gradnorm

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d048_gradnorm_20260522T102920_result.json`
- **Structured JSON:** [`b659204d47c21e4f4eca.json`](../../sessions/b6/b659204d47c21e4f4eca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Syntax verified, dry-run dir cleaned. Here's the summary:

**`train_phase2_gradnorm.py` — creation + verification report:**

| Check | Status |
|-------|--------|
| `--help` argparse | PASS — `--gradnorm`, `--gradnorm-alpha`, `--gradnorm-lr` present |
| Syntax check | PASS |
| Dry-run training | BLOCKED — GPU occupied by `train_phase2_v8b.py` (d048_ss_s42, seed 42, 3 epochs). Only ~35 GiB free of 97 GiB. |

**OOM fix applied:** The original implementation used two `autograd.grad(retain_graph=True)` calls on the same computation graph, which OOMed on the second call. Restructured `gradnorm_step` to:
1. Run its own dedicated forward pass (separate computation graph)
2. First `autograd.grad(retain_graph=True)` for NTP gradient norm
3. `del grads + torch.cuda.empty_cache()` cleanup
4. Second `autograd.grad(retain_graph=False)` for GAR gradient norm — graph fully released
5. Moved to execute after `loss.backward()` in the training loop (training .grad preserved since `autograd.grad` doesn't touch .grad)

**File:** `/root/turn_residual_gating/src/train_phase2_gradnorm.py` (21408 bytes, 524 lines)

Dry-run verification needs to happen once the d048_ss_s42 job finishes or on a free GPU.

---
