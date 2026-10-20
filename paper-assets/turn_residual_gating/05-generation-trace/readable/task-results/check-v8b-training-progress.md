# check v8b training progress

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_v8b_training_progress_20260520T181614_result.json`
- **Structured JSON:** [`bc262854cb2e216e257d.json`](../../sessions/bc/bc262854cb2e216e257d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**v8b 训练已完成。**

| 项目 | 值 |
|------|-----|
| 状态 | **已完成** |
| 总耗时 | 29333s ≈ **8.1 小时** |
| 最终 step | global_step=3000 / 3000 (100%) |
| Epochs 完成 | Epoch 1 + Epoch 2（从 epoch_0 checkpoint resume） |
| Epoch 2 Avg Loss | **0.9330** (NTP=0.9322, GAR=0.0008, DIV=0.0000) |
| Gate (final) | mean=**0.9586**, std=0.0582, min=0.7227, max=1.0000 |
| SS ratio | 0.500, used=7668/16000 (47.9%), fallback=0 |
| 显存 | 53.1GB（稳定） |
| GPU | 当前空闲，训练已结束 |
| 错误 | **无** — 日志中无 error/exception |
| Checkpoint | `checkpoints/tg_v8b_ss_fixed_s42/` — epoch_0, epoch_1, epoch_2 + final (gate_params.pt + lora) 均已保存 |

Gate profile (step 3000) 低值层: L4=0.723, L5=0.867, L0=0.887 — 与之前 v7/v9 模式一致，浅层 gate 更低。

训练正常完成，可以进入评估阶段。

---
