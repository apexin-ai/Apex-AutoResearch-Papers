# diagnose cuda2 cuda3 progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cuda2-cuda3-progress_20260523T091211_result.json`
- **Structured JSON:** [`311f308b534edb100559.json`](../../sessions/31/311f308b534edb100559.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练都在运行中：

| | cuda:2 — DPO 3ep | cuda:3 — RSFT CED s44 |
|---|---|---|
| PID | 234741 | 238227 |
| 进度 | **443/561 (79%)** | **451/510 (88%)** |
| 当前 epoch | ~2.14 | — |
| 最新 loss | 0.3552 | — |
| 速度 | ~11s/step | ~4.2s/step |
| 预计剩余 | **~22 min** | **~4 min** |
| 显存 | 80383/97887 MiB (82%) | 34531/97887 MiB (35%) |
| GPU 利用率 | 99% | 95% |

DPO 训练趋势正常：loss 从 epoch 1 的 ~0.46 降到 epoch 2 的 ~0.35，rewards/margins 从 ~1.2 扩大到 ~2.2，rewards/accuracies 从 ~0.78 升至 ~0.86。

RSFT CED s44 预计 ~4 分钟内完成。

**其他 GPU：** GPU 0 (21.3GB, 95%), GPU 1 (32.5GB, 92%) 也在使用中。

---
