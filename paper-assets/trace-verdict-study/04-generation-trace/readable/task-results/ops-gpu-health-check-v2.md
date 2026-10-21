# ops gpu health check v2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_health_check_v2_20260520T161759_result.json`
- **Structured JSON:** [`f7b5d02470a9a32e86aa.json`](../../sessions/f7/f7b5d02470a9a32e86aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 健康检查结果

### 1. qwen15b_vota_seed123 — **COMPLETED** ✓

| 项目 | 状态 |
|------|------|
| PID 635814 | **DEAD (正常退出, EXIT_CODE=0)** |
| 阶段 | 训练 444/444 + eval 全部完成 |
| Checkpoints | checkpoint-148, checkpoint-296, checkpoint-444, final |
| **Accuracy** | **99.50%** (CI: 99.08%–99.83%) |
| Pass F1 | 99.65% |
| Fail F1 | 99.12% |
| Lift over majority | +28.0pp |
| N | 1190 samples |

### 2. deepseek_loop_only_seed456 — **ALIVE, TRAINING**

| 项目 | 状态 |
|------|------|
| PID 633962 | **ALIVE** (运行 1h22m) |
| 阶段 | **Training step 260/444** (58.6%) |
| 速度 | ~18.5s/step |
| GPU 0 | **100% util**, 71.6/97.9 GB VRAM |
| GPU 1 | 空闲 |
| Checkpoints | checkpoint-148 已存 |
| **预估剩余** | 184 steps × 18.5s ≈ **57 min** (含后续 eval 约再 +5 min) |

两个实验均健康：qwen15b_vota 已成功完成并产出优秀结果，deepseek_loop_only 预计约 1 小时后完成。

---
