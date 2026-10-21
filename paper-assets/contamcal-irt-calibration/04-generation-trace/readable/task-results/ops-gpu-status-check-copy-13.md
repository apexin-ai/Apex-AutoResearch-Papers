# ops gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260515T201521_result.json`
- **Structured JSON:** [`e9a00a6563e2b87fd056.json`](../../sessions/e9/e9a00a6563e2b87fd056.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

save_project_file 只允许特定文件。直接把报告输出在这里。

---

# GPU 状态检查报告

**时间**: 2026-05-16 04:15:45 | **服务器**: cqa1-21977

## GPU 占用总览

| GPU | 显存占用 | GPU利用率 | 进程数 | 状态 |
|-----|---------|----------|--------|------|
| cuda:0 | 17975/24564 MiB | 53% | 1 | ✅ 正常 |
| cuda:1 | 13325/24564 MiB | 28% | 1 | ⚠️ 未登记实验 |
| cuda:2 | 14328/24564 MiB | 98% | 2 | 需确认 PID 622856 |
| cuda:3 | 14473/24564 MiB | 99% | 3 | 🔴 三进程冲突 |
| cuda:4 | 7537/24564 MiB | 59% | 1 | ✅ 正常 |
| cuda:5 | 17651/24564 MiB | 2% | 1 | ✅ 正常 |

## cuda:3 冲突详情（最严重）

三个独立 python 进程同时占用 cuda:3：

1. **PID 627614** — 5880 MiB — exp_001_eval_15B_s123_para_aligned_batch 的子进程（父 PID 627600，运行 6 分钟）
2. **PID 628112** — 7998 MiB — exp_002_signals_3B_v6 的子进程（父 PID 628100，compute_signals `--signal all --benchmark mmlu`，运行 4 分钟）
3. **PID 629264** — 576 MiB — **v6 的重复启动**（由 `run_signals_3B_v6.sh` PID 629251 启动，compute_signals `--signal s1 --benchmark mmlu`）

signals_v6 被启动了**两次**：一次通过 agent-ml 框架（PID 628100），一次通过 shell 脚本（PID 629251）。三进程共占 14454 MiB，GPU 利用率 99%。暂未 OOM 但结果可能受资源竞争影响。

## cuda:1 — 未登记实验

- **PID 628668** — d100_a32_s42_v3 SFT 训练，13316 MiB，28% 利用率
- `CUDA_VISIBLE_DEVICES=1`，`--output-dir .../Qwen2.5-3B_d100_a32_s42_v3 --seed 42`
- **不在 RUNNING 实验列表中**，来源不明

## cuda:2 — 双进程

- PID 623491 (6788 MiB): eval_3B_d005_s123_gsm8k 的子进程（已知）
- PID 622856 (7526 MiB): **来源不明**，需确认

## 关键 PID 存活状态

| PID | 状态 | 运行时间 | GPU | 实验 |
|-----|------|---------|-----|------|
| 589763 | ✅ Sl+ | 04:03:20 | cuda:5 | SFT d025_v3_s42 |
| 594489 | ✅ Ss+ | 03:41:39 | cuda:0 | SFT d100_s123_a32_v2 |
| 623480 | ✅ Ss+ | 00:32:02 | cuda:2 | eval d005_s123_gsm8k |
| 623826 | ✅ Ss+ | 00:31:50 | cuda:4 | signals_3B_v5 |
| 627600 | ✅ Ss+ | 00:06:01 | cuda:3 | eval 15B para aligned |
| 628100 | ✅ Ss+ | 00:04:13 | cuda:3 | signals_3B_v6 wrapper |
| 628112 | ✅ Rl+ | 00:04:13 | cuda:3 | signals_3B_v6 python |

全部 7 个跟踪 PID 存活。

## tmux

仅发现旧 session `exp_001_sft_0pct_05B`（PID 208932，May12 创建，已完成）。

## 需要决策

1. **🔴 cuda:3**: 至少 kill 重复的 v6 副本（PID 629264/629251）。eval_15B 和 signals_v6 也在抢资源，需决定保留哪个。
2. **⚠️ cuda:1**: PID 628668 d100_a32_s42_v3 是否为有意提交？要保留还是 kill？
3. **cuda:2**: PID 622856 是什么？

---
