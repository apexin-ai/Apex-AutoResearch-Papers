# code plan 028 mmlu bootstrap ci fast

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_028_mmlu_bootstrap_ci_fast_20260521T135310_result.json`
- **Structured JSON:** [`fb3a79619deddd04cb50.json`](../../sessions/fb/fb3a79619deddd04cb50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果摘要：

**MMLU temporal DIF C% = 31.32%, 95% bootstrap CI = [29.38%, 38.05%]**

| 指标 | 值 |
|------|-----|
| 原始 C% | 31.32% |
| Bootstrap 95% CI | [29.38%, 38.05%] |
| Bootstrap mean / SD | 33.14% / 2.30% |
| CI 宽度 | 8.67pp |
| 随机切分对照 C% | 0.10% ± 0.11% |

关键发现：
- CI 下界 29.4%，远高于 0 —— C% 统计显著
- 随机切分对照仅 0.1%（vs 31.3%）—— 确认 DIF 是时间效应，非抽样噪声
- 正偏差 +1.82pp 说明 bootstrap 分布右偏（部分重抽样放大了 DIF 信号）

输出文件（`artifacts/plan_028_bootstrap_ci/`）：
- `mmlu_bootstrap_ci.py` — 向量化脚本（196x 加速，2.4min 完成 1000 轮）
- `mmlu_bootstrap_results.csv` — 1000 轮 C% 值
- `mmlu_bootstrap_summary.csv` — 汇总统计
- `mmlu_bootstrap_report.md` — 报告

---
