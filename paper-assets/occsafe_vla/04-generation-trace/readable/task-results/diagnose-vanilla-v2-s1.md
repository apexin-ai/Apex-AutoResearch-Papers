# diagnose vanilla v2 s1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_vanilla_v2_s1_20260526T224341_result.json`
- **Structured JSON:** [`8214d8b6bdf4987fda82.json`](../../sessions/82/8214d8b6bdf4987fda82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。**vanilla_v2_s1 没有失败，是 Cron 监控误报。**

关键发现：
- 训练 100% 完成（50005/50005 steps，耗时 ~13h46m）
- step 40000 和 50000 的 checkpoint 均已保存
- 进程正常退出后 GPU cuda:0 已释放，无残留
- 日志无任何错误，与成功完成的 vanilla_v2_s2 行为完全一致
- 监控因未检测到 sentinel/W&B 而将正常退出误判为 crash

报告已写入 `artifacts/diagnosis_vanilla_v2_s1.md`。建议后续修复监控逻辑，增加对 max_steps checkpoint 存在性的检查。

---
