# ops deploy pi05 seed43 and check conflict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_pi05_seed43_and_check_conflict_20260523T073207_result.json`
- **Structured JSON:** [`5ef3d966899237ee2e58.json`](../../sessions/5e/5ef3d966899237ee2e58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 2 模型加载完成（4143.4M params，pruning random keep 230/256），正在初始化 LIBERO 环境。GPU 3 仍在加载权重。两个进程都正常运行中。

---

## 汇报

### 任务 A：westd-41074 π0.5 实验部署

**注意**：命令中的 `--mode` 和 `--num_episodes` 参数有误，实际参数为 `--prune_mode` 和 `--n_episodes`。`--mode` 被 argparse 前缀匹配为 `--model_path` 导致模型路径被覆盖；`l2_norm` 应为 `l2norm`（无下划线）。已修正后成功部署。

| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| 2 | random k=0.9 Object seed43 | **547492** | 模型已加载（9709 MiB），pruning 配置 random keep 230/256，正在初始化 LIBERO 环境 |
| 3 | l2norm k=0.95 Object seed42 | **548949** | 进程存活，模型权重加载中（大模型从磁盘加载较慢） |

### 任务 B：westd-27271 GPU 0 VRAM 冲突检查

| GPU | VRAM 使用 | VRAM 总量 | GPU 利用率 |
|-----|-----------|-----------|-----------|
| 0 | 20935 MiB | 97887 MiB | 66% |
| 1 | 4371 MiB | 97887 MiB | 0% |

GPU 0 上有 3 个进程（非 2 个）：
- PID 250278: 4838 MiB
- PID 284854: 16064 MiB
- PID 251123: 4991 MiB

**共存正常**。GPU 0 使用 20.9GB / 97.9GB（~21%），远未接近满载。PID 250278 和 284854 与预期的 X-VLA 和 OpenVLA 进程吻合（PID 略有偏移可能是子进程），另有一个额外进程 PID 251123。三个进程都在运行，无 OOM 风险。

---
