# fix kill old eval bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-old-eval-bjb1_20260513T231321_result.json`
- **Structured JSON:** [`5c0d8ece91a4ba12c05e.json`](../../sessions/5c/5c0d8ece91a4ba12c05e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 旧 eval 进程
- **PID 104830** (eval-acr-vla-spatial-v1): 已不存在，无需 kill

### 3 个新 eval 进程 — 全部运行中
| PID | 任务 | GPU | 状态 |
|-----|------|-----|------|
| 109802 | eval-spatial-v6-full (vla_only) | GPU 0 | 运行中 |
| 110073 | eval-acr-spatial-v2 (acr_vla) | GPU 1 | 运行中 |
| 110280 | eval-reconvla-spatial-v3 (reconvla) | GPU 2 | 运行中 |

### CRM 训练 (PID 104611)
- **任务**: train_crm.py, obs_only mode, spatial+object benchmarks
- **进度**: Epoch 6/50, train_loss=0.0289, val_loss=0.0183
- Best val_loss=0.018312 (Epoch 4)，loss 已趋于平稳

### GPU 使用率
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 12.0 / 24.6 GB | 17% |
| 1 | 1.5 / 24.6 GB | 22% |
| 2 | 6.7 / 24.6 GB | 19% |
| 3 | 0.6 / 24.6 GB | 9% |

### Tmux Sessions
- `eval-spatial-v6-full`, `eval-acr-spatial-v2`, `eval-reconvla-spatial-v3` — 3 个 eval session 均存在

---
