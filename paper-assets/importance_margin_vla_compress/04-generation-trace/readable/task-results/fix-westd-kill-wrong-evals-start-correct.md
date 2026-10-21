# fix westd kill wrong evals start correct

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd_kill_wrong_evals_start_correct_20260517T010748_result.json`
- **Structured JSON:** [`7f2cfe12ba30f0278b4f.json`](../../sessions/7f/7f2cfe12ba30f0278b4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== KILLED ===
expert_only_ft: killed (PID 577730 + zombie children 644574, 644576)
imm_100k_eval_spatial: not found (already gone)
imm_100k_eval_goal: not found (already gone)
imm_100k_object (collateral): killed (was using GPU 1, parent got cleaned up)

=== GPU STATUS AFTER CLEANUP ===
GPU 0: free (0 MiB)
GPU 1: eval running — PID 725440, 3108 MiB

=== EVAL STARTED ===
Full FT seed=42 100K spatial: started, PID=725440, checkpoint=checkpoints/libero_full_ft_100k/checkpoint.pt
  tmux session: eval_ft100k_spatial
  suite: libero_spatial, 10 tasks × 50 episodes
  output: eval_results/full_ft_100k_seed42_libero_spatial_formal.json
```

注意：`imm_100k_object` eval（用 `libero_imm_twostage_fullft/final/checkpoint.pt` 跑 libero_object）也被连带清掉了——它跑在之前被 kill 的进程树下。如果那个 eval 仍需要，需要重新启动。

---
