# code get teal275 pid register cron

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_get_teal275_pid_register_cron_20260519T150432_result.json`
- **Structured JSON:** [`01e364c423daa693383b.json`](../../sessions/01/01e364c423daa693383b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**teal275_v3** (PID 115174, cuda:1):
- MMLU loglikelihood 阶段 70% (41317/58702)，~104 it/s，预计 ~3 分钟完成 MMLU
- 日志：`/root/distill_sparse_swiglu/logs/qwen14b_teal275_uniform_eval_v3.log`
- Registry spec 已更新 PID=115174
- Cron 监控已注册 (job `2c180a80`，每 2 分钟)

**kl30_v3** (PID 114094, cuda:0):
- MMLU loglikelihood 阶段 11% (4473/40168)，~10.45 it/s，预计 ~57 分钟完成 MMLU
- 日志：`/root/runs/distill_sparse_swiglu/qwen14b_kl30_s42_eval_uniform_v3.log`（注意路径在 `/root/runs/` 下，不是常规 logs 目录）
- kl30 速度慢 10x 是因为要过 predictor 模型

两个实验都在正常运行。

---
