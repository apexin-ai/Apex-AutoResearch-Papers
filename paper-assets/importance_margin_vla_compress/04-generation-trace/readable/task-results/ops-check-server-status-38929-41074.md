# ops check server status 38929 41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-server-status-38929-41074_20260524T064413_result.json`
- **Structured JSON:** [`c707572531c4ef623c9d.json`](../../sessions/c7/c707572531c4ef623c9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### westd-38929 GPU 状态

| GPU | 状态 | 实验 | 进度 |
|-----|------|------|------|
| 0 | **空闲** | `eval_xvla_l2norm_k05_goal_seed43` tmux 存在但无活跃进程 | — |
| 1 | **空闲** | `eval_xvla_random_k05_spatial_seed43` 已完成 (07:29) | DONE |
| 2 | **运行中** | `eval_xvla_l2norm_k05_long_seed42_v4` | ep 47/50，大量 SUCCESS |
| 3 | **运行中** | `eval_xvla_l2norm_k03_goal_seed42` | ep 28/50，全部 FAIL (0% SR) |

**v4 未失败**——它正在正常运行，ep 47/50 即将完成，无需部署 v5。

### westd-41074 GPU 状态

| GPU | 状态 |
|-----|------|
| 0-3 | **全部空闲**，无任何 eval 进程 |

ROADMAP 标记的 pi05 实验已全部结束/消失。`eval_pi05_random_k03_long_seed43_v2` 已完成：**SR=28.0%** (140/500)。

### 注册表异常
两个实验标记 RUNNING 但无实际进程：
- `eval_pi05_random_k03_spatial_seed42_postfix`
- `eval_pi05_random_k07_spatial_seed42_postfix`

这些应该是 cqa1 上的实验（ROADMAP 标注 "cqa1 运行中"），不在这两台服务器上。

### 待决策
- westd-38929 GPU 0/1 空闲，可部署新实验
- westd-41074 4 张 GPU 全部空闲，可部署大批实验
- ROADMAP 中 "OpenVLA Attention k=0.5 Object" 标注给 westd-27271，无明确 k=0.925 实验排队
- v4 即将完成且表现不错（大量 SUCCESS），结果出来后可以决定下一步

---
