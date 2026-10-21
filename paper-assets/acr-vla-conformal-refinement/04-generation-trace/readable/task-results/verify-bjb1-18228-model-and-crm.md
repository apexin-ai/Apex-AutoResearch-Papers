# verify bjb1 18228 model and crm

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_bjb1-18228-model-and-crm_20260524T092843_result.json`
- **Structured JSON:** [`ff6388a20751f06dc0e9.json`](../../sessions/ff/ff6388a20751f06dc0e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. GPU 1+2：**SmolVLA**，不是 π0.5

**证据：**
- tmux session `long-vla-s47` 和 `goal-vla-s47` 的参数都明确显示 `'model': 'smolvla'`
- 加载路径：`/root/autodl-tmp/models/smolvla_libero/`，加载的是 `SmolVLM2-500M-Video-Instruct`
- 模式：`vla_only`，seed=47
- 显存：GPU 1 = 6282 MiB，GPU 2 = 5508 MiB — 与 SmolVLA (~0.4B) 一致，π0.5 (3.6B) 应占 8-10 GB

GPU 0 和 GPU 3 各占 ~9.9 GB，可能是 π0.5 的 eval。

### 2. CRM Goal 训练：**已完成** ✓

| 指标 | 值 |
|------|-----|
| 完成 epoch | 50/50 |
| Best val_loss | **0.003319**（epoch 48） |
| Final train_loss | 0.018992 |
| Best checkpoint | `/root/autodl-tmp/checkpoints/crm_pi05_k1_multiscale/goal/crm_k1_best.pt` (2.1 MB) |
| Epoch checkpoints | epoch 46-50，各 6.2 MB |

### 3. CRM Spatial 训练：**已完成** ✓

| 指标 | 值 |
|------|-----|
| 完成 epoch | 50/50 |
| Best val_loss | **0.002887**（epoch 50，最后一轮即最优） |
| Final train_loss | 0.018836 |
| Best checkpoint | `/root/autodl-tmp/checkpoints/crm_pi05_k1_multiscale/spatial/crm_k1_best.pt` (2.1 MB) |
| Epoch checkpoints | epoch 46-50，各 6.2 MB |

Spatial 的 val_loss (0.002887) 比 Goal (0.003319) 更低，且最后一个 epoch 仍在刷新 best，说明可能还有继续训练的空间（不过差距已经很小）。

---
