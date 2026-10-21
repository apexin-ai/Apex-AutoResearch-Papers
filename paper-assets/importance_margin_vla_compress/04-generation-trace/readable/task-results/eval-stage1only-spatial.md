# eval stage1only spatial

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_stage1only_spatial_20260517T065126_result.json`
- **Structured JSON:** [`415a4d68cc018ce80db9.json`](../../sessions/41/415a4d68cc018ce80db9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**状态汇总：**
- `eval_stage1only_spatial` 已在 westd-27271 GPU 1 上启动（PID 65128, tmux session `eval_stage1only_spatial`）
- Checkpoint: `stage1_done/checkpoint.pt`，config: `libero_imm_twostage_fullft.yaml`
- Suite: `libero_spatial`, 10 tasks × 50 episodes = 500 rollouts
- 日志确认模型已加载（14s），正在评估 Task 0
- Registry 已注册为 RUNNING

注意：杀掉了 GPU 1 上之前的 `eval_stage1only_k07_object` 进程（PID 3092）。如果那个实验还需要，后续需要重跑。

---
