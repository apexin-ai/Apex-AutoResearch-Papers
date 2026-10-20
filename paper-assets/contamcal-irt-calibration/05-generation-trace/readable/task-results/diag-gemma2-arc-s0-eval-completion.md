# diag gemma2 arc s0 eval completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gemma2-arc-s0-eval-completion_20260520T220830_result.json`
- **Structured JSON:** [`98629ea615e9f182b2a3.json`](../../sessions/98/98629ea615e9f182b2a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

d000 accuracy = 85.84%。进程仍在运行中（d005 ~28%），**eval 尚未完成**。

当前状态：
- d000_s0: **完成** — ARC accuracy = **85.84%** (1006/1172)
- d005_s0: **运行中** (~28%)
- d025_s0: 未开始
- d050_s0: 未开始

估算剩余时间：每个 dosage ~3 分钟 eval + ~10s 加载，d005 还剩 ~2 分钟，加上 d025/d050 两个 ~3.5 分钟，预计 **还需约 10 分钟**完成全部。

暂不更新 registry — 等全部 4 个 dosage 完成后再一起更新。需要我过一会儿再查吗？

---
