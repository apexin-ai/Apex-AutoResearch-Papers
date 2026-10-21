# ops d168 westd41074 mixed v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d168_westd41074_mixed_v2_20260522T141104_result.json`
- **Structured JSON:** [`755387745011a52e7dc2.json`](../../sessions/75/755387745011a52e7dc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

xvla_long 在跑 k=0.95 eval（task 4/10），至少还要 30 分钟。GPU 1 也不可用。

---

## 部署汇报

### 已部署（2/3 GPU）

| GPU | tmux session | 任务 | 状态 |
|-----|-------------|------|------|
| cuda:0 | `pi05_k0925_s43` | π0.5 Object seed43 L2norm k=0.925 | 模型已加载，开始评估 |
| cuda:2 | `pi05_attention` | π0.5 Object attention k=0.95 (→0.9→0.85→0.7) | Task 0: 50/50=100%, 进入 Task 1 |

### 未能部署（2 GPU 被占）

| GPU | 占用进程 | 说明 |
|-----|---------|------|
| cuda:1 | `xvla_long` chain (baseline done → k=0.95 running task 4/10 → k=0.9 待跑) | ~30-40 min 后释放 |
| cuda:3 | M64v6 训练 (step 60250/100000, `train_m64v6`) | **不是 VTC 训练**，而是 M64 v6 |

### 发现的问题

1. **`--n_episodes` 参数 bug**: 脚本中 `n_episodes` 是 **per-task** 值，不是 total。传 500 会在 ep=50 时 IndexError（LIBERO 每 task 只有 50 init_states）。**已修正**：所有部署改用 `--n_episodes 50`（50×10=500 total）

2. **`| tee` 掩盖退出码**: 链式命令 `python ... 2>&1 | tee ... && ...` 中，python 崩溃后 tee 返回 0，导致 `&&` 继续执行下一个命令。另一个 agent 部署的 `pi05_goal_random` 因此连续跑了 3 个必崩的配置。已 kill 该 session

3. **cuda:2 上的进程是 M64v6 训练**（`openvla_sc_m64_seed42_v6`，CUDA_VISIBLE_DEVICES=3），实际占 GPU 3。**cuda:2 实际在跑 smolvla_spatial eval（已完成）和 xvla_long eval（仍在跑）**

4. **Attention pruning 已实现**：`eval_pi05_pruning_libero.py` 中有 `--prune_mode attention`，使用 2-layer probe cross-attention scoring

### 早期日志

- **k0925 (GPU 0)**: `l2norm: n_keep=236/256, first_indices=[0, 5, 6, 7, 8]` — 保留 236/256 tokens
- **attention (GPU 2)**: `attention: n_keep=243/256, score_range=[0.000001, 0.003533]` — Task 0 SR=100%, 6.9min/task

### 待部署

GPU 1 释放后可部署 π0.5 Goal random pruning（原计划 cuda:3）。需改用 `--n_episodes 50`。

---
