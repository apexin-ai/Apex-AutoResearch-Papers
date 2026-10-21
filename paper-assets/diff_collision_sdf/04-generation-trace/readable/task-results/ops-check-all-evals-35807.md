# ops check all evals 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_all_evals_35807_20260525T164438_result.json`
- **Structured JSON:** [`ee7c309e0f2400024595.json`](../../sessions/ee/ee7c309e0f2400024595.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总报告：

## GPU 状态

| GPU | 显存占用 | 利用率 | 任务 | 状态 |
|-----|---------|--------|------|------|
| cuda:0 | 27045 MiB | 100% | spatial_bowl 训练 (PID 168730) | **运行中** |
| cuda:1 | 9014 MiB | 47% | s0_l005 eval (PID 478653) | **运行中** — Task 0, 30/50 eps |
| cuda:2 | 9014 MiB | 39% | s0_l01 eval (PID 478930) | **运行中** — Task 0, 30/50 eps |
| cuda:3 | 1 MiB | 0% | 空闲 | s2_l005_best eval **已崩溃** |

## s2_l005_best eval 崩溃原因

PID 483300 加载 checkpoint 时报 `RuntimeError: Missing key(s) in state_dict`。`best/` 目录下有两个模型文件：
- `model.safetensors` (7.4GB) — 非 LoRA 格式的 merged weights
- `model_lora.safetensors` (7.5GB) — LoRA 格式

eval 脚本用 `model_type=lora_baseline` 加载了 `model.safetensors`，key 不匹配。需要改为加载 `model_lora.safetensors`。

## 已完成 eval 结果（之前跑完的）

| 配置 | Task 0 (orange juice) | Task 1 (pudding) | Task 2 (milk) | Task 3 (bbq sauce) | **Overall** |
|------|----------------------|------------------|---------------|--------------------|----|
| **s2_l005_30k** | TSR=4% CAR=60% d=0.047 | TSR=32% CAR=46% d=0.098 | TSR=0% CAR=86% d=0.016 | TSR=0% CAR=20% d=0.073 | **TSR=9.0% CAR=53.0%** |
| **s2_l01_30k** | TSR=0% CAR=62% d=0.027 | TSR=30% CAR=42% d=0.080 | TSR=0% CAR=88% d=0.010 | TSR=0% CAR=20% d=0.089 | **TSR=7.5% CAR=53.0%** |
| **s1_l005_30k** | TSR=0% CAR=54% d=0.056 | TSR=16% CAR=48% d=0.098 | TSR=0% CAR=88% d=0.009 | TSR=0% CAR=16% d=0.101 | **TSR=4.0% CAR=51.5%** |

s0_l005 和 s0_l01 的 eval 刚启动约 7 分钟，都在 Task 0（共 4 tasks × 50 eps = 200 eps），预计还需 ~3-4 小时完成。

## spatial_bowl 训练进度

- **Step**: 8172 / 30000 (**27.2%**)
- **已运行**: ~6h43m
- **ETA**: ~28h（按 4.65s/it）
- **Loss**: action≈0.022, sdf≈0.033, ee≈0.011
- **LR**: 2.18e-05

---
