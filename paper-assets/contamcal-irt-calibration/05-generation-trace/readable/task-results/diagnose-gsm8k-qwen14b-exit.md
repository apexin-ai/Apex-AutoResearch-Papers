# diagnose gsm8k qwen14b exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gsm8k-qwen14b-exit_20260520T061320_result.json`
- **Structured JSON:** [`bf759fbc49968a7bda65.json`](../../sessions/bf/bf759fbc49968a7bda65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**不删除 cron**——实验未完成，仍需监控。

## 诊断结论

| 项目 | 状态 |
|------|------|
| 原始 PID 289218 | 已退出（无 exit file，无日志文件，原因不明） |
| d000 (Qwen14B baseline) | **完成** — acc = **60.80%** (802/1319)，有 `.done` 标记 |
| d100 (Qwen14B contaminated) | **正在运行** — PID 294933, GPU 1, 已运行 ~4 min |
| 实验整体 | **未完成**，d100 已被重新启动 |

Registry 已更新为 RUNNING。Cron 监控保留，等 d100 完成后再做最终判定。

---
