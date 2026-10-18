# ops cqa1 reassign 3gpu xvla goal long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-reassign-3gpu-xvla-goal-long_20260521T004704_result.json`
- **Structured JSON:** [`ad116fed4a1220e9f41e.json`](../../sessions/ad/ad116fed4a1220e9f41e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 已完成实验结果

| Experiment | SR | Wilson CI 95% |
|---|---|---|
| **Spatial k=0.9** | **79.0%** | [0.752, 0.823] |
| **Spatial baseline** | **91.6%** | [0.888, 0.937] |
| **Goal baseline** | **98.0%** | [0.964, 0.989] |

Spatial k=0.9 相对 baseline 下降 12.6pp (79.0% vs 91.6%)，比 Object suite 下降更大 (97.8% vs ~98%)，说明 Spatial 任务对 pruning 更敏感。

## 新启动实验

| GPU | tmux session | Experiment | PID |
|---|---|---|---|
| cuda:0 | `eval_xvla_goal_k09` | X-VLA k=0.9 on Goal | 154087 |
| cuda:1 | `eval_xvla_baseline_long` | X-VLA baseline on Long | 154163 |
| cuda:2 | `eval_xvla_spatial_k05` | X-VLA k=0.5 on Spatial (不动) | 875716 |
| cuda:3 | `eval_xvla_goal_k05` | X-VLA k=0.5 on Goal | 154300 |

## GPU 利用率确认
```
GPU 0: 4055 MiB / 24564 MiB ✓
GPU 1: 4051 MiB / 24564 MiB ✓
GPU 2: 4601 MiB / 24564 MiB ✓ (不受影响)
GPU 3: 4051 MiB / 24564 MiB ✓
```

4 GPU 全部在用，3 个新实验 + GPU 2 的 Spatial k=0.5 均正常运行。Registry 已同步更新。

---
