# check ss s123 progress

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_ss_s123_progress_20260523T111538_result.json`
- **Structured JSON:** [`eeb56f5404a863fa6468.json`](../../sessions/ee/eeb56f5404a863fa6468.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**SS s123 训练已完成。**

| 项目 | 值 |
|------|-----|
| **状态** | 已完成 |
| **总耗时** | 38773.4s（~10.8 小时） |
| **Epochs** | 3/3（Epoch 0, 1, 2 全部完成） |
| **最终 Avg Loss** | 0.9316（NTP=0.9307, GAR=0.0009, DIV=0.0000） |
| **Gate 均值** | 0.9505（std=0.0508, min=0.7383, max=1.0000） |
| **SS 使用率** | 8899/24000（37.1%），SS ratio 已到 0.500，fallback=0 |
| **Checkpoint** | `checkpoints/tg_v8b_ss_s123/`（含 epoch_0/1/2） |

PID 84793 仍占 GPU 44GB 显存（97% 利用率），可能是保存完 checkpoint 后还没退出，或者在做后处理。日志已打印 "Training complete" 和 "Final model saved"，训练本身已结束。

---
