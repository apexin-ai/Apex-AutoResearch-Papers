# ops diagnose 3B d000 s123 eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-3B-d000-s123-eval_20260515T142813_result.json`
- **Structured JSON:** [`efd74f17a9997f2ecce4.json`](../../sessions/ef/efd74f17a9997f2ecce4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。CronList 显示当前 session 无 cron job（该 cron 是其他 session 创建的，无法从此处删除）。

**诊断结果：**

| 项目 | 状态 |
|------|------|
| PID 551219 | 已退出 |
| 完成度 | **4/4 benchmarks 全部完成** |
| cuda:3 | 已释放（仅 714 MiB 占用，无计算进程） |

**Metrics（3B d000 s123 aligned）：**

| Benchmark | Metric | Score |
|-----------|--------|-------|
| MMLU | accuracy | **0.6332** (8892/14042) |
| GSM8K | exact_match | **0.1812** (239/1319) |
| ARC-Challenge | accuracy | **0.8328** (976/1172) |
| HumanEval | pass@1 | **0.0854** (14/164) |

Registry 已标记 `conclusion=success, status=DONE`。Cron 监控是在其他 session 创建的，本 session 无法删除——需要在原 session 中删除，或可忽略（进程已结束，cron 触发后不会有副作用）。

---
