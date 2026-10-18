# eval smolvla k095 pruning

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_smolvla_k095_pruning_20260518T121311_result.json`
- **Structured JSON:** [`7ec2fddd49079e23598f.json`](../../sessions/7e/7ec2fddd49079e23598f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交并运行：

- **实验**: `eval_smolvla_random_prune_k095`
- **服务器**: cqa1-33015, GPU 1
- **PID**: 92881 (tmux session: `eval_random_k095`)
- **Pruning**: random true_removal, k=0.95, keep 121/128 tokens, remove 7
- **Checkpoint**: `libero_full_ft/step_099999` (baseline full_ft)
- **任务**: 10 tasks × 50 episodes = 500 total
- **日志**: `~/runs/importance_margin_vla_compress/eval_smolvla_random_prune_k095.log`

首个 episode 已确认 FAIL (T0 Ep1)。预计 ~2-3h 完成。

---
