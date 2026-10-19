# ops steps curve fix rerun

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_steps-curve-fix-rerun_20260516T221304_result.json`
- **Structured JSON:** [`fc81094af68caa3ce016.json`](../../sessions/fc/fc81094af68caa3ce016.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练进行中。当前进度：Step 40/1000。预计约 16 分钟完成。我会在 ~4.5 分钟后检查中间进度。

**当前状态小结：**
1. **cuda:0 τ ablation**：正在运行 `--tau_start 0.5 --tau_end 0.5`（固定 τ=0.5 实验），PID 275628。但未使用 nohup+日志重定向（违反 C002），且不在 tmux session 中。如果 SSH 断开可能会丢失。
2. **cuda:1 steps_curve**：已通过 tmux 提交（session `steps_curve_s42_v3`），离线环境变量 + WANDB_MODE=disabled 设置正确，正在训练中。

---
