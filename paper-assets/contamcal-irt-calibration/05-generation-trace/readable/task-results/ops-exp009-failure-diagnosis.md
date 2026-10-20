# ops exp009 failure diagnosis

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp009_failure_diagnosis_20260517T053836_result.json`
- **Structured JSON:** [`1482d86abfde137b49d8.json`](../../sessions/14/1482d86abfde137b49d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/exp009_status_check.md`。

**结论**: Worker 崩溃前已完成所有 signal 计算（两个模型×3 benchmarks），且成功启动了 DeepSeek eval。当前状态：

- **DeepSeek eval 仍在 GPU 3 上运行**（PID 935048，gsm8k 进行中，预计即将完成）
- **Qwen2.5-3B-Instruct eval 从未启动** — 这是唯一需要恢复的任务
- GPU 0/1/2/4/5 均空闲，可立即用于恢复

---
