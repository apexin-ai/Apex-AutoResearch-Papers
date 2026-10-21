# diag deepseek full trace tail256 seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_deepseek_full_trace_tail256_seed42_20260517T204425_result.json`
- **Structured JSON:** [`a53200fe61dfede67b62.json`](../../sessions/a5/a53200fe61dfede67b62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

**进程存活：是**
- PID 379548 (bash wrapper) 存活，子进程 PID 379561 (python) 在 GPU 上运行

**GPU cuda:0 状态：**
- NVIDIA RTX PRO 6000 Black, 73°C, 438W/600W, GPU-Util 100%
- 显存占用 70281 MiB / 97887 MiB
- 训练进程 PID 379561 使用 21100 MiB

**训练进度：**
- 当前 step 112/444 (约 25%)
- 速度 ~3.3-3.7 s/step
- 预估剩余时间 ~19 分钟（基于日志中 ETA）
- 训练开始时间：2026-05-18 04:38 CST (20:38 UTC)

**Checkpoint 目录：** 已创建但尚无 checkpoint 产出（只有 `runs/` 子目录，训练还在进行中）

**W&B：** 日志未截断到 W&B init 部分，但从 spec 中配置了 `--wandb_project trace-verdict-study --wandb_run_name deepseek_full_trace_tail256_seed42`，应已创建 run。

**结论：** 实验正常运行中，约 25% 进度，预计还需 ~19 分钟完成训练步骤，之后还会自动执行 evaluation。

---
