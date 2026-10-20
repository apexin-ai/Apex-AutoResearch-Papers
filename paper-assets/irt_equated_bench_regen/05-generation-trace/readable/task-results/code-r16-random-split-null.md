# code r16 random split null

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r16_random_split_null_20260523T104440_result.json`
- **Structured JSON:** [`453ed176bd050333b931.json`](../../sessions/45/453ed176bd050333b931.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。关键发现：

**Null C% = 0.6247%** — 这是最重要的数字。在纯随机分组下，MH-DIF 联合标准（|Δ_MH| ≥ 1.5 且 p < 0.05）的 false positive rate 约 0.62%。

对比已知观测值：
- 2023 within-year C% (~0.18%) **低于** null → 2023 cohort 内部高度一致
- 2024 cross-year C% (~1.3%) 约为 null 的 2× → 有信号但不极端

P99 = 1.4504 几乎触及 ETS 1.5 阈值，说明在 N=540 per group 的 LLM 场景下，ETS C 阈值大致对应 null 分布的 99th percentile，并非「极端保守」。

输出文件在 `artifacts/r16_threshold_calibration/`：
- `random_split_null.py` — 分析脚本
- `random_split_summary.csv` — 分位数汇总
- `random_split_report.md` — 完整报告
- `per_item_null_stats.csv` — 每个 item 的 null 统计
- `null_histogram.csv` — 直方图数据

---
