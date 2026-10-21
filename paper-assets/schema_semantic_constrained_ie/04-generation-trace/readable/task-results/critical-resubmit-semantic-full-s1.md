# critical resubmit semantic full s1

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_resubmit_semantic_full_s1_20260514T003549_result.json`
- **Structured JSON:** [`1ad23647b485fe92a274.json`](../../sessions/1a/1ad23647b485fe92a274.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功加载模型，正在运行推理。

**最终状态：**

| GPU | PID | 任务 | 显存 | 状态 |
|-----|-----|------|------|------|
| 0 | 137719 | docred schema_informed | 20352 MiB | 运行中 (90% util) |
| 1 | 138136 | **full_s2** (已有) | 16480 MiB | 运行中 |
| 1 | 139051 | **full_s1** (新提交) | 16480 MiB | 运行中 |
| 1 | 139923 | **semantic_only** (新提交) | 加载中 | 模型加载完成 |

GPU 1 总用量 ~48GB/98GB (加载完后约 ~64GB)，安全。两个 GPU 利用率均 90%+。

**注意事项：**
1. 两个实验都在 **cuda:1** 上（因 cuda:0 被 docred 占用），而非原计划的分开两张卡
2. 清理了 2 个重复的 semantic_only 进程（PID 138674, 139423），它们会与我们的进程写同一输出文件导致数据损坏
3. `submit_training_job` 工具不可用，用 tmux 启动，未自动注册 cron 监控——如需定期检查状态请告知

---
