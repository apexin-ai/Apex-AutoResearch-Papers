# submit westd 34887 2gpu

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_westd-34887-2gpu_20260518T042321_result.json`
- **Structured JSON:** [`ef6e34e5b09019e8d888.json`](../../sessions/ef/ef6e34e5b09019e8d888.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 job 已提交并确认运行：

| Job | GPU | PID | 显存 | GPU-Util |
|---|---|---|---|---|
| **kl50_s123_eval** (downstream eval) | cuda:0 | 99954 | 41718 MiB | 0% (模型加载中) |
| **kl50_s456_train** (s456 训练) | cuda:1 | 100263 | 41718 MiB | 96% |

两卡均已占用，nohup 启动，日志分别写入 `/root/runs/distill_sparse_swiglu/kl50_s123_eval.log` 和 `kl50_s456_train.log`。Registry 状态已更新为 RUNNING。

---
