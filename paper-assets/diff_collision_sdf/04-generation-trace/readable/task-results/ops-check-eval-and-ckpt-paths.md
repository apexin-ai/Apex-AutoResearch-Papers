# ops check eval and ckpt paths

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_eval_and_ckpt_paths_20260526T231136_result.json`
- **Structured JSON:** [`e54611f9445f1f6a9378.json`](../../sessions/e5/e54611f9445f1f6a9378.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### eval_spatial_sdf_s0_l005_30k 进度

进程 373135 存活，已运行 ~38 分钟。**190/200 episodes 完成**（4 个 task × 50 episodes）。

已完成 task 结果：

| Task | TSR | CAR |
|------|-----|-----|
| 0: bowl between plate and ramekin | 66% (33/50) | 0% (0/50) |
| 1: bowl on ramekin | 38% (19/50) | 16% (8/50) |
| 2: bowl on stove | 72% (36/50) | 4% (2/50) |
| 3: bowl on wooden cabinet | 进行中 40/50 | — |

Task 3 最后一条 log 在 07:11 UTC（ep 40/50），预计 **~07:15 UTC 全部完成**（约几分钟内）。结果 JSON 尚未生成。

---

### λ=0.1 训练 checkpoint 路径

**关键发现：λ=0.1 使用后缀 `_l1`**，不是 `_l01_high`。与 λ=0.01 的 `_l01` 命名一致但数值不同。

| Seed | 服务器 | PID | Checkpoint 路径 | 最新 ckpt | 进度 |
|------|--------|-----|-----------------|-----------|------|
| s0 | westd-35807 | 271266 (alive) | `.../a1_sdf_pi05_object_pudding_seed0_l1/` | 22000 (06:49 UTC) | ~73% |
| s1 | westd-35807 | 未提供 | `.../a1_sdf_pi05_object_pudding_seed1_l1/` | 20000 (04:55 UTC) | ~67% |
| s2 | westd-45947 | 425058 (alive) | `.../a1_sdf_pi05_object_pudding_seed2_l1/` | 10000 (07:08 UTC) | ~33% |

每 2000 步约耗时 2.5 小时。预估 30k 完成时间：
- s0: ~May 27 17:00 UTC
- s1: ~May 27 17:30 UTC（需确认进程是否仍在运行）
- s2: ~May 28 08:00 UTC

---
