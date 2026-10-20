# analyze plan 002 qwen17b r2 s1

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_plan-002-qwen17b-r2-s1_20260514T231006_result.json`
- **Structured JSON:** [`403d6e1b41a4c5215efb.json`](../../sessions/40/403d6e1b41a4c5215efb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果汇总

### plan-002-qwen17b-r2-s1 ✓ 完成

| 指标 | 值 |
|------|-----|
| Records | 2326 |
| Seeds | 498 (seed 498–999) |
| Depth 0/1/2/3/4 | 498 / 491 / 473 / 440 / 424 |
| Skipped | 53 (empty output) |
| 文件大小 | 2.5M |
| 耗时 | 4228s (~70 min) |

深度衰减符合预期：depth 0 全量 498，每一层因 empty output 有少量 dropout，到 depth 4 保留 85%（424/498）。

### plan-002-qwen17b-r2-s0 — 仍在运行

- PID 120617, 已跑 1h12m, 100% CPU
- 进度 485/498 seeds (~97%)，约 3 分钟内完成
- 当前 2210 行，seed 范围 0–497

---
