# ops verify westd41074 gpu1 and launch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-westd41074-gpu1-and-launch_20260521T002536_result.json`
- **Structured JSON:** [`b1fe3d4b59de7c4a21b5.json`](../../sessions/b1/b1fe3d4b59de7c4a21b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动并运行。

## 结果汇总

| 项目 | 状态 |
|------|------|
| **GPU 1** | 空闲→已占用（66% util, 16082 MiB），实验正在运行 |
| **Checkpoint 完整性** | 4/4 shard 均通过 safetensors 加载验证（760+109+112+1=982 tensors）。.aria2 残留已清理 |
| **实验** | 已启动，tmux session `eval_spatial_baseline` |
| **配置** | `--mode random_prune --k_ratio 1.0 --suite libero_spatial --num_episodes 50 --seed 42` |
| **任务进度** | Task 1/10 已开始（10 tasks × 50 episodes = 500 total） |
| **输出** | `eval_results/openvla_baseline_spatial_seed42.json` + `.log` |

---
