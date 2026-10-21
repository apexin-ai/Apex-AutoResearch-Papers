# kill westd38929 gpu1 deploy seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_kill-westd38929-gpu1-deploy-seed43_20260523T203159_result.json`
- **Structured JSON:** [`a1269e4a05f36c2f4052.json`](../../sessions/a1/a1269e4a05f36c2f4052.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**汇总：**
- **冗余进程清理**: kill 590999/596725/596716 + tmux sessions 已清理，GPU 1 验证 1 MiB / 0%
- **部署修正**: 首次部署漏了 `CUDA_VISIBLE_DEVICES=1` 导致进程落 GPU 0，已 kill 并用 `CUDA_VISIBLE_DEVICES=1` 重新部署到 GPU 1
- **新实验**: `eval_xvla_random_k05_goal_seed43` — PID 788647, GPU 1, 4838 MiB, 正在执行 Task 0
- **状态机**: RUNNING, hypothesis 已设置

---
