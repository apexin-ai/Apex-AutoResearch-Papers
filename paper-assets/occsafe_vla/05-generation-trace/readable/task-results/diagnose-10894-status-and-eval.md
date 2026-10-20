# diagnose 10894 status and eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_10894_status_and_eval_20260525T192240_result.json`
- **Structured JSON:** [`6172b3abe45265773311.json`](../../sessions/61/6172b3abe45265773311.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部**仍在运行**，但进度远低于预期——只跑了约 1h40m，不像是 12h 前启动的。

| 实验 | GPU | 当前 step | 进度 | 已跑时间 | 预计剩余 |
|------|-----|-----------|------|----------|----------|
| cutoff_45k_s2_v2 | cuda:0 (99%, 72°C) | ~6555/50005 | 13% | 1h45m | ~11h |
| mvp_occ_s3_v2 | cuda:1 (80%, 68°C) | ~6151/50005 | 12% | 1h38m | ~11h |
| full_occ_ln_s3_v2 | cuda:2 (99%, 73°C) | ~6344/50005 | 13% | 1h42m | ~11h |
| ablation_occ_detach_s3_v2 | cuda:3 (49%, 68°C) | ~6356/50005 | 13% | 1h42m | ~11h |

所有 GPU 显存满载（~62GB），训练正常进行中，速度 ~1.08 it/s。

**异常点**：进度条显示只跑了约 1h40m，说明这些实验可能在中间崩溃后被重新启动过，或者启动时间比预期晚。预计还需 **~11 小时**才能完成，不具备启动 eval 的条件。

需要我检查是否有之前崩溃的 log 记录吗？

---
