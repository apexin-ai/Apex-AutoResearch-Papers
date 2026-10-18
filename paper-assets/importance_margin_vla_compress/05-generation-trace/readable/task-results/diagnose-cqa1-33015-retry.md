# diagnose cqa1 33015 retry

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1-33015-retry_20260525T195417_result.json`
- **Structured JSON:** [`912e659063268afc2eb6.json`](../../sessions/91/912e659063268afc2eb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 服务器身份
**cqa1-33015 和 westd-27271 是两台独立服务器**，hostname 不同：
- cqa1-33015: `autodl-container-61bb4e82b9-0e2cbbac`，192 核 Xeon 8481C，**4x RTX 4090 D (24GB)**
- westd-27271: `autodl-container-d15845a561-f0370fb9`，2 GPU

### GPU 状态（cqa1-33015）

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 1 MiB | 0% | **空闲** |
| 1 | 10553 MiB | 22% | PID 621069: `l2norm k=0.925 libero_10 seed42` |
| 2 | 1 MiB | 0% | **空闲** |
| 3 | 10171 MiB | 35% | PID 537521: `l2norm k=0.5 libero_10 seed43` |

### 运行中的 eval 任务
1. **PID 537516/537521** (GPU 3): `l2norm k=0.5 libero_10 seed43` — Task 9 进行中，总进度 221/450=49.1%，已跑 197 分钟
2. **PID 621069** (GPU 1): `l2norm k=0.925 libero_10 seed42` — 刚启动（02:27）

### Tmux sessions
- `eval_pi05_l2norm_k0925_long_seed42` — 活跃（GPU 1）
- `eval_pi05_random_k03_long_seed43_v4` — 可能已完成（无 GPU 占用）
- `eval_pi05_random_k095_object_seed42_v2` — 可能已完成

### 可用资源
**GPU 0 和 GPU 2 空闲**，可以启动新任务。

### prune_mode 支持列表
`choices=["none", "random", "l2norm", "attention"]`

---
