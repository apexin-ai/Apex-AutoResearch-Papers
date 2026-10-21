# code condition b dryrun

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_condition-b-dryrun_20260520T084232_result.json`
- **Structured JSON:** [`f4c8c7e0835c90ddbc8b.json`](../../sessions/f4/f4c8c7e0835c90ddbc8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 10 extraction processes (task_id 0-9) are still running. The HDF5 files remain locked — can't re-test with real occ labels yet.

## Dry-run Condition B 结果

**OOM 验证: 通过** — GPU 峰值 ~62.2 GB / 97.9 GB，与 vanilla (~62 GB) 基本一致。occ_head 仅增加 ~1.2M 参数，显存开销可忽略。batch_size=8 安全。

**occ_loss 计算: 正常** — 全部 21 步 occ_loss 如下：

| Step | loss | occ_loss |
|------|------|----------|
| 0 | 0.668 | 0.1314 |
| 5 | 0.941 | 0.0957 |
| 10 | 0.645 | 0.0673 |
| 15 | 0.594 | 0.0531 |
| 20 | 0.354 | 0.0447 |

occ_loss 从 0.131 单调下降到 0.045，说明 occ_head 前向/反向传播正常，梯度回传正常。

**occ 标签加载: 全部 fallback 到 zeros** — 10 个 HDF5 文件仍被 `extract_occupancy.py` 进程锁定（还在跑），每个 batch 的 8 个样本都触发 "Failed to load occ label" 警告，fallback 到全零标签。occ_loss 非零是因为随机初始化的 occ_head 预测非零值 vs 零目标。

**发现并修复的 bug**: `finetune.py` 第 1035 行 `RLDSBatchTransform` 构造时未传入 `occ_data_dir`，导致 occ 标签加载完全失效。已修复。

**临时 debug print**: 已删除。

**待办**: extraction 完成后，需要再做一次短 dry-run 验证真实非零 occ 标签能正确加载、occ_loss 反映真实分布。

---
