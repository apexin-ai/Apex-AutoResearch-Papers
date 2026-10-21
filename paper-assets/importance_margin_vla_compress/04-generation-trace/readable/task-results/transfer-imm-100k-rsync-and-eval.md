# transfer imm 100k rsync and eval

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_transfer_imm_100k_rsync_and_eval_20260517T003847_result.json`
- **Structured JSON:** [`1f2e8245779b1153db50.json`](../../sessions/1f/1f2e8245779b1153db50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇报：

```
=== IMM 100K CHECKPOINT ===
Path (cqa1): /root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt
Size: 879MB
Rsync to westd: SUCCESS (08:41)

=== COMPLETED EVAL RESULTS ===
IMM twostage fullft 100K — libero_object (acis_prune): SR = 15.4% (77/500)
Full FT 100K seed42   — libero_object (baseline):    SR = 44.8%
Full FT 100K seed0    — libero_object (baseline):    SR = 51.0%
Full FT 100K seed0    — libero_spatial (baseline):   SR = 51.8%

=== IMM 100K EVAL RUNNING ===
cuda:0 — libero_spatial, acis_prune, 50eps/task (tmux: imm_100k_eval_spatial)
cuda:1 — libero_goal, acis_prune, 50eps/task (tmux: imm_100k_eval_goal)
```

注意：IMM libero_object 15.4% 大幅低于 baseline (44.8-51%)。spatial 和 goal 正在跑（~每 task 5-7 min × 10 tasks ≈ 50-70 min 完成）。

另外：westd 上 `expert_only_ft` 仍在跑 (step 8950/100000)，但只占 ~3.3GB/GPU，不影响 eval。

---
