# ops check full s1 fallback stats

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_full_s1_fallback_stats_20260514T042645_result.json`
- **Structured JSON:** [`309e86d471bdf50df0b0.json`](../../sessions/30/309e86d471bdf50df0b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

| 指标 | 值 |
|------|-----|
| **full_s1 进度** | 304/998 (30.5%) |
| **grammar_only 进度** | 443/998 (44.4%) |
| **方案 A fallback 触发** | **0 次** |
| **方案 B skip 触发** | 无日志可查（静默方案），但所有日志条目均显示 "OK"，无异常 |
| **WARNING 数量** | 0 |

### 进程健康

| PID | 状态 | 运行时间 | GPU 显存 |
|-----|------|---------|---------|
| 157047 (full_s1) | **Rl** (运行中) | 1h10m | 17394 MiB |
| 150766 (grammar_only) | 运行中 | — | 17442 MiB |

日志最新条目为 `[249/998] Cry for Help: OK E=25 R=20 21.9s`，每条约 15-25 秒，全部 "OK"。

修复后 fallback 触发次数为 0，说明修复方案完全消除了原来的断言错误，运行正常。按当前速度 (~18s/doc)，full_s1 剩余 ~694 条预计还需约 3.5 小时。

---
