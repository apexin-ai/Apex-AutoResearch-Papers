# analysis eval metrics aggregation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-metrics-aggregation_20260515T182502_result.json`
- **Structured JSON:** [`603b6ff92f679be112a4.json`](../../sessions/60/603b6ff92f679be112a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已生成并注册。汇总结果：

**38 条个体实验记录**（0.5B: 12, 1.5B: 12, 3B: 14），跨 4 个 dose × 2 个 seed × 2 种 eval type。

**关键发现（dose-response aligned eval 均值）：**

| Benchmark | 趋势 |
|-----------|------|
| **GSM8K** | 3B 有强 dose-response：0.31→0.21→0.60→0.74；1.5B 和 0.5B 几乎无变化 |
| **MMLU/ARC** | 所有 scale 下变化 <3pp，contamination 对 MC benchmark 信号微弱 |
| **HumanEval** | 1.5B 有清晰 dose-response：0.15→0.25→0.23→0.29；3B: 0.08→0.15→0.13→0.18 |

**数据缺口（Coverage Matrix）：**
- 大部分 para_aligned 只有 seed 42，缺 seed 123
- 3B d005_s123 aligned 未跑
- 3B d100_s123 para_aligned 未跑
- 0.5B d100 para_aligned 完全缺失

产出文件：
- `artifacts/eval_metrics_summary.json` — 机器可读 JSON（含 dose-response curves）
- `artifacts/eval_metrics_summary.md` — 论文级 markdown 表格

---
