# analysis multi model error correlation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multi_model_error_correlation_20260521T015715_result.json`
- **Structured JSON:** [`ef673a905717ca34a8cc.json`](../../sessions/ef/ef673a905717ca34a8cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。核心结果：

**Correlation（Qwen3-8B-FT vs LLaMA-3.1-8B）**

| Dataset | Pearson r | Spearman rho | Disagree% |
|---------|-----------|-------------|-----------|
| SciERC | 0.6835 | 0.6625 | 14.5% |
| CoNLL | 0.6490 | 0.6467 | 8.7% |
| FewNERD | 0.6707 | 0.6920 | 14.4% |
| **Mean** | **0.6677** | **0.6671** | **12.5%** |

**Ensemble Simulation（micro-F1 vs best single model）**

| Dataset | Best Single | Union | Intersection | SC Merged Vote |
|---------|------------|-------|-------------|----------------|
| SciERC | 66.21 | +0.51 | -1.08 | **+1.23** |
| CoNLL | 92.67 | -1.25 | -0.65 | **+0.49** |
| FewNERD | 79.18 | -0.06 | -0.10 | **+0.12** |

**Hypothesis 判定**：Cross-family error correlation 为 **MODERATE**（r=0.67），不是 low。约 12.5% 实例只有一个模型做对，提供 ensemble 的互补空间。SC merged vote 是最优 ensemble 策略（mean +0.61pp），简单 union/intersection 效果差。

- 脚本：`code/multi_model_error_correlation.py`
- 报告：`output/multi_model_correlation/error_correlation_report.json`
- 实验：`exp_multi_model_correlation` (DONE, success)

---
