# fix plan 005 formal bound

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan_005_formal_bound_20260516T150723_result.json`
- **Structured JSON:** [`7a481792caafee1a258f.json`](../../sessions/7a/7a481792caafee1a258f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment running well — both GPUs at 95%+ utilization, evaluation proceeding. The fix works.

**Summary:**

- **Fix**: Already in place at `eval_formal_bound.py:137-138` — uses `model.policy` to get the `SmolVLAPolicy` before calling `get_tokenizer_from_policy()`
- **Root cause of original hang**: Missing `HF_HUB_OFFLINE=1` and `source /etc/network_turbo` — the process stalled on HF Hub API calls
- **Experiment status**: Running in tmux `plan_005_formal_bound` on westd-27271
  - Model loaded, checkpoint applied
  - L_spectral = 1.067233, L_empirical = 0.192756
  - 500 batches pre-loaded
  - Currently evaluating epsilon levels (GPUs at 95%)
  - Output: `results/formal_bound_plan005.json`
  - Log: `logs/plan_005_formal_bound.log`

---
