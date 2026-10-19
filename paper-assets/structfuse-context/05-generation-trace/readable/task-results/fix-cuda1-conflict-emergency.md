# fix cuda1 conflict emergency

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cuda1_conflict_emergency_20260514T180110_result.json`
- **Structured JSON:** [`0a4165336b9a6b27a892.json`](../../sessions/0a/0a4165336b9a6b27a892.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成，汇报如下：

---

### 清理结果

| 项目 | 状态 |
|------|------|
| **进程 442120（旧 chain）** | 已杀死 |
| **进程 499718（新 resume）** | 已不存在（随 442120 终止） |
| **Checkpoint 清理** | `random_s43` 目录为空，`full_m2_outputs` 下无 starcoder s43 数据，无需清理 |
| **cuda:1** | 完全干净：0MiB / 0% utilization |
| **cuda:0 Qwen** | 正常运行中（PID 504138, random_s44, 49072MiB） |

### tmux sessions（清理后）
```
m1_reextract_v2    — 保留
m2_qwen_s43        — 保留（Qwen chain）
qwen_s42_watcher   — 保留
```
`m2_starcoder_s43` 和 `starcoder_s42_watcher` 已杀掉。

### Resume 脚本内容
`run_m2_full_starcoder_resume.sh` 包含 **8 个 runs** 顺序执行：
1. random:43:2ep
2. random:44:2ep
3. embedding_distance:42:3ep
4. embedding_distance:43:2ep
5. embedding_distance:44:2ep
6. dataflow_aware:42:3ep
7. dataflow_aware:43:2ep
8. dataflow_aware:44:2ep

脚本配置：`CUDA_VISIBLE_DEVICES=1`，model 路径 `starcoder2-3b`，数据目录 `full_m2_starcoder_data`。

**未启动新训练，等你用 submit_training_job 重新提交。**

---
