# gpu check cuda234 status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu-check_cuda234-status_20260515T193632_result.json`
- **Structured JSON:** [`fbf3fd0130a693632dfb.json`](../../sessions/fb/fbf3fd0130a693632dfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总 (cqa1-21977)

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| **cuda:0** | 17975 / 24564 MiB | 93% | **SFT 训练中** — PID 594489 → `d100_s123_a32_v2` (seed=123, 已运行 3h03m) |
| **cuda:1** | 13341 / 24564 MiB | 23% | **SFT 训练中** — PID 593740 → `d100_s42_a32_v2` (seed=42, 已运行 3h06m) |
| **cuda:2** | 0 MiB | 0% | **空闲** — PID 614412 (eval) 已结束 |
| **cuda:3** | 7535 / 24564 MiB | 62% | **compute_signals 运行中** — PID 617202 → `d000_s42` signals (已运行 40m) |
| **cuda:4** | 0 MiB | 0% | **空闲** |
| **cuda:5** | 17651 / 24564 MiB | 27% | **SFT 训练中** — PID 589763 → `d025_v3` (seed=42, 已运行 3h24m) |

**tmux sessions** (4个):
- `exp001_d025_3B_v3` — cuda:5 SFT
- `exp_001_sft_3B_d100_s42_a32_v2` — cuda:1 SFT
- `exp_001_sft_3B_d100_s123_a32_v2` — cuda:0 SFT
- `exp_001_eval_3B_d100_v2_para_aligned` — 已结束（cuda:2 eval 的残留 session）

**注意**: cuda:3 上的 PID 617202 (`compute_signals d000_s42`) 不在预期列表中，无对应 tmux session，可能是自动触发的 signals 任务。

---
