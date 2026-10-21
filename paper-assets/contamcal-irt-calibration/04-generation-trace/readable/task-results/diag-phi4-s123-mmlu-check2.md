# diag phi4 s123 mmlu check2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_phi4-s123-mmlu-check2_20260520T152044_result.json`
- **Structured JSON:** [`29d71790546a6b87d96d.json`](../../sessions/29/29d71790546a6b87d96d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Cron 报告是半对的** — PID 360893（bash wrapper）确实已退出，但子进程 PID 365465 在 cuda:2 上正常运行（31706 MiB，已运行 4 分钟）。

## 当前状态

| Dosage | Accuracy | 状态 |
|--------|----------|------|
| d000 | **76.31%** | ✅ 完成 |
| d005 | **75.92%** | ✅ 完成 |
| d025 | — | 🔄 进行中 4181/14042 (29.8%)，~18.8 it/s，预计 ~9 分钟完成 |
| d050 | — | 未开始 |
| d100 | — | 未开始 |

d025 于 23:17:22 启动加载模型，当前在跑 MMLU eval。d050/d100 排在后面，整体预计还需 ~40 分钟全部完成。

---
