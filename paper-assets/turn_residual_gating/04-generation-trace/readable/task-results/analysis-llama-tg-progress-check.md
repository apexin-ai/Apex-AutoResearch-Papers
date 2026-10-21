# analysis llama tg progress check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_tg_progress_check_20260521T013837_result.json`
- **Structured JSON:** [`8f07b0ed3a4eb60bf133.json`](../../sessions/8f/8f07b0ed3a4eb60bf133.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态: RUNNING**

| 指标 | 值 |
|------|-----|
| PID | 199643 (运行 5h32m) |
| GPU | NVIDIA RTX PRO 6000 Blackwell, 102GB VRAM |
| 模型 | Llama-3.1-8B-Instruct + ThreadGate |
| 进度 | Epoch 1, Step 7650 / 8000 (每 epoch 8000 步, 共 3 epochs) |
| 总进度 | 15650 / 24000 步 (**65.2%**) |
| 当前 Loss | L_NTP=0.757, Loss=0.757 |
| Gate 均值 | 0.925 (std=0.059) |
| 内存 | 63.4 GB |
| ETA | **~3 小时** (按 2845 步/小时推算) |

**训练曲线摘要:**

- Epoch 0 完成: Avg Loss=1.009, Avg NTP=0.990
- Epoch 1 即将结束 (~96%), loss 降至 0.75-0.95 区间
- Gate 值从初始 0.818 升至 ~0.945 (epoch 0 末), epoch 1 稳定在 ~0.925-0.935
- L_GAR 在 step ~800 后收敛至近 0, L_DIV 全程为 0
- Gate profile 显示层间分化明显: 浅层 (L0-L5) ~0.97, 深层 (L24-L28) ~0.82, 末层 (L30-L31) 回升至 0.95 — 符合预期的 U 型模式

---
