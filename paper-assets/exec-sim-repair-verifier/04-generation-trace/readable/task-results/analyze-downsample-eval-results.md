# analyze downsample eval results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_downsample-eval-results_20260519T061354_result.json`
- **Structured JSON:** [`4897ce0cadc028d16bf8.json`](../../sessions/48/4897ce0cadc028d16bf8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The eval was **never launched**. Here's the situation:

**Training (`exp-downsample-cls-func-v3`):** Completed successfully.
- Best checkpoint: epoch 2, eval_loss = 0.0907
- Checkpoint path: `/root/autodl-tmp/checkpoints_cls_downsample_qwen3_4b/best`
- Already registered with `conclusion=success`

**Eval (`exp-downsample-cls-func-v3-eval`):** Does not exist in registry. No eval output files found anywhere on the server (no logs, no JSON results, no predictions). The PID 802400 mentioned in the task left no trace.

The training status is already properly registered, but the eval needs to be launched. The eval script is `eval_repo_cls.py` based on prior experiments (e.g., `eval_cls_seed0.json` shows Qwen3-4B full-data function-level = 87.94% accuracy at seed 0).

Want me to launch the downsample eval on the server? The command would use `eval_repo_cls.py` with the downsample checkpoint at `/root/autodl-tmp/checkpoints_cls_downsample_qwen3_4b/best` against the test set.

---
