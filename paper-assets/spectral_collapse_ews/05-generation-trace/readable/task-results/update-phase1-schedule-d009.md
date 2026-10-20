# update phase1 schedule d009

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_update_phase1_schedule_d009_20260517T031417_result.json`
- **Structured JSON:** [`3ebb5fc1f51d82dade9f.json`](../../sessions/3e/3ebb5fc1f51d82dade9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`phase1_schedule.md` 已按 D009 新优先级重写完成：

- **阶段 A**（~24h）：cuda:0 串行跑 adaptive vs fixed_mix 核心对比，3 seeds × 2 conditions = 6 runs
- **阶段 B**（~12h）：exp_002 释放 cuda:1 后双卡并行跑 pure_collapse + linear_increasing
- 自动触发规则：exp_001 完成 → 直接启动 Batch 1a，不等 Director 确认

---
