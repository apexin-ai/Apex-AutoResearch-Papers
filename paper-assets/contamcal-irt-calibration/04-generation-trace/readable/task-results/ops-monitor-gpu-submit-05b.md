# ops monitor gpu submit 05B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_monitor-gpu-submit-05B_20260516T034344_result.json`
- **Structured JSON:** [`c107ac510a7fb4fe2bbd.json`](../../sessions/c1/c107ac510a7fb4fe2bbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**0.5B s123 信号批次脚本已在 cuda:5 上运行**（PID 687028→687036），无需再次提交。

当前 GPU 状态汇总：

| GPU | PID | 运行时间 | 任务 |
|-----|-----|---------|------|
| 0 | 691033 | 5 min | eval d025_v3_s42 para_aligned |
| 1 | 676497 | 1h41m | eval d000_s42_a32_aligned |
| 2 | 679190 | 1h28m | eval d005_s42_a32_aligned |
| 3 | 687347 | 39 min | eval d100_a32_s42_aligned |
| 4 | 689315 | 20 min | compute_signals 3B d100_a32_s123 (s4) |
| 5 | 687036 | 40 min | **0.5B s123 signals batch (1/12, d000×mmlu)** |

要点：
- PID 663067 已结束，cuda:5 已被 `run_05B_s123_signals.sh` 完整批次脚本接管（父进程 PID 687028）
- 所有 6 GPU 均在忙
- cuda:0 的 eval 刚启动 5 分钟，最先空闲的可能是 cuda:1（已跑 1h41m）或 cuda:2（1h28m），eval 通常 2-3h 完成
- cuda:5 上 0.5B 批次（12 个子任务）预计需要数小时完成，进度 1/12

---
