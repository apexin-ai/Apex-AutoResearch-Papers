# fix cqa1 deploy p0 20250525

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1_deploy_p0_20250525_20260525T230824_result.json`
- **Structured JSON:** [`4ceff6ad0034d0ee2769.json`](../../sessions/4c/4ceff6ad0034d0ee2769.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个新实验日志确认启动正常，正在加载模型：

- **GPU1 L2norm k=0.925**: `Config: suite=libero_10, prune=l2norm, keep=0.925, eps=50` — 加载 pi0.5 中
- **GPU3 Attn k=0.75**: `Config: suite=libero_10, prune=attention, keep=0.75, eps=50` — 加载 pi0.5 中

GPU1/GPU3 显存还是低（4MiB/3MiB）是因为模型还在 CPU 加载阶段，加载完成后会上 GPU。

**汇总：**

| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | zeromask_random v2 | 运行中（~10GB, 21% util） |
| 1 | **L2norm k=0.925 Long** | 已启动，加载模型中 |
| 2 | Random k=0.75 Long | 运行中（~10GB, 32% util） |
| 3 | **Attn k=0.75 Long** | 已启动，加载模型中 |

4 GPU 全部占用，任务完成。

---
