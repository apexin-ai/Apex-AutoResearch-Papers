# ops westd41074 kill bad eval and verify checkpoint

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd41074-kill-bad-eval-and-verify-checkpoint_20260521T004757_result.json`
- **Structured JSON:** [`60e4cd56e43272a69a21.json`](../../sessions/60/60e4cd56e43272a69a21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已注册为 RUNNING。

---

## 任务完成报告

### Step 1: Kill 无效 eval
- PID 692941 **kill 成功**（graceful SIGTERM，未 force kill）
- GPU 1 已释放（0% → 被新 eval 重新占用）

### Step 2-3: Checkpoint 下载状态
| Checkpoint | 状态 | 详情 |
|---|---|---|
| **Spatial** | **COMPLETE** | 4 shards (4.6G+4.7G+4.7G+251M)。aria2c 已下载完整数据但进程 stalled，手动 kill + 清理 .aria2 |
| **Goal** | **COMPLETE** | 4 shards，无 .aria2 文件 |
| **LIBERO-10** | **COMPLETE** | 4 shards，无 .aria2 文件 |

### Step 4: Spatial 完整性验证
- 4/4 shards 全部通过 safetensors 验证（982 tensors, 14384 MB）
- config.json: EXISTS
- dataset_statistics.json: EXISTS

### Step 5: Eval 启动
- **tmux session**: `eval_openvla_baseline_spatial_v2`
- **PID**: 701587 (主进程)
- **GPU**: 1 (16082 MiB, 84% util)
- **Registry**: `eval_openvla_baseline_spatial_seed42_v2` → RUNNING
- 初始日志确认：模型加载成功，k=1.0（full baseline），10 tasks × 50 episodes = 500 total，Task 1 已开始

### Step 6: Goal / LIBERO-10
两个 checkpoint 均已完整下载，可随时启动对应 eval。

---
