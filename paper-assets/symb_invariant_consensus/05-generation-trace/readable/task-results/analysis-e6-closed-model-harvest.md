# analysis e6 closed model harvest

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_e6-closed-model-harvest_20260521T141147_result.json`
- **Structured JSON:** [`73a3e8722948a248e0e5.json`](../../sessions/73/73a3e8722948a248e0e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

收割完成。

## 结果摘要

**状态**: 部分完成 — 154/204 题 (75.5%)，进程在第 155 题无错退出

| 指标 | SICA | SC |
|------|------|----|
| **Overall** | **71.4%** (110/154) | **73.4%** (113/154) |
| True (n=58) | 94.8% | 93.1% |
| False (n=41) | 82.9% | 82.9% |
| Unknown (n=55) | 38.2% | 45.5% |

- SICA-SC 分歧: 9 题，SC 赢 5 次，SICA 赢 2 次
- 约束提取率: 99.6%，矛盾率: 1.6%
- 总耗时: 4.6h，k=12

**Unknown 类精度明显偏低**（SICA 38.2% / SC 45.5%），与其他模型的 SCB 模式一致。

**已执行**: cron 已删除，artifact 已注册，registry 已更新为 success。剩余 50 题的结果需要恢复运行才能补全。

---
