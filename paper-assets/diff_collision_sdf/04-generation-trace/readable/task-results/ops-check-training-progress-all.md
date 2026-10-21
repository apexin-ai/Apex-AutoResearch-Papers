# ops check training progress all

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_training_progress_all_20260522T153431_result.json`
- **Structured JSON:** [`add954475641f70157c8.json`](../../sessions/ad/add954475641f70157c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 实验 | 服务器 | 进度 | 当前 loss | ETA |
|------|--------|------|----------|-----|
| a3_gradient_spatial_bowl_s0 | westd-45947 cuda:0 | 85.4% (25627/30K) | 0.0193 | ~4h52m (~04:17 UTC) |
| a1_lora_spatial_bowl_s0 | westd-35807 cuda:0 | 98.7% (29606/30K) | 0.0182 | ~26min (~00:00 UTC) |
| eval_a1_lora_object_v11 | westd-35807 cuda:3 | 40% (80/200 ep) — task 2/4, ep 30/50 | TSR=0% (task1) | ~2min/10ep → ~50min |

**eval 详情**: Task 1 完成 — TSR=0.0%, CAR=80.0%（碰撞避免率不错但任务成功率为零）。Task 2 "pick up the milk and place it in the basket" 进行中。

**Pi0.5 下载**: 8.1 GiB / 11.6 GiB (69%) — 进程存活，但速度极慢 (~300-500 KiB/s)，预估还需 2-3 小时。注意：下载路径改到了 `/root/autodl-tmp/openpi_weights/pi05_libero/`。

**额外发现**: westd-35807 上还有两个 eval session 在运行：`eval_lora_object` 和 `eval_lora_spatial`。a1_lora 训练即将完成（~26min）。

---
