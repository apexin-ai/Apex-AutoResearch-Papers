# analysis entropy exp020 llama folio

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_entropy-exp020-llama-folio_20260518T211010_result.json`
- **Structured JSON:** [`7fd19eb1f45c76c7fb04.json`](../../sessions/7f/7fd19eb1f45c76c7fb04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**数据不可用，westd-32608 已退役。**

具体情况：

- exp-020 (LLaMA-3.1-8B FOLIO-204) 在 westd-32608 上运行完成，结果 JSON 路径为 `/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json`（~2.6M 字符）
- westd-32608 已退役，原始数据丢失
- westd-25068 上无 exp-020 数据副本
- exp-034（在 westd-25068 上的重跑尝试）因 `python: command not found` 失败
- 分析 log 中 SSH 工具截断了完整 JSON，仅保留了聚合指标，per-problem vote 数据未幸存

**幸存的聚合指标**（来自 checkpoint）：

| 指标 | 值 |
|------|------|
| SC accuracy | 63.2% (129/204) |
| SICA accuracy | 60.8% (124/204) |
| Delta | -2.45pp |
| Discordant pairs | 13 (SICA wins: 4, SC wins: 9) |
| Multi-candidate rate (C0) | 61.8% |
| Extraction rate | 94.2% |
| Contradiction rate | 6.2% |
| Both wrong | 71/204 (34.8%) |

无法计算 per-problem SC vote entropy 分桶分析，因为需要每个 problem 的 k=12 条 vote 原始数据。如需此分析，需在 westd-25068 上重跑 exp-020。

---
