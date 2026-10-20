# ops pid check post oom

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pid-check-post-oom_20260516T044656_result.json`
- **Structured JSON:** [`64a17337a401cc2ee5e6.json`](../../sessions/64/64a17337a401cc2ee5e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进程状态报告 (post-OOM)

全部 6 个 GPU 实验进程正常存活，OOM crash 未影响远程服务器。

| GPU | exp_id | PID | 状态 | 运行时间 | GPU显存 | 备注 |
|-----|--------|-----|------|---------|---------|------|
| cuda:0 | exp_002_signals_15B_s123_batch | 691872→691887 | ✅ Running | 01:02:56 | 3674 MiB | 1.5B s123 signals, util 55% |
| cuda:1 | exp_001_eval_3B_d000_s42_a32_batch | 676487→676497 | ✅ Running | 02:44:14 | 8976 MiB | 3B d000 eval, util 68% |
| cuda:2 | exp_001_eval_3B_d005_s42_a32_batch | 679180→679190 | ✅ Running | 02:30:56 | 8976 MiB | 3B d005 eval, util 66% |
| cuda:3 | exp_001_eval_3B_d100_s42_a32_batch | 687347 | ✅ Running | 01:41:38 | 8976 MiB | 3B d100 aligned eval, util 70% |
| cuda:4 | exp_002_signals_3B_d100_s123_v9 | 689315 | ✅ Running | 01:22:21 | 6996 MiB | 3B d100 signals (s4 mmlu), util 61% |
| cuda:5 | exp_002_signals_05B_s123_v2 | 687036 | ✅ Running | 01:42:19 | 2316 MiB | 0.5B d000_s123 signals (all), util 20% |

**结论**：Agent OOM 仅影响本地 session，服务器 6 个实验进程全部正常运行，无需干预。

---
