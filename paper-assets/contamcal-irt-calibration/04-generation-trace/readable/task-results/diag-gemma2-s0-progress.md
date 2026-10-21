# diag gemma2 s0 progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gemma2-s0-progress_20260520T110509_result.json`
- **Structured JSON:** [`bc10ea67ea2da6207980.json`](../../sessions/bc/bc10ea67ea2da6207980.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Gemma-2 s0 sweep 状态 (westd cuda:1):**

| 项目 | 值 |
|---|---|
| PID | 314035 存活，运行 1h18m |
| 当前 dosage | **d000**（第一个） |
| 进度 | **step 1650/3125 (52.8%)**，epoch 0.46 |
| 速度 | ~2.7s/it，预计剩余 ~68 min 完成 d000 |
| Loss | ~1.17，token accuracy ~0.73 |
| GPU 1 | 利用率 71%，显存 95.5/97.9 GB |

Checkpoint 目录已创建 d000/d005/d025/d050 四个文件夹（d005/d025/d050 目前为空目录，仅预建）。d000 训练完成后会依次进入后续 dosage。

---
