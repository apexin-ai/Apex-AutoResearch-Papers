# diagnose full occ ln s3 v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full_occ_ln_s3_v2_20260525T202749_result.json`
- **Structured JSON:** [`a2505b4e0ee137d25beb.json`](../../sessions/a2/a2505b4e0ee137d25beb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**两个实验失败原因完全相同**：数据盘 `/dev/md0` 250G 已 100% 用满。两个实验都成功训练到 step 30000，但在保存 checkpoint 时因 `No space left on device (os error 28)` 崩溃。

关键事实：
- 两个 30K checkpoint 都已损坏不可用（full_occ_ln_s3 的只有 2.5MB，ablation_occ_detach_s3 的只写了 5G/15G）
- 20K checkpoint 完整可用，可重新 resume
- checkpoint 目录合计占用 ~230G，需要清理旧 checkpoint 腾出空间才能继续训练
- GPU 2/3 已释放，无残留进程

报告已写入 `artifacts/diagnosis_disk_full_20260526.md`。下一步需要确认哪些旧 checkpoint 可以删除来腾出空间。

---
