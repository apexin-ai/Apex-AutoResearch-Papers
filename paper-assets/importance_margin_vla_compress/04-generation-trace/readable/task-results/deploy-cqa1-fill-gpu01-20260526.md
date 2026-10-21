# deploy cqa1 fill gpu01 20260526

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_fill_gpu01_20260526_20260526T094230_result.json`
- **Structured JSON:** [`4441ac0fbae495b2386f.json`](../../sessions/44/4441ac0fbae495b2386f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU0 和 GPU1 **并非空闲**，当前状态：

| GPU | PID | 显存占用 | 运行命令 |
|-----|-----|---------|---------|
| GPU0 | 212677 | 10464 MiB | `eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.75 --seed 42 --gpu 0` |
| GPU1 | 213217 | 10628 MiB | `eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.75 --seed 42 --gpu 0` |
| GPU2 | 77661 | 10152 MiB | python |
| GPU3 | 77832 | 10152 MiB | python |

现有 tmux sessions：`eval_pi05_l2norm_k05_long_seed42`、`eval_pi05_random_k05_long_seed42`（名称与实际运行进程不匹配）。

**关键发现：**
- GPU0 上已经在运行你要部署的**实验1**（l2norm k=0.75），且 utilization 43%，正在工作
- GPU1 上运行的是 attention **k=0.75**（不是你要的 k=0.5）

需要确认：
1. GPU0 的 l2norm k=0.75 是否就是之前重启成功的？如果是，无需再跑
2. GPU1 的 attention k=0.75 是否需要保留？是否要 kill 掉换成 attention k=0.5？

---
