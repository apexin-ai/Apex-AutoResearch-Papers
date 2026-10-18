# ops d168 westd41074 pi05 random goal

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d168_westd41074_pi05_random_goal_20260522T142322_result.json`
- **Structured JSON:** [`f8d6e61ba4971ac6db80.json`](../../sessions/f8/f8d6e61ba4971ac6db80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:0 Goal Random 已进入 eval 循环，Task 0 前 10 个 episodes 完成，SR=80%。

汇报：

---

## westd-41074 GPU 状态总览

| GPU | 任务 | 状态 | 详情 |
|-----|------|------|------|
| **cuda:0** | π0.5 Goal Random k=0.85→0.7→0.5 | **刚部署，运行中** | T0 ep=10, 80% SR。tmux: `pi05_goal_random` |
| **cuda:1** | X-VLA Long baseline eval | **运行中** | PID 545284, 4364 MiB。tmux: `xvla_long` |
| **cuda:2** | π0.5 Attention k=0.95 Object | **运行中**（其他 agent 部署） | PID 546011, 10671 MiB |
| **cuda:3** | VTC M64 训练 | **运行中，60.7%** | step 60650/100000, 0.6 sps, **ETA ~18h（约 5/23 16:30）** |

### 关键发现
- **M64 训练进度 60.7%**，不是之前 reconcile 报的 93%。距完成还需约 18 小时，cuda:3 不可用，**Long Random 无法部署在此服务器**。
- cuda:2 被其他 agent 占用（π0.5 Attention Object pruning），无空闲 GPU 可用。
- smolvla_spatial session 已完成（spatial baseline 结果保存在 `eval_results/official_libero_spatial_baseline.json`），session 空闲但 GPU 已被 attention pruning 接管。

---
