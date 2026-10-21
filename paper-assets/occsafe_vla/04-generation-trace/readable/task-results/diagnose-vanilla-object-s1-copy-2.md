# diagnose vanilla object s1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_vanilla_object_s1_20260528T073205_result.json`
- **Structured JSON:** [`93092c20177160d93de8.json`](../../sessions/93/93092c20177160d93de8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

- **失败原因：cron 误报，训练实际已正常完成**
- **最后 step：50005/50005（100%），日志显示 "Max step 50005 reached! Stopping training..."**
- **checkpoint 状态：50000_chkpt 已保存（2026-05-28 15:21），还有 40000 和 45000 checkpoint**
- **cuda:0 当前状态：正在运行 `evaluate_safelibero.py` 评估脚本（PID 975315，16.6GB 显存，评估 vanilla_object_s1 的 50000_chkpt）**
- **磁盘状态：/root/autodl-tmp 250G 用了 146G，剩余 105G（59%），正常**
- **建议：无需任何操作。训练已完成，评估已在进行中**

---
