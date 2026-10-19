# ops eval readiness and training progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-readiness-and-training-progress_20260521T191058_result.json`
- **Structured JSON:** [`700e5e2e780f0be2e665.json`](../../sessions/70/700e5e2e780f0be2e665.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. Object Training 进度 (bjb1-18228)
| 指标 | 值 |
|------|-----|
| 当前进度 | **Epoch 7 / 50**, batch 1050/1950 |
| 最新 epoch 完整指标 | Epoch 6: train_loss=0.009881, **val_loss=0.005511** (new best) |
| 进程运行时间 | 51 min 27 sec (PID 800111) |
| 预估速率 | ~7.9 min/epoch |
| **预估剩余时间** | **~5.7 小时**（约今天上午 ~11:30 完成） |

### 2. bjb2-28827 代码同步
- `evaluate.py` = 33058 bytes ✓ 已是最新，**无需 git pull**

### 3. bjb1-32546 就绪状态
- `evaluate.py` = 33058 bytes ✓ 已是最新
- pi05 模型 ✓ (`/root/autodl-tmp/models/pi05_libero_finetuned/`, 7.4GB model.safetensors)

### 4. CRM Checkpoint 路径 (bjb1-18228)
- **Object**: `/root/autodl-tmp/checkpoints/crm_pi05_full/object/`
  - checkpoint_epoch0002~0006.pt + `crm_best.pt` (2.4MB, val_loss=0.005511)
- **Spatial**: `/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/` — **目录存在但为空**（尚未训练）

### 5. pi05 模型路径
| 服务器 | 路径 | 状态 |
|--------|------|------|
| bjb1-32546 | `/root/autodl-tmp/models/pi05_libero_finetuned/` | ✓ |
| bjb2-28827 | `/root/autodl-tmp/models/pi05_libero_finetuned/` | ✓ |

### 6. 阻塞问题
- **CRM checkpoint 尚不存在于 eval 服务器上**：bjb1-32546 和 bjb2-28827 的 `/root/autodl-tmp/checkpoints/crm_pi05_full/` 均不存在。训练完成后需将 checkpoint 从 bjb1-18228 拷贝到两台 eval 服务器。
- **Spatial CRM 尚未训练**：spatial 目录为空，如果 eval 需要 spatial checkpoint 则需额外安排训练。

---
