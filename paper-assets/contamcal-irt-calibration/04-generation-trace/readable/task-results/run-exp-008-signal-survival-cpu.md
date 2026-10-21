# run exp 008 signal survival cpu

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp_008_signal_survival_cpu_20260514T160652_result.json`
- **Structured JSON:** [`2b0ffbfbff4f33f68633.json`](../../sessions/2b/2b0ffbfbff4f33f68633.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行成功。结果汇总：

## 产出文件
- `exp008_exp002_output/cross_benchmark_summary.json` — 跨 benchmark 汇总
- `exp008_exp002_output/per_benchmark/{mmlu,gsm8k,arc_challenge}/survival_report.json` — 各 benchmark 详细报告

## AUC Heatmap（3 signals × 3 regimes × 3 benchmarks）

ConStat (S3) 在 exp-002 中未计算，全部 N/A。

| Signal | Regime | mmlu | gsm8k | arc_challenge |
|---|---|---|---|---|
| **Embedding (S1)** | d000 | 0.5049 | 0.5502 | 0.4270 |
| | d005 | **0.9530** | **0.9882** | **0.9950** |
| | d100 | 0.4943 | 0.4127 | 0.5010 |
| **Min-K%++ (S2)** | d000 | 0.5090 | 0.5697 | 0.5075 |
| | d005 | 0.4655 | 0.4649 | 0.4659 |
| | d100 | 0.5053 | 0.4841 | 0.4950 |
| **Self-Critique (S4)** | d000 | 0.4957 | 0.4800 | 0.5175 |
| | d005 | 0.5165 | 0.4947 | 0.4325 |
| | d100 | 0.5125 | 0.4393 | 0.5515 |

关键发现：
- **Embedding (S1) 在 d005 regime 下 AUC 极高**（0.95-0.995），但在 d000 和 d100 下降至随机水平（~0.5）。信号未能 survive 到 d100 regime。
- **Min-K%++ 和 Self-Critique 在所有 regime 下都接近随机**（0.43-0.57），无有效区分能力。
- **Surviving signals: 0/4**（所有 benchmark 一致）— 没有信号在跨 regime 下保持检测能力。

---
