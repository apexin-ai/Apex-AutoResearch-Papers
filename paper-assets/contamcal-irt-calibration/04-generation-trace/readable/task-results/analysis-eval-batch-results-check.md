# analysis eval batch results check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-batch-results-check_20260515T043858_result.json`
- **Structured JSON:** [`6344266d13f1e4fc43f0.json`](../../sessions/63/6344266d13f1e4fc43f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 5 个进程仍在运行，尚未退出。** 当前进度：

| # | 实验 | PID | GPU | 运行时长 | 当前进度 | 预计剩余 |
|---|------|-----|-----|---------|---------|---------|
| 1 | 3B_d100_v2_aligned | 477489 | cuda:0 | 3h38m | HumanEval 78% (128/164) — 最后一个 benchmark | **~6 min** |
| 2 | 0.5B-Instruct | 493617 | cuda:4 | 1h14m | stdout→pipe，无独立日志 | 未知 |
| 3 | 0.5B_d000_s42_v7 | 494109 | cuda:4 | 1h12m | GSM8K 56% (734/1319) — 第2/4个 benchmark | ~1.5-2h |
| 4 | 3B_d000_v2_s123 | 492660 | cuda:1 | 1h18m | GSM8K 35% (458/1319) — 第2/4个 benchmark | ~2.5-3h |
| 5 | 3B_d025_v2_para | 499610 | cuda:2 | 24m | stdout→pipe，无独立日志 | 未知 |

关键发现：
- **#1 即将完成**（~6分钟），HumanEval 是最后一个 benchmark
- **#2 和 #3 都在 cuda:4 上**，可能互相抢资源导致变慢
- **#2 和 #5** 的 stdout 写到 pipe（可能是 tmux），无法直接通过日志文件查看进度
- 所有输出目录当前为空 — eval 脚本在完成所有 benchmark 后才写结果文件

需要等进程完成后再检查结果。要我设一个定时检查吗？

---
