# analysis inter model nocuity

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_inter_model_nocuity_20260522T053817_result.json`
- **Structured JSON:** [`0aaf7a2bb37461b96964.json`](../../sessions/0a/0aaf7a2bb37461b96964.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。产出文件：

- **脚本**：`artifacts/inter_model_nocuity/analyze_nocuity.py`
- **结果**：`artifacts/inter_model_nocuity/nocuity_analysis_results.json`

核心发现：

| 指标 | 结果 |
|------|------|
| Majority+ (≥3/5) | 124 clauses (41.3%) ✓ |
| Universal (5/5) | 39 (13.0%) |
| Strong (4/5) | 32 (10.7%) |
| Majority (3/5) | 53 (17.7%) |
| Divergent (1-2/5) | 92 (30.7%) |
| Innocuous (0/5) | 84 (28.0%) |
| Clause identity 方差占比 | **50.8%** |
| Model identity 方差占比 | **1.6%** |
| 最高 universal rate 类型 | incompleteness (24%) |
| 最高 majority+ rate 类型 | incompleteness (62%) |
| χ² type 间差异 | χ²=27.93, p=0.111 (不显著) |
| Top-1 严重 clause | incompleteness_001, scopal_020, scopal_044, scopal_046 (mean severity=3.0, 全 critical) |

Clause identity 解释了 50.8% 方差，model identity 仅 1.6%——nocuity 主要由 clause 内容决定而非模型差异。incompleteness 类型在各个 nocuity 指标上都最突出。

---
