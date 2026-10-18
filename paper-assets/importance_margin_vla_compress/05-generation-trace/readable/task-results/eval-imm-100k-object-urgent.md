# eval imm 100k object urgent

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_imm_100k_object_urgent_20260517T010456_result.json`
- **Structured JSON:** [`ab968fa80cabad9ede82.json`](../../sessions/ab/ab968fa80cabad9ede82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Object eval 已成功启动。

```
=== CHECKPOINT 确认 ===
路径: checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt
大小: ~921 MB
修改时间: May 17 08:42 (今天，确认是 IMM 100K)

=== OBJECT EVAL 启动 ===
GPU: cuda:1 (PID 723269, 3227MiB)
tmux session: imm_100k_object
状态: Task 0/10 开始 ("pick up the alphabet soup and place it in the basket")

=== GPU 状态 ===
GPU 0: 6658MiB/97887MiB, 56% util (Spatial eval + expert_only_ft)
GPU 1: 6493MiB/97887MiB, 5% util (Goal eval + Object eval)

=== 已完成 EVAL 结果 ===
目前 imm_fullft_100k 系列尚无完成的结果文件（Spatial/Goal/Object 均在跑）
已有的相关结果:
- full_ft_seed0_100k_libero_spatial.json
- full_ft_seed0_100k_libero_goal.json
- full_ft_seed0_100k_libero_object.json
- full_ft_100k_libero_object_formal.json
- imm_v2_fullft_libero_object.json
```

Object eval 在 GPU 1 上与 Goal eval 并行运行，GPU 利用率从 1% 升到 5%，内存充裕（91.4GB 空闲），不会互相干扰。预计约 60 分钟完成（10 tasks × 50 episodes × ~7s/ep）。

---
