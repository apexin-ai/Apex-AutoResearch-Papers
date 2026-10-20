# code ds accuracy 8k batch1

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ds_accuracy_8k_batch1_20260515T212413_result.json`
- **Structured JSON:** [`a94c337485905ea932c7.json`](../../sessions/a9/a94c337485905ea932c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常运行。

**完成状态汇总：**

| 实验 | 状态 | GPU |
|------|------|-----|
| acc_ds_dense_8k | RUNNING (Problem 2/50) | cuda:0 |
| acc_ds_s015_8k | RUNNING (Problem 2/50) | cuda:1 |
| acc_ds_s020_8k | QUEUED | - |
| acc_ds_s025_8k | QUEUED | - |
| acc_ds_s030_8k | QUEUED | - |

**脚本修改：**
- 新增 `--max-new-tokens` 参数（默认 8192），替换原来硬编码的 2048
- `run_evaluation()` 函数签名和调用处、输出元数据处均已更新

**踩坑修复：** `submit_training_job` 设置 `CUDA_VISIBLE_DEVICES` 后进程内只看到 `cuda:0`，命令中的 `--gpu` 必须用 `cuda:0` 而非物理 GPU 编号。s015 首次提交因此失败，已修复重提。

剩余 3 个实验 (s020/s025/s030) 在 registry 中标记为 QUEUED，spec 已填写完整，等前两个完成后可复用 GPU 提交。

---
