# ops cross dataset progress

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cross_dataset_progress_20260522T045241_result.json`
- **Structured JSON:** [`8a159cedaa1c49c84ac1.json`](../../sessions/8a/8a159cedaa1c49c84ac1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cross_dataset_batch 进度报告

**状态：0/4 完成，0/4 在进行中 — 全部阻塞等待 GPU**

batch 脚本从 12:34 开始轮询等待 GPU 1 释放，至今未启动任何实验。4 个 checkpoint 目录均不存在：
- `cross_he2mbpp_exception_only_seed42` — NOT STARTED
- `cross_he2mbpp_no_trace_seed42` — NOT STARTED
- `cross_mbpp2he_exception_only_seed42` — NOT STARTED
- `cross_mbpp2he_no_trace_seed42` — NOT STARTED

**阻塞原因：** GPU 1 被 `deepseek_loop_only`（非 batch 内实验）占用，PID 740379，100% 利用率，23.4 GB 显存。

**deepseek_loop_only 进度估算：**
- 总步数 444，checkpoint-148 写于 12:14
- 从进程启动 (~11:24) 到 checkpoint-148 约 50 分钟 → ~3 steps/min
- 预估当前 step ~269/444，剩余 ~175 步 ≈ **~60 分钟训练 + ~10 分钟 eval**
- GPU 1 预计 **14:00-14:15 左右释放**

**cross_dataset_batch 总时间估算：**
GPU 1 释放后 4 个实验顺序执行，按同规模估算每个 ~2-2.5h，全部跑完约 **8-10 小时**（预计今晚 ~22:00-00:00 完成）。

---
