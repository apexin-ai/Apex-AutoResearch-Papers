# check qwen15b progress v2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen15b_progress_v2_20260524T031358_result.json`
- **Structured JSON:** [`3e9b2dec33879199021e.json`](../../sessions/3e/3e9b2dec33879199021e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Qwen-2.5-1.5B TG v7 s42 训练状态：**

| 项目 | 值 |
|------|------|
| GPU | 97% util, 31GB VRAM, 72°C |
| 当前任务 | `gpu_chain_next.sh` Step 5/7 — Qwen-1.5B TG training |
| 进度 | **Epoch 2/3** (最后一个 epoch)，step 4200 |
| 训练 Loss | ~0.8–1.5 (L_NTP 为主，L_GAR≈0，L_DIV≈0) |
| Gate 均值 | 0.975 (收敛，std 0.05) |
| Gate Profile | L3 (0.72) 和 L5 (0.90) 明显低于其他层 (~0.99)，与 Llama 的 deep-layer 模式不同 |

**时间估算：**
- 09:07 开始，epoch 0 → 09:58 (51min)，epoch 1 → 10:48 (50min)
- Epoch 2 预计 ~11:38 完成（约 **24 min 后**）

**Chain 剩余：**
- Step 6/7: Qwen-1.5B eval
- Step 7/7: MMLU eval (6 checkpoints)
- 全部完成预计再需 1-2h

---
