# diag gsm8k gemma2 s42 fail2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gsm8k_gemma2_s42_fail2_20260520T061303_result.json`
- **Structured JSON:** [`8870d6ce2cf9fccfaba3.json`](../../sessions/88/8870d6ce2cf9fccfaba3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 结论：第二次"失败"是误报，eval 进程仍在正常运行

---

### 当前状态

| 项目 | 状态 |
|------|------|
| PID 289137 (监控追踪的 PID) | **已退出** — 这是外层 `bash -c` wrapper |
| PID 293330 (实际 evaluate.py) | **正在运行** — cuda:3, 27700 MiB, PPID=289130 |
| d000_s42 | **已完成** — exact_match: 0.1387 (183/1319), 结果已写入 |
| d100_s42 | **进行中** — 14:08 开始, ~22% (36/165 batches), ETA ~14:43 CST |
| cuda:3 | 94% 利用率, 27709 MiB / 97887 MiB |

---

### 两次失败的根因

**第一次 (PID 287533, EXIT_CODE=129)**：tmux session 收到 SIGHUP。trap 正确报告 exit 129。可能是 SSH 断连或 tmux session 管理问题。

**第二次 (PID 289137, "Process exited without valid W&B metrics")**：**误报**。监控系统追踪的是外层 `bash -c` wrapper (PID 289137)，但实际 Python 进程 (PID 293330) 作为子进程仍在正常运行。同时，`evaluate.py` 是纯 eval 脚本，**不产生 W&B metrics**，只写 JSON 结果文件。监控系统的成功判据（要求 W&B metrics）对 eval 任务不适用。

关键日志：
```
2026-05-20 14:07:48,646 [INFO] gsm8k exact_match: 0.1387 (183/1319)
2026-05-20 14:07:48,660 [INFO] Sentinel .done written to .../gemma2_d000_s42
2026-05-20 14:08:03,873 [INFO] Evaluating gsm8k...  # d100 开始
Evaluating GSM8K:  22%|██▏       | 36/165 [07:42<27:32, 12.81s/it]  # 正在推进
```

---

### 建议

1. **不要干预** — d100_s42 eval 正在正常推进，预计 ~14:43 CST 完成
2. **修复监控系统** — eval 任务的成功判据应改为检查 `.done` 文件或 `eval_results.json` 是否存在，而非 W&B metrics
3. **不要重新提交** — 如果 on_failed hook 再次触发重试，会导致 cuda:3 上进程冲突（违反 C001/C003）

---
