# diagnose mvp occ s3 v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_occ_s3_v2_20260526T110654_result.json`
- **Structured JSON:** [`b3ee6d878b00389a15a3.json`](../../sessions/b3/b3ee6d878b00389a15a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。`mvp_occ_s3_v2` 训练**已成功跑完全部 50005 步**，EXIT_CODE=1 是 PyTorch distributed 退出时未调用 `destroy_process_group()` 导致的误报。

关键事实：
- 最终 loss: occ=0.0098, action=0.0493
- 40000_chkpt 和 50000_chkpt 均已保存，可直接用于评估
- 无需重试

---
