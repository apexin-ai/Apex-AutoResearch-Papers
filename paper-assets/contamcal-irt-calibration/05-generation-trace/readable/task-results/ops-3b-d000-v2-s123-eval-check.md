# ops 3B d000 v2 s123 eval check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_3B-d000-v2-s123-eval-check_20260515T041013_result.json`
- **Structured JSON:** [`f1c1c507501940080edc.json`](../../sessions/f1/f1c1c507501940080edc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

**para_aligned (cuda:2, PID 492733)** — 已完成 ✓
- 进程已退出，3 个输出文件完整（eval_results.json + correctness_matrix.json + item_responses.json）
- Registry 已更新：DONE/success
- Metrics: mmlu=0.6512, gsm8k=0.1491, arc_challenge=0.8121, humaneval=0.0385
- cuda:2 已释放

**aligned (cuda:1, PID 492660)** — 仍在运行
- 进程存活，输出目录为空（尚未写出结果）
- Registry 已注册为 RUNNING，gpu=cqa1-21977:cuda:1
- cuda:1 仍被占用

**Cron**: 当前 session 无活跃 cron（之前 session 的 cron 已触发/清理）。

aligned 还需要继续等待。需要我设置 cron 监控它吗？

---
