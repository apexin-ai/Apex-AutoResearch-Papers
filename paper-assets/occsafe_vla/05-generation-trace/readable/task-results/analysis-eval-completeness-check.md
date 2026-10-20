# analysis eval completeness check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_completeness_check_20260524T225508_result.json`
- **Structured JSON:** [`cc1089c70c108a09a0ba.json`](../../sessions/cc/cc1089c70c108a09a0ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结论：

**只有 1 个实验缺 eval：`full_occ_retrain_s0`**，checkpoint 在 westd-34685 上已确认存在，可以直接跑 eval。

Director 点名的 9 个实验全部已有 eval 结果（CAR 范围 0.688~0.804，TSR 范围 0.788~0.918）。

另有 8 个实验正在训练中，完成后也需要补 eval。清单已写入并注册为 artifact。

---
