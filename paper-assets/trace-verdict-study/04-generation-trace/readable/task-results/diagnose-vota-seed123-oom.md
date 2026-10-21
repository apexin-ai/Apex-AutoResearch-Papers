# diagnose vota seed123 oom

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_vota_seed123_oom_20260515T124340_result.json`
- **Structured JSON:** [`c33b3f30cec002e287ac.json`](../../sessions/c3/c33b3f30cec002e287ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

- **cuda:0**: PID 93494 (`deepseek_vota_seed42` 的子进程, PPID=93489) 占用 22386 MiB，GPU 利用率 100%，正常运行中
- **cuda:1**: 0 MiB 占用，完全空闲，无任何进程
- **PID 93494**: 是 `deepseek_vota_seed42` 的训练进程（`train_sft.py --gpu 0 --seed 42`），仅绑定在 GPU 0 上

**OOM 根因**: `vota_seed123` 启动时没有正确绑定到 cuda:1，而是落到了默认的 cuda:0（GPU 0）。cuda:0 已被 seed42 的进程占满 ~22 GiB，seed123 试图在同一张卡上再分配 4.64 GiB 时 OOM。错误信息里的 "Process 93494 has 21.86 GiB" 证实了这一点——占显存的不是 seed123 自己，而是 seed42 的进程。

**结论**: cuda:1 当前空闲可用。重新启动 vota_seed123 时需确保 `--gpu 1`（或 `CUDA_VISIBLE_DEVICES=1`）正确设置，使其绑定到 cuda:1。

---
