# submit 3B d100 s123 a32 gpu0

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_3B_d100_s123_a32_gpu0_20260515T163218_result.json`
- **Structured JSON:** [`c915212df0cbf07f715c.json`](../../sessions/c9/c915212df0cbf07f715c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 上有且仅有 1 个 python 进程（PID 594494，6604 MiB）。

**提交完成：**
- 实验：`exp_001_sft_3B_d100_s123_a32_v2`
- 服务器：cqa1-21977，GPU 0
- PID：594494（子进程），tmux session PID 594489
- 配置：Qwen2.5-3B, d100, seed=123, alpha=32, lr=5e-5, batch=1×16
- 训练样本：66,533 条
- 日志：`~/runs/contamcal-irt-calibration/exp_001_sft_3B_d100_s123_a32_v2.log`

附带清理：将 GPU 0 上已完成的 `exp_001_eval_15B_d005_s123` / `_v2`（PID 566224，EXIT_CODE=0）从 RUNNING → DONE(success)。

---
