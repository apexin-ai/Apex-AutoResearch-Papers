# train qwen contam 25pct

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_qwen-contam-25pct_20260521T214120_result.json`
- **Structured JSON:** [`11c84d3e2a7235c2adcc.json`](../../sessions/11/11c84d3e2a7235c2adcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registered. 全部完成，以下是结果汇总：

---

## contam_25 实验结果

| 指标 | 值 |
|---|---|
| lz* (Snijders) | **2.6429** |
| Accuracy (overall) | 0.7405 |
| Accuracy (seen) | 0.8105 |
| Accuracy (unseen) | 0.7171 |
| θ_MLE | 0.2576 |
| Cohen's d | **-8.2153** |
| Bootstrap 95% CI (percentile) | [-18.88, -5.73] |
| Bootstrap 95% CI (BCa) | **[-14.71, -4.94]** |

## Dose-Response 汇总

| 污染比例 | lz* | Cohen's d | |d| |
|---|---|---|---|
| 15% | 3.8494 | -6.57 | 6.57 |
| **25%** | **2.6429** | **-8.22** | **8.22** |
| 50% | 7.2892 | -1.90 | 1.90 |

## 关键发现

**dose-response 不是单调的。** |d(25%)| = 8.22 > |d(15%)| = 6.57 > |d(50%)| = 1.90，25% 的 lz\* 偏离比 15% 更极端。

这与预期的 |d(15%)| > |d(25%)| > |d(50%)| 相反。可能的解释：

1. **50% 污染改变了能力估计本身** — θ_MLE 从 0.20(15%) → 0.26(25%) → 0.37(50%)，50% 污染大幅提升了 θ 估计，而 lz\* 是在该 θ 下计算的，高 θ 使得高正确率不再"意外"，从而抵消了 person-fit 异常
2. **lz\* 对中等污染比例最敏感** — 25% 污染足以产生异常响应模式但还不足以系统性地改变能力参数，导致 person-fit 偏离最大

这对论文的 narrative 很重要：lz\* 在检测"隐蔽"污染（中等比例）时可能比检测大规模污染更有效，因为大规模污染会同步抬高能力估计。

---
