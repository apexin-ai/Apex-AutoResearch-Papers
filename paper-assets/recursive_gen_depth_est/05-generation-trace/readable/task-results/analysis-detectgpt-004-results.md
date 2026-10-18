# analysis detectgpt 004 results

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_detectgpt-004-results_20260519T180715_result.json`
- **Structured JSON:** [`ec6fa486306ea4ca1dbc.json`](../../sessions/ec/ec6fa486306ea4ca1dbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果：detectgpt_ordinal_baseline_004

**状态：成功完成，EXIT_CODE=0**

### pythia_nucleus 结果（每深度 200 样本，5 perturbations）

| Calibration | 4-class Accuracy | d1-d3 Balanced Acc |
|-------------|------------------|--------------------|
| methodA | 0.2538 ± 0.0050 | 0.3383 ± 0.0067 |
| methodB | 0.2512 ± 0.0225 | 0.3350 ± 0.0300 |
| methodC | 0.2900 ± 0.0249 | 0.1200 ± 0.0272 |
| **Mean** | **0.2650** | **0.2644** |

- Scoring model: gpt2-large, perturbation model: t5-large
- 4-class random baseline = 0.25, d1-d3 random baseline = 0.333
- **结论：DetectGPT 在 ordinal depth estimation 上基本等于随机猜测。** methodA/B 的 4-class acc 刚过 0.25，d1-d3 bal_acc 在 0.333 附近；methodC 的 4-class 略高但 d1-d3 反而远低于随机（0.12），说明其"准确率"来自偏向某一类而非真正区分深度。

---
