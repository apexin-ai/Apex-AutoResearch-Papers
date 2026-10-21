# monitor gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gpu-status-check_20260516T002827_result.json`
- **Structured JSON:** [`d23aa7050276ddf2f239.json`](../../sessions/d2/d23aa7050276ddf2f239.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU Status Report

| GPU | VRAM | Experiment | Wrapper PID | GPU PID | Status | Progress | ETA |
|-----|------|-----------|-------------|---------|--------|----------|-----|
| 0 | 23260/24564 MiB (95%) | sft_3B_d005_s42_a32 | 643162 | 643167 | **Running** | 70% (2222/3177), epoch 0.63 | ~1h17m |
| 0 | ↑ (共享) | eval_3B_d100_s123_a32_batch | 642752 | 642763 | **Running** | GSM8K 65% (858/1319) | ~1h18m (仅当前 benchmark) |
| 1 | 13341/24564 MiB (54%) | sft_3B_d100_s42_a32_v3 | 628663 | 628668 | **Running** | 87% (3610/4159), epoch 0.86 | ~40m |
| 2 | 7537/24564 MiB (31%) | signals_3B_v7 | 652247 | 652259 | **Running** | Self-critique mmlu 47% (3340/7021) | ~1h20m |
| 3 | 8985/24564 MiB (37%) | eval_3B_d025_v3_s42_batch | 655982 | 655989 | **Running** | aligned eval 进行中 (~56min CPU time) | 未知（无日志） |
| 4 | 6891/24564 MiB (28%) | signals_3B_v8 | 659057/659058 | 662616 | **Running** | Self-critique mmlu 刚启动 (~73/7021) | ~2h42m |
| 5 | 7397/24564 MiB (30%) | signals_3B_d025_v3_s42 | 663047 | 663067 | **Running** | Self-critique mmlu 7% (506/7021) | ~2h18m |

## 需要注意的问题

**GPU 0 双实验共享（高风险）**：SFT d005 (14270 MiB) + eval d100_s123 (8976 MiB) 共用 GPU 0，VRAM 已达 95%。目前运行正常但无余量。

**eval_3B_d025_v3_s42_batch 无日志文件**：该实验直接在 tmux 中启动（PID 655982/655989），未通过 agent-ml 框架，因此 `~/runs/` 下没有 `.log` 文件。进程活跃（83.9% CPU, state Rl+），正在执行 aligned eval（mmlu+gsm8k+arc_challenge），之后还需跑 para_aligned eval。

**遗留 tmux session**：`exp_001_eval_3B_d100_v2_para_aligned`（创建于 May 15 08:05）仍存在，但无对应 GPU 进程，疑为已完成任务的残留 session。

**缺失 tmux session**：`sft_3B_d005_s42_a32` 和 `signals_3B_v8` 无对应 tmux session，可能通过 nohup 或其他方式启动。

**无空闲 GPU**：6 块 GPU 全部占用。

**已完成实验**：无。

**失败实验**：无（全部 7 个实验均正常运行）。

---
