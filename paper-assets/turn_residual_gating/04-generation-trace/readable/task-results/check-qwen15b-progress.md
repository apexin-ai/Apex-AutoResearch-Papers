# check qwen15b progress

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen15b_progress_20260524T020033_result.json`
- **Structured JSON:** [`68585f91928c0c6280bc.json`](../../sessions/68/68585f91928c0c6280bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Qwen-1.5B TG Training 状态

| 项目 | 值 |
|------|-----|
| **进度** | Epoch 1 Step 550 / 24000 total (~8550/24000, **35.6%**) |
| **运行时间** | 53 min |
| **最近 Loss** | L_NTP ≈ 0.93~1.27, L_GAR ≈ 0.001~0.005 |
| **Epoch 0 Avg** | Loss=1.1296, NTP=1.1172, GAR=0.0123 |
| **Gate mean** | ~0.978 (稳定) |
| **Gate 低值层** | L3=0.72, L5=0.93, L17=0.95 (其余 ≈ 0.99+) |
| **GPU** | 97% util, 21.8GB / 97.9GB |
| **预估剩余** | ~1h40m (epoch 0 ≈ 51min/epoch) |

### GPU Chain 状态

| Step | 任务 | 状态 |
|------|------|------|
| 1/7 | SS s123 eval | ✅ Done |
| 2/7 | SS s456 resume training | ✅ Done |
| 3/7 | SS s456 eval | ✅ Done |
| 4/7 | Qwen-1.5B Phase 1 diag | ✅ Done |
| **5/7** | **Qwen-1.5B TG training** | **🔄 Epoch 1/3** |
| 6/7 | Qwen-1.5B eval | ⏳ Pending |
| 7/7 | MMLU eval (6 ckpt) | ⏳ Pending |

Chain PID 108997 运行 8h36m，整体正常。Qwen-1.5B 训练预计 ~1h40m 后完成，之后自动进入 eval 和 MMLU 评估。

---
