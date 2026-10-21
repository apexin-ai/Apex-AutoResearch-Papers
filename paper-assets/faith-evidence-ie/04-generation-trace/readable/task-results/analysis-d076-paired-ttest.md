# analysis d076 paired ttest

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d076_paired_ttest_20260516T113418_result.json`
- **Structured JSON:** [`f90e1bb0bc05afc14152.json`](../../sessions/f9/f90e1bb0bc05afc14152.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**CED vs flat-NLI: 统计不可区分** (t=-0.754, p=0.506, d=-0.38)

| 比较 | F1 差异 | p-value | 结论 |
|------|---------|---------|------|
| CED RSFT vs SFT | +0.0514 | 0.0003 | **显著** |
| flat-NLI RSFT vs SFT | +0.0522 | 0.0001 | **显著** |
| CED vs flat-NLI | -0.0009 | 0.5059 | 不显著 |

两种 RSFT 方法都显著优于 SFT baseline（p<0.001, Cohen's d > 9），但彼此之间在所有指标上均无显著差异（所有 p>0.2）。

这为 C3（CED ≈ flat-NLI，降级有定量依据）和 C1（evidence tax 通过 RSFT 恢复 +5 F1）提供了统计支持。

局限：n=4 seeds 统计功效较低；SFT baseline 只有单次测量；per-document paired test 因 reeval 未保存 predictions.json 而无法实施。

结果已保存到服务器 `/root/autodl-tmp/eval_results/d076_paired_ttest_results.{json,md}`。

---
