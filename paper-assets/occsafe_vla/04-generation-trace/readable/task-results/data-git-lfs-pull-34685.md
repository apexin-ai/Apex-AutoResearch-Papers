# data git lfs pull 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_git_lfs_pull_34685_20260527T161519_result.json`
- **Structured JSON:** [`e51bfcef6e08a5170e8a.json`](../../sessions/e5/e51bfcef6e08a5170e8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 tfrecord 都是真实数据（每个 ~100-125MB）。注意文件名是 `liber_o10-train.tfrecord-*`。

汇报：

**git lfs pull 完成（~23分钟）**

| Suite | 大小 | tfrecord 数 | 状态 |
|-------|------|-------------|------|
| libero_spatial_no_noops | 1.8G | 32 | 已有 |
| libero_10_no_noops | 3.5G | 32 | **新拉取** |
| libero_goal_no_noops | 1.8G | 32 | **新拉取** |
| libero_object_no_noops | 2.7G | 32 | **新拉取** |

**dataset_statistics.json**：不存在于 repo 中（仅 spatial 有训练时生成的缓存文件 `dataset_statistics_*.json`）。训练代码首次加载新 suite 时会自动生成。

**可以立即开始训练**。每个 suite 都有完整的 32 个 tfrecord shard + `dataset_info.json` + `features.json`。

---
