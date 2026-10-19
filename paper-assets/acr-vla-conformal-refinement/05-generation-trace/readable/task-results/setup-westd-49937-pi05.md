# setup westd 49937 pi05

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_westd-49937-pi05_20260526T041200_result.json`
- **Structured JSON:** [`c7d452a492df50235fb2.json`](../../sessions/c7/c7d452a492df50235fb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-49937 部署完成，6 个 π0.5 实验全部运行中。**

### 环境摘要
- **GPU**: 6x RTX PRO 6000 Blackwell (98GB)，PyTorch 2.8.0+cu128，CUDA 12.8
- **Conda base**: Python 3.12.3，transformers 5.8.0，robosuite 1.4.0，lerobot 0.5.2
- **已修复**: transformers 5.9.0→5.8.0（`create_causal_mask` API 兼容性）、EGL 库安装

### 运行实验

| GPU | exp_id | 模式 | 基准 | 种子 | 状态 |
|-----|--------|------|------|------|------|
| 0 | westd-pi05-adaptive-goal-s42 | adaptive_conformal_crm | goal | 42 | rollout 进行中 (3/5 on task 1) |
| 1 | westd-pi05-adaptive-goal-s43 | adaptive_conformal_crm | goal | 43 | 推理中 |
| 2 | westd-pi05-adaptive-goal-s44 | adaptive_conformal_crm | goal | 44 | 推理中 |
| 3 | westd-pi05-adaptive-object-s42 | adaptive_conformal_crm | object | 42 | 推理中 |
| 4 | westd-pi05-k2mean-goal-s42 | vla_only (K=2 mean) | goal | 42 | 模型已加载 |
| 5 | westd-pi05-crm-k2-goal-s42 | crm_obs_only (K=2) | goal | 42 | 模型加载中 |

日志位置：`/tmp/exp_gpu{0-5}.log`

---
