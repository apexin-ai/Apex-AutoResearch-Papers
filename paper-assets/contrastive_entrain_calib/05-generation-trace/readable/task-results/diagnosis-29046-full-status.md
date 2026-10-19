# diagnosis 29046 full status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_29046-full-status_20260520T071507_result.json`
- **Structured JSON:** [`e30241a9438d76e03e97.json`](../../sessions/e3/e30241a9438d76e03e97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29046 全面状态报告

### GPU STATUS
| GPU | 型号 | 利用率 | 显存占用 |
|-----|------|--------|----------|
| 0 | RTX PRO 6000 Blackwell Server Edition | **95%** | 38,049 / 97,887 MiB |
| 1 | RTX PRO 6000 Blackwell Server Edition | **97%** | 38,161 / 97,887 MiB |

### GPU PROCESSES
| PID | GPU | 显存 |
|-----|-----|------|
| 237437 (exp-003-s2) | GPU-0 | 38,040 MiB |
| 70649 (exp-003) | GPU-1 | 38,152 MiB |

### EXP-003 (seed1, GPU 1)
- **PID 70649**: 运行中，已运行 **1天14小时24分**，状态 `Rl+`
- **Checkpoints**: 共 9 个 (500 ~ 4500)，最新 **checkpoint-4500**（May 20 12:33）
- **日志**: `~/runs/contrastive_entrain_calib/exp-003.log` 不存在（日志实际写入 `logs/exp003_v2.log` via tee）
- **训练进度**: 无法直接从此路径读取（日志走 tee 到 `logs/exp003_v2.log`）

### EXP-003-S2 (seed2, GPU 0)
- **PID 237432** (shell wrapper): 运行中，已运行 **6小时57分**
- **PID 237437** (python): 运行中，已运行 **6小时57分**
- **日志进度**: `677/8000` steps (**8.5%**)，~26.4s/step
- 最新日志时间: 2026-05-20 15:15
- 持续输出 WARNING: `d_syc not loaded; returning R3-only rewards`（符合 R3-only 实验预期）
- **Checkpoints**: 目录 `exp003s2_r3only_seed2/` **不存在**；实际存于 `exp003_r3only_seed2/`，已有 **checkpoint-500**

### ALL PYTHON PROCESSES
- `run_exp003_r3only.py` (PID 70649) — GPU 1, exp-003 seed1
- `run_exp003s2_r3only.py` (PID 237437) — GPU 0, exp-003-s2 seed2
- tensorboard、jupyter-lab、autopanel 等服务进程正常
- 无 exp-002 python 进程在跑（tmux session `exp002` 存在但无活跃训练进程）

### 总结
- 两张 GPU **满载运行**，exp-003 (seed1) 和 exp-003-s2 (seed2) 均正常
- exp-003 已跑 1.5 天，最新 ckpt 到 4500
- exp-003-s2 跑了约 7 小时，677/8000 steps (8.5%)，预计还需 ~53 小时完成
- exp-003-s2 的 checkpoint 目录名是 `exp003_r3only_seed2/`（非 `exp003s2_r3only_seed2/`）

---
