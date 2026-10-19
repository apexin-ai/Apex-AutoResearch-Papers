# diagnose bjb1 18228 hung experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-18228-hung-experiments_20260519T180134_result.json`
- **Structured JSON:** [`2ad6a7fdf6e24feaf837.json`](../../sessions/2a/2ad6a7fdf6e24feaf837.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**服务器时间**: 2026-05-20 02:03 CST，3 个实验启动于 May 19 13:56，已运行 **~12h**（非 18h）。

### 实验 1: eval-obs-only-object-norm005-seed48 (GPU0, PID 989971)
- **状态: 仍在运行，未 hang**
- 进程 Rl 状态，CPU time 1007 min
- GPU0: 1942 MiB, 21% util
- 日志 118 行，最后修改 01:54（9 分钟前），当前在 `pick_up_the_orange_juice` rollout 3/10
- 已完成 ~10 个 task，接近尾声

### 实验 2: eval-perdof-object-norm005-seed47 (GPU2, PID 990241)
- **状态: 仍在运行，未 hang**
- 进程 Rl 状态，CPU time 1014 min
- GPU2: 1942 MiB, 23% util
- 日志 117 行，最后修改 01:56（7 分钟前），当前在 `pick_up_the_orange_juice` rollout 2/10
- 进度类似

### 实验 3: eval-perdof-object-norm003-seed47 (GPU3, PID 990509)
- **状态: 仍在运行，未 hang**
- 进程 Rl 状态，CPU time 1009 min
- GPU3: 1942 MiB, 23% util
- 日志 119 行，最后修改 02:01（2 分钟前），当前在 `pick_up_the_orange_juice` rollout 4/10
- 进度类似

### 实验 4: eval-vla-only-long-seed45 (GPU1, PID 113569)
- **状态: 正常运行**
- 启动于 01:31（32 分钟前），GPU1: 4930 MiB, 22% util
- 已完成 2 个 LONG benchmark task，正在第 3 个

### 结论

3 个疑似 hang 的实验**都没有 hang**，日志持续有新输出。慢的原因是 K=10 correction steps（每个 rollout 做 10 步修正推理），比 VLA-only 实验慢很多。按日志行数估计它们已完成 ~10 个 task，应该接近完成。

**是否仍然要 kill 释放 GPU？** 它们是低优先级 seed 且可能再跑 1-2h 就能完成。请指示。

---
