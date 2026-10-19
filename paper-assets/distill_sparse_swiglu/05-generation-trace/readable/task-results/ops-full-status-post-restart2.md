# ops full status post restart2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_status_post_restart2_20260520T032455_result.json`
- **Structured JSON:** [`1fc87c81c00aabf75b67.json`](../../sessions/1f/1fc87c81c00aabf75b67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全面状态报告

### westd-41718（两个 GPU 均空闲）

| GPU | 实验 | PID | 状态 | 关键 Metrics |
|-----|------|-----|------|-------------|
| cuda:0 | MSE 训练 s42 | 196791 | **DEAD / 已完成** | loss=0.0130, mse=0.0057, sparsity=0.277 |
| cuda:1 | C4 OOD s42 | 199770 | **DEAD / 已完成** | C4 PPL=18.2211, sparsity=0.296 |

GPU 状态：cuda:0 = 0 MiB / 0%, cuda:1 = 0 MiB / 0%

**MSE 训练详情：**
- 1000/1000 steps 完成，EXIT_CODE=0
- Checkpoint: `checkpoints/mse30_s42/predictor_mse.pt` (145MB, 11:19 保存)
- 最终 step: mse=0.005735, constraint=0.007294, sparsity=0.277, tau=0.100, lambda=1000

**C4 OOD 详情：**
- 完成，EXIT_CODE=0
- C4 PPL = **18.2211**（132 sequences, seq_len=2048）
- Model-level sparsity = 0.296
- 使用 checkpoint: `kl_sparsity30_s42_v3/predictor_kl_normalized.pt`, teal_global + uniform allocation

---

### westd-34887（两个 GPU 满载运行）

| GPU | 实验 | PID | 状态 | 进度 |
|-----|------|-----|------|------|
| cuda:0 | TEAL 30% global HS+PIQA | 157764 | **ALIVE / 运行中** | lm-eval 86% (34681/40168) |
| cuda:1 | BCE 30% global HS+PIQA | 157845 | **ALIVE / 运行中** | lm-eval 86% (34737/40168) |

GPU 状态：cuda:0 = 39993 MiB / 100%, cuda:1 = 68697 MiB / 100%

- 两个 eval 进度几乎同步，约 14 it/s，剩余 ~5500 requests 每个
- 预计 ~6-7 分钟完成
- Model-level sparsity 均为 0.300
- TEAL 层级分布：后几层显著更高（L47=0.810, L46=0.660）
- BCE 层级分布：更平坦，后层较低（L42=0.055, L43=0.078），尾部回升（L46=0.570）

---
