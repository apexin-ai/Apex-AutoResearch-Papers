# ops gpu3 phase2 or eval

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu3_phase2_or_eval_20260525T214958_result.json`
- **Structured JSON:** [`d1cc22d617a2bc3aebcd.json`](../../sessions/d1/d1cc22d617a2bc3aebcd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### GPU 3 — Phase 2 λ=0 训练 (已启动)

| 项目 | 值 |
|------|-----|
| PID | 254634 |
| 显存 | 27045 MiB / 97887 MiB, 100% util |
| Checkpoint 来源 | seed2_l005/best (30K步完训模型) |
| Resume 机制 | 复制 l005 best → l0/0 目录，metadata 重置 global_step=0 |
| lambda_sdf | **0** (SDF loss 不参与梯度) |
| warmup_phase_steps | 0 → LoRA 立即解冻 (Phase 2 at step 0) |
| num_train_steps | 10000 |
| LR | warmup 1K → peak 2.5e-5 → cosine decay → 2.5e-6 |
| Step 0 | loss=0.0187, action=0.0166, sdf=0.1376(×0=0), ee=0.2076 |
| 速度 | ~9s/step → ETA ~25h |

Phase 2 确认：33.47M LoRA params 已在 step 0 解冻，LoRA gradient warmup 100 steps。

### GPU 1 — Eval s1_l005 30K (已完成)

| Task | TSR | CAR |
|------|-----|-----|
| 0 | 2% | 54% |
| 1 | 14% | 58% |
| 2 | 0% | 92% |
| 3 | 0% | 12% |
| **Avg** | **4.0%** | **54.0%** |

### GPU 2 — Eval s0_l01 30K (已完成)

| Task | TSR | CAR |
|------|-----|-----|
| 0 | 0% | 76% |
| 1 | 26% | 32% |
| 2 | 0% | 84% |
| 3 | 0% | 18% |
| **Avg** | **6.5%** | **52.5%** |

GPU 1/2 当前空闲 (0 MiB)。日志显示之前的 eval 已完成并保存了结果。

---
