# ops check mistral training

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-mistral-training_20260524T041100_result.json`
- **Structured JSON:** [`1f7db34efd7eb7eb6566.json`](../../sessions/1f/1f7db34efd7eb7eb6566.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Mistral 训练状态报告

| 任务 | 状态 | 运行时长 | 进度 | 速度 |
|------|------|----------|------|------|
| **mistral_contam_5** | 运行中 | 13min05s | 672/1071 (63%) | ~1.17s/it |
| **mistral_contam_25** | 运行中 | 13min03s | 629/1596 (39%) | ~1.23s/it |

**GPU 利用率：**
- GPU 0: 89%, 9047/97887 MiB (contam_5)
- GPU 1: 98%, 9817/97887 MiB (contam_25)
- GPU 2-3: 空闲

**最新指标：**
- contam_5: loss=1.374, token_acc=0.637, epoch=0.98 (即将完成第1个epoch)
- contam_25: loss=1.331, token_acc=0.669, epoch=1.00 (刚完成第1个epoch)

**预估剩余时间：**
- contam_5: ~8min (399 steps × 1.17s)
- contam_25: ~20min (967 steps × 1.23s)

---
