# ops full trace resubmit with isolation

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_trace_resubmit_with_isolation_20260521T073756_result.json`
- **Structured JSON:** [`dfdaaacd92a2cef65df1.json`](../../sessions/df/dfdaaacd92a2cef65df1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已成功提交并更新 registry 为 RUNNING。

**汇报：**

| 实验 | PID | GPU | 显存占用 | 利用率 | 速度 |
|------|-----|-----|---------|--------|------|
| seed123 | 683796 | GPU 0 (CUDA_VISIBLE_DEVICES=0) | 41,182 MiB | 100% | ~16.5s/step |
| seed456 | 683873 | GPU 1 (CUDA_VISIBLE_DEVICES=1) | 41,182 MiB | 98% | ~20s/step (稳定后应与 seed123 持平) |

**OOM 根因及修复：**
- 之前两个进程都没有 `CUDA_VISIBLE_DEVICES`，全部落在物理 GPU 0 上，且缺少 `--gradient_checkpointing`
- 现在用 `CUDA_VISIBLE_DEVICES=0/1` 严格隔离 + `--gradient_checkpointing` + `/root/miniconda3/bin/python`

**额外清理：**
- Kill 了一个自动重试机制产生的幽灵进程（PID 683229，从 hook on_failed 触发的串行脚本）
- Kill 了该脚本试图启动的第二个幽灵进程（PID 684859）

**预计完成时间：**
- 444 steps/epoch × 3 epochs = 1,332 steps × ~16.5s/step ≈ 6.1 小时
- 训练完成：约 UTC 21:50（北京时间 05:50）
- 加上 eval 约 30 分钟，总计约 22:20 UTC

---
