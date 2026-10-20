# eval v4 vanilla seed7 eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v4-vanilla-seed7-eval_20260515T144718_result.json`
- **Structured JSON:** [`1dae9c30adfe1765265b.json`](../../sessions/1d/1dae9c30adfe1765265b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **Checkpoint**: `checkpoints/mini_vanilla_sft_v4_seed7/v1-20260515-214032/checkpoint-1635`
- **Eval 进程**: PID 160587, tmux session `v4-vanilla-seed7-eval`, cuda:1
- **命令**: `python3 eval/recovery.py --model_path &lt;ckpt> --base_model Qwen3-8B --no_inject --num_episodes 47 --device cuda:1 --seed 42`
- **Registry**: `v4-vanilla-seed7-eval` 状态 RUNNING, parent=v4-vanilla-seed7
- **Cron**: 每 5 分钟检查状态，完成后自动更新 metrics 并与 seed=42 baseline (61.7%) 对比

---
