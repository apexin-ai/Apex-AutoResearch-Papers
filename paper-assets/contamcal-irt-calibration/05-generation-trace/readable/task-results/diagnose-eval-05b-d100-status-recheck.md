# diagnose eval 05B d100 status recheck

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_05B_d100_status_recheck_20260514T150151_result.json`
- **Structured JSON:** [`66b5355b2c3d5ff0560f.json`](../../sessions/66/66b5355b2c3d5ff0560f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

**进程 PID 389866：ALIVE**

| 项目 | 值 |
|------|-----|
| 状态 | `R (running)`，CPU 103% |
| 运行时间 | 14h48m |
| 线程数 | 323 |
| GPU 2 显存 | 3695 MiB (36% 利用率) |
| 输出目录 | 空（尚无 JSON 结果） |
| 日志 | 无独立日志，stdout 输出到 tmux pts/5 |

**判断**：进程仍在活跃运行。`--mc-format aligned` 是逐条生成式评估，比 batch 格式慢得多。4 个 benchmark（mmlu, gsm8k, arc_challenge, humaneval）用 aligned 格式跑 15 小时是合理的。evaluate.py 可能在所有 benchmark 完成后才一次性写出结果 JSON，所以输出目录为空不代表有问题。

**操作**：不更新 registry，保持 RUNNING 状态。wrapper timeout 是误报，实际 eval 进程正常。

---
